import streamlit as st
from dynaconf import Dynaconf

# 加载配置
settings = Dynaconf(settings_files=['./../config/config.yaml'])

