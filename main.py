from flask import Flask, render_template, request, send_file
from convert_arabic_to_thai import convert


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        f = request.files['file']
        file_name = f.filename.split(".")[0]
        tmp = convert(f.stream.read())
        return send_file(tmp, 
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        as_attachment=True,
        download_name=f"{file_name}_converted.xlsx"
        )
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
