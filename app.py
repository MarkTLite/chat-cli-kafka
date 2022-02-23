import argparse
from confluent_kafka import Producer, Consumer
 
def parse_cli_args(): 
    '''Returns a namespace object formed from parsing Command line arguments''' 
    parse_obj = argparse.ArgumentParser()
    parse_obj.add_argument("command", help="Command", choices=['send', 'receive'])
    parse_obj.add_argument('--channel', help="Kafka Topic to work with", required=True)
    parse_obj.add_argument('--server', help="server to work with", required=True)
    parse_obj.add_argument('--group', help="The group id to send messages to", required=False)
    parse_obj.add_argument('--_from', help="The point to start receiving messages from", 
                        choices=['start', 'latest'], default='start')
    args = parse_obj.parse_args()
    print(args)
    return args

def delivery_report(err, msg): 
        """ For each message produced, indicates delivery result. Is triggered by poll() or flush(). """
        if err is not None:
            print('Message delivery error: {}'.format(err))
        else:
            print('Message delivered to topic:{} partition:{}'.format(msg.topic(), msg.partition()))

def produce_message(channel, server):
    '''Produce the message to a given topic using server''' 
    producer = Producer({'bootstrap.servers': server})    
    message = ''
    print("Chat CLI")
    while message != 'q':        
        message = input("Enter message or 'q' to quit: ")
        if message == 'q':
            break
    	
        producer.produce(channel, message.encode('utf-8'), callback=delivery_report)
        producer.flush()
        

def consume_message(start_pt,server, channel):
    '''Subscribe to a given kafka topic, listening on server and receive from a given starting point''' 
    offset_config = {'start': 'earliest', 'latest': 'latest'}
    consumer = Consumer({
        'bootstrap.servers': server,
        'group.id': 'mygroup',
        'default.topic.config': {
            'auto.offset.reset': offset_config[start_pt]  # 'smallest'
        }
    })
    
    consumer.subscribe([channel])
    running = True
    try:
        print("Chat CLI") 
        while running:
            msg = consumer.poll(1.0)

            if msg is None:
                continue
            if msg.error():
                print(msg.error())
                break
                
            print('Received message: {}'.format(msg.value().decode('utf-8')))
            
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
    return True
