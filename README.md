# wechat_auto_tools
一个用于实现微信自动化的python库
## 将库导入到您本地的环境中
可以使用pip install wechat_auto_tools。也可以下载我提供的wechat_auto_tools-1.0.27-py3-none-any.whl包，使用命令：pip install dist/wechat_auto_tools-1.0.27-py3-none-any.whl进行安装。

## 引用库
from wechat_auto_tools import WechatAutoTools, ListenObjectType, MessageProcessorType, AIProviderInterface

## 获取自动化工具实例
wechat = WechatAutoTools()

## 介绍
您可以使用WechatAutoTools进行一些常见的微信自动化工作。
目前提供的功能有：定时发送消息、自动添加好友、群/好友消息监听、全局消息监听。
具体的使用方法可以查看demo目录的实例。
