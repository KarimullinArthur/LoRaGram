from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.enums.chat_action import ChatAction

from routers.client import markup
from loader import bot, meshtastic_client

router = Router(name=__name__)


class SendMessage(StatesGroup):
    get_msg = State()


@router.message(F.text == markup.text_button_send_message)
async def send_message(message: Message, state: FSMContext):
    await message.answer("Отправь текстовое сообщение", reply_markup=markup.back())
    await state.set_state(SendMessage.get_msg)


@router.message(lambda message: message.text is not None)
async def get_mgs(message: Message):
    await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    if await meshtastic_client.send_message_as("TEST", str(message.text)):
        await message.answer("Отправил!")
    else:
        await message.answer("Что-то пошло не так(")

