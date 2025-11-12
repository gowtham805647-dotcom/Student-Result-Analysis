# Student Result Analysis System

A complete web-based student result analysis system using Python Flask backend with Trees & Sorting algorithms.

## Project Structure

```
Student Result Analysis/
├── app.py                 # Flask backend
├── data_structures.py     # BST & Sorting algorithms
├── requirements.txt       # Python dependencies
├── students.json          # Student data storage
├── templates/
│   ├── dashboard.html     # Main dashboard
│   ├── add_student.html   # Add student form
│   ├── sorting.html       # Sorting page
│   ├── tree.html          # Tree visualization
│   └── analysis.html      # Analysis & reports
└── static/
    └── style.css          # Styling
```

## Features

### 1. **Dashboard** 
- View all students with marks and grades
- Shows topper, class average, and lowest scorer
- Navigation to other features

### 2. **Add Student**
- Form to add new students
- Input: Name, Register Number, Marks (Maths, Science, English)
- Auto-calculates total and grade

### 3. **Sorting Algorithms**
- Bubble Sort
- Selection Sort
- Insertion Sort
- Sort by Total Marks or Name
- Shows execution time

### 4. **Tree Visualization**
- Binary Search Tree based on total marks
- Visual tree representation
- Traversal options: Inorder, Preorder, Postorder

### 5. **Analysis Report**
- Class average calculation
- Top 3 students list
- Grade distribution chart
- Students above/below average count
- Download report as text file

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open browser and go to: `http://localhost:5000`

## Sample Data

The system comes with 5 sample students pre-loaded.

## API Endpoints

- `GET /` - Dashboard
- `GET /add` - Add student page
- `POST /api/add-student` - Add new student
- `GET /sorting` - Sorting page
- `POST /api/sort` - Sort students
- `GET /tree` - Tree visualization page
- `GET /api/tree-data` - Get tree data
- `GET /analysis` - Analysis page
- `GET /api/analysis` - Get analysis data
- `GET /api/download-report` - Download report
