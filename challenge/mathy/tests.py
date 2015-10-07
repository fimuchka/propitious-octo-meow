import random
import json

from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse


from .models import Solution
from .api import SolutionApiView

def naive_sum_of_squares(n):
    result = 0
    for i in range(1, n+1):
        result += i**2
    return result
    
def naive_square_of_sum(n):
    return sum(xrange(1,n+1))**2
    
# Create your tests here.
class SolutionTests(TestCase):
    
    def test_sum_of_squares(self):
        '''
        Compares the naive method used in 
        the test to the formula used in the app
        '''

        n = random.randint(1,100)
        self.assertEqual(naive_sum_of_squares(n),
                            SolutionApiView.sum_of_squares(n), 'Wrong sum of squares result')

    def test_square_of_sums(self):
        '''
        Compares the naive method used in 
        the test to the formula used in the app
        '''
        n = random.randint(1,100)
        self.assertEqual(naive_square_of_sum(n),
                           SolutionApiView.square_of_sum(n), 'Wrong sum of squares result')
        
    def test_correct_result(self):
        '''
            Correct status code
            Correct value
            Had datetime, number, occurences
        '''
        n = random.randint(1,100)
        client = Client()
        response = client.get('%s?number=%s'% (reverse('mathy:difference'), n),
                        HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200, 'Response returned %d' %
                         response.status_code)
        result = json.loads(response.content)
        self.assertIn('datetime', result, 'Response does not have datetime')
        self.assertIn('value', result, 'Response does not have a value')
        self.assertIn('number', result,'Response does not have a number')
        self.assertIn('occurences', result,'Response does not have an occurence')
    
        self.assertEquals(result['value'], naive_square_of_sum(n)-naive_sum_of_squares(n),
            'Value is not equal to computed test value for %s' % n)
            
    def test_out_of_bounds(self):
        '''
            Less than 0, more than 100
        '''
        self.fail('Not implemented')
        
    def test_increment_of_occurence(self):
        self.fail('Not implemented')
        
    def test_created_in_db(self):
        '''
        Test that a get request result is stored in the db
        '''
        n = random.randint(1,100)
        client = Client()
        response = client.get('%s?number=%s'% (reverse('mathy:difference'), n),
                        HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200, 'Response returned %d' %
                         response.status_code)
        
        Solution.objects.get(number=n)