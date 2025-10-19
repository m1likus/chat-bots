from bot.handler import Handler
import bot.telegram_client


class MessagePhoto(Handler):
    def can_handle(self, update: dict) -> bool:
        return "message" in update and "photo" in update["message"]

    def handle(self, update: dict) -> bool:
        response = bot.telegram_client.get_file(
            update["message"]["photo"][-1]["file_id"]
        )
        bot.telegram_client.downloadFile(response["file_path"])
        bot.telegram_client.sendPhoto(
            chat_id=update["message"]["chat"]["id"],
            photo=update["message"]["photo"][-1]["file_id"],
        )
        return False
