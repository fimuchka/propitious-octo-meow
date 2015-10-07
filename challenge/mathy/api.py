from django.http import HttpResponse
from django.views.generic import View
from django.http import JsonResponse


class SolutionApiView(View):
    
    @staticmethod
    def sum_of_squares(n):
        #http://www.trans4mind.com/personal_development/mathematics/series/sumNaturalSquares.htm
        return n*(n+1)*(2*n+1)/6
    
    @staticmethod
    def square_of_sum(n):
        return (n*(n+1)/2)**2
        
    def get(self, request, *args, **kwargs):
        return 