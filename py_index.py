import tea
# The key must be 16 characters
key = "0123456789abcdef"
message = "pasword1234567"
cipher = tea.encrypt(message, key)

f = open("secret_page.html", "w")
f.write("<p>Este sitio contiene un mensaje secreto</p>\n<div class='TEA' id='"+cipher+"'></div>")
f.close()

print("Se ha creado un archivo html con el contenido encriptado.")