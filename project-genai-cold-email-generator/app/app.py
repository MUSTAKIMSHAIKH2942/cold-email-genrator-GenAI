from flask import Flask, request, render_template, jsonify
from chains import Chain
from portfolio import Portfolio
from utils import clean_text

app = Flask(__name__)
portfolio = Portfolio()
chain = Chain()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        url_input = request.form.get("url")
        try:
            data = clean_text(chain.load_url(url_input))
            portfolio.load_portfolio()
            jobs = chain.extract_jobs(data)
            responses = []
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = chain.write_mail(job, links)
                responses.append(email)
            return jsonify({"emails": responses})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
