from telethon import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon import TelegramClient, functions
api_id = 
api_hash = 
phone_number =
client = TelegramClient('session_name', api_id, api_hash)
async def change_avatar(file_path):
    await client.start(phone_number)
    # Upload và đổi ảnh đại diện
    result = await client(functions.photos.UploadProfilePhotoRequest(
        file=await client.upload_file(file_path)
    ))
    print('Avatar đã được đổi:', result)

with client:
    client.loop.run_until_complete(change_avatar(r'C:\Users\Windows\OneDrive\Desktop\Picture1.png'))
