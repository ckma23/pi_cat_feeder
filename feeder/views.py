from django.shortcuts import render

class FeederView:
    def index(request):
        page_body = CatsMessage()
        page_body.populate()

        if request.method == 'GET':
            return render(request,'feeder/index.html', page_body.context)

        elif request.method == 'POST':
            feedus(request)
            return render(request,'feeder/index.html', page_body.context)

class CatsMessage:
    def __init__(self):
        self.context = {}

    def populate(self):
        self.context["cat_1"] = "Goose"
        self.context["cat_2"] = "Tuna"

def feedus(request):
    print("FEEDING")
# Create your views here.
