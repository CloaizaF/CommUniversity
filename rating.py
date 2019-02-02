from question import Question
from comment import Comment
from new import New


class Rating:


	def __init__(self, user, qcn, like):
		"""Attributes:
		self._user
		self._qcn (qcn stands for question, comment or new)
		self._like
		"""
		self.set_like(like)
		self.set_user(user)
		self.set_qcn(qcn)		

	def set_like(self, like):
		self._like = like

	def set_user(self, user):
		"""Sets the ratings's user, appends the rating to the user's likes or dislikes 
		list, depending on the type of rating it is.

		Args:
			user (User): user to be set.
		"""
		self._user = user
		user_ratings = user.get_ratings()
		if self._like == "like":
			(user_ratings["likes"]).append(self)
		elif self._like == "dislike":
			(user_ratings["dislikes"]).append(self)

	def set_qcn(self, qcn):
		"""Sets the ratings's qcn, appends the rating to the qcn's likes or dislikes 
		list, depending on the type of rating it is.

		Args:
			qcn (Question/Comment/New): The question/comment/new to be set.
		"""
		self._qcn = qcn
		qcnr = qcn.get_ratings()
		if self._like == "like":
			(qcnr["likes"]).append(self)
		elif self._like == "dislike":
			(qcnr["dislikes"]).append(self)

	def get_like(self):
		return self._like

	def get_user(self):
		return self._user

	def get_qcn(self):
		return self._qcn

	def delete_rating(self):
		"""Deletes the rating from the question/new/comment list of likes/dislikes and
		removes it from the user list of likes/dislikes
		"""
		((self._qcn).get_ratings()[str(self.get_like() + "s")]).remove(self)
		((self._user).get_ratings()[str(self.get_like() + "s")]).remove(self)