import random
import time

import requests


url = 'https://live.douyin.com/webcast/room/like/?aid=6383&app_name=douyin_web&live_id=1&device_platform=web&language=zh-CN&enter_from=page_refresh&cookie_enabled=true&screen_width=1280&screen_height=800&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Chrome&browser_version=123.0.0.0&room_id=7355825862882888502&count=1&msToken=rHmxhxrUOZy3y-hYJXTs-LOK4lSfvQe9omafHFAvs6Z2P7dUNKR0j_xMqFCTSJqYddFKuEI7vOVFDmFgCM8TLmg38TVaEnNZTBqYBR5LKDNbysmLzOMv7L7NSm5jXxMp&a_bogus=DyW0%2FVgDDkDBkDWZ565LfY3q6vKJYMCU0tLVMD2fEInAfg39HMY59exYX-XvxsujLT%2FAIeLjy4hbTNaMi5dGA3v378DKWoAZ-g00te%2FQ5xSSs1XJtyUgnzwNmktUCec2Rv3lrOXBoJKCKm00AIee-wHvyhnFwo8sNike'

headers = {
    # ":authority": "live.douyin.com",
    # ":method": "POST",
    # ":path": "/webcast/room/like/?aid=6383&app_name=douyin_web&live_id=1&device_platform=web&language=zh-CN&enter_from=page_refresh&cookie_enabled=true&screen_width=1280&screen_height=800&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Chrome&browser_version=123.0.0.0&room_id=7355825862882888502&count=1&msToken=rHmxhxrUOZy3y-hYJXTs-LOK4lSfvQe9omafHFAvs6Z2P7dUNKR0j_xMqFCTSJqYddFKuEI7vOVFDmFgCM8TLmg38TVaEnNZTBqYBR5LKDNbysmLzOMv7L7NSm5jXxMp&a_bogus=YvWMMRg6DE6BffS2565LfY3q6vKJYMCd0tLVMD2fEInAjy39HMYk9exYX5TvdqyjLT%2FAIeLjy4hbTNaMi5dGA3v378DKWoAZ-g00te%2FQ5xSSs1XJtyUgnzwNmktUCec2Rv3lrOXBoJKCKm00AIee-wHvyhnFwo8sNidp",
    # ":scheme": "https",
    # "Accept": "application/json, text/plain, */*",
    # "Accept-Encoding": "gzip, deflate, br, zstd",
    # "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    # "Content-Type": "application/json",
    "Cookie": "__ac_nonce=066153acb00c083f782a6; __ac_signature=_02B4Z6wo00f01BMgOeAAAIDA0ING5uCPmxATAD1AAGLjTvstGgtxlRmjv0KQZjnRtteL1-e.bCLcN-BpzYWtA1U-X2nd38seSzA2k4j6bpbKptYw5Z2RxP70MOqwBBFWhdeIRANcOWgCcGida1; ttwid=1%7CfCwl_vJqZJ0kmFev1H6w6QAQf5ba-G0IcXibEg3YjRc%7C1712667339%7C22b7b1d5d30b5826af8028c92ddc9e7103d729307046f4eefc546ec95bb9217d; __live_version__=%221.1.1.9453%22; has_avx2=null; device_web_cpu_core=2; device_web_memory_size=8; webcast_local_quality=null; live_use_vvc=%22false%22; xgplayer_user_id=761554724775; csrf_session_id=79a9456f2732e590a56015cf5cb0763d; webcast_leading_last_show_time=1712667344515; webcast_leading_total_show_times=1; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; bd_ticket_guard_client_web_domain=2; passport_csrf_token=64c0f5be0859e7ad72cd81a064c0e820; passport_csrf_token_default=64c0f5be0859e7ad72cd81a064c0e820; passport_assist_user=CkFVcocFReO3J8Serw9BbHdiZj_knnfCymLGQn03e_K7ojRu0q9ebIIgbJgpol71lX0FwX0tkdvo9VcHWrvToV6WNxpKCjxgGBcoUbPKvQ7j8PYOfTblQWGnPmssdoMiuVn4N4K1g3Jps2y75h9J6Hjy6EKzkf0pd_Un7r1JUgH1QRsQoZvODRiJr9ZUIAEiAQNkXWuq; n_mh=MxzZcNpOUfxxPu4KN9U8byzch5UopddycJhzskkc7RU; sso_uid_tt=9a7a2df6e955d6e1c011a545a8f37c7f; sso_uid_tt_ss=9a7a2df6e955d6e1c011a545a8f37c7f; toutiao_sso_user=bad093983ecd84227786b4fe98eb3f0a; toutiao_sso_user_ss=bad093983ecd84227786b4fe98eb3f0a; sid_ucp_sso_v1=1.0.0-KGI2ZTJlZWNlMTNkMzQ5N2RjMWUwM2I0OTc1MTM3ZTFjYmY4NzNjNjQKHwi8srC-kPTJBRDu9dSwBhjvMSAMMKGOwvAFOAZA9AcaAmxxIiBiYWQwOTM5ODNlY2Q4NDIyNzc4NmI0ZmU5OGViM2YwYQ; ssid_ucp_sso_v1=1.0.0-KGI2ZTJlZWNlMTNkMzQ5N2RjMWUwM2I0OTc1MTM3ZTFjYmY4NzNjNjQKHwi8srC-kPTJBRDu9dSwBhjvMSAMMKGOwvAFOAZA9AcaAmxxIiBiYWQwOTM5ODNlY2Q4NDIyNzc4NmI0ZmU5OGViM2YwYQ; passport_auth_status=cd39804035de85f547e31a14e92f33d4%2C; passport_auth_status_ss=cd39804035de85f547e31a14e92f33d4%2C; uid_tt=349a3f3c8faea10aa8c5269ba5b22134; uid_tt_ss=349a3f3c8faea10aa8c5269ba5b22134; sid_tt=7e37a2f5df7acdd1c8d75d1ae0b66cbe; sessionid=7e37a2f5df7acdd1c8d75d1ae0b66cbe; sessionid_ss=7e37a2f5df7acdd1c8d75d1ae0b66cbe; xg_device_score=5.493529411764706; live_can_add_dy_2_desktop=%221%22; passport_fe_beating_status=true; IsDouyinActive=true; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=53c724407185762d7169cdd69f6c0fd8; __security_server_data_status=1; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCT29LR1dFMVh6YzRLaDZTNzAxYmVBVGY1YTZFTUlIY3U1QWZWRSsveUkxVmd3QkFjUzlvRms0WVV5TEQ1OVNIR01yUkhKTEZmNGNxQTVrL3lmTkppSGs9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; sid_guard=7e37a2f5df7acdd1c8d75d1ae0b66cbe%7C1712667385%7C5183992%7CSat%2C+08-Jun-2024+12%3A56%3A17+GMT; sid_ucp_v1=1.0.0-KDNiNGFmMmI0YTg4MWQxM2IzZmE4OGI5NzdhNTZlMDY4YTYxMGQxMDMKGwi8srC-kPTJBRD59dSwBhjvMSAMOAZA9AdIBBoCbHEiIDdlMzdhMmY1ZGY3YWNkZDFjOGQ3NWQxYWUwYjY2Y2Jl; ssid_ucp_v1=1.0.0-KDNiNGFmMmI0YTg4MWQxM2IzZmE4OGI5NzdhNTZlMDY4YTYxMGQxMDMKGwi8srC-kPTJBRD59dSwBhjvMSAMOAZA9AdIBBoCbHEiIDdlMzdhMmY1ZGY3YWNkZDFjOGQ3NWQxYWUwYjY2Y2Jl; publish_badge_show_info=%220%2C0%2C0%2C1712667385674%22; odin_tt=850ee80e6369b5535c3a6966a2381bb6cc879b09688bde9b35297a709fed26bdd5c7b0406c1e23d78993372b9066aa6ba2ee2cb20d0d67611416790a53a675b0; download_guide=%221%2F20240409%2F0%22; msToken=qfVPc1rLTUvfsPXEFGuftqbBC0XDcVhAERNyAzBIfC9hDxaz-HCOWwT77IYoQD0O05wmRN6gTFAM9Od81LXfwVlZLA6rXolatQICeFDpWOwMpfwU-t4LiOXToOQP6DBO; pwa2=%220%7C0%7C1%7C0%22",
    "Origin": "https://live.douyin.com",
    "Referer": "https://live.douyin.com/560837938830",
    # "Sec-Ch-Ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
    # "Sec-Ch-Ua-Mobile": "?0",
    # "Sec-Ch-Ua-Platform": "\"macOS\"",
    # "Sec-Fetch-Dest": "empty",
    # "Sec-Fetch-Mode": "cors",
    # "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "X-Secsdk-Csrf-Token": "000100000001c36da69668e6e930197aed878cd32fde4f394e2bbefcba069ad9cfd05cec1bc617c49de872166c08"
}

data = {
    "aid": "6383",
    "app_name": "douyin_web",
    "live_id": "1",
    "device_platform": "web",
    "language": "zh-CN",
    "enter_from": "page_refresh",
    "cookie_enabled": "true",
    "screen_width": "1280",
    "screen_height": "800",
    "browser_language": "zh-CN",
    "browser_platform": "MacIntel",
    "browser_name": "Chrome",
    "browser_version": "123.0.0.0",
    "room_id": "7355825862882888502",
    "count": "1",
    "msToken": "rHmxhxrUOZy3y-hYJXTs-LOK4lSfvQe9omafHFAvs6Z2P7dUNKR0j_xMqFCTSJqYddFKuEI7vOVFDmFgCM8TLmg38TVaEnNZTBqYBR5LKDNbysmLzOMv7L7NSm5jXxMp",
    "a_bogus": "YvWMMRg6DE6BffS2565LfY3q6vKJYMCd0tLVMD2fEInAjy39HMYk9exYX5TvdqyjLT%2FAIeLjy4hbTNaMi5dGA3v378DKWoAZ-g00te%2FQ5xSSs1XJtyUgnzwNmktUCec2Rv3lrOXBoJKCKm00AIee-wHvyhnFwo8sNidp"
}
if __name__ == '__main__':
    session = requests.Session()
    t = 0
    while True:
        result = session.post(url=url,headers=headers)
        # print(result.text)
        t += 1
        print(f'已点赞{t}次')
        if t % 10 == 0:
            time.sleep(random.randint(3, 5))
        else:
            time.sleep(1)
