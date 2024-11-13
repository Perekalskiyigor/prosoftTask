from flask import Flask
from flask import render_template
from flask import request
from flask import Flask, render_template, request, redirect, url_for
from pprint import pprint
import provider as p # Данные с базы через доп модуль
app = Flask(__name__)


# Внешняя функция для получения данных
def get_external_data(order_number):
    extData = p.OrderJsonData(order_number)
    return extData


# index
@app.route('/')
def hello():
    return render_template('index.html')

# Кнопка
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    # Получаем номер заказа из формы
    order_number = request.form['orderNumber']
    order_data, status_code = get_external_data(order_number)
    if status_code == '200':
        # print(f'Код ответа{status_code}')
        return render_template('order_details.html', order_data=order_data)
    return render_template('500.html')



if __name__ == '__main__':
    app.run(debug=True)
   

