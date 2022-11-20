from loader import dp
from aiogram import types


@dp.message_handler()
async def other_message(message: types.Message):
	send_message = await message.answer('Команда не распознана! введите команду /info')
	await message.delete()
