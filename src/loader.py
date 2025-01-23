from aiogram import Bot, Dispatcher
import meshtastic.serial_interface
import meshtastic.tcp_interface

from config import settings
from meshtastic_client import MeshtasticClient


interface = meshtastic.tcp_interface.TCPInterface(hostname="192.168.0.8")
node = meshtastic.Node(interface, "!938c08b4", timeout=10000)

meshtastic_client = MeshtasticClient(interface, node)

dp = Dispatcher()
bot = Bot(settings.bot_token)
