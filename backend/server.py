from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

def load_data():
    products = []
    with open("./backend/data.txt", "r", encoding="utf-8") as file:
        for line in file:
            name, price, image, desctiption, id = line.strip().split(";")
            products.append({
                "name":name,
                "price": int(price),
                "image": image,
                "desctiption": desctiption,
                "id": (id)
            })
    return products

#Termékek vissza adása JSON formátumba
@app.route("/api/products")
def get_products():
    products = load_data()
    return jsonify(products)

#index/hmtl küldése
@app.route("/")
def serve_index():
    return send_from_directory("../frontent", "index.html")

#
@app.route("/<path:filename>")
def serve_static(filename):
    return send_from_directory("../frontend", filename)

if __name__ == "__main__":
    app.run(port=8000, debug=True)