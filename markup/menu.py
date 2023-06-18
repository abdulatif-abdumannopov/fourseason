from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

contact = KeyboardButton('Contact us')
rates = KeyboardButton('Check rates')
reservation = KeyboardButton('Reservation')
cancel = KeyboardButton('Cancel')

mr = KeyboardButton('Mr')
mrs = KeyboardButton('Mrs')
ms = KeyboardButton('Ms')
dr = KeyboardButton('Dr')

mk = KeyboardButton('Make or Change Reservation')
ge = KeyboardButton('General Question')
tr = KeyboardButton('Travel Agent Inquiry')
te = KeyboardButton('Technical Support')
off = KeyboardButton('Office Of The President')
com = KeyboardButton('Comments & Concerns')
oth = KeyboardButton('Other')

rem = KeyboardButton('Reservation')
ho = KeyboardButton('Hotel')
fo = KeyboardButton('Food')
gi = KeyboardButton('Gift-Card')
lo = KeyboardButton('Loss')
je = KeyboardButton('Jet')

menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(rates).add(reservation).add(contact)

status = ReplyKeyboardMarkup(resize_keyboard=True)
status.add(mr).add(mrs).add(ms).add(dr).add(cancel)

back = ReplyKeyboardMarkup(resize_keyboard=True)
back.add(cancel)

res = ReplyKeyboardMarkup(resize_keyboard=True)
res.add(mk).add(ge).add(tr).add(te).add(off).add(com).add(oth).add(cancel)

rest = ReplyKeyboardMarkup(resize_keyboard=True)
rest.add(rem).add(ho).add(fo).add(gi).add(lo).add(je).add(oth).add(cancel)
