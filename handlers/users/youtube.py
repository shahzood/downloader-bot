# from aiogram import types
# from aiogram.dispatcher.filters import Text
# from pytube import YouTube
# from io import BytesIO
#
#
# from keyboards.inline.shareKeyboard import shareMenu
# from loader import dp
#
# @dp.message_handler(Text(startswith="http"))
# async def get_audio(message:types.Message):
#     link=message.text
#     buffer=BytesIO()
#     url=YouTube(link)
#     if url.check_availability() is None:
#         audio=url.streams.get_audio_only()
#         audio.stream_to_buffer(buffer=buffer)
#         buffer.seek(0)
#         filename=url.title
#         await message.answer_audio(audio=buffer, caption=filename, reply_markup=shareMenu)
#     else:
#         await message.answer("Xato xabar yubordingiz!")
