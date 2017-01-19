#coding:utf-8
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response

from iom.views import login_valid
from server.models import *

# @login_valid
def list(request):
    statue = "服务器展示页"
    table_list = Server.objects.all()
    return render_to_response("list.html", locals())

def content(request,ids):
    Server_data = Server.objects.get(id = int(ids))
    hostname = Server_data.host.strip()
    statue = "%s 详情页"%hostname.encode("utf-8")
    host_data = {
        "hostname":Server_data.host,
        "ip":Server_data.ip,
        "mac":Server_data.mac,
        "cpu":Server_data.cpu,
        "mem":Server_data.mem,
        "disk":Server_data.disk,
        "system":Server_data.system,
        "model":Server_data.model,
        "id":Server_data.id
    }
    return render_to_response("server_content.html",locals())