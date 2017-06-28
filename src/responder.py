import fbchat
import markovify
import config as c

class MarkovResponder(fbchat.Client):

    def __init__(self, email, password):
        fbchat.Client.__init__(self, email, password)

    def on_message(self, mid, author_id, author_name, message, metadata):
        self.markAsDelivered(author_id, mid)
        self.markAsRead(author_id)

        if str(author_id) != str(self.uid):
            # messages = self.getThreadInfo(author_id, last_n=5000)
            self.send(author_id, text_model.make_sentence())


text_model = markovify.Text(open('/Users/ZanderShah/git/markov-responder/test.txt').read())

bot = MarkovResponder(c.USERNAME, c.PASSWORD)
bot.listen()
