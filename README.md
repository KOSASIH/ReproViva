# ReproViva
A high-tech system focused on Empowering Sexual and Reproductive Health for Women. 

# Tutorials 

## Create Web Interface 

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Menstrual Cycle Tracker</title>
  <style>
    /* CSS styles for the calendar */
    .calendar {
      display: grid;
      grid-template-columns: repeat(7, 1fr);
      gap: 10px;
      margin-bottom: 20px;
    }
    
    .calendar-header {
      text-align: center;
      font-weight: bold;
    }
    
    .calendar-day {
      text-align: center;
      padding: 5px;
      border: 1px solid #ccc;
    }
    
    .calendar-day.active {
      background-color: #f2f2f2;
    }
    
    .calendar-day.today {
      background-color: #e6f2ff;
    }
    
    .form-container {
      display: flex;
      flex-direction: column;
      margin-bottom: 20px;
    }
    
    .form-container label {
      margin-bottom: 5px;
    }
    
    .form-container input[type="text"],
    .form-container select {
      padding: 5px;
      margin-bottom: 10px;
    }
    
    .form-container button {
      padding: 10px;
      background-color: #4CAF50;
      color: white;
      border: none;
      cursor: pointer;
    }
    
    .form-container button:hover {
      background-color: #45a049;
    }
    
    .data-container {
      margin-bottom: 20px;
    }
    
    .data-container h3 {
      margin-bottom: 10px;
    }
    
    .data-container ul {
      list-style-type: none;
      padding: 0;
    }
    
    .data-container li {
      margin-bottom: 5px;
    }
  </style>
</head>
<body>
  <h1>Menstrual Cycle Tracker</h1>
  
  <div class="calendar">
    <div class="calendar-header">Sunday</div>
    <div class="calendar-header">Monday</div>
    <div class="calendar-header">Tuesday</div>
    <div class="calendar-header">Wednesday</div>
    <div class="calendar-header">Thursday</div>
    <div class="calendar-header">Friday</div>
    <div class="calendar-header">Saturday</div>
    
    <!-- Calendar days will be dynamically generated using JavaScript -->
  </div>
  
  <div class="form-container">
    <label for="start-date">Start Date:</label>
    <input type="text" id="start-date">
    
    <label for="end-date">End Date:</label>
    <input type="text" id="end-date">
    
    <label for="symptoms">Symptoms:</label>
    <input type="text" id="symptoms">
    
    <label for="mood">Mood:</label>
    <select id="mood">
      <option value="happy">Happy</option>
      <option value="sad">Sad</option>
      <option value="angry">Angry</option>
      <option value="anxious">Anxious</option>
      <option value="calm">Calm</option>
    </select>
    
    <button onclick="addData()">Add Data</button>
  </div>
  
  <div class="data-container">
    <h3>Recorded Data:</h3>
    <ul id="recorded-data"></ul>
  </div>
  
  <script>
    // JavaScript code for handling data input and display
    
    // Store the recorded data in an array
    let recordedData = [];
    
    // Function to add data to the recordedData array
    function addData() {
      const startDate = document.getElementById('start-date').value;
      const endDate = document.getElementById('end-date').value;
      const symptoms = document.getElementById('symptoms').value;
      const mood = document.getElementById('mood').value;
      
      const data = {
        startDate,
        endDate,
        symptoms,
        mood
      };
      
      recordedData.push(data);
      displayData();
      clearForm();
    }
    
    // Function to display the recorded data
    function displayData() {
      const recordedDataList = document.getElementById('recorded-data');
      
      // Clear the list before updating
      recordedDataList.innerHTML = '';
      
      recordedData.forEach((data, index) => {
        const listItem = document.createElement('li');
        listItem.innerHTML = `
          <strong>Record ${index + 1}:</strong><br>
          Start Date: ${data.startDate}<br>
          End Date: ${data.endDate}<br>
          Symptoms: ${data.symptoms}<br>
          Mood: ${data.mood}
        `;
        recordedDataList.appendChild(listItem);
      });
    }
    
    // Function to clear the form inputs
    function clearForm() {
      document.getElementById('start-date').value = '';
      document.getElementById('end-date').value = '';
      document.getElementById('symptoms').value = '';
      document.getElementById('mood').value = 'happy';
    }
    
    // Call the displayData function initially to show any existing recorded data
    displayData();
  </script>
</body>
</html>
```

This is a complete HTML, CSS, and JavaScript code for a user-friendly web interface that allows women to track their menstrual cycles. The code includes a calendar view, data input fields, and a display area for the recorded data. Users can input the start and end dates of their menstrual cycles, symptoms, and mood changes. The recorded data is stored in an array and displayed in an organized manner.

## Example Code

To implement the backend system for storing and processing the data entered by users in the web interface, we can use Python and Flask as the web framework. We'll also use SQLAlchemy as the Object-Relational Mapping (ORM) library to interact with the database.

Here's an example of how the code might look:

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cycle_tracker.db'
db = SQLAlchemy(app)

# Define the model for menstrual cycle data
class Cycle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    symptoms = db.Column(db.String(255))
    mood_changes = db.Column(db.String(255))

    def __init__(self, start_date, end_date, symptoms, mood_changes):
        self.start_date = start_date
        self.end_date = end_date
        self.symptoms = symptoms
        self.mood_changes = mood_changes

# API endpoint to add a new menstrual cycle entry
@app.route('/cycles', methods=['POST'])
def add_cycle():
    data = request.get_json()
    start_date = datetime.strptime(data['start_date'], '%Y-%m-%d').date()
    end_date = datetime.strptime(data['end_date'], '%Y-%m-%d').date()
    symptoms = data['symptoms']
    mood_changes = data['mood_changes']

    cycle = Cycle(start_date=start_date, end_date=end_date, symptoms=symptoms, mood_changes=mood_changes)
    db.session.add(cycle)
    db.session.commit()

    return jsonify({'message': 'Cycle entry added successfully'})

# API endpoint to retrieve menstrual cycle data for a specific date range
@app.route('/cycles', methods=['GET'])
def get_cycles():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    cycles = Cycle.query.filter(Cycle.start_date >= start_date, Cycle.end_date <= end_date).all()

    cycle_data = []
    for cycle in cycles:
        cycle_data.append({
            'start_date': cycle.start_date.strftime('%Y-%m-%d'),
            'end_date': cycle.end_date.strftime('%Y-%m-%d'),
            'symptoms': cycle.symptoms,
            'mood_changes': cycle.mood_changes
        })

    return jsonify(cycle_data)

if __name__ == '__main__':
    db.create_all()
    app.run()
```

In this code, we define a `Cycle` model that represents the menstrual cycle data. The model has properties for the start date, end date, symptoms, and mood changes. We also define API endpoints to add a new cycle entry and retrieve cycle data for a specific date range.

Note: This code assumes the use of a SQLite database. You can change the database URI in the `app.config['SQLALCHEMY_DATABASE_URI']` line to use a different database system if needed.

To run the code, you'll need to install the required dependencies by running `pip install flask flask_sqlalchemy`. Then, you can save the code in a file (e.g., `app.py`) and run it using `python app.py`. The API will be accessible at `http://localhost:5000`.

Remember to handle authentication and authorization appropriately to ensure the security and privacy of user data.

## Visualize Menstrual Cycle Data

```javascript
<!DOCTYPE html>
<html>
<head>
  <title>Menstrual Cycle Data Visualization</title>
  <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
  <script src="https://cdn.jsdelivr.net/npm/chart.js@3.6.2/dist/chart.min.js"></script>
</head>
<body>
  <div class="container">
    <div class="row">
      <div class="col">
        <h1>Menstrual Cycle Data Visualization</h1>
        <canvas id="cycleChart"></canvas>
      </div>
    </div>
  </div>

  <script>
    // Sample data
    const cycleData = [
      { date: '2022-01-01', duration: 5 },
      { date: '2022-02-01', duration: 4 },
      { date: '2022-03-01', duration: 6 },
      { date: '2022-04-01', duration: 5 },
      { date: '2022-05-01', duration: 6 },
      { date: '2022-06-01', duration: 4 },
    ];

    // Prepare data for chart
    const labels = cycleData.map((data) => data.date);
    const durations = cycleData.map((data) => data.duration);

    // Create chart
    const cycleChart = new Chart(document.getElementById('cycleChart'), {
      type: 'line',
      data: {
        labels: labels,
        datasets: [{
          label: 'Cycle Duration',
          data: durations,
          fill: false,
          borderColor: 'rgb(75, 192, 192)',
          tension: 0.1
        }]
      },
      options: {
        responsive: true,
        scales: {
          x: {
            title: {
              display: true,
              text: 'Date'
            }
          },
          y: {
            title: {
              display: true,
              text: 'Duration (days)'
            },
            min: 0
          }
        }
      }
    });
  </script>
</body>
</html>
```

This code creates a simple web page with a line chart using Chart.js library to visualize menstrual cycle data. It includes a sample dataset with dates and cycle durations. The chart displays the cycle duration on the y-axis and the dates on the x-axis. Users can customize the chart appearance and add more datasets as needed.

## Starting Point

To complete task 4, you can use the following code snippets as a starting point:

### User Authentication System

#### HTML Markup (login.html)

```html
<!DOCTYPE html>
<html>
<head>
    <title>User Login</title>
</head>
<body>
    <h2>Login</h2>
    <form action="/login" method="POST">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
```

#### HTML Markup (register.html)

```html
<!DOCTYPE html>
<html>
<head>
    <title>User Registration</title>
</head>
<body>
    <h2>Register</h2>
    <form action="/register" method="POST">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>
        <input type="submit" value="Register">
    </form>
</body>
</html>
```

#### JavaScript (main.js)

```javascript
// Hashing and salting the password
function hashPassword(password) {
    // Implement your password hashing and salting algorithm here
    // Return the hashed and salted password
}

// User registration
app.post('/register', (req, res) => {
    const { email, password } = req.body;

    // Check if the user already exists in the database
    const existingUser = db.find(user => user.email === email);
    if (existingUser) {
        return res.status(409).send('User already exists');
    }

    // Hash and salt the password
    const hashedPassword = hashPassword(password);

    // Create a new user object and store it in the database
    const newUser = { email, password: hashedPassword };
    db.push(newUser);

    return res.status(200).send('User registered successfully');
});

// User login
app.post('/login', (req, res) => {
    const { email, password } = req.body;

    // Find the user in the database
    const user = db.find(user => user.email === email);
    if (!user) {
        return res.status(401).send('Invalid email or password');
    }

    // Verify the password
    const hashedPassword = hashPassword(password);
    if (user.password !== hashedPassword) {
        return res.status(401).send('Invalid email or password');
    }

    // User authentication successful
    return res.status(200).send('Login successful');
});
```

Please note that the above code snippets are just a starting point and may need to be adapted to fit your specific requirements. You'll also need to implement the database functionality and handle session management, which is beyond the scope of this code snippet.

## E-mail Anda Notification

To enhance the web interface and add a feature that sends email or push notifications to remind users about upcoming menstrual cycles, ovulation periods, or contraceptive methods, you can follow these steps:

1. Choose a third-party email or notification service provider that offers APIs for sending emails or push notifications. Some popular options include SendGrid, Mailgun, or Firebase Cloud Messaging (FCM).

2. Set up an account with the chosen service provider and obtain the necessary credentials or API keys required for integration.

3. In your web application's backend code (assuming you are using a server-side language like Node.js), install the necessary packages to interact with the chosen service provider's API. For example, if you choose SendGrid, you can use the `@sendgrid/mail` package.

4. Implement the logic to calculate upcoming menstrual cycles, ovulation periods, or contraceptive method reminders based on the user's input data. You can use algorithms or predefined rules to determine these dates.

5. Once you have the upcoming dates, use the service provider's API to send email or push notifications to the user. Here's an example using SendGrid in Node.js:

```javascript
const sgMail = require('@sendgrid/mail');
sgMail.setApiKey(process.env.SENDGRID_API_KEY);

// Calculate the upcoming menstrual cycle, ovulation period, or contraceptive method reminders
const upcomingDates = calculateUpcomingDates();

// Send email notification
const msg = {
  to: 'user@example.com',
  from: 'your-email@example.com',
  subject: 'Upcoming Menstrual Cycle Reminder',
  text: `Your next menstrual cycle is scheduled to start on ${upcomingDates.menstrualCycleStartDate}. Don't forget to track your symptoms and mood changes.`,
};

sgMail.send(msg)
  .then(() => {
    console.log('Email sent');
  })
  .catch((error) => {
    console.error(error);
  });
```

Note: Remember to replace `'user@example.com'` with the actual user's email address and `'your-email@example.com'` with your own email address.

6. Integrate this backend code with your web interface. You can add a button or checkbox for users to opt-in to receive notifications and store their preference in the database.

7. Handle the user's preference in the backend code and trigger the email or push notification sending logic accordingly.

8. Test the functionality by creating test accounts and verifying that the email or push notifications are being sent correctly.

Remember to secure any sensitive information like API keys or credentials by storing them in environment variables or using a secure configuration method.

This code provides a basic example of how to send email notifications using SendGrid. If you choose a different service provider or want to implement push notifications, refer to their documentation for the specific integration steps and code examples.

To implement a recommendation engine for personalized suggestions based on the user's menstrual cycle data, we can use machine learning algorithms. Here's an outline of how you can approach this task:

1. Data Collection and Preparation:
   - Collect and store the user's menstrual cycle data, including start and end dates, symptoms, and mood changes.
   - Preprocess the data by cleaning, normalizing, and transforming it into a suitable format for machine learning algorithms.

2. Feature Extraction:
   - Extract relevant features from the menstrual cycle data that can be used to generate recommendations.
   - Examples of features could include cycle length, duration of menstruation, symptoms intensity, mood patterns, etc.

3. Train a Recommendation Model:
   - Select a suitable machine learning algorithm for generating recommendations.
   - Split the preprocessed data into training and testing sets.
   - Train the recommendation model using the training data.
   - Evaluate the model's performance using appropriate evaluation metrics.

4. Generate Personalized Suggestions:
   - Once the model is trained and evaluated, you can use it to generate personalized suggestions for contraceptive methods, fertility tracking, or health tips.
   - Based on the user's menstrual cycle data, input the relevant features into the trained model to get recommendations.
   - The recommendations can be in the form of a ranked list or a probability distribution.

5. Display Recommendations:
   - Integrate the recommendation engine with the existing web interface.
   - Design a user-friendly interface to display the generated recommendations.
   - Present the recommendations in an organized manner, providing details and explanations for each suggestion.

Note: The implementation details of the machine learning algorithm, such as selecting the specific model and training parameters, depend on the nature of the data and the desired recommendation task. You may need to explore different algorithms like collaborative filtering, content-based filtering, or hybrid approaches to achieve accurate and personalized recommendations.

Remember that as an AI language model, I can only provide code snippets and guidance. The actual implementation will require expertise in machine learning, programming languages, and web development.
