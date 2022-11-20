from aiogram.utils import executor
from loader import dp, bot


async def on_startup(_):
	import handlers
	print('Бот успешно запустился')

if __name__ == '__main__':
	executor.start_polling(dp, on_startup=on_startup)