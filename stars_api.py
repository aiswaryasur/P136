from flask import Flask, jsonify,request
from stars import stars
app=Flask(__name__)

@app.route('/')
def home():
    return jsonify ({
        'data':stars,
        'message':'success'

    }),200


@app.route('/star')
def planet():
    name=request.args.get('name')
    for item in stars:
        if item['name']==name:
            star_data=item
    return jsonify ({
        'data':star_data,
        'message':'success'

    }),200

if __name__ == '__main__':
    app.run()
