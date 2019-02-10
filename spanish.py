

class Spanish:


	spanish = {
	"mm": """
		1. Registrarse
		2. Ingresar
		3. Generar datos ficticios
		4. Generar datos ficticios desde un txt
		5. Guardar usuarios generados
		$. Salir
	    """,
	"usero": """
		¿Que quieres hacer?
		1. Revisar mi perfil
		2. Actualizar my perfil
		3. Revisar un canal
		4. Leer algunas noticias
		5. Revisar mis favoritos
		6. Expulsar un usuario
		7. Eliminar mi cuenta
		8. Salir
		""",
	"favo": """
		¿Que quieres hacer?
		1. Leer mis preguntas favoritas
		2. Leer mis comentarios favoritos
		3. Leer mis noticias favoritas
		@. Ir al menu anterior.
		""",
	"updateo": """
		¿Que modificaras?
		1. Todo en mi perfil
		2. Solo mi nombre
		3. Solo mi nombre de usuario
		4. Solo mi correo
		5. Solo mi contrasena
		@. Ir al menu anterior.
		""",
	"channelo": """
		¿Que quieres hacer?
		1. Buscar una pregunta
		2. Hacer una pregunta
		3. Leer algunas preguntas
		4. Ver el top de preguntas
		5. Eliminar este canal
		@. Ir al menu anterior.
		""",
	"selectq":"""
		1. Seleccionar una pregunta para desplegar más opciones. 
		@. Ir al menu anterior.
		""",
	"questiono": """
		¿Que quieres hacer?
		1. Responder la pregunta
		2. Leer sus comentarios
		3. Darle me gusta
		4. Darle no me gusta
		5. Ver sus me gusta 
		6. Ver sus no me gusta
		7. Guardar esta pregunta
		8. Editar esta pregunta
		9. Eliminar esta pregunta
		@. Ir al menu anterior.
		""",
	"selectc":"""
		1. Selecciona un comentario para ver mas opciones
		@. Ir al menu anterior.
		""",
	"commento": """
		¿Que quieres hacer?
		1. Darle me gusta
		2. Darle no me gusta
		3. Ver sus me gusta
		4. Ver sus no me gusta 
		5. Guardar este comentario
		6. Editar este comentario
		7. Eliminar este comentario
		@. Ir al menu anterior.
		""",
	"selectn":"""
		1. Subir una noticia
		2. Selecciona una noticia para ver mas opciones
		3. Ver el top de noticias
		@. Ir al menu anterior.
		""",
	"newo": """
		¿Que quieres hacer?
		1. Comentar
		2. Leer sus comentarios
		3. Darle me gusta
		4. Darle no me gusta
		5. Ver sus me gusta
		6. Ver sus no me gusta
		7. Guardar esta noticia
		8. Editar esta noticia
		9. Eliminar esta noticia
		@. Ir al menu anterior.
		""",
	"editnew": """
		¿Qué quieres editar de esta noticia?
		1. Todo en esta noticia
		2. Solo su título
		3. Solo su contenido
		4. Solo su autor
		5. Solo su categoría
		@. Ir al menu anterior.
		""",
	"gbp": """
		@. Ir al menu anterior. 
		""",
	"needo": """
	    ¿Necesitas utilizar algún operador(Y,O,NO)?:
	    1. Sí, lo necesito.
	    2. No, no lo necesito.
	    """,
	"selecto": """
	    Selecciona el operador que quieres utilizar:
	    1. Y
	    2. O
	    3. NO
	    """,
	"attempts": """
		Ya has tratado de ingresar 3 veces, ¿quieres intentarlo una vez mas?
		1. Sí
		2. No
		""",
	"sure": """
		Estas segur@ de que quieres eliminar tu cuenta?
		1. Sí, quiero eliminar mi cuenta
		2. No, no quiero eliminar mi cuenta
		""",
	"sorto": """
		¿Quieres ordenar los canales?
		1. Sí.
		2. No.
		""",
	"sortby": """
		Ordenar los canales por:
		1. El número de visitas del canal
		2. El número de preguntas del canal
		""",
	"maxattempts": "Ya has tratado de ingresar 4 veces, te redireccionaremos al menu principal",
	"lastattempt": "Ultimo intento antes de redireccionarte",
	"i": "La opcion elegida es incorrecta, por favor elija otra opcion.",
	"keyword": "Ingrese la palabra clave: ",
	"nomatch": "No hay coincidencias para la(s) palabra(s) ingresadas.",
	"name": "Ingrese su nombre: ",
	"nn": "Ingrese el nuevo nombre",
	"n": "Nombre: ",
	"username": "Ingrese su nombre de usuario: ",
	"nu": "Ingrese el nuevo nombre de usuario: ",
	"un": "Usuario: ",
	"una": "El usuario ya se encuentra registrado.",
	"email": "Ingrese su correo: ",
	"email2": "Confirme su correo: ",
	"ne": "Ingrese el nuevo correo: ",
	"e": "Email: ",
	"ea": "El email ya se encuentra registrado.",
	"edm": "Los correos no coinciden.",
	"password": "Ingrese su contraseña: ",
	"password2": "Confirme su contraseña:",
	"oldpassword": "Ingrese su última contraseña: ",
	"np": "Ingrese la nueva contraseña: ",
	"pdm": "Las contraseñas no coinciden.",
	"wp": "Contraseña incorrecta.",
	"wu": "Nombre de usuario incorrecto",
	"uc": "El usuario ha sido creado.",
	"iu": "El usuario no existe.",
	"channel": "Ingrese el tema del canal: ",
	"channels": "Estos son los canales disponibles: ",
	"nchannels": "No hay canales disponibles",
	"nquestions": "No hay preguntas disponibles",
	"ncomments": "No hay commentarios disponibles",
	"ic": "El canal no existe",
	"chs": "Canales: ",
	"nq": "Este canal no tiene preguntas",
	"topic": "Tema: ",
	"de": "Descripción: ",
	"question": "Escriba una pregunta: ",
	"ncq": "Esta pregunta no tiene comentarios.", 
	"nuq": "No tienes permisos para editar esta pregunta.", 
	"nun": "No tienes permisos para editar esta noticia.",
	"q": "Pregunta: ",
	"mb": "Hecha por: ",
	"mb1": "Hecho por: ",
	"da": "Fecha: ",
	"news": "estas son las noticias disponibles",
	"News": "NEWS",
	"nnews": "No hay noticias disponibles",
	"title": "Ingrese el titulo de la noticia: ",
	"title1": "Título: ",
	"content": "Ingrese el contenido de la noticia: ",
	"author": "Ingrese el nombre del author", 
	"aut": "Autor: ",
	"label": "Ingrese la categoría: ",
	"ncn": "Esta noticia no tiene comentarios.",
	"id": "id: ",
	"idin": "Ingrese the id: ",
	"iid": "id invalido",
	"la": "Categoría: ",
	"comment": "Escriba un comentario: ",
	"nuc": "No tienes permisos para editar este comentario.",
	"c": "Comentario: ",
	"lks": "me gusta: ",
	"dlks": "no me gusta: ",
	"l": "Usuarios a los que les gusta esto: ",
	"dl": "Usuarios a los que les disgusta esto: ",
	"nls": "A nadie le gusta esto",
	"ndls": "A nadie le disgusta esto",
	"fs": "Favorito guardado.",
	"fhs": "El favorito ya ha sido guardado.",
	"nfq": "No tienes preguntas favoritas.",
	"nfc": "No tienes comentarios favoritos.",
	"nfn": "No tienes noticias favoritas.",
	"lo": "Regresa pronto.",
	"np": "No tienes permiso para realizar esta acción",
	"ub": "Tu usuario actualmente está excluido, por lo tanto, no puedes ingresar",
	"inub": "Ingresa el usuario que será expulsado",
	"chd": "Canal eliminado",
	"qd": "Pregunta eliminada",
	"cod": "Comentario eliminado",
	"nd": "noticia eliminada",
	"aam": "Esta acción ya se ha realizado una vez, por lo tanto, no se puede realizar de nuevo",
	"ara": "Esta acción requiere que la acción 4 sea realizada",
	"nusers": "No hay usuarios",
	"redirecting": "Redireccionandote al menu anterior",
	"idmb": "El id debe ser un entero."
	}
