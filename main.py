import os

import discord
import dotenv

dotenv.load_dotenv()


class Client(discord.Client):

    def __init__(self):
        super().__init__()

    async def on_ready(self):
        print(self.user.name)
        print(self.user.id, "\n")

    async def on_voice_state_update(self, member, before, after):
        channel = await self.fetch_channel(os.getenv("CHANNEL_ID"))
        if before.channel is None:
            event_name = "参加"
        elif after.channel is None:
            event_name = "退出"
        message = f"{event_name}: {member.name}"
        await channel.send(message)


def main():
    client = Client()
    client.run(os.getenv("BOT_TOKEN"))


if __name__ == "__main__":
    main()
