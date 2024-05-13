from telegram import Bot
from telegram.error import TelegramError
import asyncio
import logging
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import datetime
import time

#機器人token
token ="6050558993:AAG2bVi_nn1FR7LujWTg3uGZmDh-CBeSsW4"
#群組id
id="-1001826089044"
#url=f"https://api.telegram.org/bot{token}/getUpdates"



# 將特定檔案內容抓出
def get_message(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            message = file.read()
        return message
    
    except FileNotFoundError:
        print(f"File not found at path: {file_path}")
        return None    

message_path = "C:\go2\message.txt"
message = get_message(message_path)
    
#列出目前機器人所在的群組ID
async def main():
    bot = Bot(token=token)
    updates = await bot.get_updates()
    printed_ids = set()  # 用于存储已经打印过的 ID
    ids_to_write = []  # 用于存储要写入 TXT 文件的 ID
    for update in updates:
        if update and update.message:
            chat_id = update.message.chat.id
            if chat_id not in printed_ids:  # 检查 ID 是否已经打印过
                print("ID:", chat_id)
                printed_ids.add(chat_id)  # 将 ID 添加到已打印集合中
                ids_to_write.append(str(chat_id))  # 将 ID 添加到写入列表中

#每月1號將群組ID匯出
def write_in():
    while True:
        start_date= datetime.datetime.now()
        if start_date.day ==1:#1號才執行
            with open("C:\go2\chat_ids.txt", "w") as file:
                for chat_id in ids_to_write:
                    file.write(chat_id + "\n")
        
        else:
            print("月初才會寫入")
            time.sleep(24 * 60 * 60)  # 暂停一天
        
    

# 发送消息
async def send_message(chat_id, message):
    bot = Bot(token=token)
    try:
        await bot.send_message(chat_id=chat_id, text=message)
        logging.info(f"Message sent successfully to chat_id: {chat_id}")
    except TelegramError as e:
        logging.error(f"An error occurred while sending message to chat_id {chat_id}: {e}")

if __name__ == "__main__":
    asyncio.run(main())
    asyncio.run(send_message("-1001826089044", message))
    # write_in()
