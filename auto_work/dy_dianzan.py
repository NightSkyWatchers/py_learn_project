import uiautomator2 as u2
# https://www.youtube.com/watch?v=ZA6NOhFRaxw

d = u2.connect()

print(d.info)

d(text='抖音').click()

d(resourceId="com.ss.android.ugc.aweme:id/g=b").click()
d.send_keys(text='蜘蛛膜')

d(resourceId="com.ss.android.ugc.aweme:id/op0").click()

d(classname="com.lynx.tasm.behavior.ui.view.UIView").click()
d.swipe_ext("up", scale=0.5)

d(resourceId="com.ss.android.ugc.aweme:id/container").click()


while True:
    d(resourceId="com.ss.android.ugc.aweme:id/djf").click()
    d.swipe_ext("up", scale=0.5)
