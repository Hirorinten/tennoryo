import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

df = pd.read_csv('locate.csv', encoding='shift_jis')

tenno_name = '001jinmu'

tenno = df['name1'][df['name'] == tenno_name].iloc[-1]

title_left, title_middle, title_right = st.columns([2,6,3])#, width=[100,100,100])#, widths=[200,200])

title_left.write('天皇陵')
if title_left.button('[神武天皇陵]'):
    tenno_name = '001jinmu'
    tenno = '神武天皇陵'
if title_left.button('[綏靖天皇陵]'):
    tenno_name = '002suizei'
    tenno = '綏靖天皇陵'
#if title_left.button('[崇神天皇陵]'):
#    tenno_name = '003sujin'
#    tenno = '崇神天皇陵'
#if title_left.button('[景行天皇陵]'):
#    tenno_name = '004keikou'
#    tenno = '景行天皇陵'
if title_left.button('[応神天皇陵]'):
    tenno_name = '005oujin'
    tenno = '応神天皇陵'
if title_left.button('[清寧天皇陵]'):
    tenno_name = '006seinei'
    tenno = '清寧天皇陵'    
if title_left.button('[仁賢天皇陵]'):
    tenno_name = '007ninken'
    tenno = '仁賢天皇陵'
if title_left.button('[安閑天皇陵]'):
    tenno_name = '008ankan'
    tenno = '安閑天皇陵'
if title_left.button('[敏達天皇陵]'):
    tenno_name = '009bidatu'
    tenno = '敏達天皇陵'
if title_left.button('[用明天皇陵]'):
    tenno_name = '010youmei'
    tenno = '用明天皇陵'
if title_left.button('[推古天皇陵]'):
    tenno_name = '011suiko'
    tenno = '推古天皇陵'
if title_left.button('[天智天皇陵]'):
    tenno_name = '012tenji'
    tenno = '天智天皇陵'
if title_left.button('[天武天皇・持統天皇陵]'):
    tenno_name = '013tenmujitou'
    tenno = '天武天皇・持統天皇陵'
if title_left.button('[六条天皇・高倉天皇陵]'):
    tenno_name = '014rokujotakakura'
    tenno = '六条天皇・高倉天皇陵'
if title_left.button('[仲恭天皇陵]'):
    tenno_name = '015chukyo'
    tenno = '仲恭天皇陵'
if title_left.button('[後堀河天皇陵]'):
    tenno_name = '016gohorikawa'
    tenno = '後堀河天皇陵'
if title_left.button('[四條天皇陵、他]'):
    tenno_name = '017shijou'
    tenno = '四條天皇陵、他'
if title_left.button('[後醍醐天皇陵]'):
    tenno_name = '018godaigo'
    tenno = '後醍醐天皇陵'
if title_left.button('[後村上天皇陵]'):
    tenno_name = '019gomurakami'
    tenno = '後村上天皇陵'
if title_left.button('[孝明天皇陵]'):
    tenno_name = '020koumei'
    tenno = '孝明天皇陵'
if title_left.button('[大正天皇陵]'):
    tenno_name = '021taisho'
    tenno = ''
if title_left.button('[昭和天皇陵]'):
    tenno_name = '022showa'
    tenno = '昭和天皇陵'

title_middle.title(tenno) 
title_middle.write(df['yomi'][df['name'] == tenno_name].iloc[-1])
title_middle.write('別名：' + df['name2'][df['name'] == tenno_name].iloc[-1])

img_haisho = Image.open('haisho/'+tenno_name+'.png')
title_middle.image(img_haisho, caption='拝所')#, use_column_width=True)
img_2 = Image.open('haisho/'+tenno_name+'2.png')
title_middle.image(img_2, caption='遠景等')#, use_column_width=True)
title_middle.header('【基本情報】')
items = ['時代','形','墳丘長','出土品','その他']
title_middle.write("\n".join([f"- {item}" for item in items]))

title_right.write('所在地：' + df['address'][df['name'] == tenno_name].iloc[-1])
#title_right.image('conter/c' + tenno_name +'.png', caption='地形図')#, use_column_width=True)
img_goryoin = Image.open('goryoin/'+ tenno_name +'.png')
#title_right.image(img_goryoin, caption=tenno + '御陵印')#, use_column_width=True)
title_right.image(img_goryoin, caption='御陵印')#, use_column_width=True)

df_map=df[df['name'] == tenno_name].iloc[0:1]
title_right.map(df_map)
