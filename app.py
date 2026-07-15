from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulamos una base de datos
usuarios = [
    {
        "id": 1,
        "nombre": "Boris",
        "edad": 22
    },
    {
        "id": 2,
        "nombre": "Juan",
        "edad": 25
    }
]


# -------------------------
# GET - Obtener usuarios
# -------------------------
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(usuarios)


# -------------------------
# GET por ID
# -------------------------
@app.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):

    usuario = next((u for u in usuarios if u["id"] == id), None)

    if usuario:
        return jsonify(usuario)

    return jsonify({"mensaje": "Usuario no encontrado"}), 404



# -------------------------
# POST - Crear usuario
# -------------------------
@app.route('/usuarios', methods=['POST'])
def crear_usuario():

    datos = request.json

    nuevo_usuario = {
        "id": len(usuarios) + 1,
        "nombre": datos["nombre"],
        "edad": datos["edad"]
    }

    usuarios.append(nuevo_usuario)

    return jsonify(nuevo_usuario), 201



# -------------------------
# PATCH - Actualizar usuario
# -------------------------
@app.route('/usuarios/<int:id>', methods=['PATCH'])
def actualizar_usuario(id):

    usuario = next((u for u in usuarios if u["id"] == id), None)

    if usuario:

        datos = request.json

        if "nombre" in datos:
            usuario["nombre"] = datos["nombre"]

        if "edad" in datos:
            usuario["edad"] = datos["edad"]

        return jsonify(usuario)

    return jsonify({"mensaje": "Usuario no encontrado"}), 404



# -------------------------
# DELETE - Eliminar usuario
# -------------------------
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):

    usuario = next((u for u in usuarios if u["id"] == id), None)

    if usuario:

        usuarios.remove(usuario)

        return jsonify({
            "mensaje": "Usuario eliminado"
        })

    return jsonify({
        "mensaje": "Usuario no encontrado"
    }),404



# Ejecutar servidor
if __name__ == '__main__':
    app.run(debug=True)