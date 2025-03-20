from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

projects = [
    {
        'title': 'CO-PO',
        'description': 'CO-PO Stands for Course Outcome And Project Outcome. We have made this app to Generate and Calculate the excel sheet for particula subject.',
        'image': 'images/Project2.jpg',
        'link': 'https://github.com/CodeBrij/CO-PO-Project'
    },
    {
        'title': 'BLE Remote',
        'description': 'Remote for Mobile and Laptop(PPT) navigation.',
        'image': 'images/Project1.png',
        'link': 'https://example.com/project2'
    },
    {
        'title': 'Park-Ease',
        'description': 'A Smart Parking App to find parking spots and book the slots smartly.',
        'image': 'images/Project3.png',
        'link': 'https://example.com/project3'
    },
    {
        'title': 'Fitness-Campus Health and Wellness Platform',
        'description': 'A platform to monitor mental and physical health, integrated with Gemini AI for fitness plans.',
        'image': 'images/Project5.png',
        'link': 'https://github.com/BKCODE2003/Campus_Health'
    },
    {
        'title': 'Fitness Plan Generator',
        'description': 'AI-driven fitness plan generator tailored to specific goals and needs.',
        'image': 'images/Project5.png',
        'link': 'https://fitnessplangenerator.streamlit.app/'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', projects=projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Basic email format check. More robust validation is recommended.
        if "@" not in email or "." not in email:
            return render_template("contact.html", error="Invalid Email")

        return redirect(url_for('success', name=name, email=email, subject=subject, message=message))
    return render_template('contact.html')

@app.route('/success')
def success():
    name = request.args.get('name')
    email = request.args.get('email')
    subject = request.args.get('subject')
    message = request.args.get('message')
    return render_template('success.html', name=name, email=email, subject=subject, message=message)

if __name__ == '__main__':
    app.run(debug=True)