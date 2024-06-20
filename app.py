from flask import Flask, render_template, request, redirect, url_for, send_file
import pandas as pd
import os

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
PROCESSED_FOLDER = os.path.join(os.getcwd(), 'processed')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file and file.filename.endswith('.csv'):
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        new_columns = {
            request.form.get('new_column_name1'): request.form.get('new_column_value1'),
            request.form.get('new_column_name2'): request.form.get('new_column_value2'),
            request.form.get('new_column_name3'): request.form.get('new_column_value3')
        }
        default_value = request.form.get('default_value') or "0"
        new_filename = process_file(filepath, new_columns, default_value)
        return redirect(url_for('download_file', filename=new_filename))
    return "Invalid file type"

def process_file(filepath, new_columns, default_value):
    df = pd.read_csv(filepath)

    # Remove completely empty rows
    df.dropna(how='all', inplace=True)

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Fill empty cells with default value provided by user
    df.fillna(default_value, inplace=True)

    # Adding new columns
    for col_name, col_value in new_columns.items():
        if col_name:
            df[col_name] = col_value if col_value else default_value

    new_filename = 'processed_' + os.path.basename(filepath)
    new_filepath = os.path.join(PROCESSED_FOLDER, new_filename)
    df.to_csv(new_filepath, index=False)
    return new_filename

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(PROCESSED_FOLDER, filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
