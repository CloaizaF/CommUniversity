

class English:


	english = {
	"mm": """
		1. Sign in
		2. Log in 
		3. Generate fictional data 
		4. Generate fictional data from a txt
		5. Save generated users
	    $. Go out
	    """,
	"usero": """
		What do you want to do?
		1. Check my profile
		2. Update my profile
		3. Check a channel
		4. Read some news
		5. Check my favorites
		6. Ban a user
		7. Delete my account
		8. Log out
		""",
	"favo": """
		What do you want to do?
		1. Read my favorite questions
		2. Read my favorite comments
		3. Read my favorite news
		@. Go back to the previous menu
		""",
	"updateo": """
		What will you modify?
		1. Everything in my profile
		2. Only my name
		3. Only my username
		4. Only my email
		5. Only my password
		@. Go back to the previous menu
		""",
	"channelo": """
		What do you want to do?
		1. Search for a question
		2. Make a question
		3. Read some questions
		4. Watch top questions
		5. Delete this channel
		@. Go back to the previous menu
		""",
	"selectq":"""
		1. Select a question to unfold more options 
		@. Go back to the previous menu
		""",
	"questiono": """
		What do you want to do?
		1. Answer the question
		2. Read its comments
		3. Give it a like
		4. Give it a dislike
		5. Watch its likes 
		6. Watch its dislikes
		7. Save this question
		8. Edit this question
		9. Delete this question
		@. Go back to the previous menu
		""",
	"selectc":"""
		1. Select a comment to unfold more options 
		@. Go back to the previous menu
		""",
	"commento": """
		What do you want to do?
		1. Give it a like
		2. Give it a dislike
		3. Watch its likes 
		4. Watch its dislikes
		5. Save this comment
		6. Edit this comment
		7. Delete this comment
		@. Go back to the previous menu
		""",
	"selectn":"""
		1. Upload a new
		2. Select a new to unfold more options
		3. Watch top news
		@. Go back to the previous menu
		""",
	"newo": """
		What do you want to do?
		1. Comment
		2. Read its comments
		3. Give it a like
		4. Give it a dislike
		5. Watch its likes 
		6. Watch its dislikes
		7. Save this new
		8. Edit this new
		9. Delete this new
		@. Go back to the previous menu
		""",
	"editnew": """
		What do you want to edit from this new?
		1. Everything in this new.
		2. Only it's title
		3. Only it's content
		4. Only it's author
		5. Only it's label
		@. Go back to the previous menu 
		""",
	"gbp": """
		@. Go back to the previous menu.
		""",
	"needo": """
	    Do you need to use an operator(AND,OR,NOT)?:
	    1. Yes, I do.
	    2. No, I do not.
	    """,
	"selecto": """
	    Select the operator you want to use:
	    1. AND
	    2. OR
	    3. NOT
	    """,
	"attempts": """
		You have already tried to log in 3 times, do you want to try once more?
		1. Yes
		2. No
		""",
	"sure": """
		Are you sure you want to delete your account?
		1. Yes, I want to delete my account
		2. No, I do not want to delete my account
		""",
	"sorto": """
		Do you want to sort the channels?
		1. Yes.
		2. No.
		""",
	"sortby": """
		Sort the channels by:
		1. Channel's number of visits
		2. Channel's number of questions
		""",
	"maxattempts": "You have already tried to log in 4 times, we will redirect you to the main menu",
	"lastattempt": "Last attempt before redirecting you",
	"i": "The option selected is invalid, please choose a valid option.",
	"keyword": "Insert the keyword: ",
	"nomatch": "There is no match for the word(s) inserted.",
	"name": "Insert your name: ",
	"nn": "Insert the new name: ",
	"n": "Name: ",
	"username": "Insert your username: ",
	"nu": "Insert the new username: ",
	"un": "Username: ",
	"una": "The username is already registered.",
	"email": "Insert your email: ",
	"email2": "Confirm your email: ",
	"ne": "Insert the new email:",
	"e": "Email: ",
	"ea": "The email is aleardy registered.",
	"edm": "The emails do not match.",
	"password": "Insert your password: ",
	"password2": "Confirm your password: ",
	"oldpassword": "Insert your last password: ",
	"np": "Insert the new password: ",
	"pdm": "The passwords do not match.",
	"wp": "wrong password",
	"wu": "wrong username",
	"uc": "The user has been created.",
	"iu": "The user does not exist.",
	"channel": "Insert the channels topic: ",  # Apostrophe
	"channels": "These are the available channels: ",
	"nchannels": "There are no available channels",
	"ic": "The channel does not exist.",
	"chs": "Channels: ",
	"nq": "This channel has no questions",
	"topic": "Topic: ",
	"de": "Description: ",
	"question": "Type a question: ",
	"ncq": "This question has no comments.",
	"nuq": "You have no permission to edit this question.",
	"nun": "You have no permission to edit this new.",
	"q": "Question: ",
	"mb": "Made by: ",
	"mb1": "Made by: ",
	"da": "Date: ",
	"news": "These are the available news: ",
	"News": "NEWS ",
	"nnews": "There are no available news",
	"title": "Insert the news title: ",
	"title1": "Title: ",
	"content": "Insert the news content: ",  # Apostrophe
	"author": "Insert the authors name",  # Apostrophe
	"aut": "Author: ",
	"label": "Insert the category: ",
	"la": "Label: ",
	"ncn": "This new has no comments.",
	"id": "id: ",
	"idin": "Insert the id: ",
	"iid": "Invalid id",
	"comment": "Type a comment: ",
	"nuc": "You have no permission to edit this comment.",
	"c": "Comment: ",
	"lks": "likes: ",
	"dlks": "dislikes: ",
	"l": "Users who like this: ",
	"dl": "Users who dislike this: ",
	"nls": "No one likes this.",
	"ndls": "No one dislikes this.",
	"fs": "Favorite saved.",
	"fhs": "The favorite has already been saved.",
	"nfq": "You have no favorite questions.",
	"nfc": "You have no favorite comments.",
	"nfn": "You have no favorite news.",
	"lo": "Come back soon",
	"np": "You have no permission to make this action",
	"ub": "Your user is currently banned, thus, you can not log in",
	"inub": "Insert the username who will be banned",
	"chd": "Channel deleted",
	"qd": "Question deleted",
	"cod": "Comment deleted",
	"nd": "New deleted",
	"aam": "This action has already been made, therefore, it cannot be done again",
	"ara": "This action requires action 4 to be made",
	"nusers": "There are no users", 
	"redirecting": "Redirecting you to the previous menu",
	"idmb": "The id must be an integer."
	}