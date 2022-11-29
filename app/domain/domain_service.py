import os
import csv
import urllib3
import io
from PIL import Image
import log


from infrastructure import mongoDBRepositoryImpl


# 출원번호 가져오기
def get_appnum(start, end):
    print(f'------- * Start_date:{start} End_date:{end} * ------- ')
    query = {"$and":[{"applicationDate":{"$gte":start,"$lt":end}}, {"imageLinkInfo.bigDrawing":{"$ne": None}}, {"$or":[{"trademarkTypeInfo.tmDivisionCode":{"$in":["도형복합", "도형상표"]}},{"viennaCodeInfo":{"$ne": None}}]}]},{"_id":1,"imageLinkInfo.bigDrawing":1}
    docs = mongoDBRepositoryImpl.mongo_find(list(query))
    docs = list(docs)
    return docs

# 출원번호 csv 저장
def save_app_csv(end, docs, main_path):
    path = f'{main_path}/{end}_applicationNumber.csv'
    print("[airflow]:: csv_saved_path : ",path)
    with open (path,'w') as f:
        write = csv.writer(f)
        write.writerow(['applicationNumber'])
        for doc in docs:
            write.writerow([doc['_id']])
  
# 이미지 링크 가져오기
def get_image_link(docs):  
    img_source = dict() 
    for doc in docs:
        try:
            file_name = doc['_id']
            url = doc['imageLinkInfo']['bigDrawing']
            img_source[file_name]=url
            
        except KeyboardInterrupt:
                log.log_saving('error',applicationNumber=file_name, detail='KeyboardInterrupt')
        except:
            log.log_saving('error',applicationNumber=file_name, detail = 'url error')
    return img_source

# 이미지 저장
def save_img(end, img_source, main_path):
    
    # 저장될 폴더
    folder_name = f'{main_path}/img/{end}_img'
    print("[airflow]:: img_saved_path : ",folder_name)
    os.makedirs(folder_name, exist_ok=True)

    for idx,(file_name, url) in enumerate(img_source.items()):
        if not os.path.isfile(f'{folder_name}/{file_name}.jpg'):
            try:
                http = urllib3.PoolManager()
                res = http.request("GET", url, timeout= 5)
                img = Image.open(io.BytesIO(res.data))
                img.save(f'{folder_name}/{file_name}.jpg')
                print(f"\rapplicationNumber : {file_name} is saved. .! {idx}/{len(img_source)}",end = "\r")
                
            except KeyboardInterrupt:
                log.log_saving('error',applicationNumber=file_name, detail='KeyboardInterrupt')
                
            except:
                log.log_saving('error',applicationNumber=file_name, detail='img_save_error')
        else:
            log.log_saving('save',applicationNumber=file_name)
        
        
