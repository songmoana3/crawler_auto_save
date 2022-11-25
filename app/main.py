import sys
import application_service

start_date = sys.argv[1]
end_date = sys.argv[2]

application_service.Save(start_date, end_date)
