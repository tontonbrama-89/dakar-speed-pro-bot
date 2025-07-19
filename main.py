from flask import Flask, request, send_from_directory
from reportlab.pdfgen import canvas
import io
import os

app = Flask(__name__)

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

    # Génération du PDF
    filename = 'bon_livraison.pdf'
    filepath = os.path.join('static', filename)
    c = canvas.Canvas(filepath)
    c.drawString(100, 800, "Bon de Livraison - Dakar Speed Pro")
    c.drawString(100, 770, f"Client : {nom_client}")
    c.drawString(100, 740, f"Adresse de récupération : {adresse_recup}")
    c.drawString(100, 710, f"Adresse de livraison : {adresse_livraison}")
    c.drawString(100, 680, f"Description du colis : {description_colis}")
    c.drawString(100, 650, f"Nom / Téléphone destinataire : {destinataire}")
    c.save()

    # Retourne une URL publique vers le PDF
    pdf_url = request.host_url + 'static/' + filename
    return {'pdf_url': pdf_url}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
