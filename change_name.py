from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
api_id = 
api_hash = 
phone_number =
client = TelegramClient('session_name', api_id, api_hash)
async def change_name(new_first_name, new_last_name=''):
    await client.start(phone=phone_number)
    result = await client(UpdateProfileRequest(
        first_name=new_first_name,
        last_name=new_last_name if new_last_name else None
    ))
    print("Đổi tên thành công:", result)
import asyncio
asyncio.run(change_name('Tên mới', 'Họ mới'))
