from models import Bank,Location

def required_context(request):
    bank_list=Bank.objects.all()
    location_list=Location.objects.all()
    return {'bank_list':bank_list,'location_list':location_list}
    #return {'bank_list':bank_list}
    

    
  
  