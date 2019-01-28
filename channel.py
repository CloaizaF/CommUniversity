

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
		self._questions = []
		Channel.channels[self._topic] = self

	def set_topic(self, topic):
		self._topic = topic  # Check if it already exists

	def set_description(self, description):
		self._description = description

	def set_num_of_questions(self, num_of_questions):
		self._num_of_questions = num_of_questions

	def increase_num_of_questions(self):
		self._num_of_questions += 1

	def get_topic(self):
		return self._topic

	def get_description(self):
		return self._description

	def get_num_of_questions(self):
		return self._num_of_questions

	def get_questions(self):
		return self._questions

	def to_string(self, language):
		return str(self._topic + "\n" + language.get("de") + self._description 
				+ "\n\n")

	def to_string1(self, language):
		printing = str(self.to_string(language))
		if len(self._questions):
			for question in self._questions:
				printing += question.to_string(language)
		return printing

	def delete_channel(self):
		for question in self._questions:
			question.delete_question()
		(Channel.channels).pop(self.get_topic())

	def top_questions(self, language):
		printing = ""
		sorted_list = sorted(self._questions, key=lambda question: len(question.get_likes()), reverse=True)
		top_list = sorted_list[:10]
		for question in top_list:
			printing += question.to_string(language)
		return printing