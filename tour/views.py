from random import sample
from django.shortcuts import render
from django.views import View
from tour.data import title, subtitle, description, departures, tours

context = { "title" : title, "subtitle" : subtitle, "description" : description, "departures" : departures}

class MainView(View):
    def get(self, request, *args, **kwargs):
        random_tour = {}
        index_list = sample(range(1,16), 6)

        for i in index_list:            
            random_tour.update( { i : tours[i]} )
            

        context["tours"] = random_tour

        return render(
            request, 'tour/index.html', context=(context) 
        )        

        
class DepartureView(View):
    def get(self, request, departure, *args, **kwargs):        
        depart = {}

        for key, value in tours.items():
            if value["departure"] == departure:
                depart[key] = value

        context["tours"] = depart

        return render(
            request, 'tour/departure.html', context=(context)
        )
    

class TourView(View):
    def get(self, request, id):
        departure = tours[id]
        departure = departures[departure["departure"]]

        context.update({"tour" : tours[id], "departure" : departure })
        
        return render(
            request, 'tour/tour.html', context=(context)
        )
