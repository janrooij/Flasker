#1 importeer de flask biblio
from flask import Flask, render_template

#2 maak een flask omgeving(instance)
app = Flask(__name__)

#3 maak een route decorator, verbindt urls met paden
# deze route verwijst naar de root
@app.route('/')
#def index():
#return "<h1>Hello World !</h1>"
#of verwijzen naar html paginas zie hieronder

#je kunt filters meegeven
#safe, om html door te geven aan pagina
#capitalize
#lower
#upper
#title
#trim
#striptags

def index():
	first_name = "Jan"
	stuff = "Dit is vette tekst "
	favoriete_pizza=["Pepperoni", "Paddo", "Mozarella", "Formaggio", 40]
	return render_template('index.html', 
		first_name=first_name,
		stuff=stuff,
		favoriete_pizza = favoriete_pizza)

#deze verwijst naar de ingelogde user met de var 'name'
#functie var naamd
#return var naam  
#pad wordt dan localhost:5000/user/Jan
@app.route('/user/<name>')
def user(name):
	return render_template('user.html', user_name=name)
	
  

#custom error pages maken

#invalid url
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

#internal  server error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500