import time

import uiautomator2 as u2

# https://www.youtube.com/watch?v=ZA6NOhFRaxw

d = u2.connect(addr='fa5lifgiba6tbaug')
# 打开抖音APP

d(text='抖音').click()
# 点击搜索框
d(resourceId="com.ss.android.ugc.aweme:id/j=c").click()
d.send_keys(text='蜘蛛膜')
# 搜索
d(resourceId="com.ss.android.ugc.aweme:id/yza").click()

# 进入视频
d(text="视频，按钮").click()
# 点赞
d(className="android.widget.ImageView").click()
d.swipe_ext("up")
#
time.sleep(1)

while True:
    d(className="android.widget.ImageView").click()
    d.swipe_ext("up")
    time.sleep(1)
