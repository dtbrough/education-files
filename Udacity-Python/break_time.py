import webbrowser
import time

total_breaks = 3
breaks_count = 0
work_time = 0.2 # Time in minutes

print ("The program was started on " + time.ctime())
while (breaks_count < total_breaks):
    time.sleep(work_time * 60)
    webbrowser.open("https://www.youtube.com/watch?v=vt79JcPfZQA")
    breaks_count = breaks_count + 1
