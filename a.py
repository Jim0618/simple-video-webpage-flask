import flask
from flask import render_template

app = flask.Flask(__name__)


@app.route('/')
def index():
	html = r'''	
		<!DOCTYPE html> 
		<html>
		  <head>
		    <meta charset="UTF-8">
		    <title>Leveraging Long and Short-term Information in Context-aware movie recommendation</title>
		  </head>
		  <body>
		    <video src="/video/paper-talk-fast.wmv" 
		      poster="/images/background-cover.jpg"
		      width="1404" height="928" 
		      controls 
		      autoplay 
		      loop>
		      <p>Leveraging Long and Short-term Information in Context-aware movie recommendation</p>
		      <p>主讲人：黄宏兴</p>
		    </video>
		  </body>
		</html>
	'''
	return render_template('papertalk.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8200)