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
