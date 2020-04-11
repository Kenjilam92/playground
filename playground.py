from flask import Flask, render_template  
app = Flask(__name__)    

@app.route('/play')
def play():
    return render_template('play.html',times=3)
@app.route('/play/<times>')
def multiple(times):
    return render_template('play.html',times=int(times))
@app.route('/play/<times>/<color>')
def multiple_and_change(times,color):
    return render_template('play.html',times=int(times),color='style=background-color:'+ color)

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again."

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.s