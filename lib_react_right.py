# 🎉 Danh sách emoji để thả
emoji_list = ["❤️", "🔥", "👍", "😎", "🎉", "💯"]

# 😆 Emoji cho chuyện cười (dành cho sticker)
funny_emoji_list = ["😁","🤣","🤪", "👀"]

def react_to_recent_messages(client, log_file):
    for group in TARGET_GROUPS:
        try:
            entity = await client.get_entity(group)
            history = await client(GetHistoryRequest(
                peer=entity,
                limit=1,  # Chỉ lấy tin nhắn gần nhất
                offset_date=None,
                offset_id=0,
                max_id=0,
                min_id=0,
                add_offset=0,
                hash=0
            ))

            for message in history.messages:
                # Kiểm tra xem tin nhắn có phải là sticker không
                if message.sticker:
                    # Nếu là sticker, chọn emoji từ danh sách chuyện cười
                    random_emoji = random.choice(funny_emoji_list)
                else:
                    # Nếu không phải sticker, chọn emoji ngẫu nhiên từ danh sách bình thường
                    random_emoji = random.choice(emoji_list)
                
                reaction = [ReactionEmoji(emoticon=random_emoji)]
                
                try:
                    # React vào tin nhắn
                    await client(SendReactionRequest(
                        peer=entity,
                        msg_id=message.id,
                        reaction=reaction
                    ))
                    log_message(log_file, f"✅ Reacted with {random_emoji} to message {message.id} in {group}")

                    # Tăng lượt xem cho tin nhắn
                    result = await client(GetMessagesViewsRequest(
                        peer=entity,
                        id=[message.id],
                        increment=True
                    ))
                    log_message(log_file, f"✅ Increased views for message {message.id} in {group}")

                    wait_time = random.uniform(5, 10)  # Tăng lên khoảng 5-10 giây
                    await asyncio.sleep(wait_time)  # Đợi thêm thời gian ngẫu nhiên

                except FloodWaitError as e:
                    log_message(log_file, f"⏳ Flood wait detected! Waiting {e.seconds} seconds...")
                    await asyncio.sleep(e.seconds + random.uniform(1, 3))  # Thêm thời gian ngẫu nhiên sau khi hết thời gian chờ

        except Exception as e:
            log_message(log_file, f"❌ Error reacting in {group}: {e}")
