from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

'''
@app.route('/', methods = ['GET', 'POST']) #to render home page

#function for rendering the HTML page
def home_page():
    return render_template('index.html') #example of a HTML page
'''

# body function(POST) via postman
@app.route('/via_postman', methods = ['POST']) # this is called from the Postman UI

def calulations_via_postman():

    if (request.method == 'POST'):
        operation = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])

        if (operation == 'ADD'):
            res = num1 + num2
            result = 'The Sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(res)

        if (operation == 'SUB'):
            res = num1 - num2
            result = 'The Subtraction of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(res)

        if (operation == 'MULTIPLY'):
            res = num1 * num2
            result = 'The Product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(res)

        if (operation == 'DIVIDE'):
            res = num1 / num2
            result = 'The Division of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(res)

        return jsonify(result) #accepting the result in json format
        # return render_template('results.html', result = result) #using html page to view the app

#url function(GET) using flask
@app.route('/url_function')
def url_test():
    test1 = request.args.get('val1')
    test2 = request.args.get('val2')
    test = int(test1) + int(test2)
    return '''<h1>My result is: {}</h1>'''.format(test)


if __name__ == '__main__':
    app.run()
