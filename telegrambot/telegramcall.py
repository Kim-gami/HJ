from telegram import Bot
import asyncio

TOKEN = "8377018783:AAFno8tQxWgJLFzDf_0Dt9THV5J3LKT10oE" # BOT 의 HTTP 토큰 API 유출 시 REVOKE로 키 변경
CHAT_ID = '-4908530291'# BOT 이 입장한 채팅방의 ID : 그룹 채팅방 ID

async def main():
	bot = Bot(token=TOKEN)
	await bot.send_message(chat_id=CHAT_ID, text="window 연결 성공!!")

if __name__ == "__main__":
	asyncio.run(main())