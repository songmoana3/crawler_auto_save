import application_service
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-s","--start_date", type =str)
parser.add_argument("-e","--end_date", type=str)
args = parser.parse_args()


start_date = args.start_date
end_date = args.end_date
main_path = os.getcwd()

application_service.Save(start_date, end_date, main_path) # 시작날짜, 끝나는 날짜
