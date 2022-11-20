from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMAddWords(StatesGroup):
	add_word = State()
	