import unittest
import app
from app import parse_cli_args
from unittest.mock import Mock


class TestKafka(unittest.TestCase):   

    def test_read_args_with_no_arguments(self):
        with self.assertRaises(SystemExit):
            parse_cli_args()

    def test_produce_message(self):
        app = Mock() 
        app.produce_message('test-event','localhost:9092')
        app.produce_message.assert_called_once()
        app.produce_message.assert_called_with('test-event','localhost:9092')
        assert app.produce_message.call_count == 1
        print(app.produce_message.call_args_list)

    def test_consume_message(self):
        app = Mock() 
        app.consume_message('start','test-event','localhost:9092')
        app.consume_message.assert_called_once()  
        app.consume_message.assert_called_once_with('start','test-event','localhost:9092')
        assert app.consume_message.call_count == 1
        print(app.consume_message.call_args_list)


#set .side_effect to a function that Mock will invoke when you call your mocked method.
    def logger(self, err, msg):
        if err is not None:
            print('Message delivery error: {}'.format(err))
            return 'error logged'
        else:
            print('Message {} delivered to topic'.format(msg))

            return 'message logged'
    
    def test_delivery_report_logging(self):
            # Test a successful, logged request
            app = Mock() 
            app.delivery_report.side_effect = self.logger('error','hey')
            assert app.delivery_report() != 'error logged'
            app.delivery_report.side_effect = self.logger(None,'hey')
            assert app.delivery_report() != 'message logged'             

if __name__=='__main__': 
       
    unittest.main()
    
        