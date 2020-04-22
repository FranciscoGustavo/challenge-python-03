# Resolve the problem!!
import re

def run():
    with open('encoded.txt', 'r', encoding='utf-8') as f:
        read = f.read()
        m = re.compile('([a-z])')
        hidden_message = ''.join(m.findall(read))
        print(hidden_message)


if __name__ == '__main__':
    run()
