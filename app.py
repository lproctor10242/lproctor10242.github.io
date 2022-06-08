from flask import Flask, render_template

app = Flask(__name__)


#Using the below, the popup message appears on the page load of index.html
#0x00001000 - This makes the popup appear over the browser window
@app.route('/')
def index():
    return render_template('index.html',text='You have just run a python script on the page load!')

#Using the below, the popup message appears when the button is clicked on the webpage.
#0x00001000 - This makes the popup appear over the browser window
@app.route('/test')
def test():
    print('You have just run a python script on the button press!')
    return("successful run")

if __name__ == "__main__":
    app.run(debug=True)