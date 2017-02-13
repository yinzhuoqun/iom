from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from server.models import Server
def savedata(request):
    result = {}
    if request.method == "POST" and request.POST:
        req_data = request.POST

        # 判断 mac 地址不存在时保存，存在时报错
        # print(Server.objects.get(mac=req_data.get("mac")).mac)
        # if len(Server.objects.get(mac=req_data.get("mac")).mac) < 1:

        server = Server() # 实例化
        server.host = req_data.get("hostname")
        server.ip = req_data.get("ip")
        server.mac = req_data.get("mac")
        server.cpu = req_data.get("cpu")
        server.mem = req_data.get("mem")
        server.model = req_data.get("model")
        server.disk = req_data.get("disk")
        server.system = req_data.get("system")
        server.save()
        result["statue"] = "success"

        # else:
        #     result["statue"] = "exist"
    else:
        result["statue"] = "error"
    return JsonResponse(result)


def list(request):

    return render(request, "index.html",locals())