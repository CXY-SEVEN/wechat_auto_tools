from wechat_auto_tools import WechatAutoTools, MessageProcessorType, AIProviderInterface, ListenObjectType

wechat = WechatAutoTools()

# 群聊监听示例
keyword_dict = {
    "你好": "你好呀！很高兴见到你。",
    "再见": "再见啦，期待下次聊天！",
    "帮助": "你可以输入：你好1 / 再见 / 帮助",
}
# 把想要监听的群聊添加到消息监听队列
wechat.add_message_listen_queue(listen_object="监听的群聊的名称", listen_object_type=ListenObjectType.GROUP,
                                message_processor_type=MessageProcessorType.KEYWORDS, default_message="默认消息")
wechat.init_keyword_reply_dbbase("监听的群聊的名称", keyword_dict)
# 好友监听示例
wechat.add_message_listen_queue(listen_object="监听的好友的名称", listen_object_type=ListenObjectType.FRIEND,
                                message_processor_type=MessageProcessorType.KEYWORDS, default_message="默认消息")
wechat.init_keyword_reply_dbbase("监听的好友的名称", keyword_dict)
# 开启消息监听
wechat.start_message_listen()
# 维持主线程心跳
wechat.maintain_main_thread_heartbeat()
