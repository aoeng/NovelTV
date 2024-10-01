import os

import yaml
from dynaconf import Dynaconf

# 获取当前文件的绝对路径
current_dir = os.path.dirname(__file__)
# 构建配置文件的绝对路径
config_path = os.path.abspath(os.path.join(current_dir, '../config/config.yaml'))


def load_config():
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config


def edit_config(data):
    """读取yaml配置文件"""

    with open(config_path, 'w', encoding='utf-8') as file:
        yaml.dump(data, file)
