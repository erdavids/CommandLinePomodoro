import click, sys, os, os.path, configparser, subprocess, time

reload(sys)
sys.setdefaultencoding('utf8')

@click.group()
def main():
    """
        \b
        Pomodoro in the terminal.
        
        
        
        """
    pass

@main.command()
@click.argument('worktime')
@click.argument('breaktime')
@click.argument('cycles')
@click.argument('longbreaktime')
def start(worktime, breaktime, cycles, longbreaktime):
    """
        
        pomodoro start [WORK_TIME] [BREAK_TIME] [CYCLES] [LONG_BREAK_TIME]
        
        All time inputs should be in minutes.
        
        """
    for x in range(0,int(cycles)):
        timer_total = int(int(worktime)*60)
        start_time = int(time.time())
        time_left = timer_total

        while (time_left > 0):

            time_left = timer_total
            now_time = int(time.time())
            elapsed_time = now_time - start_time

            time_left = timer_total - elapsed_time
            
            
            # Minutes Left
            minInt = time_left/60
            minStr = str(minInt)
            
            # Seconds Left
            secInt = time_left%60
            secStr = str(secInt)
            if (secInt < 10):
                secStr = "0" + secStr
            
            print("   Work: " + minStr + ":" + secStr)
            sys.stdout.write("\033[F")
            sys.stdout.flush()
            time.sleep(.05)
        print("   Work: Finally, time for a break!")
        
        timer_total = int(int(breaktime)*60)
        start_time = int(time.time())
        time_left = timer_total
                  
        while (time_left > 0 and x < int(cycles)):
          time_left = timer_total
          now_time = int(time.time())
          elapsed_time = now_time - start_time
          
          time_left = timer_total - elapsed_time
          
          # Minutes Left
          minInt = time_left/60
          minStr = str(minInt)
              
          # Seconds Left
          secInt = time_left%60
          secStr = str(secInt)
          if (secInt < 10):
              secStr = "0" + secStr
          
          print("   Break: " + minStr + ":" + secStr)
          sys.stdout.write("\033[F")
          sys.stdout.flush()
          time.sleep(.05)
        print("   Break: Time to get back to it!")
            
    timer_total = int(int(longbreaktime)*60)
    start_time = int(time.time())
    time_left = timer_total

    while (time_left > 0):
    
        time_left = timer_total
        now_time = int(time.time())
        elapsed_time = now_time - start_time
        
        time_left = timer_total - elapsed_time


        # Minutes Left
        minInt = time_left/60
        minStr = str(minInt)

        # Seconds Left
        secInt = time_left%60
        secStr = str(secInt)
        if (secInt < 10):
            secStr = "0" + secStr

        print("   Long Break: " + minStr + ":" + secStr)
        sys.stdout.write("\033[F")
        sys.stdout.flush()
        time.sleep(.05)
    print("   Long Break: Congratulations! That was a great session!")
