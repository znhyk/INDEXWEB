import csv
import pickle
import time

#fr.close()반드시 기입

def time_maker():
    now_time=time.localtime(time.time())
    now_year=now_time.tm_year
    now_month=now_time.tm_mon
    now_date=now_time.tm_mday
    times=[]
    times.append(now_year)
    times.append(now_month)
    times.append(now_date)
    return times

#[[202X/X/X,X],[],[]...
def visit_data_generator():
    now_time=time_maker()
    date=str(now_time[0])+'/'+str(now_time[1])+'/'+str(now_time[2])
    new_visitor_data=[]
    new_visitor_data.append(date)
    new_visitor_data.append(1)
    return new_visitor_data 
    
def visit_data_reader():
    with open("visitor_pickle.bin","rb") as fr:
        visitor_data = pickle.load(fr)
    return visitor_data
    
def visit_data_sorter():
    now_time=time_maker()
    with open("visitor_pickle.bin","rb") as fr:
        visitor_data = pickle.load(fr)
    last_date=visitor_data[-1][0]#마지막 날의 날짜 불러옴
    last_date_list=last_date.split('/')
    if last_date_list[2] != str(now_time[2]):
        new_visitor_data=visit_data_generator()
        visitor_data.append(new_visitor_data)
    elif last_date_list[1] != str(now_time[1]):
        new_visitor_data=visit_data_generator()
        visitor_data.append(new_visitor_data)
    elif last_date_list[0] != str(now_time[0]):
        new_visitor_data=visit_data_generator()
        visitor_data.append(new_visitor_data)
    else:
        visitor_data[-1][1]=visitor_data[-1][1]+1    
    return visitor_data

def visitor_checker():
    visitor_data=visit_data_sorter()
    with open("visitor_pickle.bin","wb") as fw:
        pickle.dump(visitor_data,fw)
    return visitor_data
    
def zero_patcher(month):
    if month > 9:
        abrv_month=str(month)
    else:
        abrv_month='0'+str(month)
    return abrv_month
    
def single_file_namer(year,month):
    filename='PROCESSEDVGA_'+str(year)+'-'+str(month)+'.csv'
    return filename

def index_file_namer(year,month):
    filename='INDEXVGA_'+str(year)+'-'+str(month)+'.csv'
    return filename
    
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
    
def this_month_sorter():#당월의 모든 데이터를 분류 및 정리
    filename=single_file_namer_now()
    #코드레드:파일이름을 전월데이터 누락이 생긴 csv 파일 명으로 한다.
    #filename='PROCESSEDVGA_22-0X.csv'
    fr=open(filename,'r',encoding='utf-8')
    rdr=csv.reader(fr)
    month_data=[]#line list
    for line in rdr:
        month_data.append(line)
    fr.close()
    return month_data
    
def single_num_to_line_searcher(filename,stock_num):#개개의 stock_num을 검색(단일/전월검색) with csv
    fr=open(filename,'r',encoding='utf-8')#단일검색=>전월검색으로 여유
    rdr=csv.reader(fr)
    for line in rdr:
        if line[0] == str(stock_num):
            return line
        else:
            pass
    fr.close()
    return ['CANNOT FIND THIS VGA']#찾을 수 없는 경우 빈 라인을 반환

"""
def single_num_to_line_searcher_bin(stacked_month,stock_num):#->全月검색이므로 바이너리 검색 지원X
    a_time=time.time()
    with open("all_data_pickle.bin","rb") as fr:
        all_data = pickle.load(fr)
        month_data=all_data[stacked_month]
        for line in month_data:
            if line[0] == str(stock_num):
                return line
            else:
                pass
    b_time=time.time()
    stop=b_time-a_time
    return stop#바이너리 검색이 더 오래걸림.
"""

#filename을 어떻게 하는지에 대한 문제
def multiple_nums_to_lines_searcher(stock_num_list):#여러개의 stock_num들을 검색(다중검색)
    filename=single_file_namer_now()#다중검색=>당월검색으로 제한
    fr=open(filename,'r',encoding='utf-8')
    rdr=csv.reader(fr)
    line_list=[]
    for line in rdr:
        for stock_num in stock_num_list:
            if line[0] == stock_num:
                line_list.append(line)
            else:
                pass
    fr.close()
    return line_list

def multiple_nums_to_lines_searcher_bin(stock_num_list):#여러개의 stock_num들을 검색(다중/당월검색)-바이너리 검색 지원O
    with open("month_pickle.bin","rb") as fr:
        month_data = pickle.load(fr)
        line_list=[]
        for line in month_data:
            for stock_num in stock_num_list:
                if line[0] == stock_num:
                    line_list.append(line)
                else:
                    pass
    return line_list

def series_to_num_searcher(series_num):#제품시리즈로 검색하여 stock_num_list 반환
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
    return stock_num_list
    
def today_searcher():
    years=['25','24','23','22']
    months=['12','11','10','09','08','07','06','05','04','03','02','01']
    for year in years:
        for month in months:
            try:
                filename=index_file_namer(year,month)
                fr=open(filename,'r',encoding='utf-8')
                rdr=csv.reader(fr)
                days=[]
                for line in rdr:
                    days.append(line[0])
                today=days[-1]
                fr.close()
                return today
            except:
                pass

def series_to_num_searcher_bin(series_num):#제품시리즈로 검색하여 stock_num_list 반환 -바이너리 검색 지원O
    with open("month_pickle.bin","rb") as fr2:
        month_data = pickle.load(fr2)
        stock_num_list=[]
        series_num=str(series_num)
        for line in month_data:
            if series_num in line[1]:
                stock_num_list.append(line[0])
            else:
                pass
    return stock_num_list
    
def index_maker(filename,date):#특정날짜의 H&C GPU 500+ 지수를 산출(한달 내)
    fr=open(filename,'r',encoding='utf-8')
    rdr=csv.reader(fr)
    date=date+1
    count=0
    sum_price=0
    for line in rdr:
        day_price=int(line[date])
        if day_price > 0:
            count+=1
            sum_price+=day_price
        else:
            pass
    sc_ratio=(sum_price/count)
    h_c_index=round((sc_ratio-sc_ratio%1000)/1000)
    fr.close()
    return h_c_index
    
def index_saver(year,month):#일별 인덱스를 저장
    r_filename=single_file_namer(year,month)
    w_filename=index_file_namer(year,month)
    fw=open(w_filename,'w',encoding='utf-8',newline='')
    wr=csv.writer(fw)
    try:
        for date in range(1,31+1):
            h_c_index=index_maker(r_filename,date)
            wr.writerow([date,h_c_index])
    except:
        pass
    fw.close()

def index_sorter():#월별/전체 인덱스 데이터를 분류 및 정리 
    years=['21','22','23']
    months=['01','02','03','04','05','06','07','08','09','10','11','12']
    year_index_data=[]
    try:
        for y in years:
            for m in months:
                ym=y+'/'+m
                filename=index_file_namer(y,m)
                fr=open(filename,'r',encoding='utf-8')
                rdr=csv.reader(fr)
                index_data={}
                count=0
                for line in rdr:
                    date=str(line[0])
                    ymd=ym+'/'+date
                    index_data[ymd]=line[1]
                month_index_data=index_data
                year_index_data.append(month_index_data)
    except:
        pass
    return year_index_data

def all_data_sorter():
    years=['21','22','23']
    months=['01','02','03','04','05','06','07','08','09','10','11','12']
    year_all_data=[]
    for y in years:
        for m in months:
            try:
                filename=single_file_namer(y,m)
                fr=open(filename,'r',encoding='utf-8')
                rdr=csv.reader(fr)
                all_data=[]
                count=0
                for line in rdr:
                    all_data.append(line)
                month_all_data=all_data
                year_all_data.append(month_all_data)
            except:
                pass
    return year_all_data
        

#피클링함수들: 인덱스 페이지의 빠른 불러오기를 위해, 1시간 간격으로만 csv파일을 읽읍니다. 간격 안쪽은 바이너리로 읽어옴미다.
"""
def all_data_pickler():
    all_data=all_data_sorter()
    with open("all_data_pickle.bin","wb") as fw:
        pickle.dump(all_data,fw)
    return all_data

def all_data_time_pickler():
    pickle_time=time.time()
    with open("all_data_time_pickle.bin","wb") as fw:
        pickle.dump(pickle_time,fw)
    return 0

def all_data_pickle_checker():
    with open("all_data_pickle.bin","rb") as fr:
        all_data = pickle.load(fr)
    with open("all_data_time_pickle.bin","rb") as fr2:
        pickle_time = pickle.load(fr2)
    now_time=time.time()
    if now_time-pickle_time < 10:#마지막 피클링(csv파일 직접 참조)된 시간으로부터 1시간 이내인 경우
        return all_data
    else:#마지막 피클링된 시간으로부터 1시간 이상 경과한 경우, 시간을 기록하고 다시 피클링한다.
        all_data=all_data_pickler()
        all_data_time_pickler()
        return all_data
"""
def index_pickler():#index_sorter()로 읽은 csv를 피클링
    times=time_maker()
    abrv_year=str(times[0]%2000)#to2X
    if times[1] > 9:
        abrv_month=str(times[1])
        #코드레드
        #abrv_month='0X'
    else:
        abrv_month='0'+str(times[1])#toXX
        #코드레드
        #abrv_month='0X'
    index_saver(abrv_year,abrv_month)
    index_data=index_sorter()
    with open("index_pickle.bin","wb") as fw:
        pickle.dump(index_data,fw)
    return index_data

def index_time_pickler():#피클시간을 기록
    pickle_time=time.time()
    with open("index_time_pickle.bin","wb") as fw2:
        pickle.dump(pickle_time,fw2)
    return 0

def index_pickle_checker():#유통기한 전에 반드시 피클을 소비하게되는 함수
    with open("index_pickle.bin","rb") as fr:
        index_data = pickle.load(fr)
    with open("index_time_pickle.bin","rb") as fr2:
        pickle_time = pickle.load(fr2)
    now_time=time.time()
    if now_time-pickle_time < 10:#마지막 피클링(csv파일 직접 참조)된 시간으로부터 1시간 이내인 경우/개발자모드 세팅 10초
        return index_data
    else:#마지막 피클링된 시간으로부터 1시간 이상 경과한 경우, 시간을 기록하고 다시 피클링한다.
        index_data=index_pickler()
        index_time_pickler()
        return index_data
    
def this_month_pickler():
    this_month_csv=this_month_sorter()
    with open("month_pickle.bin","wb") as fw:
        pickle.dump(this_month_csv,fw)
    return this_month_csv

def this_month_time_pickler():
    pickle_time=time.time()
    with open("month_time_pickle.bin","wb") as fw2:
        pickle.dump(pickle_time,fw2)
    return 0

def this_month_pickle_checker():
    with open("month_pickle.bin","rb") as fr:
        month_data = pickle.load(fr)
    with open("month_time_pickle.bin","rb") as fr2:
        pickle_time = pickle.load(fr2)
    now_time=time.time()
    if now_time-pickle_time < 10:#마지막 피클링(csv파일 직접 참조)된 시간으로부터 1시간 이내인 경우/개발자모드 세팅 10초
        return month_data
    else:#마지막 피클링된 시간으로부터 1시간 이상 경과한 경우, 시간을 기록하고 다시 피클링한다.
        month_data=this_month_pickler()
        this_month_time_pickler()
        return month_data

