from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Text
from rapidAPI import instadownloader
from keyboards.inline.shareKeyboard import shareMenu

@dp.message_handler(Text(startswith='https://www.instagram.com/'))
async def send_media(message: types.Message):
    link = message.text
    data = instadownloader(link=link)
    if data == 'Bad':
        await message.answer('Bu URL manzil orqali hech narsa topolmadik!')
    else:
        if data['type'] == 'image':
            await message.answer_photo(photo=data['media'], reply_markup=shareMenu)
        elif data['type'] == 'video':
            await message.answer_video(video=data['media'], reply_markup=shareMenu)
        elif data['type'] == 'carousel':
            for i in data['media']:
                await message.answer_document(document=i, reply_markup=shareMenu)
        else:
            await message.answer('Bu URL manzil orqali hech narsa topolmadik!')