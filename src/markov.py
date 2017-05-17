import markovify


def prepare(messages):
    ret = ""
    for message in messages:
        ret += message.body + "."
    print(ret)
    return ret


def generate(text):
    text_model = markovify.Text(
        open("/Users/ZanderShah/git/discord-bot/test.txt").read())
    reply = text_model.make_sentence()
    if (reply != None):
        return reply
    else:
        return "Not enough data .."


# Get raw text as string.

# Build the model.
# text_model = markovify.Text(text.lower())

# Print five randomly-generated sentences
# for i in range(5):
#     print(text_model.make_sentence())

# Print three randomly-generated sentences of no more than 140 characters
# for i in range(3):
#     print(text_model.make_short_sentence(140))
#
# print(text_model.chain.to_json())

# Tests from github as templates
# json_model = text_model.to_json()
# new_text_model = markovify.Text.from_json(json_model)
#
# chain_json = text_model.chain.to_json()
# stored_chain = markovify.Chain.from_json(chain_json)
# assert(get_sorted(stored_chain.to_json()) == get_sorted(chain_json))
# new_text_model = markovify.Text.from_chain(chain_json)
# assert(get_sorted(new_text_model.chain.to_json()) == get_sorted(chain_json))
#
# text_model = sherlock_model
# start_str = "Sherlock Holmes"
# sent = text_model.make_sentence_with_start(start_str)
#
# sent = sherlock_model.make_short_sentence(100, min_chars=50)
#
# sent = text_model.make_sentence(max_words=0)
#
# If there are no periods but newlines instead
# model = markovify.NewlineText(f.read())
