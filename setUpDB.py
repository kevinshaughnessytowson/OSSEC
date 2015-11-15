import MySQLdb as sql

db = sql.connect(host="localhost", user="root", passwd="toor", db="scan")
cursor = db.cursor()
create_stmt = 'CREATE DATABASE scan;'

try:
	cursor.execute(create_stmt)
except:
	print("Database already exists")

try:
	cursor.execute('CREATE TABLE `services` (`port` int(8) NOT NULL,`packet_format` text NOT NULL, PRIMARY KEY (`port`)) ENGINE=InnoDB')
except:
	print("Table already exists")

cursor.execute('INSERT INTO services (`port`, `packet_format`) VALUES (7, "sr1(IP(dst=?)/ICMP())")')
cursor.execute('INSERT INTO services (`port`, `packet_format`) VALUES (21, "sr1(IP(dst=?)/ICMP())")')
#create_table = ("CREATE TABLE `services` ("
#    "  `port` int(8) NOT NULL,"
#    "  `packet_format` text NOT NULL,"
#    "  PRIMARY KEY (`port`)"
#    ") ENGINE=InnoDB")



#cursor.execute(create_table)
