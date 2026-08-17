
from flask import Flask, render_template, request, redirect, flash, session

app = Flask('logins')

app.secret_key = 'safewordslol123'

from deep_translator import GoogleTranslator

# Translate English to Spanish
text_to_translate = "Hello, how are you today?"
translated = GoogleTranslator(source='auto', target='zh-CN').translate(text_to_translate)
##en,fr,es,ger,chi,ja
print(translated)


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('tr.html')
    if request.method == 'POST':
        source = request.form.get("source")
        target = request.form.get("target")
        text = request.form.get("message")
        print(source,target,text)
        ttt = text
        translated = GoogleTranslator(source=source, target=target).translate(ttt)
        print(translated)
        return render_template('tr.html',translated=translated)

if __name__ == "__main__":
    app.run(host = "0.0.0.0",debug=True)
