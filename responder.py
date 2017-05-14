import fbchat
import markovify


class MarkovResponder(fbchat.Client):

    def __init__(self, email, password, debug=False, user_agent=None):
        fbchat.Client.__init__(self, email, password, debug, user_agent)

    def on_message(self, mid, author_id, author_name, message, metadata):
        self.markAsDelivered(author_id, mid)
        self.markAsRead(author_id)

        if str(author_id) != str(self.uid):
            # messages = self.getThreadInfo(author_id, last_n=5000)
            self.send(author_id, text_model.make_sentence())


text_model = markovify.Text(open("/Users/ZanderShah/git/discord-bot/test.txt").read())

bot = MarkovResponder("<username>", "<email>")
bot.listen()
