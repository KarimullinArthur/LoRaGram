from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from routers.client import markup

router = Router(name=__name__)


class MainMenu(StatesGroup):
    main_menu = State()


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.answer("Салам Аллейкум 🤙", reply_markup=markup.main_menu())
    await state.set_state(MainMenu.main_menu)
