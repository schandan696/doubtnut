import persistqueue
from pdfhandler import writePdf
ackq = persistqueue.SQLiteAckQueue('finalData')
while True:
    item = ackq.get()
    print(item)
    writePdf(item['user'], item['questionAnsList'])
    ackq.ack(item) # If done with the item