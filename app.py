import os
from flask import Flask, request, jsonify
import pymysql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

db_config = {
    'host': 'dbms.cbj29vmpnvrx.us-east-1.rds.amazonaws.com',
    'user': 'admin',
    'password': 'password',
    'database': 'carematch'
}


@app.route('/insert_data', methods=['POST'])
def insert_data():
    try:
        data = request.json
        print(data)

        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()
        print(data)
        users = "INSERT INTO Users (name,email,ID,Rating) VALUES (%s, %s,%s,%s)"
        applied_query = "Insert into Applies values (%s,%s)"


        table = data.get("table")
        print("just above")
        print(table)
        if (table == "Job_Listings"):
            title = data.get("job_title")
            description = data.get("description")
            pay = data.get("pay_per_hr")
            time = data.get("time_posted")
            duration = data.get("duration")
            ID = data.get("ID")
            print(title,description,pay,time,duration,ID)
            job_query = f"INSERT INTO Job_Listings (job_title,description,time_posted,pay_per_hr,duration,ID) VALUES ('{title}','{description}','{time}','{pay}','{description}','{ID}')"

            cursor.execute(job_query)
        elif (table=="rating"):
            x = data.get("user_id")
            print(x)
            rating = data.get("rating")
            print(rating)
            query = f"SELECT ratingavg({rating}, '{x}') AS calculated_rating"
            cursor.execute(query)
            result = cursor.fetchone()
            print(result)
            calculated_rating = result[0] if result else None
            print(calculated_rating)
            print("Calculated Rating:", calculated_rating)
            return jsonify({"rating": calculated_rating})



        elif(table =="Users"):
            name = data.get("name")
            email = data.get("email")
            ID = data.get("ID")
            rating = 5
            cursor.execute(users, (name,email,ID,rating))
        elif table == "Applied":
            ID = data.get("ID")
            Jid = data.get ("jid")
            cursor.execute(applied_query, (ID,Jid))
        elif table == "Usersupdate":
            ID = data.get("ID")
            email = data.get("email")
            name = data.get("name")
            phone_number = data.get("phone_number")
            bio = data.get("bio")
            print(name)
            update_user = f"UPDATE Users SET name = '{name}', email = '{email}',phone_number = '{phone_number}',bio = '{bio}' WHERE ID = '{ID}'"
            cursor.execute(update_user)
            quality1 = data.get("quality1")
            quality2 = data.get("quality2")
            quality3 = data.get("quality3")

        elif table == "Delete":
            ID = str((data.get("ID")))
            try:
                cursor.callproc('deletequery', args=(ID,))
                connection.commit()  # If using transactions, commit changes
                print("Procedure executed successfully")
            except Exception as e:
                print(f"Error executing procedure: {e}")


        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({'message': 'Data inserted successfully'}), 200

    except pymysql.Error as e:
        return jsonify({'error': f'Error inserting data: {str(e)}'}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use port provided by Heroku or default to 5000
    app.run(host='0.0.0.0', port=port)
