
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message, KeyboardButton, ReplyKeyboardMarkup
from keyboards.create_inline_kb import create_inline_kb
from lexicon.buttons import AMBIENT_BUTTONS
from aiogram.types.web_app_info import WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keyboards.pagination_kb import create_pagination_keyboard
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile
from services.file_handling import get_part_text


router = Router()

@router.callback_query(F.data == 'ambient')
async def process_beginning_command(callback: CallbackQuery):
    await callback.message.answer(
        text=get_part_text(r'electronics_without_limits\music_guide\ambient\ambient.txt'),
        reply_markup=create_pagination_keyboard('play','derived_styles_ambient','backward'))
    await callback.answer()

@router.callback_query(F.data == 'derived_styles_ambient')
async def process_beginning_command(callback: CallbackQuery):
    keyboard = create_inline_kb(3, **AMBIENT_BUTTONS)
    await callback.message.answer(
        text='Выбирай жанр!',
        reply_markup=keyboard)
    await callback.answer()

@router.callback_query(F.data == 'ambient_dub')
async def process_beginning_command(callback: CallbackQuery):
    await callback.message.answer(
        text=get_part_text(r'electronics_without_limits\music_guide\ambient\ambient_dub.txt'),
        reply_markup=create_pagination_keyboard('play','backward','main_menu'))
    await callback.answer()