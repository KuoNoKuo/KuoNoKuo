import sqlite3
#connect the scriipt to the .db file
con = sqlite3.connect("example.db")
cur = con.cursor()

#CREATE A TABLE:
#cur.execute("id integer PRIMARY KEY player(age integer, score integer , level integer)")

#INSERT INTO THE TABLE


#ORDER BY  
cur.execute('select * from player order by age asc') #Selects rows according to the age column
#asc = ascent
#desc = descent 

#LIMIT
cur.execute('select * from player limit 1 offset 2')
#liimites howo many results will be selected 

#HAVING 
#When searches, it will compare the value to the condition
cur.execute('select * from player GROUP BY age HAVING count(age) between 1 and 2')

#SELECT 
cur.execute('from player select *')
a = cur.fetchall()
print(a)



#END SCRIPT
cur.close()
con.close()