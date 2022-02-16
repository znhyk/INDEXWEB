import csv
import time
import pickle

def single_file_namer_now():
    now_time=time.localtime(time.time())
    now_year=now_time.tm_year
    now_month=now_time.tm_mon
    now_date=now_time.tm_mday
    abrv_year=str(now_year%2000)
    if now_month > 9:
        abrv_month=str(now_month)
    else:
        abrv_month='0'+str(now_month)
    filename='PROCESSEDVGA_'+abrv_year+'-'+abrv_month+'.csv'
    return filename

def series_to_num_searcher(series_num):#제품시리즈로 검색하여 stock_num_list 반환
    time_a=time.time()
    filename=single_file_namer_now()#시리즈검색=>당월검색으로 제한
    fr=open(filename,'r',encoding='utf-8')
    stock_num_list=[]
    series_num=str(series_num)
    rdr=csv.reader(fr)
    for line in rdr:
        if series_num in line[1]:
            stock_num_list.append(line[0])
        else:
            pass
    fr.close()
    time_b=time.time()
    timestop=time_b-time_a
    return timestop#시간측정결과 약 0.016초

def series_to_num_searcher_bin(series_num):#제품시리즈로 검색하여 stock_num_list 반환 -바이너리 검색 지원O
    time_a=time.time()
    with open("month_pickle.bin","rb") as fr2:
        month_data = pickle.load(fr2)
        stock_num_list=[]
        series_num=str(series_num)
        for line in month_data:
            if series_num in line[1]:
                stock_num_list.append(line[0])
            else:
                pass
    time_b=time.time()
    timestop=time_b-time_a
    return timestop#시간측정결과 0.0초(계산의미X)
