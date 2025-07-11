from flask import Flask,request, jsonify, redirect


app = Flask(__name__)
url = {}

@app.route('/', method = ['POST'])


def url_shortener():
   data = request.get_json()
   long_url = data.get("https://very-very-very-long-and-descriptive-subdomain-that-goes-on-and-on.somedomain.com/additional/directory/levels/for/more/length/really-log-sub-domain/a-really-log-page")
   validity = data.get("30")
   shortcode = data.get("abcd1")
   if not long_url or not validity or not shortcode:
      return jsonify({"Error":"Missing required fields"}),400

  
url[shortcode]

if __name__ == '__main__':
   app.run(debug = True)