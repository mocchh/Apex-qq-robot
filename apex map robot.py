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
map = on_keyword(['map','MAP'],priority=50)
@map.handle()
async def map_handle(bot: Bot, event: Event):

  URL = f"https://api.mozambiquehe.re/maprotation?auth=979d0a73104cc447ebf3cd264030a319"
  res = requests.get(URL)
  jsonobj = json.loads(res.text)
  pname = jsonobj['current']['map'] 
  plevel = jsonobj['current']['readableDate_end'] 
  prankscore = jsonobj['next']['map'] 
  prankname = jsonobj['next']['readableDate_start']

  name = "当前地图：" + pname
  level = "结束于：" + plevel
  rankscore = "下一个地图：" + prankscore
  rankname = "开始于：" + prankname

  info=(name,level,rankscore,rankname)



  await map.send('\n'.join(info))  