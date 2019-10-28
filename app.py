import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task_manager'

#app.config["MONGO_URI"] = 'mongodb+srv://rOOtUser:<mongostat --host myfirstcluster-shard-0/myfirstcluster-shard-00-00-97xkz.mongodb.net:27017,myfirstcluster-shard-00-01-97xkz.mongodb.net:27017,myfirstcluster-shard-00-02-97xkz.mongodb.net:27017 --ssl --username rOOtUser --password <PASSWORD> --authenticationDatabase admin >@myfirstcluster-97xkz.mongodb.net/test?retryWrites=true&w=majority'

app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())
'''
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(('8080')),
            debug=True)
'''            '''
if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=int(os.environ.get("PORT", 5000)),
            # port=int('5000'),
            debug=True)'''

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)