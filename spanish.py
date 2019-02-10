

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
		7. Reintegrar un usuario
		8. Eliminar mi cuenta
		9. Salir
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
	"pattemps":"""
		Ya has ingresado contraseñas 3 veces, ¿quieres intentarlo una vez mas?
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
	"maxattempts": "\t\tYa has tratado de ingresar 4 veces, te redireccionaremos al menu principal",
	"maxpattempts": "\t\tYa has escrito contraseñas 4 veces, te redireccionaremos al menu principal",
	"lastattempt": "\t\tUltimo intento antes de redireccionarte",
	"i": "\t\tLa opcion elegida es incorrecta, por favor elija otra opcion.",
	"keyword": "\t\tIngrese la palabra clave: ",
	"nomatch": "\t\tNo hay coincidencias para la(s) palabra(s) ingresadas.",
	"name": "\t\tIngrese su nombre: ",
	"nn": "\t\tIngrese el nuevo nombre",
	"n": "\t\tNombre: ",
	"username": "\t\tIngrese su nombre de usuario: ",
	"nu": "\t\tIngrese el nuevo nombre de usuario: ",
	"un": "\t\tUsuario: ",
	"una": "\t\tEl usuario ya se encuentra registrado.",
	"email": "\t\tIngrese su correo: ",
	"email2": "\t\tConfirme su correo: ",
	"ne": "\t\tIngrese el nuevo correo: ",
	"e": "\t\tEmail: ",
	"ea": "\t\tEl email ya se encuentra registrado.",
	"edm": "\t\tLos correos no coinciden.",
	"password": "\t\tIngrese su contraseña: ",
	"password2": "\t\tConfirme su contraseña:",
	"oldpassword": "\t\tIngrese su última contraseña: ",
	"np": "\t\tIngrese la nueva contraseña: ",
	"pdm": "\t\tLas contraseñas no coinciden.",
	"wp": "\t\tContraseña incorrecta.",
	"wu": "\t\tNombre de usuario incorrecto",
	"uc": "\t\tEl usuario ha sido creado.",
	"iu": "\t\tEl usuario no existe.",
	"channel": "\t\tIngrese el tema del canal: ",
	"channels": "\t\tEstos son los canales disponibles: ",
	"nchannels": "\t\tNo hay canales disponibles",
	"nquestions": "\t\tNo hay preguntas disponibles",
	"ncomments": "\t\tNo hay commentarios disponibles",
	"ic": "\t\tEl canal no existe",
	"chs": "\t\tCanales: ",
	"nq": "\t\tEste canal no tiene preguntas",
	"topic": "\t\tTema: ",
	"de": "\t\tDescripción: ",
	"question": "\t\tEscriba una pregunta: ",
	"ncq": "\t\tEsta pregunta no tiene comentarios.", 
	"nuq": "\t\tNo tienes permisos para editar esta pregunta.", 
	"nun": "\t\tNo tienes permisos para editar esta noticia.",
	"q": "\t\tPregunta: ",
	"mb": "\t\tHecha por: ",
	"mb1": "\t\tHecho por: ",
	"da": "\t\tFecha: ",
	"news": "\t\testas son las noticias disponibles",
	"News": "\t\tNEWS",
	"nnews": "\t\tNo hay noticias disponibles",
	"title": "\t\tIngrese el titulo de la noticia: ",
	"title1": "\t\tTítulo: ",
	"content": "\t\tIngrese el contenido de la noticia: ",
	"author": "\t\tIngrese el nombre del author", 
	"aut": "\t\tAutor: ",
	"label": "\t\tIngrese la categoría: ",
	"ncn": "\t\tEsta noticia no tiene comentarios.",
	"id": "\t\tid: ",
	"idin": "\t\tIngrese the id: ",
	"iid": "\t\tid invalido",
	"la": "\t\tCategoría: ",
	"comment": "\t\tEscriba un comentario: ",
	"nuc": "\t\tNo tienes permisos para editar este comentario.",
	"c": "\t\tComentario: ",
	"lks": "\t\tme gusta: ",
	"dlks": "\t\tno me gusta: ",
	"l": "\t\tUsuarios a los que les gusta esto: ",
	"dl": "\t\tUsuarios a los que les disgusta esto: ",
	"nls": "\t\tA nadie le gusta esto",
	"ndls": "\t\tA nadie le disgusta esto",
	"fs": "\t\tFavorito guardado.",
	"fhs": "\t\tEl favorito ya ha sido guardado.",
	"nfq": "\t\tNo tienes preguntas favoritas.",
	"nfc": "\t\tNo tienes comentarios favoritos.",
	"nfn": "\t\tNo tienes noticias favoritas.",
	"lo": "\t\tRegresa pronto.",
	"np": "\t\tNo tienes permiso para realizar esta acción",
	"ub": "\t\tTu usuario actualmente está excluido, por lo tanto, no puedes ingresar",
	"ub1": "\t\tUsuario expulsado",
	"unub": "\t\tUsuario reintegrado",
	"inub": "\t\tIngresa el usuario que será expulsado",
	"inunb": "\t\tIngresa el usuario que será reintegrado",
	"chd": "\t\tCanal eliminado",
	"qd": "\t\tPregunta eliminada",
	"cod": "\t\tComentario eliminado",
	"nd": "\t\tnoticia eliminada",
	"aam": "\t\tEsta acción ya se ha realizado una vez, por lo tanto, no se puede realizar de nuevo",
	"ara": "\t\tEsta acción requiere que la acción 4 sea realizada",
	"nusers": "\t\tNo hay usuarios",
	"redirecting": "\t\tRedireccionandote al menu anterior",
	"idmb": "\t\tEl id debe ser un número entero.", 
	"inputtabs": "\t\t",
	"uab": "\t\tEl usuario ya está expulsado.",
	"unb": "\t\tEste usuario no está expulsado.",
	"proupd": "\t\tPerfil actualizado",
	"usupd": "\t\tNombre de usuario actualizado",
	"nupd": "\t\tNombre actualizado",
	"pupd": "\t\tContraseña actualizada",
	"eupd": "\t\tCorreo actualizado",
	"newupd": "\t\tNoticia actualizada",
	"titleupd": "\t\tTitulo actualizado",
	"contentupd": "\t\tContenido actualizado",
	"authorupd": "\t\tAuthor actualizado",
	"labelupd": "\t\tCategoría actualizada",
	"questionupd": "\t\tPregunta actualizada",
	"commentupd": "\t\tComentario actualizado",
	}
