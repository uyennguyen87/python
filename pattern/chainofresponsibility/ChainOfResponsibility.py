'''
Created on Jan 28, 2016

@author: ncuyen
'''
import json
import traceback


class Result: 
    def __init__(self, value, message):
        self.value = value
        self.message = message
        
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print exc_type, exc_value, traceback
            # return False # uncomment to pass exception through

        return self
    
    def __enter__(self): return self
    
    def __str__(self):
        return """
        {
            'value': """ + str(self.value) + """,
            'message': '""" + self.message + """'
        }
        
        """

class Strategy:
    def __call__(self, data):
        try:
            return self.do_algorithm(data)
        
        finally:
            """ 
            do nothing because
            this example not access the resource
            """
        
    def __str__(self):
        return 'Trying ' + self.__class__.__name__ \
            + ' algorithm'

    def do_algorithm(self, data):
        assert 0, 'not implemented yet'
        
def validate_list_type(data):
    if not type(data) is list:
        raise Exception('invalid data: expect data is list')
    
class X2Value(Strategy):
    def do_algorithm(self, data):
        validate_list_type(data)

        x2_list = [x*2 for x in data]
        return Result(x2_list, 'x2 value for each element in list')

class CalculateWeight(Strategy):
    WEIGHT_FACTOR = 1.3
    
    def do_algorithm(self, data):
        validate_list_type(data)

        average_number =  sum(data)/len(data)
        calculated_weight = average_number * CalculateWeight.WEIGHT_FACTOR
        
        return Result(calculated_weight, 'calculate the weight')

class MidVarian(Strategy):
    def __init__(self):
        self.get_calculated_weight = CalculateWeight()
    
    def do_algorithm(self, data):
        validate_list_type(data)

        calculated_weight = self.get_calculated_weight(data)
        print calculated_weight
        
        mid_varian_data = self.make_mid_varian_list(data,
                                                     calculated_weight.value)
        return Result(mid_varian_data, 'make mid varian data')

    def make_mid_varian_list(self, data, weight):
        return [abs(weight - x) for x in data]

class TransformToJSONData(Strategy):
    def do_algorithm(self, data):
        validate_list_type(data)
        enumurated_data = {number:value for (number, value) in enumerate(data)}
        json_data = json.dumps(enumurated_data)
        return Result(str(json_data), 'transfrom JSON')
        
# Manage the movment through the chain and
# find a successful result:
class ChainLink:
    def __init__(self):
        self.__task_queues = [];
    
    def set_task_queue(self, new_task_queue):
        self.__task_queues = new_task_queue[:]

    def get_builder(self):
        class ChainLinkBuilder:
            def __init__(self, chain_link):
                self.task_queues = []
                self.chain_link = chain_link

            def append_task(self, strategy):
                self.task_queues.append(strategy)
                return self

            def build(self):
                self.chain_link.set_task_queue(self.task_queues)
                self.task_queues = None
                return self.chain_link
            
        return ChainLinkBuilder(self)

    def process(self, data):
        result = Result(data, 'initial data')
        print result
        
        for strategy in self.__task_queues:
            with strategy(result.value) as new_result:
                    result = new_result
                    print result
if __name__ == '__main__':
    chain = ChainLink().get_builder() \
                       .append_task(X2Value()) \
                       .append_task(MidVarian()) \
                       .append_task(TransformToJSONData()) \
                       .build()
 
    data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.7, 3.2, 1.1, 4.3, 3.7]
    chain.process(data)
    
    # Test exception
    data = "error data type"
    try:
        chain.process(data)
    except Exception, e:
        print e