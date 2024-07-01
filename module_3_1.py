calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    a = len(string), string.upper(), string.lower()
    count_calls()
    print(a)

def is_contains(a = 'string', list_to_search = []):
    list_to_search = [item.lower() for item in list_to_search]
    if a.lower() in list_to_search:
        print(True)
    else:
        print(False)
    count_calls()



string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

