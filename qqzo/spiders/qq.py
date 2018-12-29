# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import json
from qqzo.items import QqzoItem




class QqSpider(scrapy.Spider):
    name = 'qq'
    allowed_domains = ['qq.com']

    #def __init__(self):
       # url_qian = "https://h5.qzone.qq.com/proxy/domain/fav.qzone.qq.com/cgi-bin/get_fav_list?uin=39017246&type=0&start="
        #url_hou = "&num=30&inCharset=utf-8&outCharset=utf-8&need_nick=1&need_cnt=1&need_new_user=1&fupdate=1&random=0.14056805773391323&g_tk=1575700801&qzonetoken=91a1956cf840b16a489955c2c858b26cb93b03375de9f03186e1fde63cd88b0b7fb17658e6349a"

    def start_requests(self):
        url_qian = "https://h5.qzone.qq.com/proxy/domain/fav.qzone.qq.com/cgi-bin/get_fav_list?uin=39017246&type=0&start="
        url_hou = "&num=30&inCharset=utf-8&outCharset=utf-8&need_nick=1&need_cnt=1&need_new_user=1&fupdate=1&random=0.14056805773391323&g_tk=1575700801&qzonetoken=91a1956cf840b16a489955c2c858b26cb93b03375de9f03186e1fde63cd88b0b7fb17658e6349a"

        start_urls = [url_qian + str(i) + url_hou for i in range(3660, 3739, 30)]

        # 指定cookies
        cookies = {
        'RK': 'Ea5sUIiFGr',
        '_qpsvr_localtk': '0.9938698970720596',
        'cpu_performance_v8': '13',
        'p_skey': 'CEcQNExKZGKwmp-nrVU-I4fA3t*oUD9wi7nVdf-LeBk_	',
        'pgv_info': 'ssid=s4645593565',
        'pgv_pvi': '7260459008',
        'pgv_si': 's4497869824',
        'pgv_pvid': '2243225580',
        'pt4_token': 'bPzitqHvIJqIW8mKt3pmY4uvmOJ7vJDQpWKCdWWy8lw_',
        'ptcz': '3e05d3d03bc261995dcb6da301496ad02a379348a96b62a39e8c6d9b00be2cb1',
        'skey': '@orWDjxCLK',
        'p_uin': 'o0039017246',
        'Loading': 'Yes',
        'QZ_FE_WEBP_SUPPORT': '1',
        '__guid': '183552575.862613233613063000.1544075476286.3699',
        '__Q_w_s__QZN_TodoMsgCnt': '1',
        'rv2': '80BEAAF77D194B195DE38D8D7B8ACC1F62B9F4F2BAED4879B9',
        'property20': '3B7C9F7BE62DBEE6608D3DEA4CCB53F28D94B0C53B4A5556CCB56FD1C804BDF368FE6A4C21643B1A',
        'monitor_count': '1',
        'ptisp': 'ctc',
        'ptui_loginuin': '39017246',
        'pt2gguin': 'o0039017246',
        'uin': 'o0039017246',
        '__Q_w_s_hat_seed': '1'}

        # 再次请求到详情页，并且声明回调函数callback，dont_filter=True 不进行域名过滤，meta给回调函数传递数据
        for url1 in start_urls:
            yield Request(url=url1, cookies=cookies, callback=self.parse)



    def parse(self, response):
        rs = response.text
        dict1 = rs[(rs.find('(')+1):rs.rfind(')')]
        dict2=json.loads(dict1)
        dataqq = dict2['data']
        total_numqq = dataqq['total_num']
        fav_listqq= dataqq['fav_list']
        #print(fav_listqq)
        for i in fav_listqq:
            item = QqzoItem()
            #print(i['id'])
            item['id1'] = i['id']
            if 'type' in i.keys():
                item['type'] = i['type']
            if 'create_time' in i.keys():
                item['create_time'] = i['create_time']
            if 'title' in i.keys():
                item['title'] = i['title']
            if 'abstract' in i.keys():
                item['abstract'] = i['abstract']
            if 'desp' in i.keys():
                item['desp'] = i['desp']
            if 'platform' in i.keys():
                item['platform'] = i['platform']
            if 'user_agent' in i.keys():
                item['user_agent'] = i['user_agent']
            if 'origin_img_list' in i.keys():
                item['origin_img_list'] = i['origin_img_list']
            if 'album_info'in i.keys():
                item['album_info'] = i['album_info']
            if 'photo_list'in i.keys():
                item['photo_list'] = i['photo_list']
            if 'img_list' in i.keys():
                item['img_list'] = i['img_list']
            if 'share_info' in i.keys():
                item['share_info'] = i['share_info']
            if 'shuoshuo_info' in i.keys():
                item['shuoshuo_info'] = i['shuoshuo_info']

            #print(item['id1'])
            yield item



        #print(dataqq)
        #rs=json.loads(response.text)
        #print(rs)
