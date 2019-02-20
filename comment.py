from question import Question
from new import New
from datetime import date


class Comment:


	def __init__(self, user, qn, description):
		"""Attributes:
		self._qn (qn stands for question/new)
		self._user
		self._id
		self._description
		self._date
		self_ratings
		"""
		self.set_user(user)
		self.set_qn(qn)
		self.set_id(qn.get_num_of_comments())
		self.set_description(description)
		self.set_date(date(2018, 10, 7).today())
		self._ratings = {"likes": [], "dislikes": []}

	def set_user(self, user):
		"""Sets the comment's user, appends the comment to the user's comments list 
		and increases the number of comments the user has made.

		Args:
			user (User): user to be set.
		"""
		self._user = user
		user.get_comments().append(self)
		user.increase_num_of_comments()

	def set_qn(self, qn):
		"""Sets the comment's question/new, appends the comment to the question/new's 
		comments list and increases the number of comments the channel has.

		Args:
			qn (Question/New): The question/new to be set.
		"""
		self._qn = qn
		qn.get_comments().append(self)
		qn.increase_num_of_comments()

	def set_id(self, idc):
		self._id = idc

	def set_description(self, description):
		self._description = description

	def set_date(self, date):
		self._date = date

	def get_user(self):
		return self._user

	def get_qn(self):
		return self._qn

	def get_id(self):
		return self._id

	def get_description(self):
		return self._description

	def get_date(self):
		return self._date

	def get_ratings(self):
		return self._ratings

	def get_likes(self):
		"""Returns the list of likes the question has."""
		return self.get_ratings()["likes"]

	def get_dislikes(self):
		"""Returns the list of dislikes the question has."""
		return self.get_ratings()["dislikes"]

	def to_string(self, language):
		"""Allows the object comment to be printed.

        Args:
            language (dict): The language in which the information will be given.

        Returns:
            str: The comment's information.

        """
		return str("\n\t" + language.get("c") + self._description + "\n\t" + language.get("id") 
				+ str(self._id) + "\n\t" + language.get("mb1") + self._user.get_username() 
				+ "\n\t" + language.get("da") + str(self._date) + "\n\t" + language.get("lks") 
				+ str(len(self.get_likes())) + " " + language.get("dlks") 
				+ str(len(self.get_dislikes())) + "\n")

	def watch_users_reactions(self, language, reaction):
		"""Shows the users who reacted to the comment.

		Args:
            language (dict): The language in which the information will be given.
            reaction (str): The reaction the user wants to see that the other users have made.

        Returns:
            str: The users' usernames who reacted to the comment.
		"""
		printing = ""
		if reaction == "like":
			for rating in self.get_likes():
				printing += "\n\t\t\t" + (rating.get_user()).get_username()
		elif reaction == "dislike":
			for rating in self.get_dislikes():
				printing += "\n\t\t\t" + (rating.get_user()).get_username()
		if printing == "" and reaction == "like":
			printing = "\t" + language.get("nls")
		elif printing == "" and reaction == "dislike":
			printing = "\t" + language.get("ndls")
		return printing

	def check_user(self, user):
		"""Checks whether the object user is the comment's user or not.

		Args:
			user (User): An object user to be checked.

		Returns:
			bool: True if user is the comment's user. False otherwise.
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
			bool: True if comment is a user's favorite. False otherwise.
		"""
		for comment in user.get_type_fav(self):
			if comment == self:
				return True
		return False

	def delete_comment(self):
		"""Deletes the comments and all the ratings it has.
        """
		for like in self.get_likes():
			like.delete_rating()
		for dislike in self.get_dislikes():
			dislike.delete_rating()
		((self._user).get_comments()).remove(self)
		((self._qn).get_comments()).remove(self)