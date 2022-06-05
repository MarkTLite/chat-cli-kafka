
import unittest
from app import parse_cli_args
from unittest.mock import Mock, patch
import app

class TestKafka(unittest.TestCase):

    def setup_ArgumentParser(self):
        print("testing parse_args_with_arguments: {'channel':'test-channel','server':'test-server'}")
        response_args = Mock()
        response_args.parse_args.return_value = {'channel':'test-channel','server':'test-server'}
        return response_args

    def log_add_argument(self):        
        response = Mock()        
        response.add_argument.return_value = print("add_argument_called")             
        return response    

    def setup_producer_object(self,server):
        prodObject = Mock()
        prodObject.produce.return_value = print("produced encoded message to test-topic ")
        prodObject.flush.return_value = "flushed topic"
        return prodObject

    def setup_poll(self,value):
        pollObj = Mock()
        pollObj.error.return_value = False
        pollObj.value.return_value = "Value"
        return pollObj

    def setup_consumer_object(self,server):
        consumeObject = Mock()
        consumeObject.subscribe.return_value = print("produced encoded message to test-topic ")
        consumeObject.poll.side_effect = self.setup_poll
        consumeObject.close.return_value = "closed consumer"
        return consumeObject

    def test_read_args_with_no_arguments(self):
        with self.assertRaises(SystemExit):
            parse_cli_args()

    @patch('builtins.print') #test a print
    @patch('app.argparse')    
    def test_add_argument(self,mock_argparse,mock_print):           
        mock_argparse.ArgumentParser.side_effect = self.log_add_argument
        parse_cli_args()        
        mock_print.assert_called_with('add_argument_called')
            

    @patch('app.argparse')    
    def test_parse_args_with_arguments(self,mock_argparse):        
        mock_argparse.ArgumentParser.side_effect = self.setup_ArgumentParser
        assert parse_cli_args()['channel'] == 'test-channel'

    @patch('builtins.print')    
    @patch('app.ck')    
    def test_Producer(self,mock_producer,mock_produce):
        mock_producer.Producer.side_effect = self.setup_producer_object       
        app.produce_message('test-topic','test-server')           
        mock_produce.assert_called_with('Chat CLI')
        mock_produce.assert_called()               

    @patch('builtins.print')    
    @patch('app.ck') 
    def test_consumer(self,mock_consumer,mock_consume):
        mock_consumer.Consumer.side_effect = self.setup_consumer_object       
        app.consume_message('latest','test-server','test-topic')           
        mock_consume.assert_called()

    @patch('builtins.print')
    @patch('app.ck')   
    def test_msg_error_when_None(self,mock_consumer,mock_print):    
        pass

    def test_consumer_close(self):
        pass
#     @patch('app.Producer')          
#     @patch('app.produce_message')
#     def test_produce_message(self,mock_producer,mockProducer):   
#         mockProducer.return_value = 2       
#         app.produce_message('test-event','localhost:9092')
#         mock_producer.assert_called_once()        
#         mock_producer.assert_called_with('test-event','localhost:9092')        
#         self.assertTrue(2, mockProducer)

#     @patch('app.Producer.produce')  
#     @patch('app.Producer')          
#     @patch('app.produce_actions')
#     def test_produce_actions(self,mock_produce,mockProducer,pp):            
#         app.produce_actions(mockProducer,'test-event','hey')
#         mock_produce.assert_called_once() 
#         print(pp)  


#         testproduce = mockProducer.produce('test-event','hey')
#         #testproduce.assert_called_once()             
       
#     @patch('app.consume_message')
#     def test_consume_message(self,mock_consumer):
#         app.consume_message('start','test-event','localhost:9092')
#         mock_consumer.assert_called_once()  
#         mock_consumer.assert_called_once_with('start','test-event','localhost:9092')
        

#  #set .side_effect to a function that Mock will invoke when you call your mocked method.
#     def logger(self, err, msg):
#         if err is not None:
#             print('Message delivery error: {}'.format(err))
#             return 'error logged'
#         else:
#             print('Message {} delivered to topic'.format(msg))

#             return 'message logged'

#     @patch('app.delivery_report')    
#     def test_delivery_report_logging(self,mock_delivery):
#             # Test a successful, logged request
#             mock_delivery.side_effect = self.logger('error','hey')
#             assert app.delivery_report() != 'error logged'
#             mock_delivery.side_effect = self.logger(None,'hey')
#             assert app.delivery_report() != 'message logged'             

if __name__=='__main__':       
    unittest.main()
    
        