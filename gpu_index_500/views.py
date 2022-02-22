from django.shortcuts import render
from django.http import HttpResponse
from gpu_index_500.vga_data.handler import *
from gpu_index_500.vga_data.cleaner import *

import csv

# Create your views here.

def week_index(request):#필요한 것: 전체 인덱스
    csv_update_checker()#리퀘스트마다 자동 UD 되도록 설정(1시간 간격)
    index_data=index_pickle_checker()#21년 1월 1일부터 저장된 마지막 날까지의 모든 인덱스를 불러옵니다.
    this_month_pickle_checker()
    visitor_data=visitor_checker()
    today_info=today_searcher()
    context = {
        'index_data': index_data,
        'today_info': today_info
    }
    return render(request, 'week_index.html', context)
    #return HttpResponse(index_data)

def month_index(request):#필요한 것: 전체 인덱스
    index_data=index_pickle_checker()#21년 1월 1일부터 저장된 마지막 날까지의 모든 인덱스를 불러옵니다.
    today_info=today_searcher()
    context = {
        'index_data': index_data,
        'today_info': today_info
    }
    return render(request, 'month_index.html', context)
    #return HttpResponse(index_data)

def year_index(request):#필요한 것: 전체 인덱스
    index_data=index_pickle_checker()#21년 1월 1일부터 저장된 마지막 날까지의 모든 인덱스를 불러옵니다.
    today_info=today_searcher()
    context = {
        'index_data': index_data,
        'today_info': today_info
    }
    return render(request, 'year_index.html', context)
    #return HttpResponse(index_data)

def series_courier(request,series_num):#시리즈 전체 검색 -> contents
    #series_num = request.GET.get('series_num')#리퀘스트 안에 시리즈넘버가 들어있다고 가정~1060~3090
    stock_num_list=series_to_num_searcher_bin(series_num)#바이너리 검색
    line_list=multiple_nums_to_lines_searcher_bin(stock_num_list)#시리즈에 해당하는 종목들의 리스트를 불러옵니다.
    today_info=today_searcher()
    context = {
        'line_list': line_list,
        'today_info': today_info
    }
    return render(request, 'series.html', context)
    
def specific_courier(request,stock_num,year,month):
    #stock_num = request.GET.get('stock_num')#15091757#request.GET.get('stock_num')
    #year = 21#request.GET.get('year')
    #month = 11#request.GET.get('month')
    year=str(year)
    month=zero_patcher(month)
    filename=single_file_namer(year,month)
    line=single_num_to_line_searcher(filename,stock_num)
    line_list=[]
    line_list.append(line)
    today_info=today_searcher()
    context = {
        'line_list': line_list,
        'today_info': today_info #{{ today_info }}
    }
    return render(request, 'specific.html', context)
    
def visitor_courier(request):
    visitor_data=visitor_checker()
    return HttpResponse(visitor_data)