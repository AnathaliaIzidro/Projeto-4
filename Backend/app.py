from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

@app.route('/contacts', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    return jsonify([{'id': contact.id, 'name': contact.name} for contact in contacts])

@app.route('/contacts', methods=['POST'])
def create_contact():
    data = request.get_json()
    contact = Contact(name=data['name'])
    db.session.add(contact)
    db.session.commit()
    return jsonify({'id': contact.id, 'name': contact.name})

@app.route('/contacts/<int:contact_id>', methods=['GET'])
def get_contact(contact_id):
    contact = Contact.query.get(contact_id)
    if contact is None:
        return jsonify({'error': 'Contato não encontrado'}), 404
    return jsonify({'id': contact.id, 'name': contact.name})

@app.route('/contacts/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    contact = Contact.query.get(contact_id)
    if contact is None:
        return jsonify({'error': 'Contato não encontrado'}), 404
    data = request.get_json()
    contact.name = data['name']
    db.session.commit()
    return jsonify({'id': contact.id, 'name': contact.name})

@app.route('/contacts/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    contact = Contact.query.get(contact_id)
    if contact is None:
        return jsonify({'error': 'Contato não encontrado'}), 404
    db.session.delete(contact)
    db.session.commit()
    return jsonify({'message': 'Contato deletado com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)