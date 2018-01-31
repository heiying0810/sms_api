#!/usr/bin/env python
# *-* coding:utf-8 *-*
from py import config
import urllib2,hashlib,urllib,sys,uuid,base64,json
class Xw_method:
    '''
    MOS-HTTP接口
    '''
    def __init__(self):
        self.ip = config.IP
        self.port_down = config.PORT_down
        self.port_up = config.PORT_up
        self.user = config.mos_user
        self.password = config.mos_password
        self.md5_pwd = hashlib.md5(self.password.encode('utf-8')).hexdigest()
    def Req_url(self,url,Post=False,Data=None):
        print url
        if not Post:
            req = urllib2.Request(url)
        else:
            headers = {'Content-Type': 'application/json'}
            req = urllib2.Request(url=url,data=Data,headers=headers)
        req = urllib2.urlopen(req).read()
        return req
    def Yue(self):
        '''
        GetAccountInfo调用是业务系统发起，请求获取帐号信息
        查询余额接口;下边是示例,返回信息和请求URL
        {
            "account": "user_test",
            "name": "user_test",
            "identify": null,
            "bizNames": [
                "批发黑"
            ],
            "balance": 88888888,
            "reserve": null,
            "userbrief": ""
        }
        http://8.8.8.8:18088/cgi-bin/getacountinfo?account=user_test&password=50871ed26c26a4d225f
        '''
        url = 'http://%s:%s/cgi-bin/getacountinfo?account=%s&password=%s' % (self.ip,self.port_up,self.user,self.md5_pwd)
        content = self.Req_url(url)
        return content
    def Type(self):
        '''
        GetBusinessType调用是业务系统发起，请求帐号绑定的业务类型。
        http://8.8.8.8:18088/cgi-bin/getbusinesstype?account=user_test&password=46f35bacb44d050871ed26c26a4d225f
        [
    {
        "id": 33847,
        "name": "批发黑",
        "priority": 4,
        "startTime": "00:00:00",
        "endTime": "23:59:59",
        "extendFlag": true,
        "state": 1,
        "bindChs": [
            {
                "carrier": "telecom",
                "specNumber": "1069030",
                "sendType": "sms"
            },
            {
                "carrier": "cmcc",
                "specNumber": "1069030",
                "sendType": "sms"
            },
            {
                "carrier": "unicom",
                "specNumber": "1069033",
                "sendType": "sms"
            }
        ]
    }
]
        '''
        url = 'http://%s:%s/cgi-bin/getbusinesstype?account=%s&password=%s' % (self.ip,self.port_up,self.user,self.md5_pwd)
        content = self.Req_url(url)
        return content
    def Shang_sms(self):
        '''
        GetMOMessage调用是业务系统发起，请求推送上行信息。已经推送过的上行，下次无法继续推送。
        http://8.8.8.8:18088/cgi-bin/getmomessage?account=user&password=77a3b0e31390105385012345b8e3088e&pagesize=1
        [
    {
        "phone": "13312345678",
        "content": "【玄武无线】测试信息，玄武无线。",
        "msgType": 1,
        "specNumber": "106578986186708107",
        "serviceType": "1600100100",
        "receiverTime": "2017-10-18 15:45:42",
        "reserve": null
    }
]
        '''
        url = 'http://%s:%s/cgi-bin/getmomessage?account=%s&password=%s&pagesize=1' % (self.ip,self.port_up,self.user,self.md5_pwd)
        content = self.Req_url(url)
        return content
    def Shang_report(self):
        '''
        GetReport调用是业务系统发起，请求推送运营商状态报告。已经推送过的状态报告，下次无法继续推送。
        http://8.8.8.8:18088/cgi-bin/getreport?account=user&password=77a3b0123450105385055657b8e3088e&pagesize=1
        [
    {
        "id": 38233031,
        "batchID": "d26eb963-00dc-4b94-9aab-9be1ff6496eb",
        "phone": "13312345678",
        "msgID": "122017325261766",
        "customMsgID": "",
        "state": 0,
        "total": 0,
        "number": 1467806333,
        "submitTime": "2017-12-20 17:32:52",
        "doneTime": "2017-12-20 17:34:00",
        "originResult": "DELIVRD",
        "reserve": null
    }
]
        '''
        url = 'http://%s:%s/cgi-bin/getreport?account=%s&password=%s&pagesize=10' % (self.ip,self.port_up,self.user,self.md5_pwd)
        content = self.Req_url(url)
        return content
    def Shang_response(self):
        '''
        GetResponse调用是业务系统发起，请求推送运营商提交报告。已经推送过的提交报告，下次无法继续推送。
        http://8.8.8.8:18088/cgi-bin/getresponse?account=user&password=12345676cafbac237cede5f6e9643152&pagesize=1
        [
    {
        "batchID": "33e629d3-c626-1234-a4c3-0e46ce294da3",
        "msgID": "122508115717720",
        "customMsgID": "null18601124278",
        "state": 1,
        "phone": "13312345678",
        "total": 1,
        "number": 1,
        "submitRespTime": "2017-12-25 08:11:57",
        "originResult": "0",
        "reserve": null
    }
]
        '''
        url = 'http://%s:%s/cgi-bin/getresponse?account=%s&password=%s&pagesize=1' % (self.ip,self.port_up,self.user,self.md5_pwd)
        content = self.Req_url(url)
        return content
    def Sms_send(self,phone,text,batchid=False,Post=False):
        '''
        短信下发(支持群发)
        GET-单发-无batchid
        http://8.8.8.8:9050/cgi-bin/sendsms?username=user&password=12345&to=17710811056&text=%B2%E2%CA%D4%B6%CC%D0%C5&subid=&msgtype=1
        GET-群发-无batchid
        http://8.8.8.8:9050/cgi-bin/sendsms?username=user&password=12345&to=17710811056%2017600248145&text=%B2%E2%CA%D4%B6%CC%D0%C5&subid=&msgtype=1
        GET-单发-有batchid
        http://8.8.8.8:9050/cgi-bin/sendsms?username=user&password=123456cafbac237cede5f6e9643152&to=17710811056&text=%B2%E2%CA%D4%B6%CC%D0%C5&subid=&msgtype=1&encode=0&version=1.0&batchid=937dc2c0-e39e-11e7-bfc3-005056c00008
        GET-群发-有batchid
        http://8.8.8.8:9050/cgi-bin/sendsms?username=user&password=1234566cafbac237cede5f6e9643152&to=17710811056%2017600248145&text=%B2%E2%CA%D4%B6%CC%D0%C5&subid=&msgtype=1&encode=0&version=1.0&batchid=937dc2c0-e39e-11e7-bfc3-005056c00008
        POST-单发-无batchid
        POST-群发-无batchid
        POST-单发-有batchid
        POST-群发-有batchid
        '''
        phone_list = ''
        if len(phone) == 1:
            phone_list = phone[0]
        else:
            phone_list = phone[0]
            for x in range(1,len(phone)):
                phone_list += ' %s' % (phone[x])
        phone_list = urllib.quote(phone_list.decode(sys.stdin.encoding).encode('gbk'))
        text = urllib.quote(text.decode(sys.stdin.encoding).encode('gbk'))
        Uuid = uuid.uuid1()
        if Post:
            print 'POST 接口还未测试!!!'
            exit()
        else:
            if batchid:
                url = 'http://%s:%s/cgi-bin/sendsms?username=%s&password=%s&to=%s&text=%s&subid=&msgtype=1&encode=0&version=1.0&batchid=%s' % (self.ip, self.port_down, self.user, self.md5_pwd, phone_list, text, Uuid)
            else:
                url = "http://%s:%s/cgi-bin/sendsms?username=%s&password=%s&to=%s&text=%s&subid=&msgtype=1" % (self.ip, self.port_down, self.user, self.password, phone_list,text)
            content = self.Req_url(url)
        return content
    def SMS_send_z(self,phone,Post=False):
        '''
        一号码一内容
        http://8.8.8.8:9050/cgi-bin/sendsingle?username=testuser&password=12345678988250654307c7fef03f5b98&to=[mobile]17710811056[mobile!][content]%B2%E2%CA%D4%B6%CC%D0%C5-aaa[content!]&text=%B2%E2%CA%D4%B6%CC%D0%C5&subid=&msgtype=1&encode=0&version=1.0
        多号码多内容
        http://8.8.8.8:9050/cgi-bin/sendsingle?username=dxxn@bjhxtx&password=5fb29bbcd88250654307c7fef03f5b98&to=[mobile]17710811056[mobile!][content]%B2%E2%CA%D4%B6%CC%D0%C5-000[content!][mobile]17600248145[mobile!][content]%B2%E2%CA%D4%B6%CC%D0%C5-111[content!][mobile]15234919016[mobile!][content]%B2%E2%CA%D4%B6%CC%D0%C5-222[content!]&text=%B2%E2%CA%D4%B6%CC%D0%C5&subid=&msgtype=1&encode=0&version=1.0
        '''
        text = '测试短信'
        text = urllib.quote(text.decode(sys.stdin.encoding).encode('gbk'))
        if Post:
            print 'POST 接口还未测试!!!'
            exit()
        else:
            if len(phone) == 1:
                phone_list = '[mobile]%s[mobile!][content]%s-000[content!]' % (phone[0], text)
            else:
                phone_list = '[mobile]%s[mobile!][content]%s-000[content!]' % (phone[0], text)
                for x in range(1, len(phone)):
                    phone_list += '[mobile]%s[mobile!][content]%s-%s%s%s[content!]' % (phone[x], text, x, x, x)
            url = 'http://%s:%s/cgi-bin/sendsingle?username=%s&password=%s&to=%s&text=%s&subid=&msgtype=1&encode=0&version=1.0' % (
            self.ip, self.port_down, self.user, self.md5_pwd, phone_list, text)
        content = self.Req_url(url)
        return content

class Webservice_API:
    from suds.client import Client
    client = Client(config.web_mos_url)
    def __init__(self):
        self.user = config.mos_user
        self.password = config.mos_password
        self.md5_pwd = hashlib.md5(config.mos_password.encode('utf-8')).hexdigest()
    def User_Info(self):
        '''
        GetAccountInfo调用是业务系统发起，请求获取帐号信息。
        (AccountInfo){
   Account = "testuser"
   Name = "testuser"
   BizNames =
      (ArrayOfString){
         string[] =
            "虚拟",
      }
   Userbrief = None
   Balance = 88888888.00
 }
        '''
        info = self.client.service.GetAccountInfo(self.user,self.password)
        return info
    def Business_info(self):
        '''
        GetBusinessType调用是业务系统发起，请求帐号绑定的业务类型。
        (ArrayOfBusinessType){
   BusinessType[] =
      (BusinessType){
         Id = 40355
         Name = "虚拟"
         Priority = 4
         StartTime = "00:00:00"
         EndTime = "23:59:59"
         ExtendFlag = True
         state = 1
         bindChs =
            (ArrayOfBindChannel){
               BindChannel[] =
                  (BindChannel){
                     ChannelNum = "9999"
                     Carrier = "移动"
                     SendType = "sms|longsms|"
                  },
            }
      },
 }
        '''
        info = self.client.service.GetBusinessType(self.user,self.password)
        return info
    def Send_sms(self,phone,text):
        '''
        Post调用是业务系统发起，请求发送短消息到指定手机。该操作为统一的发送接口，支持单发，组发，群发操作，推荐使用。
        :param phone:需要发送的目标手机号码；
        :param text:发送的信息内容；
        :param batchID:批次ID，格式必须为8-4-4-4-12UUID；
        :param batchName:批次名称；
        :param sendType:发送类型：0群发；1组发；2单发；
        :param msgType:消息类型1短信2彩信3push；
        :param bizType:业务类型ID；
        :param customNum:拓展码；
        :param distinctFlag:是否过滤重复号码；
        :param scheduleTime:计划发送时间，'1547656582992',重1970-01-01 00:00:00到现在的毫秒；
        :param remark:备注信息；
        :param deadline:下发截止时间；时间格式和scheduleTime相同；
        (GsmsResponse){
   result = 0
   uuid = "cea0600f-00a9-11e8-a557-005056c00008"
   message = "成功"
   attributes = "<map><entry><string>success_count</string><string>1</string></entry></map>"
 }
        '''
        UUID = uuid.uuid1()
        Json = {
            'batchID' : UUID,
            'uuid' : UUID,
            'batchName' : u'测试批次1',
            'sendType' : 0,
            'msgType' : 1,
            'msgs' : {
                'MessageData' :[
                    {'Phone': phone,'Content': text,  },
                ]
            },
        #    'customNum' : '123'
        #    'bizType' : 1,
        #    'distinctFlag' : True,
        #    'scheduleTime' : '1557656582992',
        #    'remark' : u'你好',
        #    'deadline' : '1547656582992'
        }
        info = self.client.service.Post(self.user,self.password,Json)
        return info
    def Report_into(self,num=1):
        '''
        GetReport调用是业务系统发起，请求推送运营商状态报告。已经推送过的状态报告，下次无法继续推送。
        :param num: 一次获取状态报告的个数；
        (ArrayOfMTReport){
   MTReport[] =
      (MTReport){
         id = 0
         batchID = "96459870-ff41-11e7-b77f-005056c00008"
         phone = "15234912345"
         msgID = "012214580148584"
         customMsgID = None
         state = 2
         total = None
         number = None
         submitTime = 2018-01-22 14:58:01
         doneTime = 2018-01-22 14:58:01
         originResult = "UNDELIV"
         reserve = None
      },
 }
        '''
        info = self.client.service.GetReport(self.user, self.md5_pwd, num)
        if info == None:
            info = u'状态报告为空!!!'
        return info
    def Reponse_info(self, num=1):
        '''
        GetResponse调用是业务系统发起，请求推送运营商提交相应。已经推送过的提交相应，下次无法继续推送
        :param num:一次获取提交报告的个数；
        (ArrayOfMTResponse){
   MTResponse[] =
      (MTResponse){
         batchID = "96459870-ff41-11e7-b77f-005056c00008"
         msgID = "012214580148583"
         customMsgID = None
         state = 1
         phone = "17600248145"
         total = 1
         number = 1
         submitRespTime = 2018-01-22 14:58:01
         originResult = "0"
         reserve = None
         id = 0
      },
 }
        '''
        info = self.client.service.GetResponse(self.user, self.md5_pwd, num)
        if info == None:
            info = u'提交报告的个数为空!!!'
        return info
    def Find_response(self, batchid='', phone='', page=1, flag=1):
        '''
        FindResponse调用是业务系统发起，根据输入条件，查询运营商提交响应。
        :param batchid:根据batchid为条件查询；
        :param phone:根据号码为条件查询；
        :param page:返回的页数；默认为15；
        :param flag:返回方式；0位精确，1位模糊；
        (ArrayOfMTResponse){
   MTResponse[] =
      (MTResponse){
         batchID = "cea0600f-00a9-11e8-a557-005056c00008"
         msgID = "012409563564222"
         customMsgID = None
         state = 0
         phone = "17710811056"
         total = 1
         number = 1
         submitRespTime = 2018-01-24 09:56:35
         originResult = "0"
         reserve = "1/1成功;0/1失败;0/1等待"
         id = 0
      },
 }
        '''
        if batchid == '' and phone == '':
            print u'batchid和phone最少传一个参数！！！'
            exit(1)
        info = self.client.service.FindResponse(self.user, self.md5_pwd, batchid, phone, page, flag)
        return info
    def Find_report(self, batchid='', phone='', page=1, flag=1):
        '''
        FindResponse调用是业务系统发起，根据输入条件，查询运营商提交响应。
        :param batchid:根据batchid为条件查询；
        :param phone:根据号码为条件查询；
        :param page:默认为15；
        :param flag:0位精确，1位模糊；
        (ArrayOfMTReport){
   MTReport[] =
      (MTReport){
         id = 0
         batchID = "3eb1228f-ff42-11e7-9b95-005056c00008"
         phone = "15234912345"
         msgID = "012215024448630"
         customMsgID = None
         state = 0
         total = None
         number = None
         submitTime = 2018-01-22 15:02:44
         doneTime = 2018-01-22 15:02:44
         originResult = "UNDELIV"
         reserve = "0/1成功;1/1失败;0/1等待"
      },
 }
        '''
        if batchid == '' and phone == '':
            print u'batchid和phone最少传一个参数！！！'
            exit(1)
        info = self.client.service.FindReport(self.user, self.md5_pwd, batchid, phone, page, flag)
        return info
    def Mo_info(self, num=1):
        '''
        GetMOMessage调用是业务系统发起，请求推送上行信息。已经推送过的上行，下次无法继续推送。
        :param num:一次获取上行短信的数量；
        '''
        info = self.client.service.GetMOMessage(self.user, self.md5_pwd, num)
        if info == None:
            info = u'上行短信的个数为空!!!'
        return info
    def Reset_pwd(self,pwd):
        '''
        ModifyPassword调用是业务系统发起，请求修改帐号密码。
        :param pd: 新密码；
        '''
        action = raw_input("确认将旧密码修改为:%s。[y/s]:" % (pwd))
        if action == 'Y' or action == 'y':
            self.client.service.ModifyPassword(self.user, self.password, pwd)
            return u'系统旧密码: %s ,系统新密码: %s .' % (self.password,pwd)
        else:
            return u'放弃修改密码！！！'

class REST_API:
    def __init__(self):
        self.user = config.mos_user
        self.password = config.mos_password
        self.md5_pwd = hashlib.md5(config.mos_password.encode('utf-8')).hexdigest()
        self.ip = config.IP_REST
        self.port = config.PORT_REST
        self.version = 'v1.0.0'
    def req_url(self,phone, content):
        '''
        http://8.8.8.8:9051/api/v1.0.0/message/mass/send
        {'Content-Length': 233, 'Content-type': 'application/json;charset=utf-8', 'Accept': 'application/json', 'Authorization': 'anNiQGJqeHNkenE6OThmYTg2ZTE5YTk0O132456kMGRiZjRiZjYwMzhmNDU='}
        {"batchName": "测试批次", "content": "单发测试22", "scheduleTime": "", "msgType": "sms", "bizType": "", "items": [{"to": "17710811234"}, {"to": "15234919016"}], "customNum": "", "extras": {"code1": "UUID1", "code2": "UUID2"}}
        {"code":"0","msg":"成功","uuid":"e456ec24-5386-435a-a2ba-53981754fae5"}
        :param phone:发送号码；
        :param content:发送内容；
        '''
        #拼接号码列表
        if len(phone) == 1:
            items = [{'to': phone[0]}]
        else:
            items = []
            for P in xrange(0, len(phone)):
                items.append({'to': phone[P]})
        data = {
            'batchName': '测试批次',  # no
            'items': items,  # yes；组发对象集合
            'content': content,  # yes；内容
            'msgType': 'sms',  # yes；现只支持sms
            'bizType': '',  # no；业务类型ID
            'scheduleTime': '',  # no；定时发送时间
            'customNum': '',  # no;自定义扩展码
            'extras': {
                'code1': 'UUID1',
                'code2': 'UUID2',
            },  # no；扩展参数
        }


        #对密码进行加密处理
        author = base64.b64encode(self.user + ':' + self.md5_pwd)
        #拼接URL
        url = 'http://%s:%s/api/%s/message/mass/%s' % (self.ip,self.port,self.version,'send')
        #请求data
        data = json.dumps(data, ensure_ascii=False, encoding='utf-8')
        #请求headers
        headers = {
            "Content-type": "application/json;charset=utf-8",
            "Authorization": author,
            "Accept": "application/json",
            "Content-Length": len(data)
        }
        print url
        print headers
        print data
        request = urllib2.Request(url=url, data=data, headers=headers)
        response = urllib2.urlopen(request)
        text = response.read()
        return text
    def req_group(self,phone, content):
        '''
        http://8.8.8.8:9051/api/v1.0.0/message/group/send
        {'Content-Length': 258, 'Content-type': 'application/json;charset=utf-8', 'Accept': 'application/json', 'Authorization': 'anNiQGJqeHNkenE6OThmYTg2ZTE5YTk0ODQyZGNkMGRi12345jYwMzhmNDU='}
        {"batchName": "测试批次", "bizType": "", "items": [{"content": "单发测试223", "to": "17710811234"}, {"content": "123test", "to": "15234919016"}], "scheduleTime": "", "extras": {"code1": "UUID1", "code2": "UUID2"}, "msgType": "sms", "customNum": ""}
        {"code":"0","msg":"成功","uuid":"10843129-e550-4296-ad46-1854509875b3"}
        '''
        #拼接号码列表
        if len(phone) == 1:
            items = [{'to': phone[0],'content' : content[0]}]
        else:
            items = []
            for P in xrange(0, len(phone)):
                items.append({'to': phone[P],'content':content[P]})
        data = {
            'batchName': '测试批次',  # no
            'items': items,  # yes；组发对象集合
            'msgType': 'sms',  # yes；现只支持sms
            'bizType': '',  # no；业务类型ID
            'scheduleTime': '',  # no；定时发送时间
            'customNum': '',  # no;自定义扩展码
            'extras': {
                'code1': 'UUID1',
                'code2': 'UUID2',
            },  # no；扩展参数
        }
        #对密码进行加密处理
        author = base64.b64encode(self.user + ':' + self.md5_pwd)
        #拼接URL
        url = 'http://%s:%s/api/%s/message/group/%s' % (self.ip,self.port,self.version,'send')
        #请求data
        data = json.dumps(data, ensure_ascii=False, encoding='utf-8')
        #请求headers
        headers = {
            "Content-type": "application/json;charset=utf-8",
            "Authorization": author,
            "Accept": "application/json",
            "Content-Length": len(data)
        }
        print url
        print headers
        print data
        request = urllib2.Request(url=url, data=data, headers=headers)
        response = urllib2.urlopen(request)
        text = response.read()
        return text
