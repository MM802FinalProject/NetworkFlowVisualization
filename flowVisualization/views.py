from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from models import *

import logRecord, json


@csrf_exempt
def index(request):
    context = {}
    
    if request.method == 'POST':
        data_grabbed = logRecord.net_io(0.5)
        incomingTraffic = data_grabbed[0]
        outgoingTraffic = data_grabbed[1]
        
        if len(TempRecord.objects.all()) == 0:
            TempRecord.objects.create(maxd = incomingTraffic, mind = incomingTraffic, totald = incomingTraffic/2, maxu = outgoingTraffic, minu = outgoingTraffic, totalu = outgoingTraffic/2, time = 0.5)
        else:
            tempRec = list(TempRecord.objects.all())[0]
            if tempRec.maxd < incomingTraffic:
                tempRec.maxd = incomingTraffic
            if tempRec.mind > incomingTraffic:
                tempRec.mind = incomingTraffic
            
            if tempRec.maxu < outgoingTraffic:
                tempRec.maxu = outgoingTraffic
            if tempRec.minu > outgoingTraffic:
                tempRec.minu = outgoingTraffic
            
            tempRec.totald += incomingTraffic/2
            tempRec.totalu += outgoingTraffic/2
            tempRec.time += 0.5
            tempRec.save()
        
        current_data = {"i" : str(incomingTraffic), "o": str(outgoingTraffic)}
        # print "Incoming: "+current_data["i"]
        # print "Outgoing: "+current_data["o"]
        return JsonResponse(current_data)
    
    return render(request, 'index.html', context)

@csrf_exempt
def createRecord(request):
    tempRec = list(TempRecord.objects.all())[0]
    
    print tempRec.maxd
    print tempRec.mind
    print tempRec.totald
    print tempRec.maxu
    print tempRec.minu
    print tempRec.totalu
    print tempRec.time
    
    des = json.loads(request.body)['des']
    print des
    
    DataRecord.objects.create(timeLasted = tempRec.time, 
                              maxUploadValue = tempRec.maxu, 
                              minUploadValue = tempRec.minu, 
                              avgUploadValue = tempRec.totalu/tempRec.time,
                              totalUploadValue = tempRec.totalu,
                              
                              maxDownloadValue = tempRec.maxd, 
                              minDownloadValue = tempRec.mind, 
                              avgDownloadValue = tempRec.totald/tempRec.time,
                              totalDownloadValue = tempRec.totald,
                              
                              description = des
                              )
    
    TempRecord.objects.all().delete()
    
    return JsonResponse({})

@csrf_exempt
def viewStaticCharts(request):
    return render(request, 'staticChart.html', {"data" : list(DataRecord.objects.all())})

@csrf_exempt
def clrCache(request):
    TempRecord.objects.all().delete()
    return JsonResponse({})
        