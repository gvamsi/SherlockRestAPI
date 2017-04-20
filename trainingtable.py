import MySQLdb

def traininginsert():
	conn = MySQLdb.connect(host='localhost',user='root',passwd='GroupTen',db='sherlock')
	dataset = []
	for i in range(0,300):
		dataset.append("x"+str(i+1))
		dataset.append("y"+str(i+1))
		dataset.append("z"+str(i+1))
	cursor = conn.cursor()
	cursor.execute("CREATE TABLE training (latitude VARCHAR(100) NOT NULL, longitude VARCHAR(100) NOT NULL, city VARCHAR(100) NOT NULL)")
	#print dataset
	for i in range(0,900):
		val = dataset[i]
		strval = str(val)
		cursor.execute("ALTER TABLE training ADD %s FLOAT(10) NOT NULL"%(strval))

	cursor.execute("ALTER TABLE training ADD id VARCHAR(100) NOT NULL")
	cursor.execute("ALTER TABLE training ADD PRIMARY KEY(id)")
	cursor.close()
	conn.close()

def main():
	traininginsert()

if __name__ == '__main__':
  main()
