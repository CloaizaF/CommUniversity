from user import User
from admin import Admin
from channel import Channel
from question import Question
from comment import Comment
from new import New
from rating import Rating
from message import Message
import os
import random


class Client:


	@staticmethod
	def in_name(language):
		"""Asks the user for a name and returns it. 

		Args:
            language (dict): The language in which the information will be given.

        Returns:
            str: The user's name.
		"""
		print(language.get("name"))
		name = input()
		return name

	@staticmethod
	def in_username(language):
		"""Asks the user for a username, verifies if it's valid and returns it if true,
		otherwise, invokes itself to get valid input. 

		Args:
            language (dict): The language in which the information will be given.

        Returns:
            str: The user's username.
		"""
		print(language.get("username"))
		username = input()
		for usernamek in User.users:
			if username == usernamek:
				print(language.get("una"))
				return Client.in_username(language)
		return username

	@staticmethod
	def in_email(language):
		"""Asks the user for an email, verifies if it's valid and returns it if true,
		otherwise, invokes itself to get valid input. 

		Args:
            language (dict): The language in which the information will be given.

        Returns:
            str: The user's email.
        """
		print(language.get("email"))
		email = input()
		print(language.get("email2"))
		email2 = input()
		if email != email2:
			print(language.get("edm"))
			return Client.in_email(language)
		for usernamek in User.users:
			if email == (User.users[usernamek]).get_email():
				print(language.get("ea"))
				return Client.in_email(language)
		return email

	@staticmethod
	def in_password(language):
		"""Asks the user for a password, verifies if it's valid and returns it if true,
		otherwise, invokes itself to get valid input. 

		Args:
            language (dict): The language in which the information will be given.

        Returns:
            str: The user's password.
        """
		print(language.get("password"))
		password = input()
		print(language.get("password2"))
		password2 = input()
		if(password != password2):
			print(language.get("pdm"))
			return Client.in_password(language)
		return password
	
	@staticmethod
	def sign_in(language):
		"""Invokes Client.in_name(), Client.in_username(), Client.in_email(), 
		Client.in_password() to get a valid input for creating a user, creates it 
		and returns it.

		Args:
            language (dict): The language in which the information will be given.

        Returns:
            User: The created user object.
		"""
		name = Client.in_name(language)
		username = Client.in_username(language)
		email = Client.in_email(language)
		password = Client.in_password(language)
		user = User(name, username, email, password)
		return user

	@staticmethod
	def log_in(language):
		"""Makes the required verifications for a user to log in and then, if the user
		passes the verifications, allows him/her to log in.

		Args:
			language (dict): The language in which the information will be given.
		"""
		break_while = 0
		EXIT = 1
		attempts = 0
		while break_while != EXIT:
			print(language.get("username"))
			username = input()
			u = None
			for usernamek in User.users:
				if username == usernamek:
					u = User.users.get(usernamek)
			if isinstance(u, User):
				print(language.get("password"))
				password = input()
				passwordv = u.get_password()
				break_while1 = 0
				pattempts = 1
				while break_while1 != EXIT:
					if password != passwordv:
						print(language.get("wp"))
						print(language.get("password"))
						password = input()
						pattempts += 1
						if pattempts == 3:
							break_while2 = 0
							while break_while2 != EXIT:
								print(language.get("attempts"))
								opt = input()
								if opt == "1":
									print(language.get("lastattempt"))
									break_while2 = EXIT
								elif opt == "2":
									break_while2 = EXIT
									break_while1 = EXIT
									break_while = EXIT
									u = None
								else: 
									print(language.get("i"))
						elif pattempts == 4:
							print(language.get("maxattempts"))
							break_while1 = EXIT
							break_while = EXIT
							u = None
					else:
						break_while1 = EXIT
				if isinstance(u, User):
					if u.get_ban_state() == 0:
						break_while = EXIT
					else:
						print(language.get("ub"))
						attempts += 1
			else:
				print(language.get("iu"))
				attempts += 1

			if attempts == 3:
				w1 = 0
				while w1 == 0:
					print(language.get("attempts"))
					opt = input()
					if opt == "1":
						print(language.get("lastattempt"))
						w1 = 1
					elif opt == "2":
						w1 = 1
						break_while = EXIT
					else: 
						print(language.get("i"))
			elif attempts == 4:
				print(language.get("maxattempts"))
				break_while = EXIT
		return u

	@staticmethod
	def in_user(language):
		"""Asks for a username and returns the user if the user's username exists.

		Args:
			language (dict): The language in which the information will be given.

		Returns:
			object: A User object if the username exists, otherwise, None.
		"""
		print(language.get("inub"))
		username = input()
		user_returned = None
		for username_key in User.users:
			if username_key == username:
				user_returned = User.users[username_key]
		return user_returned

	@staticmethod
	def is_user_password(user, language):
		"""Asks the user for his/her last password and checks if it is the true 
		password.

		Args:
			user (User): The user whose password will be checked
			language (dict): The language in which the information will be given.

		Returns:
			bool: True if the password inserted is the user's password. Otherwise, 
				False.
		"""
		print(language.get("oldpassword"))
		password = input()
		true_password = user.get_password()
		break_while = 0
		EXIT = 1
		pattempts = 1
		while break_while != EXIT:
			if password != true_password:
				print(language.get("wp"))
				print(language.get("oldpassword"))
				password = input()
				pattempts += 1
				if pattempts == 3:
					break_while1 = 0
					while break_while1 != EXIT:
						print(language.get("attempts"))
						opt = input()
						if opt == "1":
							print(language.get("lastattempt"))
							break_while1 = EXIT
						elif opt == "2":
							break_while1 = EXIT
							break_while = EXIT
						else: 
							print(language.get("i"))
				elif pattempts == 4:
					print(language.get("maxattempts"))
					break_while1 = EXIT
					break_while = EXIT
			else:
				break_while = EXIT
				return True
		return False

	@staticmethod 
	def in_id(language, ch_q_n=None):
		"""Allows the user to insert an id to get a question, new or comment and 
		returns the respective object.

		Args:
			language (dict): The language in which the information will be given.
			ch_q_n (Channel/Question/New): The object in which the another object (the 
					one gotten with the id) will be looked for.

		Returns:
			object : A Question object if the user is looking for a question, a 
			Comment object if the user is looking for a comment, a New object if the
			user is looking for a new.
		"""
		try:
			print(language.get("idin"))
			id_inserted = int(input())  
			if isinstance(ch_q_n, Channel):
				question_returned = None
				for question in ch_q_n.get_questions():   
					if id_inserted == question.get_id():
						question_returned = question
				if isinstance(question_returned, Question):
					return question_returned
				else:
					print(language.get("iid"))
					return Client.in_id(language, ch_q_n)
			elif isinstance(ch_q_n, Question) or isinstance(ch_q_n, New):
				comment_returned = None
				for comment in ch_q_n.get_comments():  
					if id_inserted == comment.get_id():
						comment_returned = comment
				if isinstance(comment_returned, Comment):
					return comment_returned
				else:
					print(language.get("iid"))
					return Client.in_id(language, ch_q_n)
			else:
				new_returned = None
				for new in New.news:
					if id_inserted == (New.news[new]).get_id():  
						new_returned = New.news[new]
				if isinstance(new_returned, New):
					return new_returned
				else:
					print(language.get("iid"))
					return Client.in_id(language)
		except ValueError:
			print(language.get("idmb"))
			return Client.in_id(language, ch_q_n)

	@staticmethod
	def in_channel(language):
		"""Asks the user for a channel, verifies if it's exists and returns it if true,
		otherwise, invokes itself to get valid input. 

		Args:
            language (dict): The language in which the information will be given.

        Returns:
            str: The channel that the user chose.
        """
		print(language.get("channel"))
		channel = input()
		channelr = None
		if channel in Channel.channels:
			channelr = Channel.channels[channel]
		if isinstance(channelr, Channel):
			return channelr
		else: 
			print(language.get("ic"))
			return Client.in_channel(language)

	@staticmethod
	def show_channels(language):
		"""If the dict Channel.channels has channels, allows the user to sort and show
		their information, otherwise, if the dict is empty, shows that there are no 
		channels. 
		Args:
            language (dict): The language in which the information will be given.

        Returns:
            str: The channels' names if they exist. Otherwise, shows there are none.
        """
		if len(Channel.channels):
			break_while = 0
			EXIT = 1
			while break_while != EXIT:
				print(language.get("sorto"))
				option = input()
				if option == "1":
					break_while1 = 0
					while break_while1 != EXIT:
						print(language.get("sortby"))
						option1 = input()
						sorted_channels = None
						if option1 == "1":
							sorted_channels = sorted((Channel.channels).values(), key=lambda channel: channel.get_visits(), reverse=True)
						elif option1 == "2":
							sorted_channels = sorted((Channel.channels).values(), key=lambda channel: len(channel.get_questions()), reverse=True)
						else:
							print(language.get("i"))

						if sorted_channels != None:
							print(language.get("channels"))
							for channel in sorted_channels:
								print(channel.to_string(language))
							break_while = EXIT
							break_while1 = EXIT
				elif option == "2":
					print(language.get("channels"))
					for channel in Channel.channels:
						print(Channel.channels[channel].to_string(language))
					break_while = EXIT
				else:
					print(language.get("i"))
		else:
			print(language.get("nchannels"))

	@staticmethod
	def make_a_question(language, user, channel):
		"""Asks the user for a description to create a question, creates it and 
		returns it.

		Args:
            language (dict): The language in which the information will be given.
            user (User): The user that creates the questions.
            channel (Channel): The channel where the question will be created.

        Returns:
            Question: The created question.
		"""
		print(language.get("question"))
		description = input()
		question = Question(user, channel, description)
		return question

	@staticmethod
	def edit_question(language, question, user):
		"""Verifies if the user that wants to edit the question is the same that 
		created it and if it is true, allows him/her to perform the action.

		Args:
            language (dict): The language in which the information will be given.
            user (User): The user that creates the questions.
            question (Question): The question that will be edited.

		"""
		if question.check_user(user):
			print(language.get("question"))
			q = input()
			question.set_question(q)
		else:
			print(language.get("nuq"))

	@staticmethod
	def search_question(language, channel):
		"""Allows the user to search for a question based in the logic operators
		AND, OR and NOT and one or two keywords, depending on the user's choice.

		Args:
			language (dict): The language in which the information will be given.
			channel (Channel): The channel where the question will be searched.

		Returns:
			str: The information of the questions that match the search.
		"""
		break_while = 0
		EXIT = 1
		while break_while != EXIT:
			print(language.get("needo"))
			opt = input()
			if opt == "1":
				print(language.get("keyword"))
				keyword1 = input()
				print(language.get("keyword"))
				keyword2 = input()
				printing = ""
				print(language.get("selecto"))
				op = input()
				if op == "1":
					for question in channel.get_questions():
						if (keyword1 in question.get_question()) and (keyword2 in question.get_question()):
							printing += question.to_string(language)
				elif op == "2":
					for question in channel.get_questions():
						if (keyword1 in question.get_question()) or (keyword2 in question.get_question()):
							printing += question.to_string(language)
				elif op == "3":
					for question in channel.get_questions():
						if not ((keyword1 in question.get_question()) and (keyword2 in question.get_question())):
							printing += question.to_string(language)
				else:
					print(language.get("i"))
				if len(printing):
					print(printing)
				else:
					print(language.get("nomatch"))
				break_while = EXIT
			elif opt == "2":
				print(language.get("keyword"))
				keyword1 = input()
				printing = ""
				for question in channel.get_questions():
					if keyword1 in question.get_question():
						printing += question.to_string(language)
				if len(printing):
					print(printing)
				else:
					print(language.get("nomatch"))
				break_while = EXIT
			else:
				print(language.get("i"))

	@staticmethod
	def show_news(language):
		"""If the dict New.news has news, shows their information, otherwise,
		shows that there are no news. 
		Args:
            language (dict): The language in which the information will be given.

        Returns:
            str: The news' information if they exist. Otherwise, shows there are none.
        """
		if len(New.news):
			print(language.get("news"))
			for new in New.news:
				print(language.get("title1") + str((New.news[new]).get_title()) + "\n" 
				+ language.get("id") + str((New.news[new]).get_id()))
		else:
			print(language.get("nnews")) 

	@staticmethod
	def top_news(language):
		"""Sorts the New.news dictionary by the news' views and gets the first 
		10 items to create a top.

		Args:
			language (dict): The language in which the information will be given.

		Returns:
			str: Top of news.
		"""
		printing = ""
		sorted_dict  = sorted(New.news, key=lambda new: New.news[new].get_views(), reverse=True)
		top_dict = sorted_dict[:10]
		for new in top_dict:
			printing += New.news[new].to_string(language)
		return printing

	@staticmethod
	def upload_a_new(language, admin):
		"""Asks the admin for the title, content, author and label to create a comment,
		creates it and returns it.

		Args:
            language (dict): The language in which the information will be given.
            admin (Admin): The admin that creates the questions.

        Returns:
            New: The created new.
		"""
		print(language.get("title"))
		title = input()
		print(language.get("content"))
		content = input()
		print(language.get("author"))
		author = input()
		print(language.get("label"))
		label = input()
		new = New(admin, title, content, author, label)
		return new 

	@staticmethod
	def edit_new(language, new, admin):
		"""Verifies if the admin that wants to edit the question is the same that 
		created it and if it is true, allows him/her to perform the action.

		Args:
            language (dict): The language in which the information will be given.
            admin (Admin): The admin that creates the questions.
            new (New): The new that will be edited.

		"""
		if new.check_user(admin):
			break_while = 0
			EXIT = 1
			while break_while != EXIT:
				print(language.get("editnew"))
				opt = input()
				if opt == "1":
					print(language.get("title"))
					title = input()
					new.set_title(title)
					print(language.get("content"))
					content = input()
					new.set_content(content)
					print(language.get("author"))
					author = input()
					new.set_author(author)
					print(language.get("label"))
					label = input()
					new.set_label(label)
					break_while = EXIT
				elif opt == "2":
					print(language.get("title"))
					title = input()
					new.set_title(title)
					break_while = EXIT
				elif opt == "3":
					print(language.get("content"))
					content = input()
					new.set_content(content)
					break_while = EXIT
				elif opt == "4":
					print(language.get("author"))
					author = input()
					new.set_author(author)
					break_while = EXIT
				elif opt == "5":
					print(language.get("label"))
					label = input()
					new.set_label(label)
					break_while = EXIT
				else:
					print(language.get("i"))
		else:
			print(language.get("nun"))

	@staticmethod
	def comment(language, user, q_n):
		"""Asks the user for a description to create a comment, creates it and 
		returns it.

		Args:
            language (dict): The language in which the information will be given.
            user (User): The user that creates the questions.
            q_n (Question/New): The question/new where the comment will be created.

        Returns:
            Comment: The created comment.
		"""
		print(language.get("comment"))
		description = input()
		comment = Comment(user, q_n, description)
		return comment

	@staticmethod
	def edit_comment(language, comment, user):
		"""Verifies if the user that wants to edit the comment is the same that 
		created it and if it is true, allows him/her to perform the action.

		Args:
            language (dict): The language in which the information will be given.
            user (User): The user that creates the questions.
            comment (Comment): The comment that will be edited.

		"""
		if comment.check_user(user):
			print(language.get("comment"))
			c = input()
			comment.set_description(c)
		else:
			print(language.get("nuc"))

	@staticmethod
	def delete_favorite(q_c_n):
		"""Deletes the object from the favorite's corresponding list all of the users 
        that have it as one of their favorites.

        Args:
            q_c_n (Question/Comment/New) : An object to be deleted.
        """
		for username_key in User.users:
			if q_c_n.is_favorite(User.users[username_key]):
				(User.users[username_key].get_type_fav(q_c_n)).remove(q_c_n)

	@staticmethod
	def menu_user(user, language):
		"""Displays a menu that allows the user to interact with the user's options.

		Args:
			language (dict): The language in which the information will be given.
            user (User): The user that interacts with the user's options.

		"""
		break_while = 0
		EXIT = 1
		while break_while != EXIT:   #While n2
			print(language.get("usero"))
			option = input()
			if option == "1":
				print(user.to_string(language))
			elif option == "2":
				Client.menu_user_updates(user, language)
			elif option == "3":
				Client.menu_channel(user, language)
			elif option == "4":
				Client.menu_new(user, language)
			elif option == "5":
				Client.menu_favorites(user, language)
			elif option == "6":
				if isinstance(user, Admin):
					user_to_ban = Client.in_user(language)
					user_to_ban.set_ban_state(1)
				else:
					print(language.get("np"))
			elif option == "7":
				print(language.get("username"))
				username = input()
				if user.check_username(username):
					print(language.get("password"))
					password = input()
					if user.get_password() == password: 
						print(language.get("sure"))
						option1 = input()
						if option1 == "1":
							if isinstance(user, Admin):
								user.delete_admin()
							else:
								user.delete_user()
						elif option1 == "2":
							print(language.get("redirecting"))
						else:
							print(language.get("i"))
					else:
						print(language.get("wp"))
				else:
					print(language.get("wu"))
			elif option == "8":
				break_while = EXIT
			else:
				print(language.get("i"))

	@staticmethod
	def menu_user_updates(user, language):
		"""Displays a menu to interact with the user's updating options.

		Args:
			language (dict): The language in which the information will be given.
            user (User): The user that interacts with the updating options.

		"""
		break_while = 0
		EXIT = 1
		while break_while != EXIT:   #While n3
			print(language.get("updateo"))
			option = input()
			if option == "1":
				if Client.is_user_password(user, language):
					user.set_name(Client.in_name(language))
					user.set_username(Client.in_username(language))
					user.set_email(Client.in_email(language))
					user.set_password(Client.in_password(language))
				break_while = EXIT
			elif option == "2":	
				user.set_name(Client.in_name(language))
				break_while = EXIT
			elif option == "3":
				user.set_username(Client.in_username(language))
				break_while = EXIT
			elif option == "4":
				user.set_email(Client.in_email(language))
				break_while = EXIT
			elif option == "5":
				if Client.is_user_password(user, language):
					user.set_password(Client.in_password(language))
				break_while = EXIT
			elif option == "@":
				break_while = EXIT
			else:
				print(language.get("i"))

	@staticmethod
	def menu_channel(user, language):
		"""Displays a menu to interact with the channel(s).

		Args:
			language (dict): The language in which the information will be given.
            user (User): The user that interacts with the channel(s).

		"""
		Client.show_channels(language)
		if len(Channel.channels):
			channel = Client.in_channel(language)
			channel.increase_visits()
			break_while = 0
			EXIT = 1
			while break_while != EXIT:   #While n3
				print(channel.to_string(language))
				print(language.get("channelo"))
				option = input()
				if option == "1":
					if len(channel.get_questions()):
						Client.search_question(language, channel)  
						break_while1 = 0
						while break_while1 != EXIT:
							print(language.get("gbp"))
							option1 = input()
							if option1 == "@":
								break_while1 = EXIT
							else:
								print(language.get("i"))
					else: 
						print(language.get("nq"))
				elif option == "2":
					question = Client.make_a_question(language, user, channel)
					print(question.to_string(language))
				elif option == "3":
					if len(channel.get_questions()):
						Client.menu_question(user, channel, language)
					else:
						print(language.get("nq"))
				elif option == "4":
					if len(channel.get_questions()):
						print(channel.top_questions(language))
						break_while1 = 0
						while break_while1 != EXIT:
							print(language.get("gbp"))
							option1 = input()
							if option1 == "@":
								break_while1 = EXIT
							else:
								print(language.get("i"))
					else:
						print(language.get("nq"))
				elif option == "5":
					if isinstance(user, Admin):
						channel.delete_channel()
						print(language.get("chd"))
						break_while = EXIT
					else:
						print(language.get("np"))
				elif option == "@":
					break_while = EXIT
				else: 
					print(language.get("i"))

	@staticmethod
	def menu_question(user, channel, language):
		"""Displays a menu to interact with the question(s) of the given channel.

		Args:
			language (dict): The language in which the information will be given.
            channel (Channel): The question's channel.
            user (User): The user that interacts with the question(s).

		"""
		break_while = 0
		EXIT = 1
		while break_while != EXIT:
			print(channel.to_string1(language))
			print(language.get("selectq"))
			option = input()
			if option == "1":
				question = Client.in_id(language, channel)
				question.increase_views()
				break_while1 = 0
				while break_while1 != EXIT:
					print(question.to_string(language))
					print(language.get("questiono"))
					option1 = input()
					if option1 == "1":
						comment = Client.comment(language, user, question)
						print(comment.to_string(language))
					elif option1 == "2":
						if len(question.show_comments(language)): 
							Client.menu_comment(user, question, language)
						else:
							print(language.get("ncq"))
					elif option1 == "3":
							Rating(user, question, "like")
					elif option1 == "4":
							Rating(user, question, "dislike")
					elif option1 == "5":
							print(language.get("l"))
							print(question.watch_users_reactions(language, "like"))
					elif option1 == "6":
							print(language.get("dl"))
							print(question.watch_users_reactions(language, "dislike"))
					elif option1 == "7":
						if user.repeated_fav(question):
							print(language.get("fhs"))
						else:
							print(language.get("fs"))
					elif option1 == "8":
						Client.edit_question(language, question, user)
					elif option1 == "9":
						if question.check_user(user):
							question.delete_question()
							Client.delete_favorite(question)
							print(language.get("qd"))
						else:
							print(language.get("np"))
						break_while1 = EXIT
					elif option1 == "@":
						break_while1 = EXIT
					else:
						print(language.get("i"))
			elif option == "@":   #To go to the previous menu 
				break_while = EXIT
			else:
				print(language.get("i"))

	@staticmethod
	def menu_new(user, language):
		"""Displays a menu to interact with the new(s).

		Args:
			language (dict): The language in which the information will be given.
            user (User): The user that interacts with the new(s).

		"""
		break_while = 0
		EXIT = 1
		while break_while != EXIT:
			print(language.get("News"))
			print(language.get("selectn"))
			option = input()
			if option == "1":
				if isinstance(user, Admin):
					new = Client.upload_a_new(language, user)
				else:
					print(language.get("np"))
				break_while = EXIT
			elif option == "2":
				if len(New.news):
					Client.show_news(language)
					new = Client.in_id(language)
					new.increase_views()
					break_while1 = 0
					while break_while1 != EXIT:
						print(new.to_string(language))
						print(language.get("newo"))
						option1 = input()
						if option1 == "1":
							comment = Client.comment(language, user, new)
							print(comment.to_string(language))
						elif option1 == "2":
							if len(new.show_comments(language)): 
								Client.menu_comment(user, new, language)
							else:
								print(language.get("ncn"))
						elif option1 == "3":
							Rating(user, new, "like")
						elif option1 == "4":
							Rating(user, new, "dislike")
						elif option1 == "5":
							print(language.get("l"))
							print(new.watch_users_reactions(language, "like"))
						elif option1 == "6":
							print(language.get("dl"))
							print(new.watch_users_reactions(language, "dislike"))
						elif option1 == "7":
							if user.repeated_fav(new):
								print(language.get("fhs"))
							else:
								print(language.get("fs"))
						elif option1 == "8":
							Client.edit_new(language, new, user)
						elif option1 == "9":
							if new.check_user(user):
								new.delete_new()
								print(language.get("nd"))
							else:
								print(language.get("np"))
							break_while1 = EXIT
						elif option1 == "@":
							break_while1 = EXIT
						else:
							print(language.get("i"))
			elif option == "3":
				print(Client.top_news(language))
				break_while1 = 0
				EXIT = 1
				while break_while1 != EXIT:
					print(language.get("gbp"))
					option1 = input()
					if option1 == "@":
						break_while1 = EXIT
					else:
						print(language.get("i"))
			elif option == "@":
				break_while = EXIT
			else:
				print(language.get("i"))

	@staticmethod
	def menu_comment(user, q_n, language):
		"""Displays a menu to interact with the comment(s) of the given question/new.
		Args:
			language (dict): The language in which the information will be given.
            q_n (Question/New): The question/new's comment.
            user (User): The user that interacts with the comment(s).

		"""
		break_while = 0
		EXIT = 1
		while break_while != EXIT:
			print(q_n.to_string(language))
			print(q_n.show_comments(language))
			print(language.get("selectc"))
			option = input()
			if option == "1":
				comment = Client.in_id(language, q_n)
				break_while1 = 0
				while break_while1 != EXIT:
					print(comment.to_string(language))
					print(language.get("commento"))
					option1 = input()
					if option1 == "1":
						Rating(user, comment, "like")
					elif option1 == "2":
						Rating(user, comment, "dislike")
					elif option1 == "3":
						print(language.get("l"))
						print(comment.watch_users_reactions(language, "like"))
					elif option1 == "4":
						print(language.get("dl"))
						print(comment.watch_users_reactions(language, "dislike"))
					elif option1 == "5":
						if user.repeated_fav(comment):
							print(language.get("fhs"))
						else:
							print(language.get("fs"))
					elif option1 == "6":
						Client.edit_comment(language, comment, user)
					elif option1 == "7":
						if comment.check_user(user):
							comment.delete_comment()
							Client.delete_favorite(comment)
							print(language.get("cod"))
						else:
							print(language.get("np"))
						break_while1 = EXIT
					elif option1 == "@":   #To go to the previous menu 
						break_while1 = EXIT
					else:
						print(language.get("i"))
			elif option == "@":
					break_while = EXIT
			else: 
				print(language.get("i"))

	@staticmethod
	def menu_favorites(user, language):
		"""Displays a menu to interact with the user's favorite(s).

		Args:
			language (dict): The language in which the information will be given.
            user (User): The user that interacts with his/her favorite(s).

		"""
		break_while = 0
		EXIT = 1
		while break_while != EXIT:
			print(language.get("favo"))
			option = input()
			if option == "1":
				favorites = user.watch_fav(language, "question")
				if len(favorites):
					print(favorites)
				else: 
					print(language.get("nfq"))
			elif option == "2":
				favorites = user.watch_fav(language, "comment")
				if len(favorites):
					print(favorites)
				else: 
					print(language.get("nfc"))
			elif option == "3":
				favorites = user.watch_fav(language, "new")
				if len(favorites):
					print(favorites)
				else: 
					print(language.get("nfn"))
			elif option == "@":
				break_while = EXIT
			else:
				print(language.get("i"))

	@staticmethod
	def main():
		"""Displays the main menu for the person to interact with it."""
		language = Client.language()
		attempts_to_generate_data = True
		attempts_to_generate_datat = True
		while True: 
			print(language.get("mm"))
			option = input()	
			if option == "1":   
				user = Client.sign_in(language)
			elif option == "2":   
				user = Client.log_in(language)
				if isinstance(user, User):
					Client.menu_user(user, language)
			elif option == "3":
				if attempts_to_generate_datat:
					print(language.get("ara"))
				else:
					if attempts_to_generate_data:
						Client.generate_f_data()
						attempts_to_generate_data = False
					else:
						print(language.get("aam"))
			elif option == "4":
				if attempts_to_generate_datat:
					Client.generate_f_data_txt()
					attempts_to_generate_datat = False
				else:
					print(language.get("aam"))
			elif option == "5":
				if len(User.users):
					Client.save_changes_user()
				else:
					print(language.get("nusers"))
			elif option == "$":
				break
			else:
				print(language.get("i"))
		os._exit(0)

	@staticmethod
	def generate_f_data():
		"""Generates fictional data to load the program."""
		ch = Channel("Life","This channel is made to talk about life")
		ch2 = Channel("None", "none")
		u = User.users[random.choice(list(User.users.keys()))]
		u2 = User.users[random.choice(list(User.users.keys()))]
		while u == u2:
			u2 = User.users[random.choice(list(User.users.keys()))]
		a = Admin("Valentina", "Vvasquez", "Vvasquez@gmail.com", "V123")
		q = Question(u, ch, "What is life?")
		c = Comment(u2, q, "That is; in fact, a hard question, what would it be?")
		r = Rating(u2, q, "like")
		r1 = Rating(a, c, "dislike")
		q2 = Question(u2, ch, "What is love?")
		c2 = Comment(u, q2, "The affection you feel for someone; or even, something.")
		r2 = Rating(a, q2, "dislike")
		q3 = Question(a, ch, "What is Death?")
		n = New(a, "The hollow has come!", "That witch has taken my daughthers body.", "Niklaus.", "Drama")

	@staticmethod
	def generate_f_data_txt():
		"""Generates fictional data from a file called user.txt, to load the program 
		with users.
		"""
		file = open("user.txt", "r")
		readfile = file.read()
		name_f = "Name: "
		semicolon = "; "
		username_f = "Username: "
		email_f = "Email: "
		password_f = "Password: "
		index_n = readfile.find(name_f)

		while index_n >= 0:
			index_s = readfile.find(semicolon, index_n)
			index_u = readfile.find(username_f, index_s)
			index_s1 = readfile.find(semicolon, index_u)
			index_e = readfile.find(email_f, index_s1)
			index_s2 = readfile.find(semicolon, index_e)
			index_p = readfile.find(password_f, index_s2)
			index_s3 = readfile.find(semicolon, index_p)

			name = readfile[index_n+6:index_s]
			username = readfile[index_u+10:index_s1]
			email = readfile[index_e+7:index_s2]
			password = readfile[index_p+10:index_s3]

			user = User(name, username, email, password)
			index_n = readfile.find(name_f, index_s3)
		file.close()

	@staticmethod
	def save_changes_user():
		"""Saves the changes generated to the users, and the dict User.users in a 
		file called user.txt.
		"""
		file = open("user.txt", "w")
		file.seek(0)
		file.truncate()
		for usernamek in User.users:
			user = User.users[usernamek]
			file.write("Name: " + user.get_name() + "; Username: " + user.get_username()
						+ "; Email: " + user.get_email() + "; Password: " + user.get_password() + "; "
						)
		file.close()

	@staticmethod
	def language():
		"""Allows a person to select a language for the program.

		Returns:
			dict: The language in which the information will be given.

		"""
		print(Message.MD.get("languages"))
		option = input()
		if option == "1":
			language = Message.ME
		elif option == "2" :
			language = Message.MS
		else:
			print(Message.MD.get("i"))
			return Client.language()
		return language

if __name__ == '__main__':
	Client.main()