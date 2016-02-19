#import LCD
import time

def processData(data):
    # example data: 
    # "ETA 143\nTASK MAIL\n"
    commands = data.split('\n')
    for command in commands:
        args = command.split(' ')
        if args[0] == 'ETA':
            smartStoolLCD(args)
        elif args[0] == 'TASK':
            smartStoolLCD(args)
        else:
            # if the last line is not empty
            if len(args[0]):
                print 'Invalid message format'
            
def smartStoolLCD(args):
    if args[0] == 'ETA':
        tformat = time.strftime('%M:%S',time.gmtime(int(args[1])))
        line = args[0] + ':' + ' '*7 + tformat
        #LCD.writeline(1,line)
        print line 
    elif args[0] == 'TASK':
        line = args[0] + ':' + ' '*(11-len(args[1])) + args[1]
        #LCD.writeline(2,line)
        print line
    else:
        print 'smartStoolLCD: not sure what to do with these args'
