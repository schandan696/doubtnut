from threading import Timer
import sys
import persistqueue
ackq = persistqueue.SQLiteAckQueue('data')

def scheduled_task(arg):
    processq = persistqueue.SQLiteAckQueue('finalData')
    print(arg)
    processq.put(arg)


def run_scheduled_task(arg, t):
    timer = Timer(t, scheduled_task, [arg])
    timer.start()

while True:
    item = ackq.get()
    run_scheduled_task(item, int(item['waitTime'])*60)
    ackq.ack(item)