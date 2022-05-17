import requests
import json
import PIL.Image as Image
import os
import nonebot
from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.params import ArgPlainText, CommandArg,Arg
from nonebot.adapters.onebot.v11 import Message, MessageSegment, escape, Bot, Event
from nonebot.adapters import Message
from nonebot.plugin import on_keyword

craft = on_keyword(['shop','SHOP'],priority=50)
@craft.handle()
async def craft_handle(bot: Bot, event: Event):
  await craft.send('正在查询今日换色，请稍候', at_sender=True)

  URL = "https://api.mozambiquehe.re/store?auth=979d0a73104cc447ebf3cd264030a319"
  res = requests.get(URL)
  jsonobj = json.loads(res.text)

  assets = [jsonobj[4]["asset"]]
  assets2 = [jsonobj[5]["asset"]]
#获取URL
  pic1 = assets[0]
  pic2 = assets2[0]


  url1 = pic1

  r = requests.get(url1)

  image = r.content

  with open('1.jpg','wb') as f:
      f.write(image)


  url2 = pic2

  r = requests.get(url2)

  image = r.content

  with open('2.jpg','wb') as f:
      f.write(image)

#下载图片

 
  IMAGES_PATH = 'E:\qqbot\mobot\\'  # 图片集地址
  IMAGES_FORMAT = ['.jpg', '.JPG']  # 图片格式
  IMAGE_SIZE = 256  # 每张小图片的大小
  IMAGE_ROW = 1  # 图片间隔，也就是合并成一张图后，一共有几行
  IMAGE_COLUMN = 2  # 图片间隔，也就是合并成一张图后，一共有几列
  IMAGE_SAVE_PATH = 'E:\qqbot\mobot\\shopfinal.png'  # 图片转换后的地址
 
# 获取图片集地址下的所有图片名称
  image_names = [name for name in os.listdir(IMAGES_PATH) for item in IMAGES_FORMAT if
               os.path.splitext(name)[1] == item]
 
# 简单的对于参数的设定和实际图片集的大小进行数量判断
  if len(image_names) != IMAGE_ROW * IMAGE_COLUMN:
    raise ValueError("合成图片的参数和要求的数量不能匹配！")
 
# 定义图像拼接函数
  def image_compose():
    to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_SIZE, IMAGE_ROW * IMAGE_SIZE)) #创建一个新图
    # 循环遍历，把每张图片按顺序粘贴到对应位置上
    for y in range(1, IMAGE_ROW + 1):
        for x in range(1, IMAGE_COLUMN + 1):
            from_image = Image.open(IMAGES_PATH + image_names[IMAGE_COLUMN * (y - 1) + x - 1]).resize(
                (IMAGE_SIZE, IMAGE_SIZE),Image.ANTIALIAS)
            to_image.paste(from_image, ((x - 1) * IMAGE_SIZE, (y - 1) * IMAGE_SIZE))
    return to_image.save(IMAGE_SAVE_PATH) # 保存新图
  image_compose() #调用函数

  await craft.send(MessageSegment.image('file:///E:/qqbot/mobot/shopfinal.png'))