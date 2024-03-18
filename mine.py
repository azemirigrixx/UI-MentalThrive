from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, ValidationError
from flask_bcrypt import Bcrypt
import email_validator
from datetime import datetime
import random
from flask_login import current_user, login_required



app = Flask(__name__, static_url_path='/static')
app.secret_key = "hehess"


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = 'mental_thrive'
mysql = MySQL(app)
bcrypt = Bcrypt(app)


#Our Home page
@app.route('/')
def Mhome():
    return render_template('start_page.html')





#                           "STATION OF COUNSELOR BUTTON"

class CounselorRegistrationForm(FlaskForm):
    Cemail = StringField("Enter your email", validators=[DataRequired(), Email()])
    Cpassword = PasswordField("Enter your password", validators=[DataRequired()])
    Signup = SubmitField("Signup now")
    
class CounselorLoginForm(FlaskForm):
    Cemail = StringField("Enter your email", validators=[DataRequired(), Email()])
    Cpassword = PasswordField("Enter your password", validators=[DataRequired()])
    Login = SubmitField("Login now")
    


# When the user clicks the sign up, it will directly go to counsel registration page
# Rendering the counselor registration page
# Counselor registration

@app.route('/counsel_register', methods=['GET', 'POST'])
def goto_counselor_register():
        form = CounselorRegistrationForm()
        if form.validate_on_submit():
            Cemail = form.Cemail.data
            Cpassword = form.Cpassword.data
            
            hashed_password = bcrypt.generate_password_hash(Cpassword.encode('utf-8').decode('utf-8'))
        
        #store data in our database
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM mental_thrive.counselor_portal WHERE Cemail = %s", (Cemail, ))
            counselor_check = cursor.fetchone()
            
            if counselor_check:
                flash("This email is already taken.")
                return redirect(url_for('goto_counselor_register'))
            else:
                cursor.execute(" INSERT INTO mental_thrive.counselor_portal (Cemail, Cpassword) VALUES (%s, %s)", (Cemail, hashed_password))
                mysql.connection.commit()
                cursor.close()
                return redirect(url_for('goto_counselor_login'))
        
        return render_template('counsel_register.html', form=form)


# When the user clicks the COUNSELOR button, it will directly go to counsel login page.
# Rendering the counselor login page
# Counselor login

@app.route('/counsel_login', methods=['GET', 'POST'])
def goto_counselor_login():
    form = CounselorLoginForm()
    if form.validate_on_submit():
        Cemail = form.Cemail.data
        Cpassword = form.Cpassword.data
        
        # Retrieve the hashed password from the database
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT Cpassword FROM mental_thrive.counselor_portal WHERE Cemail=%s", (Cemail,))
        counselor_result = cursor.fetchone()
        cursor.close()
        
        if counselor_result and bcrypt.check_password_hash(counselor_result[0], Cpassword.encode('utf-8').decode('utf-8')):
            session['counselor_id'] = counselor_result[0]
            return redirect(url_for('goto_counselor_landingpage'))
        else:
            flash("Invalid Credentials! Please try again.")
            return redirect(url_for('goto_counselor_login'))

    return render_template('counsel_login.html', form=form)

# It will go to counselor landing page
@app.route('/counselor_landingpage')
def goto_counselor_landingpage():
    return render_template('counselor_landingpage.html')



# When the user clicks the home button, it will directly go to home page.
@app.route('/start_page')
def all_buttons_backhome():
    return render_template('start_page.html')

# It will go to counselor dashboard
@app.route('/counselor_dash')
def goto_counselor_dash():
    
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT form_id, fcomment, fday, fmonth, fyear, ftime, dep_score, anx_score, stress_score, dep_result, anx_result, stress_result FROM mental_thrive.student_form")
    student_form = cursor.fetchall()
    
    cursor.execute("SELECT Sfirst_name FROM student_portal")
    get_firstname = [row[0] for row in cursor.fetchall()]
    cursor.close()
    return render_template('counselor_dash.html', student_data=student_form, studentname_data=get_firstname)

# It will go to counselor charts
@app.route('/counselor_charts')
def goto_counselor_charts():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT fresult FROM mental_thrive.student_form")
    data = cursor.fetchall()
    cursor.close()
    
    categorized_data = categorize_data(data)
    
    return render_template('counselor_charts.html', data=categorized_data)

def categorize_data(data):
    low_count = medium_count = high_count = 0

    for result_point, in data:
        if result_point <= 21:
            low_count += 1
        elif result_point <= 42:
            medium_count += 1
        else:
            high_count += 1

    categorized_data = [
        {'category': 'Low', 'count': low_count},
        {'category': 'Medium', 'count': medium_count},
        {'category': 'High', 'count': high_count}
    ]


    return categorized_data





#                        "END STATION OF COUNSELOR BUTTON"



#                          "STATION OF STUDENT BUTTON"

#Create class for student login and register
class StudentRegistrationForm(FlaskForm):
    Semail = StringField("Enter your email", validators=[DataRequired(), Email()])
    Spassword = PasswordField("Enter your password")
    Sfirst_name = StringField(" ")
    Slast_name = StringField(" ")
    Sid_number = StringField(" ")
    Scourse = StringField(" ")
    Signup = SubmitField("Signup now")
    
class StudentLoginForm(FlaskForm):
    Semail = StringField("Enter your email", validators=[DataRequired(), Email()])
    Spassword = PasswordField("Enter your password")
    Login = SubmitField("Login now")
    


 
   
#same goes with COUNSELOR button
@app.route('/student_register', methods=['GET', 'POST'])
@login_required
def goto_student_register():
    form = StudentRegistrationForm()
    if form.validate_on_submit():
        Sfirst_name = form.Sfirst_name.data
        Slast_name = form.Slast_name.data
        Sid_number = form.Sid_number.data
        Scourse = form.Scourse.data
        Semail = form.Semail.data
        Spassword = form.Spassword.data
        
        hashed_password = bcrypt.generate_password_hash(Spassword.encode('utf-8').decode('utf-8'))
        
        cursor = mysql.connection.cursor()
        cursor.execute(" SELECT * FROM mental_thrive.student_portal WHERE Semail = %s", (Semail, ))
        student_check = cursor.fetchone()
        
        if student_check:
            flash("This email is already taken.")
            return redirect(url_for('goto_student_register'))
        
        # Insert the record associated with the logged-in user
        user_id = current_user.id
        cursor.execute("INSERT INTO mental_thrive.student_portal (Semail, Spassword, Sfirst_name, Slast_name, Sid_number, Scourse, student_id) VALUES (%s, %s, %s, %s, %s, %s, %s)", (Semail, hashed_password, Sfirst_name, Slast_name, Sid_number, Scourse, user_id))
        mysql.connection.commit()
        cursor.close()
        
        
        
        return redirect(url_for('goto_student_login'))
 
    return render_template('student_registerr.html', form=form)

#for student login
@app.route('/student_login', methods=['GET', 'POST'])
def goto_student_login():
    form = StudentLoginForm()
    if form.validate_on_submit():
        Semail = form.Semail.data
        Spassword = form.Spassword.data
        
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT Spassword FROM mental_thrive.student_portal WHERE Semail=%s", (Semail, ))
        student_result = cursor.fetchone()
        cursor.close()
        
        if student_result and bcrypt.check_password_hash(student_result[0], Spassword.encode('utf-8').decode('utf-8')):
            session['student_id'] = student_result[0]
            return redirect(url_for('goto_student_landingpage'))
        else:
            flash("Invalid Credentials! Please try again.")
            return redirect(url_for('goto_student_login'))
    
    return render_template('student_login.html', form=form)



# It will go to student landing page
@app.route('/student_landingpage')
def goto_student_landingpage():
    return render_template('student_landingpage.html')




# It will go to student dashboard
@app.route('/student_dash')
def goto_student_dash():
    
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT form_id, fcomment, fday, fmonth, fyear, ftime, dep_score, anx_score, stress_score, dep_result, anx_result, stress_result FROM mental_thrive.student_form ")
    student_form = cursor.fetchall()
    cursor.close()

    return render_template('student_dash.html', student_data=student_form)

@app.route('/student_form', methods=['GET', 'POST'])
def goto_student_form():
    if request.method == 'POST':
        
        fcomment = request.form['fcomment']
        now = datetime.now()
        fday = now.strftime("%d")
        fmonth = now.strftime("%m")
        fyear = now.strftime("%Y")
        ftime = now.strftime("%I:%M %p")
        

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO mental_thrive.student_form (fcomment, fday, fmonth, fyear, ftime) VALUES (%s, %s, %s, %s, %s)", (fcomment, fday, fmonth, fyear, ftime))
        mysql.connection.commit()
        cursor.close()    
    

            
    return render_template('student_form.html')
    
        

@app.route('/success_student', methods =['GET', 'POST'])
def goto_success_student():
    fcomment = request.form['fcomment']
    now = datetime.now()
    fday = now.strftime("%d")
    fmonth = now.strftime("%m")
    fyear = now.strftime("%Y")
    ftime = now.strftime("%I:%M %p")      
    
    Q1 = request.form['Answer1']
    Q2 = request.form['Answer2']
    Q3 = request.form['Answer3']
    Q4 = request.form['Answer4']
    Q5 = request.form['Answer5']
    Q6 = request.form['Answer6']
    Q7 = request.form['Answer7']
    Q8 = request.form['Answer8']
    Q9 = request.form['Answer9']
    Q10 = request.form['Answer10']
    Q11 = request.form['Answer11']
    Q12 = request.form['Answer12']
    Q13 = request.form['Answer13']
    Q14 = request.form['Answer14']
    Q15 = request.form['Answer15']
    Q16 = request.form['Answer16']
    Q17 = request.form['Answer17']
    Q18 = request.form['Answer18']
    Q19 = request.form['Answer19']
    Q20 = request.form['Answer20']
    Q21 = request.form['Answer21']
    
    Score = int(Q1)+int(Q2)+int(Q3)+int(Q4)+int(Q5)+int(Q6)+int(Q7)+int(Q8)+int(Q9)+int(Q10) + \
        int(Q11)+int(Q12)+int(Q13)+int(Q14)+int(Q15) + \
        int(Q16)+int(Q17)+int(Q18)+int(Q19)+int(Q20)+int(Q21)
        
    #Deppression
    Dep = (int(Q3)+int(Q5)+int(Q10)+int(Q13)+int(Q16)+int(Q17)+int(Q21))*2
    #Anxiety
    Anx = (int(Q2)+int(Q4)+int(Q7)+int(Q9)+int(Q15)+int(Q19)+int(Q20))*2
    #Stress
    Stres = (int(Q1)+int(Q6)+int(Q8)+int(Q11)+int(Q12)+int(Q14)+int(Q18))*2
    
    
    if (Dep <= 9):
        Dep_say = "Normal"
        Dep_tip = "It's wonderful to see you embracing life! Keep moving forward, and remember that every step counts."
    elif (Dep <= 13):
        Dep_say = "Mild"
        Dep_tip = "It's wonderful to see you embracing life! Keep moving forward, and remember that every step counts."
    elif (Dep <= 20):
        Dep_say = "Moderate"
        Dep_tip = "You're navigating through tough times, and that takes strength. Share your feelings; we're here to listen and support you."
    elif (Dep <= 27):
        Dep_say = "Severe"
        Dep_tip = "Acknowledging the depth of your feelings is the first step toward healing. Reach out to professionals who can guide you through this journey."
    else :
        Dep_say = "Extremely Severe"
        Dep_tip = "Your emotions are valid, and we understand the intensity of what you're going through. Please come to our office; we're here to help."
    
    if (Anx <= 7):
        Anx_say = "Normal"
        Anx_tip = "Life is full of uncertainties, but your ability to stay present is commendable. Keep engaging with the present moment."
    elif (Anx <= 9):
        Anx_say = "Mild"
        Anx_tip = "Life is full of uncertainties, but your ability to stay present is commendable. Keep engaging with the present moment."
    elif (Anx <= 14):
        Anx_say = "Moderate"
        Anx_tip = "Life is full of uncertainties, but your ability to stay present is commendable. Keep engaging with the present moment."
    elif (Anx <= 19):
        Anx_say = "Severe"
        Anx_tip = "Life is full of uncertainties, but your ability to stay present is commendable. Keep engaging with the present moment."
    else :
        Anx_say = "Extremely Severe"
        Anx_tip = "Life is full of uncertainties, but your ability to stay present is commendable. Keep engaging with the present moment."
    
    if (Stres <= 14):
        Stres_say = "Normal"
        Stres_tip ="Balancing life can be tricky, but your efforts are noticeable. Take breaks, prioritize self-care, and remember, you're doing well."
    elif (Stres <= 18):
        Stres_say = "Mild"
        Stres_tip ="Identifying stressors is a crucial step. Delegate when possible, and feel free to share your load. We're here for you."
    elif (Stres <= 25):
        Stres_say = "Moderate"
        Stres_tip ="The stress you're feeling is real, and you don't have to carry it alone. Let's create a personalized stress management plan to help you navigate through this."
    elif (Stres <= 33):
        Stres_say = "Severe"
        Stres_tip ="Your stress levels are significant, and it's important to address them. Seek professional guidance to develop effective coping mechanisms."
    else :
        Stres_say = "Extremely Severe"
        Stres_tip ="Your feelings are valid, and we recognize the severity of your stress. Our office is a safe space for you to express yourself. Please come in; we're here to support you."
    
    cursor = mysql.connection.cursor()  
    cursor.execute("INSERT INTO mental_thrive.student_form (fcomment, fday, fmonth, fyear, ftime, dep_score, anx_score, stress_score, dep_result, anx_result, stress_result) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (fcomment, fday, fmonth, fyear, ftime, Dep, Anx, Stres, Dep_say, Anx_say, Stres_say))
    mysql.connection.commit()
    cursor.close()
    
    titletips = ["Set Clear Goals:","Break Tasks into Manageable Steps:","Celebrate Progress:","Surround Yourself with Positivity:","Practice Self-Care:"]
    rantips = random.choice(titletips)
    indxtips = titletips.index(rantips)
    tips = ["Define specific, measurable, achievable, relevant, and time-bound (SMART) goals. Having a clear sense of purpose and direction can provide motivation and focus.",
        "Large tasks can be overwhelming. Break them down into smaller, more manageable steps. Achieving these smaller goals provides a sense of accomplishment and motivates you to tackle the next one.",
        "Acknowledge and celebrate your achievements, no matter how small. Recognizing your progress reinforces a positive mindset and encourages continued effort.",
        "Surround yourself with positive influences, whether it's supportive friends and family, inspirational quotes, or uplifting music. Positive environments can contribute to a more optimistic outlook.",
        "Take care of your physical and mental well-being. Ensure you get enough rest, eat nutritious meals, exercise regularly, and make time for activities you enjoy. A healthy body and mind contribute to increased motivation and resilience."]
    
    resulttitle = rantips
    result = tips[indxtips]
    
    return render_template('success_student.html', result=result,Dep=Dep,Anx=Anx,Stres=Stres,
                           Dep_say=Dep_say,Anx_say=Anx_say,Stres_say=Stres_say,resulttitle=resulttitle, Dep_tip=Dep_tip, Anx_tip=Anx_tip,
                           Stres_tip=Stres_tip)


# I will go to student charts
@app.route('/student_charts')
def goto_student_charts():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT fresult FROM mental_thrive.student_form")
    data = cursor.fetchall()
    cursor.close()
    
    categorized_data = categorize_data(data)
    
    return render_template('counselor_charts.html', data=categorized_data)

def categorize_data(data):
    low_count = medium_count = high_count = 0

    for result_point, in data:
        if result_point <= 21:
            low_count += 1
        elif result_point <= 42:
            medium_count += 1
        else:
            high_count += 1

    categorized_data = [
        {'category': 'Low', 'count': low_count},
        {'category': 'Medium', 'count': medium_count},
        {'category': 'High', 'count': high_count}
    ]


    return categorized_data




#                         "END STATION OF STUDENT BUTTON"



#                          "STATION OF ADMINISTRATION BUTTON"

class AdminRegistrationForm(FlaskForm):
    Aemail = StringField("Enter your email", validators=[DataRequired(), Email()])
    Apassword = PasswordField("Enter your password", validators=[DataRequired()])
    Login = SubmitField("Login now")
    
    
@app.route('/administration_login', methods=['GET', 'POST'])
def goto_administration_login():
    form = AdminRegistrationForm()
    if form.validate_on_submit():
        Aemail = form.Aemail.data
        Apassword = form.Apassword.data
                
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT Apassword FROM mental_thrive.admin_portal WHERE Aemail = %s", (Aemail, ))
        admin_check = cursor.fetchone()
        cursor.close()
        
        
        if admin_check:
            session['id'] = admin_check[0]
            return redirect(url_for('goto_administration_dash'))
        else:
            flash ("Invalid Credentials! Please try again.")
            return redirect(url_for('goto_administration_login'))
        
        
    return render_template('administration_login.html', form=form)

@app.route('/admin_counselors')
def goto_admin_counselors():
    
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT counselor_id, Cemail, Cpassword FROM mental_thrive.counselor_portal")
    counselor_account = cursor.fetchall()
    
    return render_template('admin_counselors.html', counselor_data=counselor_account)

@app.route('/admin_students')
def goto_admin_students():
    
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT counselor_id, Cemail, Cpassword FROM mental_thrive.counselor_portal")
    student_account = cursor.fetchall()
    
    return render_template('admin_students.html', student_dataz=student_account)


@app.route('/admin_dash')
def goto_administration_dash():
    
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT form_id, fcomment, fday, fmonth, fyear, ftime, dep_score, anx_score, stress_score, dep_result, anx_result, stress_result FROM mental_thrive.student_form ")
    student_form = cursor.fetchall()
    cursor.close()
    
    return render_template('admin_dash.html', student_data=student_form)


@app.route('/admin_charts')
def goto_admin_charts():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT fresult FROM mental_thrive.student_form")
    data = cursor.fetchall()
    cursor.close()
    
    categorized_data = categorize_data(data)
    
    return render_template('admin_charts.html', data=categorized_data)

def categorize_data(data):
    low_count = medium_count = high_count = 0

    for result_point, in data:
        if result_point <= 21:
            low_count += 1
        elif result_point <= 42:
            medium_count += 1
        else:
            high_count += 1

    categorized_data = [
        {'category': 'Low', 'count': low_count},
        {'category': 'Medium', 'count': medium_count},
        {'category': 'High', 'count': high_count}
    ]


    return categorized_data

#                         "END STATION OF ADMINISTRATION BUTTON"







if __name__ == '__main__':
    app.run(debug=True, port=8080)

