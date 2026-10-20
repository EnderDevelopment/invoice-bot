# InvoiceBot

InvoiceBot is a Discord bot designed to monitor screenshots in specified channels, extract invoice amounts from these screenshots, calculate the total, and apply a user-defined percentage discount. This bot is ideal for businesses or individuals who need to manage and track invoice amounts efficiently within their Discord communities.

## Install

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/InvoiceBot.git
   cd InvoiceBot
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Rename `.env.example` to `.env` and fill in the required values:
   ```env
   DISCORD_TOKEN=your_discord_bot_token_here
   TARGET_CHANNEL_ID=your_target_channel_id_here
   PERCENTAGE=your_percentage_here
   ```

## Use

1. Invite the bot to your Discord server using the OAuth2 URL generated from the Discord Developer Portal.

2. Ensure the bot has the necessary permissions to read messages and attachments in the specified channel.

3. Run the bot:
   ```bash
   python bot.py
   ```

4. Upload screenshots containing invoice amounts to the specified channel. The bot will process the images, extract the amounts, calculate the total, and apply the discount, then send the results back to the channel.

---

More Discord bot projects by EnderDevelopment: https://github.com/EnderDevelopment

Project page: https://dash.enderdevelopment.com/community/303be977-a9f8-4cf5-85ed-8dd0c7121651?utm_source=github&utm_medium=readme&utm_campaign=auto_publish&utm_content=303be977-a9f8-4cf5-85ed-8dd0c7121651
