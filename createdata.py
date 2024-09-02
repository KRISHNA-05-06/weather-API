import sqlconnect

con = sqlconnect.connection()
cur = con.cursor()

def createtable():
    return
    #cur.execute("CREATE TABLE data(location VARCHAR(50),temperature VARCHAR(50),weather VARCHAR(20),humidity VARCHAR(10),windspeed VARCHAR(10),datetime VARCHAR(50));")

def loaddata(location,temp_city,weather_desc,hmdt,wind_spd,date_time):
    createtable()

    cur.execute("INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s);",(location,temp_city,weather_desc,hmdt,wind_spd,date_time))
    con.commit()