from wechat_auto_tools import WechatAutoTools, MessageProcessorType, AIProviderInterface

wechat = WechatAutoTools()

filtration_set = {"XX领导", "测试", "测试2"}
# 在filtering_object参数中定义想要过滤的对象，当过滤集合中的人发消息给你时，系统不会帮你处理

# default_reply_message参数的值是指，当你的消息处理器无法处理这条消息时，系统会使用你定义的默认消息进行回复

# MessageProcessorType目前有两种类型，一种是KEYWORDS，也就是关键字类型，当你定义这种消息处理器类型时，你需要调用init_keyword_reply_dbbase方法
# 示例：
keyword_dict = {
    "你好": "你好呀！很高兴见到你。",
    "再见": "再见啦，期待下次聊天！",
    "帮助": "你可以输入：你好1 / 再见 / 帮助",
}
# 此时程序会使用你提供的这个字典进行回复
wechat.init_keyword_reply_dbbase("session", keyword_dict)


# 第二种类型是AI，Ai类型的消息处理器，但实际上你也可以理解成是一个自定义的消息类型处理器，当你想使用这个处理器时，请查看以下示例：

class OpenAIProvider(AIProviderInterface):
    def chat(self, message: str) -> str:
        # message是程序帮你拿到聊天人的消息，你可以对该消息进行处理，并回复你想要回复的消息
        # 比如在此处，你可以把消息发给ai，调用ai接口，然后拿到ai给你返回的消息进行回复
        # 调用ai接口
        # 拿到消息
        return "ai接口返回的消息"


provider = OpenAIProvider()
# 此时程序会使用你自定义的消息处理器返回的消息进行回复
wechat.load_custom_ai_reply_interface("session", provider)
# 当然你也可以把类定义在别的文件中，比如：D:\\PythonProject\\demo\\global_listen.py
wechat.load_custom_ai_reply_interface_by_file_path("session", "D:\\PythonProject\\demo\\global_listen.py")

# start_session_listen是启动全局监听的关键函数，执行之后程序会开始监听全局的消息，但如果你调用该方法时，调用完主线程就死掉的话，该方法也会停止
# 因此需要调用maintain_main_thread_heartbeat函数维持主线程心跳。如果你调用该方法的线程始终存活，就无需执行该函数
wechat.start_session_listen(MessageProcessorType.AI, filtering_object=filtration_set, default_reply_message="默认消息")
wechat.maintain_main_thread_heartbeat()
