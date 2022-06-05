import argparse 
import confluent_kafka as ck

def get_input(text,count): 
    return input(text)
 
def parse_cli_args(): 
    '''Returns a namespace object formed from parsing Command line arguments''' 
    parse_obj = argparse.ArgumentParser()
    parse_obj.add_argument("command", help="Command", choices=['send', 'receive'])
    parse_obj.add_argument('--channel', help="Kafka Topic to work with", required=True)
    parse_obj.add_argument('--server', help="server to work with", required=True)
    parse_obj.add_argument('--group', help="The group id to send messages to", required=False)
    parse_obj.add_argument('--_from', help="The point to start receiving messages from", choices=['start', 'latest'], default='start')

    args = parse_obj.parse_args()
    #print(args)
    return args

def produce_message(channel, server):
    '''Produce the message to a given topic listening on givenserver''' 
    producer = ck.Producer({'bootstrap.servers': server})    
    message = ''
    count = 0
    print("Chat CLI")
    while message != 'q':        
        message = get_input("Enter message or 'q' to quit: ",count) #count used when mocking input values
        count+=1
        if message == 'q':
            break 	

        producer.produce(channel, message.encode('utf-8'))
        producer.flush()  

def consume_message(start_pt,server, channel):
    '''Subscribe to a given kafka topic, listening on server and receive from a given starting point''' 
    offset_config = {'start': 'earliest', 'latest': 'latest'}
    consumer = ck.Consumer({
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
                
            print('Received message: {}'.format(msg.value()))
            
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
    return True
