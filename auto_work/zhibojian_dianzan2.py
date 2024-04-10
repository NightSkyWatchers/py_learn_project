import time

import uiautomator2 as u2

# https://www.youtube.com/watch?v=ZA6NOhFRaxw

d = u2.connect(addr='fa5lifgiba6tbaug')
# 打开抖音APP

# d(text='抖音').click()
# # 点击搜索框
# d(resourceId="com.ss.android.ugc.aweme:id/j=c").click()
# d.send_keys(text='二胡直播')
# # 搜索
# d(resourceId="com.ss.android.ugc.aweme:id/yza").click()
# time.sleep(1)
# # 确定
# d.xpath('//*[@resource-id="com.ss.android.ugc.aweme:id/b3w"]/android.widget.FrameLayout[1]').click()
#
# # 进入直播间
# d(className="android.widget.FrameLayout").click()


if __name__ == '__main__':
    t = 0
    while True:
        d(resourceId="com.ss.android.ugc.aweme:id/r+i").click()
        time.sleep(0.1)
        d(resourceId="com.ss.android.ugc.aweme:id/r+i").click()
        t += 1
        print(f'点赞{t}次')
        time.sleep(0.5)
