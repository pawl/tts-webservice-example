# test by using: curl --data "text=test" http://127.0.0.1:8080
# windows requires installing pywin32 to use pyttsx

import pyttsx
import web
import threading

# say the text function
def saythread(location, text):
    engine = pyttsx.init() 
    engine.say(text)
    engine.runAndWait()
    
urls = (
    '/', 'say'
)

class say:
    def POST(self):
        data = web.input()
        if data['text']:
            e = (1, data['text'])
            # must be in a thread or application will get stuck on runAndWait
            t = threading.Thread(target=saythread,args=e,name="sayitthread")
            t.start()
            result = "success"
        else:
            result = "failure: no text"
        return result

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
