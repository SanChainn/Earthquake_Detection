import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from time import sleep
from datetime import datetime
from drawnow import *

style.use('fivethirtyeight')



def main():
    timex = []
    levely= []

    plt.ion()
    
    def makefig():
        plt.title("Earthquake Detection LEVEL")
        #plt.ylim(0,50)
        plt.ylabel('LEVEL')
        plt.xlabel('TIME')
        plt.xticks(rotation=45)
        plt.xticks(fontsize=10)
        plt.plot(timex,levely ,'ro-',linewidth=1)

    
    while True: 
            graph_data = open('example.txt','r').read()
            lines = graph_data.split('\n')
            timex  = []
            levely = []
            for line in lines:
                if len(line) > 1:
                    x, y = line.split(',')
                    #H , M , S = x.split(':')
                    #print( H , M , S)
                    #count+=1
                    #print("COUNT ::",count)
                    # time_string = datetime.strptime(a , '%H:%M:%S')
                    # print(time_string)
                    
                    timex.append(x)
                    levely.append(float(y))
            
                
                    sleep(0.2)
                    print(timex," ::: ",levely)
                    drawnow(makefig)
                    #sleep(0.3)
                    #plt.pause(.001)                

    


if __name__ == "__main__":
    main()






