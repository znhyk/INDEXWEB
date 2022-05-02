import csv
import time
import pickle

def time_maker():
    now_time=time.localtime(time.time())
    now_year=now_time.tm_year
    now_month=now_time.tm_mon
    times=[]
    times.append(now_year)
    times.append(now_month)
    return times
    
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

def csv_dat_cleaner(filename):#상장폐지함수
    maj_element=['1060','1070','1650','1660','2060','2070','2080','3060','3070','3080','3090','470','480','570','580','5600','5700','6500','6600','6700','6800','6900']
    fr=open(filename,'r',encoding='utf-8')
    new_lines=[]
    rdr=csv.reader(fr)
    for line in rdr:
        for i in maj_element:
            if i in line[1]:
                stock_code=line[0]
                stock_name=line[1]
                new_line=[]
                new_line.append(stock_code)
                new_line.append(stock_name)
                for n in range(2,len(line)):
                    try:#쉼표를 빼서 숫자로 만들 수 있는 경우
                        str_price=line[n].replace(',','')
                        int_price=int(str_price)
                        if int_price > 0:
                            new_line.append(int_price)
                        else:#0인 경우
                            new_line.append(0)
                    except:#문자인경우,0인 경우
                        new_line.append(0)
                new_lines.append(new_line)
            else:
                pass
    return new_lines                  
                            
def csv_dat_saver():#CSV저장함수
    filename=single_file_namer_now()
    #코드레드: 파일명을 전월 누락이 발생한 csv 파일명으로 변경한다.
    #filename='PROCESSEDVGA_22-0X.csv'
    fw=open(filename,'w',encoding='utf-8',newline='')
    wr=csv.writer(fw)
    new_lines=csv_dat_cleaner('VGA.csv')#매일 최신월 최신일의 VGA.csv를 넣어놓아야함!(반드시 지킬것)
    for line in new_lines:
        wr.writerow(line)
    fw.close()#PROCESSEDVGA_2X-XX.csv 최신화               

def csv_update_time_pickler():
    pickle_time=time.time()
    with open("csv_time_pickle.bin","wb") as fw:
        pickle.dump(pickle_time,fw)
    return 0

def csv_update_checker():
    with open("csv_time_pickle.bin","rb") as fr:
        pickle_time = pickle.load(fr)
    now_time=time.time()
    if now_time-pickle_time < 3600:#마지막 피클링(csv파일 직접 참조)된 시간으로부터 1시간 이내인 경우/개발자모드 세팅 10초
        return 0
    else:#마지막 피클링된 시간으로부터 1시간 이상 경과한 경우, 시간을 기록하고 다시 피클링한다.
        csv_update_time_pickler()
        csv_dat_saver()
        return 1
