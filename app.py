from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from datetime import datetime
import os

app = Flask(__name__, static_url_path='')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error-404.html')

@app.route('/')
def main():
	#Read all countries in the text file
	country_list_file = open('countries.txt', 'r')
	country_list = country_list_file.readlines()
	#Get the current country in the url parameter
	get_country = request.args.get('country', default='World')
	#get current date
	date = datetime.today().strftime('%Y-%m-%d')

	return render_template('main.html', 
		countries=country_list, url_country=get_country, date=date)

if __name__ == '__main__':
	app.run()