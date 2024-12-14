import texts
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import get_all_products

all_products = get_all_products()


api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text="Рассчитать")
button2 = KeyboardButton(text="Информация")
button3 = KeyboardButton(text="Купить")
kb.row(button1, button2)
kb.add(button3)

kbl = InlineKeyboardMarkup(resize_keyboard=True)
button4 = KeyboardButton(text="Рассчитать норму калорий", callback_data="calories")
button5 = KeyboardButton(text="Формулы расчёта", callback_data="formulas")
kbl.row(button4, button5)

kbl_buy = InlineKeyboardMarkup(resize_keyboard=True)
button6 = KeyboardButton(text="Product1", callback_data="product_buying")
button7 = KeyboardButton(text="Product2", callback_data="product_buying")
button8 = KeyboardButton(text="Product3", callback_data="product_buying")
button9 = KeyboardButton(text="Product4", callback_data="product_buying")
kbl_buy.row(button6, button7, button8, button9)


@dp.message_handler(commands=["start"])
async def start(message):
    await bot.send_message(message.chat.id,
                           f"Привет, {message.from_user.first_name}! Я бот помогающий твоему здоровью.",
                           reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer("Выберите опцию: ", reply_markup=kbl)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in all_products:
        await message.answer(f"Название: {i[1]} | Описание: {i[2]} | Цена: {i[3]}")
        with open(f"images/{i[0]}.jpg", "rb") as img:
            await message.answer_photo(img)
    await message.answer("Выберите продукт для покупки: ", reply_markup=kbl_buy)

@dp.callback_query_handler(text="product_buying")
async def product_buying(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()



@dp.callback_query_handler(text="formulas")
async def get_formulas(call):
    await call.message.answer("для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5 \n"
                              "для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161")
    await call.answer()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    gender = State()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст: ')
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост: ')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой пол "М" или "Ж" : ')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def set_gender(message, state):
    await state.update_data(gender=message.text)
    await message.answer('Введите свой вес: ')
    await UserState.gender.set()


@dp.message_handler(state=UserState.gender)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = float(data['age'])
    growth = float(data['growth'])
    weight = float(data['weight'])
    if data['gender'] == "М":
        calories = 10 * weight + 6.25 * growth - 4.92 * age + 5
        await message.answer(f'Ваша норма калорий: {calories}')
    elif data['gender'] == "Ж":
        calories = 10 * weight + 6.25 * growth - 4.92 * age - 161
        await message.answer(f'Calories :{calories}')
    else:
        await message.answer('gender - введен не верно')
    await state.finish()


@dp.message_handler()
async def all_massage(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
