from wechat_auto_tools import WechatAutoTools

wechat = WechatAutoTools()

# friend_permission=0-->聊天、朋友圈、微信运动
# friend_permission=1-->仅聊天
# friend_status=0-->不给他看和不看他都不勾选
# friend_status=1-->勾选不给他看
# friend_status=2-->勾选不看他
# friend_status=3-->同时勾选

# 想要添加多个人，可以写个循环，或使用提供的ui工具进行操作
wechat.add_friend(phone="想要添加的人的手机号或微信号", remarks="申请加好友时的消息(可不传)", tags="多个标签用逗号分隔",
                  friend_permission=0, friend_status=0)
