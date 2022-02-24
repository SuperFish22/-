from flask import Flask, render_template, request #для работы с интернетом
from docxtpl import DocxTemplate #для работы с word
import json # работа с json


app = Flask(__name__) #инициализация объекта класса flask


# данный список хранит начальные значения, вашей компании.
context = { 
'nameGame':'ООО Ромашка'

}
fin = {}


def Save(b):
   print("save")
   global fin
   fin.update(b)
   print(fin)



#работа с вордом
def word(context):
    doc = DocxTemplate("static/dock/hablon.docx")# открыть word докумен
    doc.render(context)
    doc.save("static/dock/шаблон-final.docx")# сохранить word докумен





# тут все с сервером и сайтом


def postWord(): # метод обработки post запросов и запись их в словарь
   if request.method == 'POST':
      result = request.form.to_dict()
      context = result
      Save(context)
      #print("[log:]" + str(context))
      return render_template("result.html", result = result)

@app.route('/result.html',methods = ['POST', 'GET'])
def result():
   global fin
   print(fin)
   return render_template('result.html', fin = fin)

@app.route('/resultFin.html',methods = ['POST', 'GET'])
def resultFin():
   global fin
   word(fin)
   return render_template('resultFin.html')

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/1.html',methods = ['POST', 'GET'])
def student():
   return render_template('1.html')


@app.route('/2.html',methods = ['POST', 'GET'])
def twoHtml():
   postWord()
   return render_template("2.html")

@app.route('/3.html',methods = ['POST', 'GET'])
def threeHtml():
   postWord()
   return render_template("3.html")

@app.route('/4.html',methods = ['POST', 'GET'])
def fourHtml():
   postWord()
   return render_template("4.html")

@app.route('/5.html',methods = ['POST', 'GET'])
def fiveHtml():
   postWord()
   return render_template("5.html")

@app.route('/6.html',methods = ['POST', 'GET'])
def sixHtml():
   postWord()
   return render_template("6.html")

@app.route('/7.html',methods = ['POST', 'GET'])
def sevenHtml():
   postWord()
   return render_template("7.html")

@app.route('/8.html',methods = ['POST', 'GET'])
def eightHtml():
   postWord()
   return render_template("8.html")

@app.route('/9.html',methods = ['POST', 'GET'])
def nineHtml():
   postWord()
   return render_template("9.html")


   

if __name__ == '__main__':
   app.run(debug = True)
   
