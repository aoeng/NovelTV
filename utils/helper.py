import yaml


def edit_config(data):
    """读取yaml配置文件"""
    with open('./../config/config.yaml', 'w', encoding='utf-8') as file:
        yaml.dump(data, file)
