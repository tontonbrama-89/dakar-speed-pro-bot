from flask import Flask, request, jsonify
from reportlab.pdfgen import canvas
import os

app = Flask(__name__)

if not os.path.exists("static"):
    os.makedirs("static")

@app.route('/')
def home():
    return 'Serveur opérationnel.'

@app.route('/generate', methods=['GET'])
def generate_pdf():
    nom_client = request.args.get('client', 'Client inconnu')
    adresse_recup = request.args.get('pickup', 'Adresse non fournie')
    adresse_livraison = request.args.get('delivery', 'Adresse non fournie')
    description_colis = request.args.get('description', 'Pas de description')
    destinataire = request.args.get('receiver', 'Destinataire inconnu')

    filename = f"bon_livraison_{nom_client}.pdf".replace(" ", "_")
    filepath = f"static/{filename}"

    c = canvas.Canvas(filepath)
    c.drawString(100, 800, "Bon de Livraison - Dakar Speed Pro")
    c.drawString(100, 770, f"Client : {nom_client}")
    c.drawString(100, 740, f"Adresse de récupération : {adresse_recup}")
    c.drawString(100, 710, f"Adresse de livraison : {adresse_livraison}")
    c.drawString(100, 680, f"Description du colis : {description_colis}")
    c.drawString(100, 650, f"Nom / Téléphone destinataire : {destinataire}")
    c.save()

    url_pdf = request.url_root + f"static/{filename}"

    return jsonify({"pdf_link": url_pdf})

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=10000)
