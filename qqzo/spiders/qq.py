# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import json
from qqzo.items import QqzoItem




class QqSpider(scrapy.Spider):
    name = 'qq'
    allowed_domains = ['qq.com']

    #def __init__(self):
       # url_qian = "https://****/cgi-bin/get_fav_list?uin=QQhao&type=0&start="
        #url_hou = "&num=30&inCharset=utf-8&outCharset=utf-8&need_nick=1&need_cnt=1&need_new_user=1&fupdate=1&random=0.14056805773391323&g_tk=1575700801&qzonetoken=cb93b03375de9f03186e1fde63cd88b0b7fb17658e6349a"

    def start_requests(self):
        url_qian = "https://****/cgi-bin/get_fav_list?uin=QQhao&type=0&start="
        url_hou = "&num=30&inCharset=utf-8&outCharset=utf-8&need_nick=1&need_cnt=1&need_new_user=1&fupdate=1&random=0.14056805773391323&g_tk=1575700801&qzonetoken=cb93b03375de9f03186e1fde63cd88b0b7fb17658e6349a"

        start_urls = [url_qian + str(i) + url_hou for i in range(3660, 3739, 30)]

        # 指定cookies
        cookies = {
        'RK': '',
        '_qpsvr_localtk': '',
        'cpu_performance_v8': '13',
        'p_skey': '',
        'pgv_info': '',
        'pgv_pvi': '',
        'pgv_si': '',
        'pgv_pvid': '',
        'pt4_token': '_',
        'ptcz': '',
        'skey': '',
        'p_uin': 'QQhao',
        'Loading': 'Yes',
        'QZ_FE_WEBP_SUPPORT': '1',
        '__guid': '183552575.862613233613063000.1544075476286.3699',
        '__Q_w_s__QZN_TodoMsgCnt': '1',
        'rv2': '',
        'property20': '',
        'monitor_count': '1',
        'ptisp': 'ctc',
        'ptui_loginuin': 'QQhao',
        'pt2gguin': 'QQhao',
        'uin': 'QQhao',
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
