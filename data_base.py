# from flask import Flask, jsonify
# import mysql.connector

# app = Flask(__name__)

# # Configure MySQL connection
# db = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='Obinna_A1',
#     database='mydatabase2'
# )

# @app.route('/get_data', methods=['GET'])
# def get_data():
#     cursor = db.cursor()
#     cursor.execute('SELECT * FROM polling_unit')
#     data = cursor.fetchall()
#     cursor.close()
#     return jsonify({'data': data})

# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask, render_template, request, jsonify
# import mysql.connector

# app = Flask(__name__)

# # Configure MySQL connection
# db = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='Obinna_A1',
#     database='mydatabase2'
# )



# # Sample data for polling unit IDs
# polling_unit_ids = [8,9,10,11,12,13,15,16,18,19,20,21,22,23,24,25,26,27]  # Add more IDs as needed

# def get_lga_names():
#     cursor = db.cursor()
#     cursor.execute('SELECT DISTINCT lga_name FROM lga')
#     lga_names = [row[0] for row in cursor.fetchall()]
#     cursor.close()
#     return lga_names


# @app.route('/')
# def home():
#     return render_template('home.html', polling_unit_ids=polling_unit_ids,lga_names= lga_names)

# @app.route('/display_results/<int:polling_unit_uniqueid>', methods=['GET'])
# def display_results(polling_unit_uniqueid):
#     cursor = db.cursor()
#     cursor.execute('SELECT * FROM announced_pu_results WHERE polling_unit_uniqueid = %s', (polling_unit_uniqueid,))
#     data = cursor.fetchall()
#     cursor.close()
#     return render_template('display_results.html', data=data, polling_unit_uniqueid=polling_unit_uniqueid)

# @app.route('/party_scores_per_polling_unit')
# def party_scores_per_polling_unit():
#     cursor = db.cursor(dictionary=True)

#     # Fetch the data to calculate total party scores per polling_unit_uniqueid for each lga_name
#     cursor.execute('''
#         SELECT lga.lga_name, apr.polling_unit_uniqueid, apr.party_abbreviation, SUM(apr.party_score) AS total_score
#         FROM announced_pu_results apr
#         JOIN polling_unit pu ON apr.polling_unit_uniqueid = pu.uniqueid
#         JOIN lga ON pu.lga_id = lga.lga_id
#         GROUP BY lga.lga_name, apr.polling_unit_uniqueid, apr.party_abbreviation
#     ''')
#     result_rows = cursor.fetchall()

#     # Dictionary to store total party scores per polling_unit_uniqueid for each lga_name
#     total_party_scores_per_polling_unit = {}

#     for row in result_rows:
#         lga_name = row['lga_name']
#         polling_unit_uniqueid = row['polling_unit_uniqueid']
#         party_abbreviation = row['party_abbreviation']
#         total_score = row['total_score']

#         if lga_name not in total_party_scores_per_polling_unit:
#             total_party_scores_per_polling_unit[lga_name] = {}

#         if polling_unit_uniqueid not in total_party_scores_per_polling_unit[lga_name]:
#             total_party_scores_per_polling_unit[lga_name][polling_unit_uniqueid] = {}

#         total_party_scores_per_polling_unit[lga_name][polling_unit_uniqueid][party_abbreviation] = total_score

#     cursor.close()
#     return render_template('party_scores_per_polling_unit.html', total_party_scores_per_polling_unit=total_party_scores_per_polling_unit)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Obinna_A1',
    database='mydatabase2'
)

# Sample data for polling unit IDs
polling_unit_ids = [8,9,10,11,12,13,15,16,18,19,20,21,22,23,24,25,26,27]  # Add more IDs as needed

# Function to fetch lga_names from the database
def get_lga_names():
    cursor = db.cursor()
    cursor.execute('SELECT DISTINCT lga_name FROM lga')
    lga_names = [row[0] for row in cursor.fetchall()]
    cursor.close()
    return lga_names

@app.route('/')
def home():
    lga_names = get_lga_names()
    return render_template('home.html', polling_unit_ids=polling_unit_ids, lga_names=lga_names)

@app.route('/display_results/<int:polling_unit_uniqueid>', methods=['GET'])
def display_results(polling_unit_uniqueid):
    cursor = db.cursor()
    cursor.execute('SELECT * FROM announced_pu_results WHERE polling_unit_uniqueid = %s', (polling_unit_uniqueid,))
    data = cursor.fetchall()
    cursor.close()
    return render_template('display_results.html', data=data, polling_unit_uniqueid=polling_unit_uniqueid)

# @app.route('/party_scores_per_polling_unit')
# def party_scores_per_polling_unit():
#     cursor = db.cursor(dictionary=True)

#     # Fetch the data to calculate total party scores per polling_unit_uniqueid for each lga_name
#     cursor.execute('''
#         SELECT lga.lga_name, apr.polling_unit_uniqueid, apr.party_abbreviation, SUM(apr.party_score) AS total_score
#         FROM announced_pu_results apr
#         JOIN polling_unit pu ON apr.polling_unit_uniqueid = pu.uniqueid
#         JOIN lga ON pu.lga_id = lga.lga_id
#         GROUP BY lga.lga_name, apr.polling_unit_uniqueid, apr.party_abbreviation
#     ''')
#     result_rows = cursor.fetchall()

#     # Dictionary to store total party scores per polling_unit_uniqueid for each lga_name
#     total_party_scores_per_polling_unit = {}

#     for row in result_rows:
#         lga_name = row['lga_name']
#         polling_unit_uniqueid = row['polling_unit_uniqueid']
#         party_abbreviation = row['party_abbreviation']
#         total_score = row['total_score']

#         if lga_name not in total_party_scores_per_polling_unit:
#             total_party_scores_per_polling_unit[lga_name] = {}

#         if polling_unit_uniqueid not in total_party_scores_per_polling_unit[lga_name]:
#             total_party_scores_per_polling_unit[lga_name][polling_unit_uniqueid] = {}

#         total_party_scores_per_polling_unit[lga_name][polling_unit_uniqueid][party_abbreviation] = total_score

#     cursor.close()
#     return render_template('party_scores_per_polling_unit.html', total_party_scores_per_polling_unit=total_party_scores_per_polling_unit)

# @app.route('/party_scores_per_polling_unit_by_lga/<string:lga_name>', methods=['GET'])
# def party_scores_per_polling_unit_by_lga(lga_name):
#     cursor = db.cursor(dictionary=True)

#     # Fetch party scores for each party in the specified LGA
#     cursor.execute('''
#         SELECT polling_unit_uniqueid, party_abbreviation, SUM(party_score) AS total_score
#         FROM announced_pu_results apr
#         JOIN polling_unit pu ON apr.polling_unit_uniqueid = pu.uniqueid
#         JOIN lga ON pu.lga_id = lga.lga_id
#         WHERE lga.lga_name = %s
#         GROUP BY polling_unit_uniqueid, party_abbreviation
#     ''', (lga_name,))
#     result_rows = cursor.fetchall()

#     # Dictionary to store total party scores per polling_unit_uniqueid for the specified LGA
#     total_party_scores_per_polling_unit = {}

#     for row in result_rows:
#         polling_unit_uniqueid = row['polling_unit_uniqueid']
#         party_abbreviation = row['party_abbreviation']
#         total_score = row['total_score']

#         if polling_unit_uniqueid not in total_party_scores_per_polling_unit:
#             total_party_scores_per_polling_unit[polling_unit_uniqueid] = {}

#         total_party_scores_per_polling_unit[polling_unit_uniqueid][party_abbreviation] = total_score

#     cursor.close()
#     return render_template('party_scores_per_polling_unit_by_lga.html', lga_name=lga_name, total_party_scores_per_polling_unit=total_party_scores_per_polling_unit)
# @app.route('/party_scores_per_polling_unit_by_lga/<string:lga_name>', methods=['GET'])
# def party_scores_per_polling_unit_by_lga(lga_name):
#     cursor = db.cursor(dictionary=True)

#     # Fetch total party scores for each party in the specified LGA
#     cursor.execute('''
#         SELECT party_abbreviation, SUM(party_score) AS total_score
#         FROM announced_pu_results apr
#         JOIN polling_unit pu ON apr.polling_unit_uniqueid = pu.uniqueid
#         JOIN lga ON pu.lga_id = lga.lga_id
#         WHERE lga.lga_name = %s
#         GROUP BY party_abbreviation
#     ''', (lga_name,))
    
#     result_rows = cursor.fetchall()

#     # Dictionary to store total party scores for the specified LGA
#     total_party_scores_per_lga = {row['party_abbreviation']: row['total_score'] for row in result_rows}


#     cursor.close()
#     return render_template('party_scores_per_polling_unit_by_lga.html', lga_name=lga_name, total_party_scores_per_polling_unit=total_party_scores_per_lga)

@app.route('/party_scores_per_polling_unit_by_lga/<string:lga_name>', methods=['GET'])
def party_scores_per_polling_unit_by_lga(lga_name):
    cursor = db.cursor(dictionary=True)

    # Fetch the data to calculate total party scores per polling_unit_uniqueid for each lga_name
    cursor.execute('''
        SELECT lga.lga_name, apr.polling_unit_uniqueid, apr.party_abbreviation, SUM(apr.party_score) AS total_score
        FROM announced_pu_results apr
        JOIN polling_unit pu ON apr.polling_unit_uniqueid = pu.uniqueid
        JOIN lga ON pu.lga_id = lga.lga_id
        GROUP BY lga.lga_name, apr.polling_unit_uniqueid, apr.party_abbreviation
    ''')
    result_rows = cursor.fetchall()

    # Dictionary to store total party scores per polling_unit_uniqueid for each lga_name
    total_party_scores_per_polling_unit = {}

    for row in result_rows:
        lga_name = row['lga_name']
        polling_unit_uniqueid = row['polling_unit_uniqueid']
        party_abbreviation = row['party_abbreviation']
        total_score = row['total_score']

        if lga_name not in total_party_scores_per_polling_unit:
            total_party_scores_per_polling_unit[lga_name] = {}

        if polling_unit_uniqueid not in total_party_scores_per_polling_unit[lga_name]:
            total_party_scores_per_polling_unit[lga_name][polling_unit_uniqueid] = {}

        total_party_scores_per_polling_unit[lga_name][polling_unit_uniqueid][party_abbreviation] = total_score

    cursor.close()
    return render_template('party_scores_per_polling_unit.html', total_party_scores_per_polling_unit=total_party_scores_per_polling_unit,selected_lga = lga_name)

@app.route('/polling_unit_form')
def polling_unit_form():
    return render_template('polling_unit_form.html')

@app.route('/submit_results', methods=['POST'])
def submit_results():
    # Get form data
    polling_unit_uniqueid = request.form['polling_unit_uniqueid']
    party_abbreviation = request.form['party_abbreviation']
    party_score = request.form['party_score']

    # Render a template to display the form data
    return render_template('confirmation.html')

# def submit_results():
#     # Get form data
#     polling_unit_uniqueid = request.form['polling_unit_uniqueid']
#     party_abbreviation = request.form['party_abbreviation']
#     party_score = request.form['party_score']

#     # Store the results in the database
#     cursor = db.cursor()
#     cursor.execute('INSERT INTO announced_pu_results (polling_unit_uniqueid, party_abbreviation, party_score,date_entered,entered_by_useR) VALUES (%s, %s, %s,%s)',
#                    (polling_unit_uniqueid, party_abbreviation, party_score,'2023-10-18','some user'))
#     db.commit()
#     cursor.close()


#     # Render a template with a confirmation message
#     return 'Thank you'




if __name__ == '__main__':
    app.run(debug=True)

