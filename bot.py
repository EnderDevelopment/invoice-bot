import discord
import os
import re
import pytesseract
from PIL import Image
import numpy as np
import cv2
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
TARGET_CHANNEL_ID = int(os.getenv('TARGET_CHANNEL_ID'))
PERCENTAGE = float(os.getenv('PERCENTAGE'))

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.channel.id != int(os.getenv('TARGET_CHANNEL_ID')):
        return
        for attachment in message.attachments:
            if attachment.filename.lower().endswith(('png', 'jpg', 'jpeg')):
                await process_image(attachment.url, message.channel)

async def process_image(image_url, channel):
    try:
        # Download the image
        image_data = await web_fetch(image_url)
        image = Image.open(BytesIO(image_data))
        
        # Preprocess the image for better OCR results
        image = preprocess_image(image)
        
        # Extract text using pytesseract
        text = pytesseract.image_to_string(image)
        
        # Extract amounts from the text
        amounts = extract_amounts(text)
        
        if amounts:
            total = sum(amounts)
            discounted_total = total * (1 - PERCENTAGE / 100)
            await channel.send(f"Total amount: {total:.2f}")
            await channel.send(f"Discounted total ({PERCENTAGE}%): {discounted_total:.2f}")
        else:
            await channel.send("No amounts found in the image.")
    except Exception as e:
        await channel.send(f"An error occurred: {e}")

def preprocess_image(image):
    # Convert to grayscale
    image = image.convert('L')
    
    # Convert to numpy array
    image_np = np.array(image)
    
    # Apply thresholding
    _, image_np = cv2.threshold(image_np, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Convert back to PIL Image
    image = Image.fromarray(image_np)
    
    return image

def extract_amounts(text):
    # Regular expression to find amounts in the text
    amount_pattern = re.compile(r'\b\d+\.\d{2}\b')
    amounts = [float(amount) for amount in amount_pattern.findall(text)]
    return amounts

client.run(DISCORD_TOKEN)