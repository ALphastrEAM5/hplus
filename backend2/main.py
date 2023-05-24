import re
import uuid
import json
import requests
import smtplib
from functools import wraps
from chat import get_response
from views import process_price
from email.message import EmailMessage
import os
from flask import Flask,g,abort,redirect,render_template,request,flash, session, url_for,jsonify
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin,login_required,logout_user,login_user,login_manager,LoginManager,current_user
from flask_mail import Mail
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash



# mydatabase connection
local_server=True
app=Flask(__name__)
app.secret_key="dbms-project"

UPLOAD_FOLDER = 'C:/Users/Abir Biswas/Desktop/DBMS/backend/static' 

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024



with open('config.json','r') as c:
     params=json.load(c)["params"]

app.config.update(
     MAIL_SERVER='smtp.gmail.com',
     MAIL_PORT='465',
     MAIL_USE_SSL=True,
     MAIL_USERNAME=params['gmail-user'],
     MAIL_PASSWORD=params['gmail-password']     
)
mail = Mail(app)


# this is for getting unique user access
login_manager=LoginManager(app)
login_manager.login_view='login'

# app.config['SQLALCHEMY_DATABASE_URI']='mysql://username:password@localhost/databasename'

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/covid'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@login_manager.user_loader
def load_user(user_id):
     return db.session.get(user, int(user_id))






class Test(db.Model):
     id=db.Column(db.Integer,primary_key=True)
     name=db.Column(db.String(50))


class user(UserMixin,db.Model):
     id= db.Column(db.Integer,primary_key=True)
     srfid=db.Column(db.String(20),unique=True)
     email=db.Column(db.String(100),unique=True)
     dob=db.Column(db.String(1000))


class hospitaluser(UserMixin,db.Model):
     # __tablename__ = 'hospitalusers'
     id= db.Column(db.Integer,primary_key=True)
     hcode=db.Column(db.String(20),unique=True)
     email=db.Column(db.String(100),unique=True)
     password=db.Column(db.String(1000))

     # def is_hospital(self):
     #    return self.role == 'hospital'



class hospitaldata(db.Model):
     id= db.Column(db.Integer,primary_key=True)
     hcode=db.Column(db.String(200),unique=True)
     hname=db.Column(db.String(200))
     normalbed=db.Column(db.Integer)
     hicubed=db.Column(db.Integer)
     icubed=db.Column(db.Integer)
     vbed=db.Column(db.Integer)


class bookingpatient(db.Model):
     id= db.Column(db.Integer,primary_key=True)
     srfid=db.Column(db.String(50),unique=True)
     bedtype=db.Column(db.String(50))
     hcode=db.Column(db.String(20))
     spo2=db.Column(db.Integer)
     pname=db.Column(db.String(50))
     pphone=db.Column(db.String(12))
     paddress=db.Column(db.String(50))
     


class doctors(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(100))
    email= db.Column(db.String(100))
    specialization= db.Column(db.String(100))
    degree= db.Column(db.String(100))
    city= db.Column(db.String(100))
    address= db.Column(db.String(100))


class medical_data(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    hcode=db.Column(db.String(30))
    postal_code=db.Column(db.String(10))
    tests=db.Column(db.String(100))
    schedules=db.Column(db.DateTime)
    

class visiting(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    hcode = db.Column(db.String(30))
    name = db.Column(db.String(100))
    location = db.Column(db.String(100))
    appointment = db.Column(db.DateTime)


class pkgs(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    hcode = db.Column(db.String(30))
    hname = db.Column(db.String(100))
    packages = db.Column(db.String(100))

# def hospital_login_required(func):
#     @wraps(func)
#     def decorated_view(*args, **kwargs):
#         if not current_user.is_hospital():
#             # Redirect the user to the login page or show an error message
#             abort(401) # or use redirect('/login') to redirect to login page
#         return func(*args, **kwargs)
#     return decorated_view

class health(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    symptom = db.Column(db.String(100))
    doctor = db.Column(db.String(100))
    tos= db.Column(db.String(100))
    started= db.Column(db.String(50))
    ran= db.Column(db.Integer)
    additional= db.Column(db.String(100))
    threats= db.Column(db.String(100))
    pattern= db.Column(db.String(100))
    covid19= db.Column(db.String(50))
    dur= db.Column(db.String(50))
    rep= db.Column(db.String(100))
    

@app.before_request
def before_request():
    g.hospital_user = None
    if 'hospital_user_id' in session:
        g.hospital_user = hospitaluser.query.get(session['hospital_user_id'])


def hospital_login_required(f):
    @wraps(f)
    def decorated_view(*args, **kwargs):
        if g.hospital_user is None:
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Redirecting to hospital login page")
            return redirect(url_for('hospitallogin', next=request.url))
        return f(*args, **kwargs)
    return decorated_view

@app.route("/")
def home():
    return render_template("index.html")



# engine = create_engine('mysql://root:@localhost/covid')

@app.route('/signup',methods=['POST','GET'])
def signup():
     if request.method=="POST":
          srfid=request.form.get('srf')
          email=request.form.get('email')
          dob=request.form.get('dob')
          # print(srfid,email,dob)
          encpassword=generate_password_hash(dob)
          user1=user.query.filter_by(srfid=srfid).first()
          emailUser=user.query.filter_by(email=email).first()
          if user1 or emailUser:
               flash("Email or srfid is already taken", "warning")
               return render_template("usersignup.html")
          # conn=engine.connect()
          # values = [(srfid, email, encpassword)]
          new_user = user(srfid=srfid, email=email, dob=encpassword)
          db.session.add(new_user)
          db.session.commit()
          # new_user = db.engine.execute(f"INSERT INTO `user` (`srfid`, `email`, `dob`) VALUES ('{srfid}', '{email}', '{encpassword}') ")
          
          # conn.close() 
             
          flash("SignUp Success Please Login Success", "success")
          return render_template("userlogin.html")

     return render_template("/usersignup.html")



@app.route('/login',methods=['POST','GET'])
def login():
     if request.method=="POST":
          srfid=request.form.get('srf')
          dob=request.form.get('dob')
          user1=user.query.filter_by(srfid=srfid).first()

          if user1 and check_password_hash(user1.dob,dob):
               login_user(user1)
               flash("Login Success","info")
               return render_template("index.html")
          
          else:
               flash("Invalid Credentials", "danger")
               return render_template("userlogin.html")
          
          

     return render_template("/userlogin.html")







@app.route('/hospitallogin',methods=['POST','GET'])
def hospitallogin():
     if request.method=="POST":
          email=request.form.get('email')
          password=request.form.get('password')
          user=hospitaluser.query.filter_by(email=email).first()

          if user and check_password_hash(user.password,password):
               session['hospital_user_id'] = user.id
               # login_user(user)
               flash("Login Success","info")
               return redirect("/addhospitalinfo")
               # return render_template("index.html")
          
          else:
               flash("Invalid Credentials", "danger")
               return render_template("hospitallogin.html")
          
          

     return render_template("/hospitallogin.html")



@app.route('/admin',methods=['POST','GET'])
def admin():
     if request.method=="POST":
          username=request.form.get('username')
          password=request.form.get('password')
          if(username==params['user'] and password==params['password']):
               session['user']=username
               flash("Login Success", "info")
               return render_template("addHosUser.html")

          else:
               flash("Invalid Credentials", "danger")
          
     return render_template("admin.html")

@app.route('/logout')
@login_required
def logout():
     logout_user()
     flash("Logout Successful", "warning")
     return redirect(url_for('login')) 



@app.route('/addHospitalUser',methods=['POST','GET'])
def hospitalUser():
     if('user' in session and session['user']==params['user']):
          if request.method=="POST":
               hcode=request.form.get('hcode')
               email=request.form.get('email')
               password=request.form.get('password')
               encpassword=generate_password_hash(password)
               hcode=hcode.upper()
               emailUser=hospitaluser.query.filter_by(email=email).first()
               if emailUser:
                    flash("Email or srfid is already taken", "warning")
              
              
               hospital_user = hospitaluser(hcode=hcode, email=email, password=encpassword)
               db.session.add(hospital_user)
               db.session.commit()
               # db.engine.execute(f"INSERT INTO `hospitaluser` (`hcode`, `email`, `password`) VALUES ('{hcode}', '{email}', '{encpassword}') ")
               flash("Data Inserted", "warning")



               EMAIL_ADDRESS = params['gmail-user']
               EMAIL_PASSWORD = params['gmail-password']
               print('++++++++++++++++++++++++++++++',EMAIL_ADDRESS, EMAIL_PASSWORD)

               msg = EmailMessage()
               msg['Subject'] = 'Login Credentials'
               msg['From'] = 'Covid Care Centre <{}>'.format(EMAIL_ADDRESS)
               msg['To'] = [email]
               msg.set_content(f'Welcome thanks for choosing us\nYour Login Credentials are:\nEmail Address: {email}\nPassword: {password}\n\n\n\nHospital Code {hcode}\n\tDo not share your password\n\n\nThank You...')

               with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                    smtp.send_message(msg)
               # mail.send_message('COVID CARE CENTER',sender=params['gmail-user'], recipients=[email],body=f"Welcome thanks for choosing us\nYour Login Credentials are:\nEmail Address: {email}\nPassword: {password}\n\n\n\nDo not share your password\n\n\nThank You...")
               flash("Data Sent and Inserted Successfully","warning")
               return render_template("addHosUser.html")
          
     else:
          flash("Login and try again","warning")
          return redirect('/admin')
     

#testing whether db is connected or not
@app.route("/test")
def test():
    try:
         a=Test.query.all()
         print(a)
         return 'MY DATABASE IS CONNECTED'
    except Exception as e:
         print(e)
         return f'MY DATABASE IS NOT CONNECTED {e}'
    
@app.route('/logoutadmin')
def logoutadmin():
     session.pop('user')
     flash("You are logged-out admin", "primary")

     return redirect('/admin') 



# @app.before_request
# def before_request():
#     g.hospital_user = None
#     if 'hospital_user_id' in session:
#         g.hospital_user = hospitaluser.query.get(session['hospital_user_id'])


# @app.route('/hospitallogin', methods=['GET', 'POST'])
# def hospital_login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         user = hospitaluser.query.filter_by(email=email).first()
#         if user and check_password_hash(user.password, password):
#             session['hospital_user_id'] = user.id
#             return redirect(url_for('dashboard'))
#         else:
#             flash('Invalid email or password.', 'error')
#     return render_template('hospitallogin.html')



@app.route('/addhospitalinfo',methods=['POST','GET'])
@hospital_login_required
def addhospitalinfo():

     print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++addhospitalinfo function called")
     huser=db.session.query(hospitaluser).all()
     
     email=g.hospital_user.email
     posts=hospitaluser.query.filter_by(email=email).first()
     code=posts.hcode
     postsdata=hospitaldata.query.filter_by(hcode=code).first()


     if request.method=="POST":

          hcode=request.form.get('hcode')
          hname=request.form.get('hname')
          nbed=request.form.get('normalbed')
          hbed=request.form.get('hicubeds')
          ibed=request.form.get('icubeds')
          vbed=request.form.get('ventbeds')
          hcode=hcode.upper()
          huser=hospitaluser.query.filter_by(hcode=hcode).first()
          hduser=hospitaldata.query.filter_by(hcode=hcode).first()
          if hduser:
               flash("Data is already Present, you can Update it", "primary")
               return render_template("hospitaldata.html",postsdata=postsdata)
          if huser:
               
               new_hospitalinfo = hospitaldata(hcode=hcode, hname=hname, normalbed=nbed, hicubed=hbed, icubed=ibed, vbed=vbed)
               db.session.add(new_hospitalinfo)
               db.session.commit()
               # db.session.execute(f"INSERT INTO `hospitaldata` (`hcode`,`hname`,`normalbed`,`hicubed`,`icubed`,`vbed`) VALUES ('{hcode}','{hname}','{nbed}','{hbed}','{ibed}','{vbed}')")
               

               # db.engine.execute(f"INSERT INTO `hospitaldata` (`hcode`,`hname`,`normalbed`,`hicubed`,`icubed`,`vbed`) VALUES ('{hcode}','{hname}','{nbed}','{hbed}','{ibed}','{vbed}')")
               
               flash("Data Is Added", "primary")

          else:
               flash("Hospital Code does not Exist", "warning")

          
     return render_template("hospitaldata.html",postsdata=postsdata)


@app.route('/hedit/<string:id>',methods=['POST','GET'])
# @hospital_login_required
def hedit(id):
     posts=hospitaldata.query.filter_by(id=id).first()
     if request.method=="POST":

          hcode=request.form.get('hcode')
          hname=request.form.get('hname')
          nbed=request.form.get('normalbed')
          hbed=request.form.get('hicubeds')
          ibed=request.form.get('icubeds')
          vbed=request.form.get('ventbeds')
          hcode=hcode.upper()
          
          # Update the hospitaldata record
          posts.hcode = hcode
          posts.hname = hname
          posts.normalbed = nbed
          posts.hicubed = hbed
          posts.icubed = ibed
          posts.vbed = vbed
          
          db.session.commit()
          # db.engine.execute(f"UPDATE `hospitaldata` SET `hcode`='{hcode}',`hname`='{hname}',`normalbed`='{nbed}',`hicubed`='{hbed}',`icubed`='{ibed}',`vbed`='{vbed}' WHERE `hospitaldata`.`id`={id}")
          flash("Slot Updated","info")
          return redirect("/addhospitalinfo")

     posts=hospitaldata.query.filter_by(id=id).first()
     return render_template("hedit.html",posts=posts)


@app.route('/hdelete/<string:id>',methods=['POST','GET'])
# @hospital_login_required
def hdelete(id):
     post = hospitaldata.query.filter_by(id=id).first()
     db.session.delete(post) 
     db.session.commit() 
     # db.engine.execute(f"DELETE FROM `hospitaldata` WHERE `hospitaldata`.`id`={id}")
     flash("Data Deleted","danger")
     return redirect("/addhospitalinfo")


@app.route('/pdetails',methods=['GET'])
@login_required
def pdetails():
     code=current_user.srfid
     print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++',code)
     data= bookingpatient.query.filter_by(srfid=code).first()
     print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++',print(dir(data)))
     return render_template("details.html",data=data)



@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


@app.route("/slotbooking", methods=['POST', 'GET'])
@login_required
def slotbooking():
    posts = hospitaldata.query.all()
    if request.method == 'POST':
        srfid = request.form.get('srfid')
        bedtype = request.form.get('bedtype')
        hcode = request.form.get('hcode')
        spo2 = request.form.get('spo2')
        pname = request.form.get('pname')
        pphone = request.form.get('pphone')
        paddress = request.form.get('paddress')

        # Check if patient with srfid already exists
        existing_patient = bookingpatient.query.filter_by(srfid=srfid).first()
        if existing_patient:
            flash("Patient already has a booking", "warning")
            return redirect(url_for('slotbooking'))

        hospital = next((h for h in posts if h.hcode == hcode), None)
        if not hospital:
            flash("Hospital Code does not Exist", "warning")
        else:
            if bedtype == "NormalBed":
                if hospital.normalbed > 0:
                    hospital.normalbed -= 1
                else:
                    flash("No Normal Bed Available", "danger")
            elif bedtype == "HICUBed":
                if hospital.hicubed > 0:
                    hospital.hicubed -= 1
                else:
                    flash("No HICU Bed Available", "danger")
            elif bedtype == "ICUBed":
                if hospital.icubed > 0:
                    hospital.icubed -= 1
                else:
                    flash("No ICU Bed Available", "danger")
            elif bedtype == "VENTILATORBed":
                if hospital.vbed > 0:
                    hospital.vbed -= 1
                else:
                    flash("No Ventilator Bed Available", "danger")
            else:
                flash("Invalid Bed Type", "danger")
            if not all((srfid, bedtype, hcode, spo2, pname, pphone, paddress)):
                flash("Incomplete Patient Data", "danger")
            else:
                patient = bookingpatient(srfid=srfid, bedtype=bedtype, hcode=hcode, spo2=spo2, pname=pname, pphone=pphone, paddress=paddress)
                db.session.add(patient)
                db.session.commit()
                flash("Slot is Booked kindly Visit Hospital for Further Procedure", "success")
    return render_template("booking.html", posts=posts)




@app.route("/lab_tests", methods=['POST', 'GET'])
@login_required
def lab_tests():
     
     return render_template("/labtests.html")

     
@app.route('/lab_tests/portal')
def pay_portal():
     return render_template("payments.html")
     
     

@app.route('/process_payment', methods=['POST'])
def process_payment():
    # Retrieve payment data from the frontend
    payment_data = request.get_json()

    # Process the payment using Google Pay API
    # ...

    # Return a response to the frontend
    response = {'status': 'success'}
    return jsonify(response)


@app.route('/payment', methods=['POST','GET'])
def payment():
    # Get the payment amount from the form
    amount = request.form.get('amount')
    
    # Build the PhonePe payment request
    data = {
        'merchantId': 'your_merchant_id',
        'orderId': 'your_order_id',
        'amount': amount,
        'currency': 'INR',
        'redirectUrl': 'http://yourwebsite.com/payment-confirmation'
    }
    
    # Send the payment request to PhonePe
    response = requests.post('https://www.phonepe.com/merchant-pay', data=data)
    
    # Render the PhonePe payment form in a template
    return render_template('payments.html', form=response.text)


@app.route('/option', methods=['POST','GET'])
def paymentOptions():
    if request.method == "POST":
        payment_type = request.form.get("payment-option")
        
        if payment_type == 'card':
           
            return render_template("cards.html")

                # return redirect("/charge")
        else:
           
            return render_template("payments.html")
     
    return render_template('payments.html')


@app.route('/process-price', methods=['POST'])
def process_price_route():
    return process_price()


@app.route('/cards', methods=['POST','GET'])
def charge():
    try:
        # Retrieve user inputs from the form
        
        card_number = request.form['card-number']
        card_holder = request.form['card-holder']
        exp_month = request.form['exp-month']
        exp_year = request.form['exp-year']
        cvv = request.form['cvv']

        # Create a Stripe PaymentIntent
        intent = stripe.PaymentIntent.create(
            amount=100,  # Amount in cents
            currency='inr',
            payment_method_types=['card'],
            payment_method_data={
                'card': {
                    'number': card_number,
                    'exp_month': exp_month,
                    'exp_year': exp_year,
                    'cvc': cvv,
                },
                'billing_details': {
                    'name': card_holder,
                },
                'type': 'card'
            }
        )

        # Confirm the PaymentIntent
        intent.confirm()
        
        
        
    
    
        # Payment successful
        # return redirect(url_for('/payment-confirmation'))
        return render_template("payment_confirmation.html")

    except Exception as e:
        # Payment failed
        return render_template("payment_confirmation.html")
        # return jsonify({'error': str(e)})
    
    
@app.route("/ajaxlivesearch", methods=["POST", "GET"])
def ajaxlivesearch():
    if request.method == 'POST':
        search_word = request.form['query']
        if search_word == '':
            user = db.session.query(doctors, pkgs.hname).join(visiting, visiting.name == doctors.name).join(medical_data, visiting.hcode == medical_data.hcode).join(pkgs, pkgs.hcode == medical_data.hcode).order_by(doctors.id).all()
        else:
            user = db.session.query(doctors, pkgs.hname).join(visiting, visiting.name == doctors.name).join(medical_data, visiting.hcode == medical_data.hcode).join(pkgs, pkgs.hcode == medical_data.hcode).filter(
                db.or_(
                    doctors.name.like(f'%{search_word}%'),
                    doctors.email.like(f'%{search_word}%'),
                    doctors.address.like(f'%{search_word}%'),
                    doctors.specialization.like(f'%{search_word}%'),
                    doctors.degree.like(f'%{search_word}%'),
                    doctors.city.like(f'%{search_word}%'),
                    visiting.hcode.like(f'%{search_word}%'),
                    visiting.name.like(f'%{search_word}%'),
                    visiting.location.like(f'%{search_word}%'),
                    medical_data.hcode.like(f'%{search_word}%'),
                    medical_data.postal_code.like(f'%{search_word}%'),
                    medical_data.tests.like(f'%{search_word}%'),
                    pkgs.hname.like(f'%{search_word}%')
                )
            ).order_by(doctors.id.desc()).all()
        numrows = len(user)
        return jsonify({'htmlresponse': render_template('response.html', user=user, numrows=numrows)})



@app.route("/lab_tests/upload-prescription")
def upload_form():
    return render_template("upload.html")


@app.route("/lab_tests/upload-prescription", methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the files part
        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)
        files = request.files.getlist('files[]')
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                unique_filename = str(uuid.uuid4()) + '_' + filename  # Generate a unique filename
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))
        flash('File(s) successfully uploaded')
        return redirect(url_for('uploaded_files'))
    


@app.route('/uploads')
def uploaded_files():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('uploaded_files.html', files=files)

    
    
@app.route("/pdetails/specialties")
def consult():
    return render_template("consult.html")


@app.route('/pdetails/specialties/dermatology')
def dermatology_specialists():
    specialization = request.args.get('specialization')

    # Query the database for doctors with the specified specialization
    specialists = db.session.query(doctors, pkgs, visiting, medical_data).join(visiting, doctors.name == visiting.name).join(pkgs, visiting.hcode == pkgs.hcode).join(medical_data, pkgs.hcode == medical_data.hcode).filter(doctors.specialization == specialization).group_by(pkgs.hname).distinct(pkgs.hname).all()
    
    print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
    for specialist in specialists:
        print(specialist.pkgs.hname)

    return render_template('dermatology.html', specialists=specialists)



@app.route('/pdetails/specialties/pediatrics')
def pediatrics_specialists():
    specialization = request.args.get('specialization')

    # Query the database for doctors with the specified specialization
    specialists = db.session.query(doctors, pkgs, visiting, medical_data).join(visiting, doctors.name == visiting.name).join(pkgs, visiting.hcode == pkgs.hcode).join(medical_data, pkgs.hcode == medical_data.hcode).filter(doctors.specialization == specialization).group_by(pkgs.hname).distinct(pkgs.hname).all()
    
    print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
    for specialist in specialists:
        print(specialist.pkgs.hname)

    return render_template('dermatology.html', specialists=specialists)



@app.route('/pdetails/specialties/recommended-doctors')
def recommendedDoctors_specialists():
    
    specialists = db.session.query(doctors, pkgs, visiting, medical_data).join(visiting, doctors.name == visiting.name).join(pkgs, visiting.hcode == pkgs.hcode).join(medical_data, pkgs.hcode == medical_data.hcode).group_by(pkgs.hname).distinct(pkgs.hname).all()
    
    print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
    for specialist in specialists:
        print(specialist.pkgs.hname)

    return render_template('dermatology.html', specialists=specialists)



@app.route('/pdetails/specialties/get_started')
def get_started():
    return render_template('scroll.html')
    

@app.route('/support')
def support():
    return render_template("support.html")
    

@app.route('/support/feedback', methods=['POST', 'GET'])
def feedback():
    
    if request.method=="POST":
        email=request.form.get('email')
        name=request.form.get('name').split()[0]
        EMAIL_ADDRESS = params['gmail-user']
        EMAIL_PASSWORD = params['gmail-password']
        print('++++++++++++++++++++++++++++++',EMAIL_ADDRESS, EMAIL_PASSWORD)

        msg = EmailMessage()
        msg['Subject'] = 'NEWSLETTER'
        msg['From'] = 'Covid Care Centre <{}>'.format(EMAIL_ADDRESS)
        msg['To'] = [email]
        msg.set_content(f'Hey {name} !\n\tThankyou for subscribing to our newsletter. Send us if you have any query and our team will do their best to get back to you soon.\n We will keep you updated about the offers on medicines and about packages on tests. Stay tuned ;-D\n\nThanks,\nHplusCo. & Services\nBangalore')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        return render_template("feedback.html")
    
    return render_template("/support.html")


@app.route('/symptoms', methods=['POST'])
def handle_symptoms():
    # Retrieve the submitted form data
    global is_self_or_other
    global gender
    global age
    global symptom
    global tos
    if request.form.get('answer0') == 'self' or request.form.get('answer0') == 'other':
        session['is_self_or_other'] = is_self_or_other= request.form.get('answer0')
        session['gender'] = gender= request.form.get('answer1')
        session['age'] = age= request.form.get('answer2')
        session['symptom'] = symptom= request.form.get('answer3')
        print(is_self_or_other, gender, age, symptom)
        return render_template("scroll.html", symptom=symptom)
        # return render_template('symptoms.html', is_self_or_other=is_self_or_other, gender=gender, age=age, symptom=symptom)
        
        print("check")
        print(is_self_or_other, gender, age, symptom)
        
        return render_template('symptoms.html', is_self_or_other=is_self_or_other, gender=gender, age=age, symptom=symptom)
    # Process the data as needed

    tos=request.form.get('answer0')
    start=request.form.get('answer1')
    explain=request.form.get('answer2')
    ran=request.form.get('answer3')
    additional=request.form.get('answer4')
    threats=request.form.get('answer5')
    pattern=request.form.get('answer6')
    cov_19=request.form.get('answer7')
    dur=request.form.get('answer8')
    print(tos)
    
   
    # print(request.form.get('answer0'),request.form.get('answer0'),request.form.get('answer0'))
    # print(symptom)
    # a= request.form.get('answer0')
    # if a == 'dry cough':
    #     print("s", symptom)
    #     if symptom == 'cough':
    #         print("yes")
    #         tos = a
    #         print(tos)
    # Pass the retrieved answers to the template
    # if request.form.get('answer0') == 'dry cough':
    #     print(symptom)
    #     if symptom == 'cough':
    #         print("yes")
    #         tos = request.form.get('answer')
            
            # return render_template('scroll.html', symptom=symptom, tos=tos)
    
    # print(is_self_or_other, gender, age, symptom, tos)
    return render_template('symptoms.html', is_self_or_other=is_self_or_other, gender=gender, age=age, symptom=symptom, tos=tos, start=start, explain=explain, ran=ran, additional=additional, threats=threats, pattern=pattern, cov_19=cov_19, dur=dur)


# @app.route('/symptoms', methods=['POST'])
# def handle_symptoms2():
#     # Retrieve the submitted form data
#     is_self_or_other=""
#     gender=""
#     age=""
#     symptom=""
#     tos=""
#     if request.form.get('answer0') == 'self' or request.form.get('answer0') == 'other':
#         session['is_self_or_other'] = is_self_or_other= request.form.get('answer0')
#         session['gender'] = gender= request.form.get('answer1')
#         session['age'] = age= request.form.get('answer2')
#         session['symptom'] = symptom= request.form.get('answer3')
#         print(is_self_or_other, gender, age, symptom)
#         return render_template('symptoms.html', is_self_or_other=is_self_or_other, gender=gender, age=age, symptom=symptom)


@app.route('/symptoms/report', methods=['GET'])
def symptoms_report():
    is_self_or_other = request.args.get('is_self_or_other')
    gender = request.args.get('gender')
    age = request.args.get('age')
    symptom = request.args.get('symptom')
    tos = request.args.get('tos')
    start = request.args.get('start')
    ran = request.args.get('ran')
    additional = request.args.get('additional')
    threats = request.args.get('threats')
    pattern = request.args.get('pattern')
    cov_19 = request.args.get('cov_19')
    dur = request.args.get('dur')
    
    print(is_self_or_other, gender, age, symptom, tos, start, ran, additional, threats, pattern, cov_19, dur)
    
    s = health.query.join(doctors, health.doctor==doctors.specialization).filter(health.age == age, health.symptom == symptom, health.tos == tos, health.started == start, health.ran == ran, health.additional == additional, health.threats == threats, health.pattern == pattern, health.covid19 == cov_19, health.dur == dur).all()
    
    doc = doctors.query.filter(doctors.specialization == 'ENT').all()
    
    row2= '0'
    for row2 in doc:
        print(row2.name)
    
    s1 = health.query.filter(health.age == age, health.symptom == symptom, health.ran >= ran, health.threats == threats, health.covid19 == cov_19, health.dur == dur).all()
    
    row1= '0'
    for row1 in s1:
        print(row1.pattern)

    
    
    return render_template('reports.html', s=s, row1=row1, row2=row2, gen=gender)


if __name__ == "__main__":
    is_self_or_other=""
    gender=""
    age=""
    symptom=""
    tos=""
    start=""
    explain=""
    ran=""
    additional=""
    print(is_self_or_other, gender, age, symptom, tos)
    app.run(host='0.0.0.0', port=8080, debug=True)