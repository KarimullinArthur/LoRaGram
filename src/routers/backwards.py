from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from routers.client import markup
from routers.client.send_message.send_message import SendMessage
from routers.client.main_menu.main_menu import MainMenu


router = Router(name=__name__)


@router.message(F.text == markup.text_button_back)
async def back(message: Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state == SendMessage.get_msg:
        await message.answer(markup.text_button_back, reply_markup=markup.main_menu())
        await state.set_state(MainMenu.main_menu)
