import fortnitepy
import asyncio
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FortniteLobbyBot:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.client = fortnitepy.Client(email=email, password=password)

    async def login(self):
        try:
            await self.client.start()
            logger.info("Logged in as %s", self.client.user.display_name)
        except fortnitepy.AuthException as e:
            logger.error("Failed to login: %s", e)

    async def equip_item(self, item_id):
        try:
            await self.client.party.me.set_outfit(asset=item_id)
            logger.info("Equipped item: %s", item_id)
        except Exception as e:
            logger.error("Failed to equip item: %s", e)

    async def run(self):
        await self.login()
        # Example of equipping an item
        await self.equip_item('CID_001_Athena_Commando_F_Default')

def main():
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')

    if not email or not password:
        logger.error("Email and password must be set as environment variables")
        return

    bot = FortniteLobbyBot(email, password)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot.run())

if __name__ == '__main__':
    main()