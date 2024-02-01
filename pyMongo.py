from flask import Flask, render_template,make_response,request, session, redirect, url_for,current_app
from flask_restful import Api, Resource
from flask_session import Session
import pyMongo
from os import environ,system,getcwd
system("clear")
system(f"rm -rf {getcwd()}/flask_session")

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = "c365a380254da310e47c24a692dad2e8"
app.config['SESSION_TYPE'] = 'filesystem'  #Sessions are stored as files on the server.(development only)
app.config['SESSION_PERMANENT'] = True #False -> session will expire when the browser is closed.
app.config['SESSION_USE_SIGNER'] = True  # adds a cryptographic signature to the session cookie 
app.config['SESSION_COOKIE_SAMESITE'] = 'None' #cookies will be sent with cross-origin requests.
app.config['SESSION_COOKIE_SECURE'] = True #ensures that the session cookie is only sent over HTTPS connections.
Session(app)

#Shows List of Databases
class Home(Resource):
    def get(self):
        id = session.get('id')
        if id:
            databases = current_app.db.getAllDB()
            return make_response(render_template("dashboard.html",data=databases))
            # return ({"id":id,"String":string,"msg":"You are logged in"})
        else:
           return redirect(url_for("connect"))
#Shows List of Collections inside a DB
class ShowCollections(Resource):
    def get(self):
        id = session.get('id')
        if id:
            data = request.args.to_dict()
            session['currentdatabase'] = data['dbname']
            collections = current_app.db.getAllCollection(db_name=data['dbname'])
            # return (collections)
            return make_response(render_template("collections.html",data=collections))
        else:
           return redirect(url_for("connect"))       
#Shows data Inside A collection
class getData(Resource):
    def get(self):
        id = session.get('id')
        if id:
            data = request.args.to_dict()
            collection = data['collectionName']
            current_app.db.addDB(db_name=session.get('currentdatabase'),collection_name=collection)
            dbdata = current_app.db.fetch(show_id=False)
            return make_response(render_template("data.html", data=dbdata))
        else:
            return redirect(url_for("connect")) 
# Normal Login
class Connect(Resource):
    def get(self):
        return make_response(render_template('connect.html'))
    
    def post(self):
        data = request.form.to_dict()
        string = "mongodb://localhost:27017/" if not data['string'] else data['string']
        current_app.db = pyMongo.MongoDB(connectionStr=string)
        if current_app.db != False:
            session['id'] = pyMongo.genString()
            return ({"msg":"Success"})
        # return ({"msg":"Invalid Credentials or String"})  
#Logout
class Logout(Resource):
    def get(self):
      id = session.get('id')
      if 'id' in session:
        session.pop('id', None)  # Remove user_id from session
        return redirect(url_for("connect"))
    
      else:
        return redirect(url_for("connect"))  

api.add_resource(Home, '/')
api.add_resource(Connect, '/connect')
api.add_resource(Logout, '/logout')
api.add_resource(ShowCollections, '/collection')
api.add_resource(getData, '/getdata')

if __name__ == '__main__':
    app.run(debug=True,port=5000,host="0.0.0.0",threaded=True)
