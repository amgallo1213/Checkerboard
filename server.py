from flask import Flask, render_template 
app = Flask(__name__)


@app.route('/') #displays an 8 by 8 checkerboard
def big_board():
    # return 'Big Checkerboard'
    return render_template("boards.html", row=4)


@app.route('/4') #displays an 8 by 4 checkerboard
def small_board():
    return render_template('small_board.html', row=4)

@app.route('/<int:num>') #displays a checkerboard with x number of rows
def num_choice_board(num):
    x=num 
    return render_template("num_choice_board.html", row=x, column=x)
# @app.route('/int()/int()')



if __name__=="__main__":
    app.run(debug=True)    