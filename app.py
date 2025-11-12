from flask import Flask, render_template, request, jsonify, send_file
import json
import os
from datetime import datetime
from data_structures import StudentBST, SortingAlgorithms
import io

app = Flask(__name__)
DATA_FILE = os.getenv('DATA_FILE', 'students.json')

# Initialize sample data
def init_data():
    if not os.path.exists(DATA_FILE):
        sample_data = [
            {"reg_no": "001", "name": "Alice Kumar", "maths": 85, "science": 90, "english": 88},
            {"reg_no": "002", "name": "Bob Singh", "maths": 78, "science": 82, "english": 80},
            {"reg_no": "003", "name": "Charlie Brown", "maths": 92, "science": 88, "english": 95},
            {"reg_no": "004", "name": "Diana Patel", "maths": 88, "science": 85, "english": 92},
            {"reg_no": "005", "name": "Eve Johnson", "maths": 75, "science": 79, "english": 77},
        ]
        save_data(sample_data)

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/')
def dashboard():
    students = load_data()
    return render_template('dashboard.html', students=students)

@app.route('/add')
def add_page():
    return render_template('add_student.html')

@app.route('/api/add-student', methods=['POST'])
def add_student():
    data = request.json
    students = load_data()
    students.append(data)
    save_data(students)
    return jsonify({'status': 'success'})

@app.route('/sorting')
def sorting_page():
    return render_template('sorting.html')

@app.route('/api/sort', methods=['POST'])
def sort_students():
    data = request.json
    students = load_data()
    sort_type = data.get('type')
    sort_by = data.get('sort_by')
    
    sorter = SortingAlgorithms()
    sorted_students, time_taken = sorter.sort(students, sort_type, sort_by)
    
    return jsonify({'students': sorted_students, 'time': f"{time_taken:.4f}s", 'algorithm': sort_type})

@app.route('/tree')
def tree_page():
    return render_template('tree.html')

@app.route('/api/tree-data', methods=['GET'])
def get_tree_data():
    students = load_data()
    bst = StudentBST()
    for student in students:
        total = student['maths'] + student['science'] + student['english']
        bst.insert(total, student['name'])
    
    return jsonify({
        'tree': bst.to_dict(),
        'inorder': bst.inorder(),
        'preorder': bst.preorder(),
        'postorder': bst.postorder()
    })

@app.route('/analysis')
def analysis_page():
    return render_template('analysis.html')

@app.route('/api/analysis')
def get_analysis():
    students = load_data()
    
    if not students:
        return jsonify({'error': 'No students'})
    
    totals = [s['maths'] + s['science'] + s['english'] for s in students]
    average = sum(totals) / len(totals)
    
    grades = []
    for s, total in zip(students, totals):
        if total >= 90: grade = 'A'
        elif total >= 80: grade = 'B'
        elif total >= 70: grade = 'C'
        elif total >= 60: grade = 'D'
        else: grade = 'F'
        grades.append({'name': s['name'], 'grade': grade, 'total': total})
    
    grades.sort(key=lambda x: x['total'], reverse=True)
    top_3 = grades[:3]
    
    grade_dist = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for g in grades:
        grade_dist[g['grade']] += 1
    
    above_avg = sum(1 for t in totals if t >= average)
    below_avg = len(totals) - above_avg
    
    return jsonify({
        'average': round(average, 2),
        'top_3': top_3,
        'grade_distribution': grade_dist,
        'above_average': above_avg,
        'below_average': below_avg,
        'topper': max(zip(students, totals), key=lambda x: x[1])[0]['name'],
        'lowest': min(zip(students, totals), key=lambda x: x[1])[0]['name']
    })

@app.route('/api/download-report')
def download_report():
    students = load_data()
    totals = [s['maths'] + s['science'] + s['english'] for s in students]
    
    report = "STUDENT RESULT ANALYSIS REPORT\n"
    report += "=" * 60 + "\n"
    report += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    report += f"{'Reg No':<10} {'Name':<20} {'Total':<10} {'Grade':<5}\n"
    report += "-" * 60 + "\n"
    
    for s, total in zip(students, totals):
        grade = 'A' if total >= 90 else 'B' if total >= 80 else 'C' if total >= 70 else 'D' if total >= 60 else 'F'
        report += f"{s['reg_no']:<10} {s['name']:<20} {total:<10} {grade:<5}\n"
    
    return send_file(io.BytesIO(report.encode()), mimetype='text/plain', as_attachment=True, download_name='student_report.txt')

if __name__ == '__main__':
    init_data()
    app.run(debug=True, host='0.0.0.0', port=5000)
