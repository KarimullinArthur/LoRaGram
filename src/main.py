import asyncio
import logging
import sys

from routers import router_manager
from loader import *


async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    dp.include_routers(*list(router_manager._routers.values()))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
