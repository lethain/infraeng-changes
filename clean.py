import sys
from html.parser import HTMLParser


class InfraEngParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.txt = ""
        self.record = False
    
    def handle_starttag(self, tag, attrs):        
        if tag == "section":
            self.record = True
        
    def handle_endtag(self, tag):
        if tag == "section":
            self.record = False

    def handle_data(self, data):
        if self.record and data.strip():
            self.txt += data.strip() + '\n'


def clean(txt):
    parser = InfraEngParser()
    parser.feed(txt)
    return parser.txt


if __name__ == "__main__":
    cleaned = clean(sys.stdin.read())
    sys.stdout.write(cleaned)
    sys.stdout.flush()
