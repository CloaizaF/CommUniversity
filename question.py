from datetime import date


class Question:


	def __init__(self, user, channel, question):
		""" Attributes:
		    self._user
		    self._channel
			self._question
			self._idq
			self._date
			self._comments
			self._num_of_comments
			self._ratings
			self._views
		"""
		self.set_user(user)
		self.set_channel(channel)
		self.set_question(question)
		self.set_id(channel.get_num_of_questions())
		self.set_date(date(2018, 10, 7).today())
		self._comments = []
		self.set_num_of_comments(0)
		self._ratings = {"likes": [], "dislikes": []}
		self.set_views(0)

	def set_user(self, user):
		"""Sets the question's user, appends the question to the user's questions list 
		and increases the number of questions the user has made.

		Args:
			user (User): user to be set.
		"""
		self._user = user
		user.get_questions().append(self)
		user.increase_num_of_questions()

	def set_channel(self, channel):
		"""Sets the question's channel, appends the question to the channel's questions
		list and increases the number of questions the channel has.

		Args:
			channel (Channel):_ channel to be set.
		"""
		self._channel = channel
		channel.get_questions().append(self)
		channel.increase_num_of_questions()

	def set_question(self, question):
		self._question = question

	def set_id(self, idq):
		self._id = idq

	def set_date(self, date):
		self._date = date

	def set_num_of_comments(self, num_of_comments):
		self._num_of_comments = num_of_comments

	def set_views(self, views):
		self._views = views

	def get_user(self):
		return self._user

	def get_channel(self):
		return self._channel

	def get_question(self):
		return self._question

	def get_id(self):
		return self._id

	def get_date(self):
		return self._date

	def get_comments(self):
		return self._comments

	def get_num_of_comments(self):
		return self._num_of_comments

	def get_views(self):
		return self._views

	def get_ratings(self):
		return self._ratings

	def get_likes(self):
		"""Returns the list of likes the question has."""
		return self.get_ratings()["likes"]

	def get_dislikes(self):
		"""Returns the list of dislikes the question has."""
		return self.get_ratings()["dislikes"]

	def increase_num_of_comments(self):
		self._num_of_comments += 1

	def increase_views(self):
		self._views += 1

	def to_string(self, language):
		"""Allows the object question to be printed.

        Args:
            language (dict): The language in which the information will be given.

        Returns:
            str: The question's information.

        """	
		return str(language.get("q") + self._question + "\n" + language.get("id") 
				+ str(self._id) + "\n" + language.get("mb") + (self._user).get_username() 
				+ "\n" + language.get("da") + str(self._date) + "\n" + language.get("lks") 
				+ str(len(self.get_likes())) + " " + language.get("dlks") 
				+ str(len(self.get_dislikes())) + "\n\n")

	def show_comments(self, language):
		"""Shows the question's comments.

		Args:
            language (dict): The language in which the information will be given.

        Returns:
            str: The comments the question has.
		"""
		printing = ""
		if len(self._comments):
			sorted_comments = sorted(self._comments, key=lambda comment: len(comment.get_likes()))
			for comment in sorted_comments:
				printing += comment.to_string(language)
		return printing

	def watch_users_reactions(self, language, reaction):
		"""Shows the users who reacted to the question.

		Args:
            language (dict): The language in which the information will be given.
            reaction (str): The reaction the user wants to see that the other users have made.

        Returns:
            str: The users' usernames who reacted to the question.
		"""
		printing = ""
		if reaction == "like":
			for rating in self.get_likes():
				printing += (rating.get_user()).get_username() + "\n"
		elif reaction == "dislike":
			for rating in self.get_dislikes():
				printing += (rating.get_user()).get_username() + "\n"
		if printing == "" and reaction == "like":
			printing = language.get("nls")
		elif printing == "" and reaction == "dislike":
			printing = language.get("ndls")
		return printing

	def check_user(self, user):
		"""Checks whether the object user is the question's user or not.

		Args:
			user (User): An object user to be checked.

		Returns:
			bool: True if user is the question's user. False otherwise.
		"""
		if self.get_user() == user:
			return True
		else:
			return False

	def is_favorite(self, user):
		"""Checks whether the object user has the question as a favorite or not.

		Args:
			user (User): An object user to be checked.

		Returns:
			bool: True if question is a user's favorite. False otherwise.
		"""
		for question in user.get_type_fav(self):
			if question == self:
				return True
		return False

	def delete_question(self):
		"""Deletes the question, and all the comments and ratings it has.
        """
		for like in self.get_likes():
			like.delete_rating()
		for dislike in self.get_dislikes():
			dislike.delete_rating()
		for comment in self.get_comments():
			comment.delete_comment()
		((self._user).get_questions()).remove(self)
		((self._channel).get_questions()).remove(self)