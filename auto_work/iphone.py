
# d = u2.connect(addr='http://localhost:8300/')
import wda_python as wda

wda.DEBUG=True

# c=wda.USBClient(udid='00008020-000561443CC2002E', port=8300, wda_bundle_id='com.facebook.WebDriverAgentRunner.davis.xctrunner')

c=wda.USBClient()

s=c.session()

s.click(0.374, 0.375)
