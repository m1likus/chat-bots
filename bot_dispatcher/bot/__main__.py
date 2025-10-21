from bot.dispatcher import Dispatcher
from bot.handlers.message_echo import MessageEcho
from bot.handlers.message_photo import MessagePhoto
from bot.handlers.database_logger import UpdateDatabaseLogger
from bot.long_polling import start_long_polling


def main() -> None:
    try:
        dispatcher = Dispatcher()
        dispatcher.add_handler(UpdateDatabaseLogger())
        dispatcher.add_handler(MessageEcho())
        dispatcher.add_handler(MessagePhoto())
        start_long_polling(dispatcher)
    except KeyboardInterrupt:
        print("\nBye!")


if __name__ == "__main__":
    main()
