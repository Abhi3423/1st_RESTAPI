from flask import Flask,jsonify

app = Flask(__name__)
armstrong_numbers = []

@app.route('/')
def hello():
    return 'Hello type in web address'


@app.route('/armstrong', methods=['GET'])
def get_all_armstrong_numbers():
       return jsonify(Type='armstrong',numbers=armstrong_numbers)


@app.route('/armstrong/<int:n>')
def armstrong(n):
    sum = 0
    order = len(str(n))
    copy_n = n
    while(n>0):
        digit = n%10
        sum += digit ** order
        n = n//10
        
    if(sum == copy_n):
        print(f"{copy_n} is an Armstrong number")
        result = {"Number": copy_n,
                  "Armstrong": True}
        if copy_n not in armstrong_numbers:   
         armstrong_numbers.append(copy_n)
         print(armstrong_numbers)
    
    else:
        print(f"{copy_n} is not a Armstrong number")
        result = {"Number": copy_n,
                  "Armstrong": False}
        
    return jsonify(result)
    


if __name__ == "__main__":
    app.run(debug=True)


