from loader import dp
from aiogram import types
from keyboards import kb_help_client
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from states import FSMAddWords
from parser_DevKg.parser import *


WELCOME_TEXT = '''Вас приветсвует парсер бот по сайту DevKg!
Парсер был создан для удобнго поиска вакансий по ключевым словам
P.s на самом сайте поиска нет!
Что-бы прочесть инструкцию использования бота введите команду:
/info'''

INFO_TEXT = '''1) Вводите команду /start_looking
2) У вас появиться клавиатура на которой будут 2 команды:
/Начать_поиск
/Сбросить_все
3) Вводите ключевые слова по очереди отправляя каждое отдельно!'''

@dp.message_handler(commands=['start'])
async def comand_start(message: types.Message):
	await message.answer(WELCOME_TEXT)

@dp.message_handler(commands=['info'])
async def comand_help(message: types.Message):
	await message.answer(INFO_TEXT)


@dp.message_handler(commands=['start_looking'])
async def comand_help(message: types.Message):
	await FSMAddWords.add_word.set()
	await message.answer('Введите первое ключевое слово!', reply_markup=kb_help_client)

@dp.message_handler(commands=['Начать_поиск'],state=FSMAddWords.add_word)
async def comand_help(message: types.Message, state=FSMAddWords.add_word):
	async with state.proxy() as data:
		if data.get('key_words', False):
			await message.answer('Ожидание может занять от 4 до 15 секунд, пожалуйста подождите!')
			jobs_info = get_info_job(data['key_words'])
			if len(jobs_info) > 0:
				for job_info in jobs_info:
					await message.answer(job_info)
			else:
				await message.answer('По вашему запросу нечего не найденно!')
			await state.finish()
			await message.answer('спасибо за использование', reply_markup= ReplyKeyboardRemove())
		else:
			await message.answer('Вы должны ввсети хотя-бы одно ключевое слово для поиска!')

@dp.message_handler(commands=['Сбросить_все'],state=FSMAddWords.add_word)
async def comand_help(message: types.Message, state=FSMAddWords.add_word):
	await state.finish()
	await message.answer('Успешно был сброшен', reply_markup= ReplyKeyboardRemove())

@dp.message_handler(state=FSMAddWords.add_word)
async def add_word(message: types.Message, state=FSMAddWords.add_word):
	async with state.proxy() as data:
		if data.get('key_words', False):
			data['key_words'] += [message.text.lower()]
		else:
			data['key_words'] = [message.text.lower()]
		print(data['key_words'])
