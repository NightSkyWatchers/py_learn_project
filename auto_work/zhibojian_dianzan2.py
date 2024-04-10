import random
import time

import uiautomator2 as u2

# https://www.youtube.com/watch?v=ZA6NOhFRaxw


# OPPO R9测试设备 9ec0da0b ,
# 红米测试设备 fa5lifgiba6tbaug
d = u2.connect(addr='9ec0da0b')
# 打开抖音APP

d(text='抖音').click()
# 点击右上角搜索框
d(resourceId="com.ss.android.ugc.aweme:id/j=c").click()

# 输入关键字
d.send_keys(text='二胡程程')
# 点击右侧搜索
d(resourceId="com.ss.android.ugc.aweme:id/yza").click()
time.sleep(1)
# 选中下拉列表中的首条进行搜索
# d.xpath('//*[@resource-id="com.ss.android.ugc.aweme:id/b3w"]/android.widget.FrameLayout[1]').click()

# 进入直播间
d(className="com.lynx.tasm.behavior.ui.view.UIView").click()

if __name__ == '__main__':
    t = 0
    while True:
        d.click(0.907, 0.822)
        # d(resourceId="com.ss.android.ugc.aweme:id/r+i").click()
        # time.sleep(0.05)
        t += 1
        if t % 10 == 0:
            t2 = random.randint(1, 2)
            time.sleep(t2)
            print(f'已点赞{t}次，休眠{t2}s')
        # time.sleep(0.5)
