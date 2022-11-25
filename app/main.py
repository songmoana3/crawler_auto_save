import sys
import application_service
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--start_date', type =str)
parser.add_argument('--end_date', type=str)
args = parser.parse_args()


start_date = args.start_date
end_date = args.end_date

application_service.Save(start_date, end_date)
