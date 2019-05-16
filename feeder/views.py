from django.shortcuts import render
from feeder.raspberry_service import LedLighter as LedLighter
from feeder.raspberry_service import FeederMotor as FeederMotor

class FeederView:
    def index(request):
        page_body = CatsMessage()
        page_body.populate()
        if request.method == 'GET':
            return render(request,'feeder/index.html', page_body.context)

        elif 'light' in request.POST.keys():
            print ("LIGHT")
            light_up(request)
            return render(request,'feeder/index.html', page_body.context)

        elif 'feed' in request.POST.keys():
            print ("FEED")
            feed_us(request)
            return render(request,'feeder/index.html', page_body.context)

class CatsMessage:
    def __init__(self):
        self.context = {}

    def populate(self):
        self.context["cat_1"] = "Goose"
        self.context["cat_2"] = "Tuna"

def light_up(request):
    print("LIGHTING")
    ll_handler = LedLighter(18)
    ll_handler.setup_led()
    ll_handler.light_up(3)

def feed_us(request):
    print ("FEEDING")
    fm_handler = FeederMotor(32)
    fm_handler.setup_motor()
    fm_handler.motor_move(1)
# Create your views here.
