from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from keyboards.create_inline_kb import create_inline_kb
from lexicon.lexicon import LEXICON
from lexicon.buttons import BUTTONS

router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(LEXICON[message.text])

# Этот хэндлер будет срабатывать на команду "/help"
# и отправлять пользователю сообщение со списком доступных команд в боте
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON[message.text])

# Этот хэндлер будет срабатывать на команду "/beginning"
# и отправлять пользователю главное меню
@router.message(Command(commands='beginning'))
async def process_beginning_command(message: Message):
    keyboard = create_inline_kb(3, **BUTTONS)
    await message.answer(
        text='Выберай жанр!',
        reply_markup=keyboard)

@router.callback_query(F.data == 'main_menu')
async def process_beginning_command(callback: CallbackQuery):
    keyboard = create_inline_kb(3, **BUTTONS)
    await callback.message.answer(
        text='Выберай жанр!',
        reply_markup=keyboard)
    await callback.answer()