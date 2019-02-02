

class Message:


	MD = {
	"languages": """
	    Please choose a language:
	    1. English
	    2. Spanish
	    """,
	"i": "The option selected is invalid, please choose a valid option."
	}

	ME = {
	"mm": """
		1. Sign in
		2. Log in 
		3. Generate fictional data 
		4. Generate fictional data from a txt
		5. Save generated users
	    $. Go out
	    """,
	"usero": """
		What do you want to do?
		1. Check my profile
		2. Update my profile
		3. Check a channel
		4. Read some news
		5. Check my favorites
		6. Ban a user
		7. Delete my account
		8. Log out
		""",
	"favo": """
		What do you want to do?
		1. Read my favorite questions
		2. Read my favorite comments
		3. Read my favorite news
		@. Go back to the previous menu
		""",
	"updateo": """
		What will you modify?
		1. Everything in my profile
		2. Only my name
		3. Only my username
		4. Only my email
		5. Only my password
		@. Go back to the previous menu
		""",
	"channelo": """
		What do you want to do?
		1. Search for a question
		2. Make a question
		3. Read some questions
		4. Watch top questions
		5. Delete this channel
		@. Go back to the previous menu
		""",
	"selectq":"""
		1. Select a question to unfold more options 
		@. Go back to the previous menu
		""",
	"questiono": """
		What do you want to do?
		1. Answer the question
		2. Read its comments
		3. Give it a like
		4. Give it a dislike
		5. Watch its likes 
		6. Watch its dislikes
		7. Save this question
		8. Edit this question
		9. Delete this question
		@. Go back to the previous menu
		""",
	"selectc":"""
		1. Select a comment to unfold more options 
		@. Go back to the previous menu
		""",
	"commento": """
		What do you want to do?
		1. Give it a like
		2. Give it a dislike
		3. Watch its likes 
		4. Watch its dislikes
		5. Save this comment
		6. Edit this comment
		7. Delete this comment
		@. Go back to the previous menu
		""",
	"selectn":"""
		1. Upload a new
		2. Select a new to unfold more options
		3. Watch top news
		@. Go back to the previous menu
		""",
	"newo": """
		What do you want to do?
		1. Comment
		2. Read its comments
		3. Give it a like
		4. Give it a dislike
		5. Watch its likes 
		6. Watch its dislikes
		7. Save this new
		8. Edit this new
		9. Delete this new
		@. Go back to the previous menu
		""",
	"editnew": """
		What do you want to edit from this new?
		1. Everything in this new.
		2. Only it's title
		3. Only it's content
		4. Only it's author
		5. Only it's label
		@. Go back to the previous menu 
		""",
	"gbp": """
		@. Go back to the previous menu.
		""",
	"needo": """
	    Do you need to use an operator(AND,OR,NOT)?:
	    1. Yes, I do.
	    2. No, I do not.
	    """,
	"selecto": """
	    Select the operator you want to use:
	    1. AND
	    2. OR
	    3. NOT
	    """,
	"attempts": """
		You have already tried to log in 3 times, do you want to try once more?
		1. Yes
		2. No
		""",
	"sure": """
		Are you sure you want to delete your account?
		1. Yes, I want to delete my account
		2. No, I do not want to delete my account
		""",
	"sorto": """
		Do you want to sort the channels?
		1. Yes.
		2. No.
		""",
	"sortby": """
		Sort the channels by:
		1. Channel's number of visits
		2. Channel's number of questions
		""",
	"maxattempts": "You have already tried to log in 4 times, we will redirect you to the main menu",
	"lastattempt": "Last attempt before redirecting you",
	"i": "The option selected is invalid, please choose a valid option.",
	"keyword": "Insert the keyword: ",
	"nomatch": "There is no match for the word(s) inserted.",
	"name": "Insert your name: ",
	"nn": "Insert the new name: ",
	"n": "Name: ",
	"username": "Insert your username: ",
	"nu": "Insert the new username: ",
	"un": "Username: ",
	"una": "The username is already registered.",
	"email": "Insert your email: ",
	"email2": "Confirm your email: ",
	"ne": "Insert the new email:",
	"e": "Email: ",
	"ea": "The email is aleardy registered.",
	"edm": "The emails do not match.",
	"password": "Insert your password: ",
	"password2": "Confirm your password: ",
	"oldpassword": "Insert your last password: ",
	"np": "Insert the new password: ",
	"pdm": "The passwords do not match.",
	"wp": "wrong password",
	"wu": "wrong username",
	"uc": "The user has been created.",
	"iu": "The user does not exist.",
	"channel": "Insert the channels topic: ",  # Apostrophe
	"channels": "These are the available channels: ",
	"nchannels": "There are no available channels",
	"ic": "The channel does not exist.",
	"chs": "Channels: ",
	"nq": "This channel has no questions",
	"topic": "Topic: ",
	"de": "Description: ",
	"question": "Type a question: ",
	"ncq": "This question has no comments.",
	"nuq": "You have no permission to edit this question.",
	"nun": "You have no permission to edit this new.",
	"q": "Question: ",
	"mb": "Made by: ",
	"mb1": "Made by: ",
	"da": "Date: ",
	"news": "These are the available news: ",
	"nnews": "There are no available news",
	"title": "Insert the news title: ",
	"title1": "Title: ",
	"content": "Insert the news content: ",  # Apostrophe
	"author": "Insert the authors name",  # Apostrophe
	"aut": "Author: ",
	"label": "Insert the category: ",
	"la": "Label: ",
	"ncn": "This new has no comments.",
	"id": "id: ",
	"idin": "Insert the id: ",
	"iid": "Invalid id",
	"comment": "Type a comment: ",
	"nuc": "You have no permission to edit this comment.",
	"c": "Comment: ",
	"lks": "likes: ",
	"dlks": "dislikes: ",
	"l": "Users who like this: ",
	"dl": "Users who dislike this: ",
	"nls": "No one likes this.",
	"ndls": "No one dislikes this.",
	"fs": "Favorite saved.",
	"fhs": "The favorite has already been saved.",
	"nfq": "You have no favorite questions.",
	"nfc": "You have no favorite comments.",
	"nfn": "You have no favorite news.",
	"lo": "Come back soon",
	"np": "You have no permission to make this action",
	"ub": "Your user is currently banned, thus, you can not log in",
	"inub": "Insert the username who will be banned",
	"chd": "Channel deleted",
	"qd": "Question deleted",
	"cod": "Comment deleted",
	"nd": "New deleted",
	"aam": "This action has already been made, therefore, it cannot be done again",
	"ara": "This action requires action 4 to be made",
	"nusers": "There are no users", 
	"redirecting": "Redirecting you to the previous menu",
	"idmb": "The id must be an integer."
	}

	MS = {
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
