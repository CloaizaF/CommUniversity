from datetime import date

class New:


	news = {}
	num_of_news = 0

	def __init__(self, admin, title, content, author, label):
		"""Attributes:
		self._admin
	    self._title
		self._content
		self._author
		self._label
		self._id
		self._date
		self._comments
		self._num_of_comments
		self._ratings
		self._views
		"""
		self.set_admin(admin)
		self.set_title(title)
		self.set_content(content)
		self.set_author(author)
		self.set_label(label)
		New.increase_num_of_news()
		self.set_id(New.num_of_news)
		self.set_date(date(2018, 10, 7).today())
		self._comments = []
		self.set_num_of_comments(0)
		self._ratings = {"likes": [], "dislikes": []}
		self.set_views(0)
		New.news[self._id] = self

	def set_admin(self, admin):
		"""Sets the new's admin, appends the new to the admin's news list 
		and increases the number of news the user has made.

		Args:
			user (User): user to be set.
		"""
		self._admin = admin
		admin.get_news().append(self)
		admin.increase_num_of_news()

	def set_id(self, idn):
		self._id = idn

	def set_title(self, title):
		self._title = title

	def set_content(self, content):
		self._content = content

	def set_author(self, author):
		self._author = author

	def set_label(self, label):
		self._label = label

	def set_date(self, date):
		self._date = date

	def set_views(self, views):
		self._views = views

	def set_num_of_comments(self, num_of_comments):
		self._num_of_comments = num_of_comments
		
	def get_admin(self):
		return self._admin

	def get_id(self):
		return self._id

	def get_title(self):
		return self._title

	def get_content(self):
		return self._content

	def get_author(self):
		return self._author

	def get_label(self):
		return self._label

	def get_date(self):
		return self._date

	def get_views(self):
		return self._views

	def get_comments(self):
		return self._comments

	def get_num_of_comments(self):
		return self._num_of_comments

	def get_ratings(self):
		return self._ratings

	def get_likes(self):
		"""Returns the list of likes the new has."""
		return (self._ratings)["likes"]

	def get_dislikes(self):
		"""Returns the list of dislikes the new has."""
		return (self._ratings)["dislikes"]

	def increase_num_of_comments(self):
		self._num_of_comments += 1

	def increase_views(self):
		self._views += 1

	@staticmethod
	def increase_num_of_news():
		New.num_of_news += 1

	def to_string(self, language):
		"""Allows the object new to be printed.

        Args:
            language (dict): The language in which the information will be given.

        Returns:
            str: The new's information.

        """
		return str("\n\t" + language.get("title1") + self._title + "\n\t" + language.get("id") 
				+ str(self._id) + "\n\t" + language.get("de") + self._content + "\n\t" 
				+ language.get("aut") + self._author + "\n\t" + language.get("la") 
				+ self._label + "\n\t" + language.get("da") + str(self._date) + "\n\t" 
				+ language.get("lks") + str(len(self.get_likes())) + " " 
				+ language.get("dlks") + str(len(self.get_dislikes())) + "\n")

	def show_comments(self, language):
		"""Shows the news's comments.

		Args:
            language (dict): The language in which the information will be given.

        Returns:
            str: The comments the new has.
		"""
		printing = ""
		if len(self._comments):
			sorted_comments = sorted(self._comments, key=lambda comment: len(comment.get_likes()))
			for comment in sorted_comments:
				printing += comment.to_string(language)
		return printing

	def watch_users_reactions(self, language, reaction):
		"""Shows the users who reacted to the new.

		Args:
            language (dict): The language in which the information will be given.
            reaction (str): The reaction the user wants to see that the other users have made.

        Returns:
            str: The users' usernames who reacted to the new.
		"""
		printing = ""
		if reaction == "like":
			for rating in self.get_likes():
				printing += "\n\t\t\t" + (rating.get_user()).get_username()
		elif reaction == "dislike":
			for rating in self.get_dislikes():
				printing += "\n\t\t\t" + (rating.get_user()).get_username()
		if printing == "" and reaction == "like":
			printing = language.get("nls")
		elif printing == "" and reaction == "dislike":
			printing = language.get("ndls")
		return printing

	def check_user(self, user):
		"""Checks whether the object user is the new's user or not.

		Args:
			user (User): An object user to be checked.

		Returns:
			bool: True if user is the new's user. False otherwise.
		"""
		if self._admin == user:
			return True
		else:
			return False

	def is_favorite(self, user):
		"""Checks whether the object user has the new as a favorite or not.

		Args:
			user (User): An object user to be checked.

		Returns:
			bool: True if new is a user's favorite. False otherwise.
		"""
		for new in user.get_type_fav(self):
			if new == self:
				return True
		return False

	def delete_new(self):
		"""Deletes the new, and all the comments and ratings it has.
        """
		for like in self.get_likes():
			like.delete_rating()
		for dislike in self.get_dislikes():
			dislike.delete_rating()
		for comment in self._comments:
			comment.delete_comment()
		((self.get_admin()).get_news()).remove(self)
		del New.news[self._id]