

class Channel:


	channels = {}

	def __init__(self, topic, description):
		""" Attributes:
		self._topic
	    self._description
	    self._numofQ
		"""
		self.set_topic(topic)
		self.set_description(description)
		self.set_num_of_questions(0)
		self.set_visits(0)
		self._questions = []
		Channel.channels[self._topic] = self

	def set_topic(self, topic):
		self._topic = topic  

	def set_description(self, description):
		self._description = description

	def set_num_of_questions(self, num_of_questions):
		self._num_of_questions = num_of_questions

	def set_visits(self, visits):
		self._visits = visits

	def get_topic(self):
		return self._topic

	def get_description(self):
		return self._description

	def get_num_of_questions(self):
		return self._num_of_questions

	def get_visits(self):
		return self._visits

	def get_questions(self):
		return self._questions

	def increase_num_of_questions(self):
		self._num_of_questions += 1

	def increase_visits(self):
		self._visits += 1

	def to_string(self, language):
		"""Allows the object channel to be printed.

        Args:
            language (dict): The language in which the information will be given.

        Returns:
            str: The channel's information.

        """
		return str(language.get("topic") + self._topic + "\n" + language.get("de") 
				+ self._description + "\n\n")

	def to_string1(self, language):
		"""Allows the object channel to be printed with all of its questions.

        Args:
            language (dict): The language in which the information will be given.

        Returns:
            str: The channel's information.

        """
		printing = str(self.to_string(language))
		if len(self._questions):
			for question in self._questions:
				printing += question.to_string(language)
		return printing

	def delete_channel(self):
		"""Deletes the channel, and all the questions and it has.
        """
		for question in self._questions:
			question.delete_question()
		(Channel.channels).pop(self.get_topic())

	def top_questions(self, language):
		"""Sorts the channel's questions list by the questions' likes and gets the 
		first 10 items to create a top.

		Args:
			language (dict): The language in which the information will be given.

		Returns:
			str: Top of news.
		"""
		printing = ""
		sorted_list = sorted(self._questions, key=lambda question: len(question.get_likes()), reverse=True)
		top_list = sorted_list[:10]
		for question in top_list:
			printing += question.to_string(language)
		return printing