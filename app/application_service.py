from domain import value_object,domain_service

class Save:
    
    def __init__(self,start,end):
        
        #chk date format
        value_object.Datetime(start)
        value_object.Datetime(end)
        
        # csv save
        docs = domain_service.get_appnum(start,end)
        domain_service.save_app_csv(end,docs)
        print("------- * complete save CSV * -------")
        
        # image save
        img_source = domain_service.get_image_link(docs)
        domain_service.save_img(end, img_source)
        print("------- * complete all * -------")
