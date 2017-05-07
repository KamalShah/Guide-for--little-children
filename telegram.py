URL = "https://api.telegram.org/bot%s/" % BOT_TOKEN
MyURL = "https://example.com/hook"

api = requests.Session()
application = tornado.web.Application([
    (r"/", Handler),
])

if __name__ == '__main__':
    signal.signal(signal.SIGTERM, signal_term_handler)
    try:
        set_hook = api.get(URL + "setWebhook?url=%s" % MyURL)
        if set_hook.status_code != 200:
            logging.error("Can't set hook: %s. Quit." % set_hook.text)
            exit(1)
        application.listen(8888)
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        signal_term_handler(signal.SIGTERM, None)

class Handler(tornado.web.RequestHandler):
        def post(self):
            try:
                logging.debug("Got request: %s" % self.request.body)
                update = tornado.escape.json_decode(self.request.body)
                message = update['message']
                text = message.get('text')
                if text:
                    logging.info("MESSAGE\t%s\t%s" % (message['chat']['id'], text))

                    if text[0] == '/':
                        command, *arguments = text.split(" ", 1)
                        response = CMD.get(command, not_found)(arguments, message)
                        logging.info("REPLY\t%s\t%s" % (message['chat']['id'], response))
                        send_reply(response)
            except Exception as e:
                logging.warning(str(e))

def send_reply(response):
    if 'text' in response:
        api.post(URL + "sendMessage", data=response)

def help_message(arguments, message):
    response = {'chat_id': message['chat']['id']}
    result = ["Hey, %s!" % message["from"].get("first_name"),
              "\rI can accept only these commands:"]
    for command in CMD:
        result.append(command)
    response['text'] = "\n\t".join(result)
    return response

def base64_decode(arguments, message):
    response = {'chat_id': message['chat']['id']}
    try:
        response['text'] = b64decode(" ".join(arguments).encode("utf8"))
    except:
        response['text'] = "Can't decode it"
    finally:
        return response

if text[0] == '/':
    ...
else:
    response = CMD["<speech>"](message)
    logging.info("REPLY\t%s\t%s" % (message['chat']['id'], response))
    send_reply(response)         

RESPONSES = {
    "Hello": ["Hi there!", "Hi!", "Welcome!", "Hello, {name}!"],
    "Hi there": ["Hello!", "Hello, {name}!", "Hi!", "Welcome!"],
    "Hi!": ["Hi there!", "Hello, {name}!", "Welcome!", "Hello!"],
    "Welcome": ["Hi there!", "Hi!", "Hello!", "Hello, {name}!",],
}
def human_response(message):
    leven = fuzzywuzzy.process.extract(message.get("text", ""), RESPONSES.keys(), limit=1)[0]
    response = {'chat_id': message['chat']['id']}
    if leven[1] < 75:
        response['text'] = "I can not understand you"
    else:
        response['text'] = random.choice(RESPONSES.get(leven[0])).format_map(
            {'name': message["from"].get("first_name", "")}
        )
    return response

RESPONSES["What time is it?"] = ["<at_sticker>", "{date} UTC"]

if response['text'] == "<at_sticker>":
        response['sticker'] = "BQADAgADeAcAAlOx9wOjY2jpAAHq9DUC"
        del response['text']

def send_reply(response):
    if 'sticker' in response:
        api.post(URL + "sendSticker", data=response)
    elif 'text' in response:
        api.post(URL + "sendMessage", data=response)

while True:
            r = requests.get(URL + "?offset=%s" % (last + 1))
            if r.status_code == 200:
                for message in r.json()["result"]:
                    last = int(message["update_id"])
                    requests.post("http://localhost:8888/",
                                  data=json.dumps(message),
                                  headers={'Content-type': 'application/json',
                                           'Accept': 'text/plain'}
                     )
            else:
                logging.warning("FAIL " + r.text)
            time.sleep(3)



