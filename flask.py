from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      f.save('upload/' + f.filename)
      return 'uploaded success'
		
if __name__ == '__main__':
   app.run(debug = True)