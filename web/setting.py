import os
import sys

import streamlit as st

# 获取当前文件的绝对路径
# current_dir = os.path.dirname(__file__)
# # 获取项目根目录
# root_dir = os.path.dirname(current_dir)
# # 将项目根目录添加到 Python 路径中
# sys.path.append(root_dir)

from utils.helper import edit_config, load_config

# 加载配置
config = load_config()

config['source_path'] = st.text_input("资源目录", config['source_path'], help="请输入一个绝对路径")
config['stable_diffusion']['server_ip'] = st.text_input("SD_IP", config['stable_diffusion']['server_ip'],
                                                        help="SD的IP地址")
config['chatgpt']['url'] = st.text_input("AI_URL", config['chatgpt']['url'], help="AI模型的地址")
config['chatgpt']['model'] = st.text_input("AI_Model", config['chatgpt']['model'], help="AI模型的大模型名称")
config['video']['font'] = st.text_input("视频字幕字体", config['video']['font'], help="字幕的字体")
config['video']['imagemagick_path'] = st.text_input("ImageMagick", config['video']['imagemagick_path'],
                                                    help="ImageMagick的exe路径")

if st.button('保存配置'):
    edit_config(config)
