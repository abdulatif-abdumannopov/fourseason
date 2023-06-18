import re
from datetime import datetime, date
import requests as requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from markup.menu import *
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(os.getenv('Token'))
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)


class Rates(StatesGroup):
    firstname = State()
    lastname = State()
    phone = State()
    adult = State()
    children = State()
    start = State()
    end = State()

class Contact(StatesGroup):
    status = State()
    firstname = State()
    lastname = State()
    email = State()
    phone = State()
    reservation = State()
    text = State()

class Reservation(StatesGroup):
    status = State()
    firstname = State()
    lastname = State()
    email = State()
    reservation = State()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id, f'Hello, {message.chat.first_name}', reply_markup=menu)


@dp.message_handler(text='Cancel', state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await bot.send_message(message.chat.id, 'Canceled', reply_markup=menu)


# -----------------------------------------------Reservation-----------------------------------------#
@dp.message_handler(text='Reservation')
async def start(message: types.Message):
    await bot.send_message(message.chat.id, f'How do you want to be contacted?', reply_markup=status)
    await Reservation.status.set()

@dp.message_handler(state=Reservation.status)
async def start(message: types.Message, state: FSMContext):
    if message.text not in ['Mr', 'Ms', 'Mrs', 'Dr']:
        await bot.send_message(message.chat.id, f'Please, choose from menu', reply_markup=status)
        return
    await state.update_data(status=message.text)
    await bot.send_message(message.chat.id, f'Write your first name:', reply_markup=back)
    await Reservation.firstname.set()


@dp.message_handler(state=Reservation.firstname)
async def start(message: types.Message, state: FSMContext):
    if len(message.text) > 100:
        await bot.send_message(message.chat.id, f'In your name more than 100 simbols.\nPlease enter your name again:', reply_markup=back)
        return
    await state.update_data(firstname=message.text)
    await bot.send_message(message.chat.id, f'Write your last name:', reply_markup=back)
    await Reservation.lastname.set()


@dp.message_handler(state=Reservation.lastname)
async def start(message: types.Message, state: FSMContext):
    if len(message.text) > 100:
        await bot.send_message(message.chat.id, f'In your lastname more than 100 simbols.\nPlease enter your lastname again:', reply_markup=back)
        return
    await state.update_data(lastname=message.text)
    await bot.send_message(message.chat.id, f'Write your email, (example@exmple.com):', reply_markup=back)
    await Reservation.email.set()

@dp.message_handler(state=Reservation.email)
async def start(message: types.Message, state: FSMContext):
    email = message.text.strip()

    if ' ' in email:
        await bot.send_message(message.chat.id, "There shouldn't be a spaces. Please enter a valid email address.")
        return

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        await bot.send_message(message.chat.id, "Invalid email format. Please enter a valid email address.")
        return

    await state.update_data(email=email)
    await bot.send_message(message.chat.id, "Choose reservation:", reply_markup=rest)
    await Reservation.reservation.set()

@dp.message_handler(state=Reservation.reservation)
async def start(message: types.Message, state: FSMContext):
    if message.text not in ['Reservation', 'Hotel', 'Food', 'Gift-Card', 'Loss', 'Jet', 'Other']:
        await bot.send_message(message.chat.id, f'Please, choose from menu', reply_markup=rest)
        return
    await state.update_data(reservation=message.text)
    await bot.send_message(message.chat.id, f'Completed', reply_markup=menu)
    data = await state.get_data()
    p = requests.post('http://127.0.0.1:8000/api/v1/reservation', data)
    print(p.text, data)
    await state.finish()


# ------------------------------------------------Contact----------------------------------------------#
@dp.message_handler(text='Contact us')
async def start_contact(message: types.Message):
    await bot.send_message(message.chat.id, f'How do you want to be contacted?', reply_markup=status)
    await Contact.status.set()


@dp.message_handler(state=Contact.status)
async def start(message: types.Message, state: FSMContext):
    if message.text not in ['Mr', 'Ms', 'Mrs', 'Dr']:
        await bot.send_message(message.chat.id, f'Please, choose from menu', reply_markup=status)
        return
    await state.update_data(status=message.text)
    await bot.send_message(message.chat.id, f'Write your first name:', reply_markup=back)
    await Contact.firstname.set()


@dp.message_handler(state=Contact.firstname)
async def start(message: types.Message, state: FSMContext):
    if len(message.text) > 100:
        await bot.send_message(message.chat.id, f'In your name more than 100 simbols.\nPlease enter your name again:', reply_markup=back)
        return
    await state.update_data(firstname=message.text)
    await bot.send_message(message.chat.id, f'Write your lastname:', reply_markup=back)
    await Contact.lastname.set()


@dp.message_handler(state=Contact.lastname)
async def start(message: types.Message, state: FSMContext):
    if len(message.text) > 100:
        await bot.send_message(message.chat.id, f'In your lastname more than 100 simbols.\nPlease enter your lastname again:', reply_markup=back)
        return
    await state.update_data(lastname=message.text)
    await bot.send_message(message.chat.id, f'Write your email, (example@example.com):', reply_markup=back)
    await Contact.email.set()

@dp.message_handler(state=Contact.email)
async def start(message: types.Message, state: FSMContext):
    email = message.text.strip()
    if ' ' in email:
        await bot.send_message(message.chat.id, "There shouldn't be a spaces. Please enter a valid email address.")
        return

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        await bot.send_message(message.chat.id, "Invalid email format. Please enter a valid email address.")
        return

    await state.update_data(email=email)
    await bot.send_message(message.chat.id, "Please enter a valid phone number in the format +998xxxxxxxxx.", reply_markup=back)
    await Contact.phone.set()

@dp.message_handler(state=Contact.phone)
async def start(message: types.Message, state: FSMContext):
    phone_number = message.text.strip()
    if not re.match(r"\+998\d{9}$", phone_number):
        await bot.send_message(message.chat.id, "Invalid phone number format. Please enter a valid phone number in the format +998xxxxxxxxx.")
        return

    await state.update_data(phone=phone_number)
    await bot.send_message(message.chat.id, "Choose:", reply_markup=res)
    await Contact.reservation.set()

@dp.message_handler(state=Contact.reservation)
async def start(message: types.Message, state: FSMContext):
    if message.text not in ['Make or Change Reservation', 'General Question', 'Travel Agent Inquiry', 'Technical Support', 'Office Of The President', 'Comments & Concerns', 'Other']:
        await bot.send_message(message.chat.id, f'Please, choose from menu', reply_markup=res)
        return
    await state.update_data(reservation=message.text)
    await bot.send_message(message.chat.id, f'How we can help you?', reply_markup=back)
    await Contact.text.set()

@dp.message_handler(state=Contact.text)
async def start(message: types.Message, state: FSMContext):
    if len(message.text) > 200:
        await bot.send_message(message.chat.id, f'In text more than 200 simbols', reply_markup=back)
        return
    await state.update_data(text=message.text)
    await bot.send_message(message.chat.id, f'Completed', reply_markup=menu)
    data = await state.get_data()
    p = requests.post('http://127.0.0.1:8000/api/v1/contact', data)
    print(p.text, data)
    await state.finish()

# ------------------------------------------------Rates----------------------------------------------#
@dp.message_handler(text='Check rates')
async def start(message: types.Message):
    await bot.send_message(message.chat.id, f'Write your first name:', reply_markup=back)
    await Rates.firstname.set()


@dp.message_handler(state=Rates.firstname)
async def start(message: types.Message, state: FSMContext):
    if len(message.text) > 100:
        await bot.send_message(message.chat.id, f'In your name more than 100 simbols.\nPlease enter your name again:', reply_markup=back)
        return
    await state.update_data(firstname=message.text)
    await bot.send_message(message.chat.id, f'Write lastname:', reply_markup=back)
    await Rates.lastname.set()


@dp.message_handler(state=Rates.lastname)
async def start(message: types.Message, state: FSMContext):
    if len(message.text) > 100:
        await bot.send_message(message.chat.id, f'In your lastname more than 100 simbols.\nPlease enter your lastname again:', reply_markup=back)
        return
    await state.update_data(lastname=message.text)
    await bot.send_message(message.chat.id, f'Please enter a valid phone number in the format +998xxxxxxxxx.', reply_markup=back)
    await Rates.phone.set()


@dp.message_handler(state=Rates.phone)
async def start(message: types.Message, state: FSMContext):
    phone_number = message.text.strip()
    if not re.match(r"\+998\d{9}$", phone_number):
        await bot.send_message(message.chat.id, "Invalid phone number format. Please enter a valid phone number in the format +998xxxxxxxxx.")
        return

    await state.update_data(phone=phone_number)
    await bot.send_message(message.chat.id, "Number of adult:", reply_markup=back)
    await Rates.adult.set()


@dp.message_handler(state=Rates.adult)
async def start(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await bot.send_message(message.chat.id, "Please enter numbers.")
        return

    entered_value = int(message.text)
    if entered_value < 1:
        await bot.send_message(message.chat.id, "The value cannot be less than 1. Please enter a valid number.")
        return

    await state.update_data(adult=entered_value)
    await bot.send_message(message.chat.id, f'Number of children:',
                           reply_markup=back)
    await Rates.children.set()


@dp.message_handler(state=Rates.children)
async def start(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await bot.send_message(message.chat.id, "Please, enter numbers.")
        return

    entered_value = int(message.text)
    if entered_value < 0:
        await bot.send_message(message.chat.id, "The value can't be less than 0. Please enter a valid number.")
        return

    await state.update_data(children=int(message.text))
    await bot.send_message(message.chat.id, f'Start day, example (dd/mm/yyyy):',
                           reply_markup=back)
    await Rates.start.set()


@dp.message_handler(state=Rates.start)
async def start(message: types.Message, state: FSMContext):
    date_format = "%d/%m/%Y"
    today = date.today()
    try:
        entered_date = datetime.strptime(message.text, date_format).date()
    except ValueError:
        await bot.send_message(message.chat.id,
                               f"Incorrect date format (example, dd/mm/yyyy).")
        return

    if entered_date < today:
        await bot.send_message(message.chat.id,
                               "Past date.Please enter correct date")
        return

    await state.update_data(start=entered_date.strftime(date_format))
    await bot.send_message(message.chat.id, f'Enter end day (example, dd/mm/yyyy):', reply_markup=back)
    await Rates.end.set()


@dp.message_handler(state=Rates.end)
async def start(message: types.Message, state: FSMContext):
    date_format = "%d/%m/%Y"
    try:
        entered_date = datetime.strptime(message.text, date_format).date()
    except ValueError:
        await bot.send_message(message.chat.id,
                               "Incorrect date format (example, dd/mm/yyyy).")
        return

    today = date.today()
    if entered_date <= today:
        await bot.send_message(message.chat.id,
                               "Past date or Today.Please enter correct date")
        return

    await state.update_data(end=entered_date.strftime(date_format))
    data = await state.get_data()
    await bot.send_message(message.chat.id, f'Completed', reply_markup=menu)
    p = requests.post('http://127.0.0.1:8000/api/v1/rates', data)
    print(p.text)
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp)
