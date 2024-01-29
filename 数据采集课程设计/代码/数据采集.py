#!/usr/bin/env python
# coding: utf-8

# 导入所需库
import csv  # 用于 CSV 文件的读写操作
import urllib  # 用于 URL 解析
import urllib.request  # 用于 HTTP 请求
from time import sleep  # 用于添加延迟
from bs4 import BeautifulSoup as bs  # 用于解析 HTML
from urllib.parse import urljoin  # 用于处理 URL
import pymysql  # 用于连接 MySQL 数据库
import random  # 用于生成随机数
import time  # 用于处理时间
import requests  # 用于发送 HTTP 请求
from urllib.request import urlopen, build_opener  # 用于构建 HTTP 请求
from urllib.request import Request, HTTPHandler  # 用于处理 HTTP 请求
from fake_useragent import UserAgent  # 用于生成浏览器 User-Agent
import urllib3  # 用于禁用警告

# 关闭警告
urllib3.disable_warnings()

# 获取代理 IP
def getProxy():
    res = requests.get('http://127.0.0.1:5010/get/').json()  # 从代理池获取代理 IP
    proxies = {}
    if res['https']:
        proxies['https'] = res['proxy']  # 设置 https 代理
    else:
        proxies['http'] = res['proxy']  # 设置 http 代理
    return proxies  # 返回代理 IP 字典

# 获取页面信息
def get_info(page):
    sleep(1)  # 添加延迟，防止访问过快被封禁
    url = 'https://www.cnhnb.com/p/mianfen-0-0-0-0-{}/'.format(page)  # 目标网站 URL
    proxy_ip = getProxy()['http']  # 使用随机获取的代理 IP
    print(proxy_ip)
    proxy_handler = urllib.request.ProxyHandler({"http": proxy_ip})  # 构造代理处理器对象
    opener = urllib.request.build_opener(proxy_handler, urllib.request.HTTPHandler)  # 构造一个自定义的 opener 对象
    urllib.request.install_opener(opener)
    headers = {}  # 构造请求头信息
    headers['User-Agent'] = UserAgent().chrome  # 设置浏览器 User-Agent
    headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    ############ 需修改为自己的 Cookie
    headers['Cookie'] = 'Your-Cookie-Here'  # 添加自己的 Cookie
    req = Request(url, headers=headers)  # 封装请求
    response = opener.open(req)  # 使用自定义的 opener 对象发起访问请求
    html = urllib.request.urlopen(req)
    soup = bs(html.read(), 'html.parser')
    lu = soup.find_all('div', class_='show-ctn')
    product_all = []
    for i in lu:
        product_name = i.find('h2').get_text()  # 获取产品名称
        supplier = i.find("a").get_text()  # 获取供应商
        supplier_web = i.find("a").attrs['href']  # 获取供应商网址
        product_desc = i.find('div', class_='shop-image').img.attrs['alt']  # 获取产品介绍
        product_img = i.find('div', class_='shop-image').img.attrs['src']  # 获取产品图片
        product_price = str(i.find('div', class_='shops-price').get_text()).strip().replace('\n', '').replace(' ', '')  # 获取产品价格
        addr = str(i.find('div', class_='r-shop-btm').get_text())  # 获取发货地
        mailing_ins = str(i.find('div', class_='cw-tags').get_text()).strip().replace('\n', '').replace(' ', '')  # 获取邮寄说明
        product = [product_name, supplier, supplier_web, product_desc, product_img, product_price, addr, mailing_ins]
        product_all.append(product)  # 将提取的信息添加到列表中
    return product_all  # 返回产品信息列表

# 保存到 MySQL
def save_mysql(all_data):
    conn = pymysql.connect(host='127.0.0.1', user='root', port=3306, password='123456', db='mydb', charset='utf8')  # 连接 MySQL 数据库
    cursor = conn.cursor()
    insertsql = 'insert into product_info(product_name,supplier,supplier_web,product_desc,product_img,product_price,addr,mailing_ins) value (%s,%s,%s,%s,%s,%s,%s,%s)'  # 插入数据 SQL 语句
    for data in all_data:
        data = tuple(data)
        cursor.execute(insertsql, data)  # 执行插入数据操作
    conn.commit()  # 提交事务

# 主程序入口
if __name__ == '__main__':
    lst = [i for i in range(1, 88)]  # 生成页面列表
    while len(lst) > 0:
        for i in lst:
            try:
                all_data = get_info(i)  # 获取页面信息
                print(i)
                lst.remove(i)  # 移除已爬取的页面
                save_mysql(all_data)  # 保存至 MySQL

            except:
                pass  # 忽略异常
