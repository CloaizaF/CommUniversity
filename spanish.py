

class Spanish:


	spanish = {
	"welcome":"""
		 ------------------------------------------------------------------------------
		 ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
		 ||||||||||||||||||||||||| BIENVENIDO A COMMUNIVERSITY ||||||||||||||||||||||||
		 ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
		 ------------------------------------------------------------------------------""",
	"mm": 
	"""\t\t1. Registrarse.
		2. Ingresar.
		3. Generar datos ficticios.
		4. Generar datos ficticios desde un txt.
		5. Guardar usuarios generados.
		$. Salir.
	    """,
	"usero": 
	"""\t\t¿Que quieres hacer?
			1. Revisar mi perfil.
			2. Actualizar my perfil.
			3. Revisar un canal.
			4. Leer algunas noticias.
			5. Revisar mis favoritos.
			6. Expulsar un usuario.
			7. Reintegrar un usuario.
			8. Eliminar mi cuenta.
			9. Salir.
		""",
	"favo": 
	"""\t\t¿Que quieres hacer?
			1. Leer mis preguntas favoritas.
			2. Leer mis comentarios favoritos.
			3. Leer mis noticias favoritas.
			@. Ir al menu anterior.
		""",
	"updateo": 
	"""\t\t¿Que modificaras?
			1. Todo en mi perfil.
			2. Solo mi nombre.
			3. Solo mi nombre de usuario.
			4. Solo mi correo.
			5. Solo mi contrasena.
			@. Ir al menu anterior.
		""",
	"channelo": 
	"""\t\t¿Que quieres hacer?
			1. Buscar una pregunta.
			2. Hacer una pregunta.
			3. Leer algunas preguntas.
			4. Ver el top de preguntas.
			5. Eliminar este canal.
			@. Ir al menu anterior.
		""",
	"selectq":
	"""\t\t1. Seleccionar una pregunta para desplegar mas opciones. 
		@. Ir al menu anterior.
		""",
	"questiono": 
	"""\t\t¿Que quieres hacer?
			1. Responder la pregunta.
			2. Leer sus comentarios.
			3. Darle me gusta.
			4. Darle no me gusta.
			5. Ver sus me gusta.
			6. Ver sus no me gusta.
			7. Guardar esta pregunta.
			8. Editar esta pregunta.
			9. Eliminar esta pregunta.
			@. Ir al menu anterior.
		""",
	"selectc":
	"""\t\t1. Seleccionar un comentario para ver mas opciones.
		@. Ir al menu anterior.
		""",
	"commento": 
	"""\t\t¿Que quieres hacer?
			1. Darle me gusta.
			2. Darle no me gusta.
			3. Ver sus me gusta.
			4. Ver sus no me gusta. 
			5. Guardar este comentario.
			6. Editar este comentario.
			7. Eliminar este comentario.
			@. Ir al menu anterior.
		""",
	"selectn":
	"""\t\t1. Subir una noticia.
		2. Selecciona una noticia para ver mas opciones.
		3. Ver el top de noticias.
		@. Ir al menu anterior.
		""",
	"newo": 
	"""\t\t¿Que quieres hacer?
			1. Comentar.
			2. Leer sus comentarios.
			3. Darle me gusta.
			4. Darle no me gusta.
			5. Ver sus me gusta.
			6. Ver sus no me gusta.
			7. Guardar esta noticia.
			8. Editar esta noticia.
			9. Eliminar esta noticia.
			@. Ir al menu anterior.
		""",
	"editnew": 
	"""\t\t¿Que quieres editar de esta noticia?
			1. Todo en esta noticia.
			2. Solo su titulo.
			3. Solo su contenido.
			4. Solo su autor.
			5. Solo su categoria.
			@. Ir al menu anterior.
		""",
	"needo": 
	"""\t\tLos operadores sirven para enlazar palabras claves en una busqueda:
	    	Y: Hace obligatoria la ocurrencia de las dos palabras claves ingresadas.
	    	O: Hace obligatoria UNA ocurrencia de las dos palabras claves ingresadas.
	    	NO: Excluye las ocurrencias de las palabras claves ingresadas.

	    ¿Necesitas utilizar algun operador(Y,O,NO)?:
		    1. Si, lo necesito.
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
			1. Si.
			2. No.
		""",
	"pattemps":
	"""\t\tYa has ingresado contrasenas 3 veces, ¿quieres intentarlo una vez mas?
			1. Si.
			2. No.
		""",
	"sure": """
		Estas segur@ de que quieres eliminar tu cuenta?
			1. Si, quiero eliminar mi cuenta.
			2. No, no quiero eliminar mi cuenta.
		""",
	"sorto": 
	"""\t\t¿Quieres ordenar los canales?
			1. Si.
			2. No.
		""",
	"sortby":
	"""\n\t\tOrdenar los canales por:
			1. El numero de visitas del canal.
			2. El numero de preguntas del canal.
		""",
	"gbp": "\t\t@. Ir al menu anterior.\n",
	"maxattempts": "\n\t\tYa has tratado de ingresar 4 veces, te redireccionaremos al menu principal.",
	"maxpattempts": "\n\t\tYa has escrito contrasenas 4 veces, te redireccionaremos al menu principal.",
	"lastattempt": "\n\t\tUltimo intento antes de redireccionarte.",
	"i": "\n\t\tLa opcion elegida es incorrecta, por favor elija otra opcion.",
	"keyword": "\t\tIngrese la palabra clave: ",
	"nomatch": "\n\t\tNo hay coincidencias para la(s) palabra(s) ingresadas.\n",
	"name": "\t\tIngrese su nombre: ",
	"nn": "\t\tIngrese el nuevo nombre: ",
	"n": "\t\tNombre: ",
	"username": "\t\tIngrese su nombre de usuario: ",
	"nu": "\t\tIngrese el nuevo nombre de usuario: ",
	"un": "\t\tUsuario: ",
	"una": "\t\tEl usuario ya se encuentra registrado.",
	"ue": "\n\t\tSu cuenta ha sido eliminada.",
	"email": "\t\tIngrese su correo: ",
	"email2": "\t\tConfirme su correo: ",
	"ne": "\t\tIngrese el nuevo correo: ",
	"e": "\t\tEmail: ",
	"ea": "\t\tEl email ya se encuentra registrado.",
	"edm": "\t\tLos correos no coinciden.",
	"password": "\t\tIngrese su contrasena: ",
	"password2": "\t\tConfirme su contrasena:",
	"oldpassword": "\t\tIngrese su ultima contrasena: ",
	"np": "\t\tIngrese la nueva contrasena: ",
	"pdm": "\t\tLas contrasenas no coinciden.",
	"wp": "\t\tContrasena incorrecta.",
	"wu": "\t\tNombre de usuario incorrecto.",
	"uc": "\t\tEl usuario ha sido creado.",
	"iu": "\t\tEl usuario no existe.",
	"channel": "\n\t\tIngrese el tema del canal: ",
	"channels": "\n\t\tEstos son los canales disponibles:",
	"nchannels": "\n\t\tNo hay canales disponibles.",
	"nquestions": "\t\tNo hay preguntas disponibles.",
	"ncomments": "\t\tNo hay commentarios disponibles.",
	"ic": "\n\t\tEl canal no existe.",
	"cs": "\t\tCanal seleccionado: ",
	"cms": "\t\tComentario seleccionado: ",
	"ps": "\t\tPregunta seleccionada: ",
	"ns": "\t\tNoticia seleccionada: ",
	"chs": "\t\tCanales: ",
	"nq": "\n\t\tEste canal no tiene preguntas.",
	"topic": "\t\tTema: ",
	"de": "\t\tDescripcion: ",
	"question": "\n\t\tEscriba una pregunta: ",
	"ncq": "\n\t\tEsta pregunta no tiene comentarios.", 
	"nuq": "\n\t\tNo tienes permisos para editar esta pregunta.", 
	"nun": "\n\t\tNo tienes permisos para editar esta noticia.",
	"q": "\t\tPregunta: ",
	"qs": "\t\tPreguntas: ",
	"mb": "\t\tHecha por: ",
	"mb1": "\t\tHecho por: ",
	"topq": "\t\tTop Preguntas: ",
	"topn": "\t\tTop Noticias: ",
	"da": "\t\tFecha: ",
	"news": "\t\tEstas son las noticias disponibles: ",
	"News": "\t\tNoticias.",
	"nnews": "\n\t\tNo hay noticias disponibles.",
	"title": "\t\tIngrese el titulo de la noticia: ",
	"title1": "\t\tTitulo: ",
	"content": "\t\tIngrese el contenido de la noticia: ",
	"author": "\t\tIngrese el nombre del author.", 
	"aut": "\t\tAutor: ",
	"label": "\t\tIngrese la categoria: ",
	"ncn": "\n\t\tEsta noticia no tiene comentarios.",
	"id": "\t\tid: ",
	"idin": "\n\t\tIngrese el id: ",
	"iid": "\t\tid invalido",
	"la": "\t\tCategoria: ",
	"comment": "\t\tEscriba un comentario: ",
	"nuc": "\n\t\tNo tienes permisos para editar este comentario.",
	"c": "\t\tComentario: ",
	"coms": "\t\tComentarios: ",
	"comse": "\t\tComentario seleccionado: ",
	"lks": "\t\tme gusta: ",
	"dlks": "\t\tno me gusta: ",
	"l": "\n\t\tUsuarios a los que les gusta esto: ",
	"dl": "\n\t\tUsuarios a los que les disgusta esto: ",
	"nls": "\t\tA nadie le gusta esto.",
	"ndls": "\t\tA nadie le disgusta esto.",
	"fs": "\n\t\tFavorito guardado.",
	"fhs": "\n\t\tEl favorito ya ha sido guardado.",
	"nfq": "\t\tNo tienes preguntas favoritas.",
	"nfc": "\t\tNo tienes comentarios favoritos.",
	"nfn": "\t\tNo tienes noticias favoritas.",
	"fq": "\t\tPreguntas favoritas: ",
	"fc": "\t\tComentrios favoritos: ",
	"fn": "\t\tNoticias favoritas: ",
	"np": "\n\t\tNo tienes permiso para realizar esta accion.",
	"ub": "\n\t\tTu usuario actualmente esta excluido, por lo tanto, no puedes ingresar.",
	"ub1": "\n\t\tUsuario expulsado.",
	"unub": "\n\t\tUsuario reintegrado.",
	"inub": "\n\t\tIngresa el usuario que sera expulsado.",
	"inunb": "\n\t\tIngresa el usuario que sera reintegrado.",
	"chd": "\n\t\tCanal eliminado.",
	"qd": "\n\t\tPregunta eliminada.",
	"cod": "\n\t\tComentario eliminado.",
	"nd": "\n\t\tNoticia eliminada.",
	"aam": "\n\t\tEsta accion ya se ha realizado una vez, por lo tanto, no se puede realizar de nuevo.",
	"ara": "\n\t\tEsta accion requiere que la accion 4 sea realizada.",
	"nusers": "\t\tNo hay usuarios.",
	"redirecting": "\n\t\tRedireccionandote al menu anterior.",
	"idmb": "\n\t\tEl id debe ser un numero entero.", 
	"inputtabs": "\t\t",
	"sl": "\n",
	"uab": "\n\t\tEl usuario ya esta expulsado.",
	"unb": "\n\t\tEste usuario no esta expulsado.",
	"proupd": "\n\t\tPerfil actualizado.",
	"usupd": "\n\t\tNombre de usuario actualizado.",
	"nupd": "\n\t\tNombre actualizado.",
	"pupd": "\n\t\tContrasena actualizada.",
	"eupd": "\n\t\tCorreo actualizado.",
	"newupd": "\n\t\tNoticia actualizada.",
	"titleupd": "\n\t\tTitulo actualizado.",
	"contentupd": "\n\t\tContenido actualizado.",
	"authorupd": "\n\t\tAuthor actualizado.",
	"labelupd": "\n\t\tCategoria actualizada.",
	"questionupd": "\n\t\tPregunta actualizada.",
	"commentupd": "\n\t\tComentario actualizado.",
	"separator": "\n\t\t--------------------------------------------------------------------------------\n",
	"bye": "\n\t\t---------------------------------Regresa pronto---------------------------------",
	"separator1" :"\n\t\t|||||||||||||||||||||||||||||||||CommUniversity|||||||||||||||||||||||||||||||||\n"
	}