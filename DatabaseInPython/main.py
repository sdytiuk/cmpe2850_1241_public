import mysql.connector



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mydb = None
    pw = 'demo_password'
    try:
        mydb = mysql.connector.connect(
            host="thor.cnt.sast.ca",
            user="demo_user",
            password=pw,
            database='demo_project'
        )
    except mysql.connector.Error as err:
        print(f'Something went wrong: {err}')
    if mydb != None and mydb.is_connected():
        print(f'Connected : {mydb.get_server_info()}')

    #how to query database table?
    try:
        mycursor = mydb.cursor(buffered=True)
        query = f"select * from authors where state like %s" #%s is a single parameter to sub
        filter = 'CA'
        params=(filter,) #parameters tuple of arguments

        mycursor.execute(query,params)

        column_names = mycursor.column_names

        resultset = mycursor.fetchall()

    except mysql.connector.Error as err:
        print(f'Something went wrong : {err}')
        resultset = None
    finally:
        mycursor.close()

    print(column_names)
    print(resultset)


