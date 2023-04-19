from aiogram import types
from aiogram import filters

from loader import dp


@dp.message_handler(content_types='audio')
async def audio_handler(msg: types.Message):
    await msg.answer('Men audio qabul qilmayman!\n'
                     'Menga Video havolasini yuboring!')

@dp.message_handler(content_types='voice')
async def audio_handler(msg: types.Message):
    await msg.answer('Men voice qabul qilmayman!\n'
                     'Menga Video havolasini yuboring!')

@dp.message_handler(content_types='document')
async def audio_handler(msg: types.Message):
    await msg.answer('Men document qabul qilmayman!\n'
                     'Menga Video havolasini yuboring!')

@dp.message_handler(content_types='photo')
async def audio_handler(msg: types.Message):
    await msg.answer('Men rasm qabul qilmayman!\n'
                     'Menga Video havolasini yuboring!')

@dp.message_handler(content_types='video')
async def audio_handler(msg: types.Message):
    await msg.answer('Men video qabul qilmayman!\n'
                     'Menga Video havolasini yuboring!')

@dp.message_handler(content_types='sticker')
async def audio_handler(msg: types.Message):
    await msg.answer('Men sticker qabul qilmayman!\n'
                     'Menga Video havolasini yuboring!')

@dp.message_handler(content_types='location')
async def audio_handler(msg: types.Message):
    await msg.answer('Men location qabul qilmayman!\n'
                     'Menga Video havolasini yuboring!')