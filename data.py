import pymysql



connectionInstance   =  pymysql.connect(host='localhost', user='root', password='')
cursorInsatnce        = connectionInstance.cursor()                                    

 

    # SQL Statement to create a database

sqlStatement            = "CREATE DATABASE "+ 'hey'
cursorInsatnce.execute(sqlStatement)