import telebot
from aiogram import Bot, Dispatcher, executor, types


bot = Bot('7590354302:AAExvTIF-M8zFOLsMfYBeWadNnnE6AaSvyY')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть игру', web_app=WebAppInfo(url='')))
    await message.answer('Привет мой друг!', reply_markup=markup)

executor.start_polling(dp)