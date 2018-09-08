#!/usr/bin/python

# 监控

import dns.resolver
import os
import httplib

iplist = []
appdomain='www.google.com.hk'

def get_iplist(domain=""):
    try:
        A = dns.resolver.query(domain, 'A') # 解析A记录类型
    except Exception, e:
        print("dns error", str(e))
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)
    return True

def checkip(ip):
    checkurl = ip+":80"
    getcontent = ""
    httplib.sock.setdefaulttimeout(5)
    conn = httplib.HTTPConnection(checkurl)

    try:
        conn.request("GET", "/", headers={"Host":appdomain})
        r = conn.getresponse()
        getcontent = r.read(15)
    finally:
        if get_iplist(appdomain) and len(iplist)>0:
            for ip in iplist:
                checkip(ip)
        else:
            print("dns resolver error")

