from flask import g
import MySQLdb


def db_connect():
	g.conn = MySQLdb.connect(host='localhost',user='root',passwd='GroupTen',db='sherlock')
	g.cursor = g.conn.cursor()

def db_disconnect():
	g.cursor.close()
	g.conn.close()

def insertBatchTrainingData(filename):
    f_train = open(filename, "r")
    lines = f_train.readlines()
    i = 0
    iter = 0
    linecount = 0
    lines = lines[1:]
    singledatapoint = [33.388414, -111.931782, "Tempe"]
    emailID = 'joeljmj26@gmail.com'
    noOfRows = len(lines)
    count = noOfRows//300
    currentRow = []
    while(iter < count):
        while(i < 300):
            eachline = lines[linecount]
            tokens = eachline.split(',')
            tokens = tokens[1:]
            singledatapoint = singledatapoint.extend(tokens)
            linecount+= 1
            i+= 1

        insertQuery = "INSERT INTO training(latitude,longitude,city"
        for i in range(0, 300):
            insertQuery = insertQuery + ",x" + str(i + 1) + ",y" + str(i + 1) + ",z" + str(i + 1)
        insertQuery = insertQuery + ",id) VALUES ("
        insertQuery = insertQuery + str(tokens[0]) + "," + str(tokens[1]) + ",\"" + str(tokens[2]) + "\""
        for eachVal in range(3, 300):
            insertQuery = insertQuery + "," + str(eachVal)
        insertQuery = insertQuery + ",\"" + emailID + "\");"
        g.cursor.execute(insertQuery)
        g.conn.commit()
        i = 0
        iter+= 1
    db_disconnect()



def main():
    filename = "accel_log.csv"
    insertBatchTrainingData(filename)


if __name__ == '__main__':
    main()