import pyttsx
import web
import threading

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
            t = threading.Thread(target=saythread,args=e,name="sayitthread")
            t.start()
            result = "success"
        else:
            result = "failure"
        return result

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
