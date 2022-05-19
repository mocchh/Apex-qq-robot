from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.params import ArgPlainText, CommandArg,Arg
from nonebot.adapters.onebot.v11 import Message, MessageSegment, escape, Bot, Event
from nonebot.adapters import Message
from nonebot.plugin import on_keyword
import nonebot
import requests
import re
import json
help = on_keyword(['help','HELP'],priority=50)
@help.handle()
async def help_handle(bot: Bot, event: Event):
  h=("帮助信息")
  help1 = ("查询战绩/apex")
  help2 = ("查询地图轮换/map")
  help3 = ("查询商店轮换/shop")
  help4 = ("查询制造器轮换/craft")

  info=(h,help1,help2,help3,help4)

  await help.send('\n'.join(info),at_sender=True) 