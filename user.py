from question import Question
from comment import Comment
from new import New


class User:


    users = {}

    def __init__(self, name, username, email, password):
        """Attributes:
        self._name
        self._username
        self._email
        self._password
        self._questions
        self._comments
        self._ratings
        self._numofq (numofq stands for number of questions)
        self._numofc (numofa stands for number of answers)
        self._ban_state
        """
        self.set_name(name)
        self.set_username(username)
        self.set_email(email)
        self.set_password(password)
        self._questions = []
        self._comments = []
        self._ratings = {"likes": [], "dislikes": []}
        self._favorites = {"comments": [], "questions": [], "news": []}
        self.set_num_of_questions(0)
        self.set_num_of_comments(0)
        self.set_ban_state(False)    

    def set_name(self, name): 
        self._name = name

    def set_username(self, username):
        """Checks if the user already exists, to change its username, otherwise, 
        adds the user to the User.users dict. An then, sets the username."""
        if username in User.users:
            del User.users[self._username]
            self._username = username
            User.users[self._username] = self
        else:
            self._username = username
            User.users[self._username] = self
    
    def set_email(self, email):
        self._email = email
    
    def set_password(self, password):
        self._password = password

    def set_num_of_questions(self, num_of_questions):
    	self._num_of_questions = num_of_questions
    
    def set_num_of_comments(self, num_of_comments):
    	self._num_of_comments = num_of_comments

    def set_ban_state(self, ban_state):
        self._ban_state = ban_state
    
    def get_name(self):
    	return self._name
    
    def get_username(self):
    	return self._username
    
    def get_email(self):
    	return self._email

    def get_password(self):
    	return self._password
    
    def get_questions(self):
    	return self._questions

    def get_comments(self):
    	return self._comments

    def get_ratings(self):
        return self._ratings

    def get_favorites(self):
        return self._favorites

    def get_num_of_questions(self):
    	return self._num_of_questions

    def get_num_of_comments(self):
    	return self._num_of_comments

    def get_ban_state(self):
        return self._ban_state

    def get_likes(self):
        """Returns the list of likes the question has."""
        return self.get_ratings()["likes"]

    def get_dislikes(self):
        """Returns the list of dislikes the question has."""
        return self.get_ratings()["dislikes"]

    def increase_num_of_questions(self):
        self._num_of_questions += 1
    
    def increase_num_of_comments(self):
        self._num_of_comments += 1

    def to_string(self, language):
        """Allows the object user to be printed.

        Args:
            language (dict): The language in which the information will be given.

        Returns:
            str: The user's information.

        """
        return str(language.get("n") + self._name + "\n" + language.get("un")
                + self._username + "\n" + language.get("e") + self._email)

    def check_username(self, username):
        """Checks whether the username passed is the user's username or not.

        Args:
            username (str): A string to be checked.

        Returns:
            bool: True if username is the user's username. False otherwise.
        """
        if self._username == username:
            return True
        else:
            return False

    def add_fav(self, qcn):
        """Invokes self.get_type_fav() on the qcn object to know where to append it.

        Args:
            qcn (Question/Comment/New) : An object to be checked and appended.
        """
        self.get_type_fav(qcn).append(qcn)

    def get_type_fav(self, qcn): 
        """Returns the corresponding list of favorites that match the object qcn.

        Args:
            qcn (Question/Comment/New) : An object to be checked.

        Returns:
            list: A list of favorites.
        """
        if isinstance(qcn, Question):
            return self._favorites["questions"]
        elif isinstance(qcn, Comment):
            return self._favorites["comments"]
        elif isinstance(qcn, New): 
            return self._favorites["news"]

    def repeated_fav(self, qcn):       
        """Checks whether an object is already favorite of the user.

        Args:
            qcn (Question/Comment/New) : An object to be checked.

        Returns:
            bool: True if qcn is already a favorite. False otherwise. 
        """
        for fav in self.get_type_fav(qcn):
            if qcn == fav:
                return True
        self.add_fav(qcn)
        return False

    def watch_fav(self, language, q_c_n):
        """Shows the favorites of a user.

        Args:
            language (dict): The language in which the information will be given.
            q_c_n (str) : The type of favorites that are going to be watched.

        Returns:
            str: The information of all the favorites in the corresponding list. 
        """
        printing = ""
        if q_c_n == "question":
            for question in self._favorites["questions"]:
                printing += question.to_string(language)
        elif q_c_n == "comment":
            for comment in self._favorites["comments"]:
                printing += comment.to_string(language)
        elif q_c_n == "new":
            for new in self._favorites["news"]:
                printing += new.to_string(language)
        return printing

    def ban(self):
        """Changes the _ban_state of the user to ban a user.
        """
        self._ban_state = True

    def unban(self):
    	"""Changes the _ban_state of the user to ban a user.
    	"""
    	self._ban_state = False

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

    def delete_user(self):
        """Deletes the user and all the questions, comments and ratings he/she has made.
        """
        for question in self._questions:
            question.delete_question()
            User.delete_favorite(question)
        for comment in self._comments:
            comment.delete_comment()
            User.delete_favorite(comment)
        for rating in self._ratings["likes"]:
            rating.delete_rating()
        for rating in self._ratings["dislikes"]:
            rating.delete_rating()
        self._favorites.clear()
        del User.users[self._username]