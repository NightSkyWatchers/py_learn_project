import time

import uiautomator2 as u2
# https://www.youtube.com/watch?v=ZA6NOhFRaxw

d = u2.connect(addr='fa5lifgiba6tbaug')

d(text='抖音').click()

d(resourceId="com.ss.android.ugc.aweme:id/j=c").click()
d.send_keys(text='蜘蛛膜')

d(resourceId="com.ss.android.ugc.aweme:id/yza").click()

# 进入视频
d.xpath('//*[@resource-id="com.ss.android.ugc.aweme:id/btz"]/android.widget.FrameLayout[1]/com.lynx.tasm.behavior.ui.view.UIView[3]').click()
# 点赞
d(className="android.widget.ImageView").click()
d.swipe_ext("up")
#
# d(resourceId="com.ss.android.ugc.aweme:id/container").click()
time.sleep(1)

while True:
    d(className="android.widget.ImageView").click()
    d.swipe_ext("up")
    time.sleep(1)