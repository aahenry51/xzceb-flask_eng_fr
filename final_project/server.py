from machinetranslation import translator
from flask import Flask, render_template, request


app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    return translator.englishToFrench(textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
 
    return translator.frenchToEnglish(textToTranslate)

@app.route("/")
def renderIndexPage():
   return render_template('index.html') #"Hello World!"

if __name__ == "__main__":
    app.run(host="localhost", port=8080)
