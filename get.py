from flask import Flask, request, jsonify

app= Flask(__name__)
student=[]

app.route('/student',methods=['POST'])
def create_student():
    data= request.get_json()
    if not all(key in data for key in ('name','age','phone_number','bio')):
        return jsonify({'message':'Missing required fields'}), 400
    student={
        'name':data['name'],
        'age':data['age'],
        'phone_number':data['phone_number'],
        'bio':data['bio']
    }

    student.append(student)

    return.jsonify({'message':'Student created Sucessfully'}),201

app.route('/student',methods=['GET'])

def get_students():
    name_filter=request.args.get('name')
    age_range_filter=request.args.get('age')
    phone_email_filter=request.args.get('phone_email')

    filtered_students=students
    if name_filter:
        filtered_students=[s for s in filtered_students if name_filter.lower() in s['name'].lower()]

    if age_range_filter:
        min_age,max_age= age_range_filter.split(',')
        filtered_students=[s for s in filtered_students ifs['age']>= int(min_age) and s['age'] <= int(max_age)]

    if phone_email_filter:
        filtered_students=[s for s in filtered_students if phone_email_filter.lower() in s['phone_number'].lower() or phone_email.lower() in s['email'].lower()]

    return jsonify({'students':filtered_students}),200

if __name__=='__main__':
    app.run(debug=True)














    
