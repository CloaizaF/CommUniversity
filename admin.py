from user import User


class Admin(User):


    admins = {}

    def __init__(self, name, username, email, password):
        """Attributes:
        self._name
        self._username
        self._email
        self._password
        self._questions
        self._answers
        self._ratings
        self._num_of_questions 
        self._num_of_comments 
        self._num_of_news
        self._news
        """
        super().__init__(name, username, email, password)
        self._news = []
        self.set_num_of_news(0)
        Admin.admins[self._username] = self

    def set_num_of_news(self, num_of_news):
        self._num_of_news = num_of_news

    def increase_num_of_news(self):
        self._num_of_news += 1

    def get_news(self):
    	return self._news

    def get_num_of_news(self):
        return self._num_of_news
    def delete_admin(self):
        """Invokes self.delete_user() to delete the user, and then, deletes the admin and all
        the news he/she has uploaded.
        """
        self.delete_user()
        for new in self._news:
            new.delete_new()
            User.delete_favorite(new)
        del Admin.admins[self._username]