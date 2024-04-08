from wechatpayv3 import WeChatPay, WeChatPayType
from flask import Flask

app = Flask(__name__)

# 微信支付商户号
MCHID = '1230000109'
# 商户证书私钥
with open('path_to_key/apiclient_key.pem') as f:
    PRIVATE_KEY = f.read()
# 商户证书序列号
CERT_SERIAL_NO = '444F4864EA9B34415...'
# API v3密钥， https://pay.weixin.qq.com/wiki/doc/apiv3/wechatpay/wechatpay3_2.shtml
APIV3_KEY = 'MIIEvwIBADANBgkqhkiG9w0BAQE...'
# APPID
APPID = 'wxd678efh567hg6787'
# 回调地址，也可以在调用接口的时候覆盖
NOTIFY_URL = 'https://www.weixin.qq.com/wxpay/pay.php'
# 微信支付平台证书缓存目录
CERT_DIR = './cert'


wxpay = WeChatPay(
    wechatpay_type=WeChatPayType.MINIPROG,
    mchid=MCHID,
    private_key=PRIVATE_KEY,
    cert_serial_no=CERT_SERIAL_NO,
    apiv3_key=APIV3_KEY,
    appid=APPID,
    notify_url=NOTIFY_URL,
    cert_dir=CERT_DIR)




# 统一下单
@app.route('/wechat_pay')
def pay():
    code, message = wxpay.pay(
        description='demo-description',
        out_trade_no='demo-trade-no',
        amount={'total': 100},
        payer={'openid': 'demo-openid'}
    )
    print('code: %s, message: %s' % (code, message))

# 订单查询
@app.route('/wechat_query')
def query():
    code, message = wxpay.query(
        transaction_id='demo-transation-id'
    )
    print('code: %s, message: %s' % (code, message))

# 关闭订单
@app.route('/wechat_close')
def close():
    code, message = wxpay.close(
        out_trade_no='demo-out-trade-no'
    )
    print('code: %s, message: %s' % (code, message))

# 申请退款
def refund():
    code, message=wxpay.refund(
        out_refund_no='demo-out-refund-no',
        amount={'refund': 100, 'total': 100, 'currency': 'CNY'},
        transaction_id='1217752501201407033233368018'
    )
    print('code: %s, message: %s' % (code, message))


if __name__ == '__main__':
    app.run(port=5003)