import app
import test_app


if __name__=='__main__':    
     args = app.parse_cli_args()
     if args.command == 'send':  
          
          app.produce_message(args.channel,args.server)
     if args.command == 'receive':
          print(f'You are receiving from the channel:{args.channel}')
          app.consume_message(args._from,args.server,args.channel)

     