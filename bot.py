import logging
from aiogram import Bot, Dispatcher, executor, types
import random
from scipy.stats import norm
API_TOKEN='8827925639:AAELuOG_inIK_xMaKSXbfYd1xBlD0do3NAE'
logging.basicConfig(level=logging.INFO)
bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
 await message.reply("🔥 BlackUnderBot wajed! /signal")
@dp.message_handler(commands=['signal'])
async def signal_cmd(message: types.Message):
 prob=norm.cdf(random.uniform(0,2))
 coeff=round(random.uniform(1.5,5.5),2)
 await message.reply(f"🚀 SIGNAL: {coeff}x - {int(prob*100)}%")
if __name__=='__main__':
 executor.start_polling(dp, skip_updates=True)
