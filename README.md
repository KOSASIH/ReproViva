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
