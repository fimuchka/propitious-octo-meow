
from django.http import HttpResponse
from django.views.generic import View
from django.http import JsonResponse
from django.utils import timezone

from .models import Solution

class SolutionApiView(View):
    
    @staticmethod
    def sum_of_squares(n):
        #http://www.trans4mind.com/personal_development/mathematics/series/sumNaturalSquares.htm
        return n*(n+1)*(2*n+1)/6
    
    @staticmethod
    def square_of_sum(n):
        return (n*(n+1)/2)**2
        
    def get(self, request, *args, **kwargs):
        '''
            Technically a get shouldn't create 
            or modify but this is a simple case, so ...
            Also maybe make sure it's an ajax request
        '''
        n = request.GET.get('number')
        if n:
            n = int(n)
            try:
                solution = Solution.objects.get(number=n)
                solution.occurences += 1
            except Solution.DoesNotExist:
                solution = Solution(number=n)
                solution.sum_squares = SolutionApiView.sum_of_squares(n)
                solution.square_of_sum = SolutionApiView.square_of_sum(n)
                solution.difference = solution.square_of_sum-solution.sum_squares
            
            solution.save()
            
            return JsonResponse({
                'datetime': timezone.now(),
                'value': solution.difference,
                'number': n,
                'occurences': solution.occurences
            })
        
        return JsonResponse({
            'error': 'Please provide a number'}, status=400)