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

if __name__=='__main__':
    app.run(debug=True)
