string = "HeLo PyThOn"

print("string: ", string)
print("string.capitalize()", string.capitalize())
print("string.upper()", string.upper())
print("string.lower()", string.lower())
print("string.casefold()", string.casefold())
print("'hello'.center(11,'-')", "hello".center(11,'-'))
print("string.count(o)", "hello python".count('o'))
print("Ories.encode()", "Ories".encode())
print("string.endswith('n')", string.endswith('n'))
print("string.startwith('H')", string.startswith("H"))
print("string.find('o')", string.find('o'))
print("string.index('o')", string.index('o'))
print("{} {}".format("Hello", "Python"), "\n")

print("string.isalnum()", string.isalnum())
print("string.isalpha()", string.isalpha())
print("12311.isnumeric()", "12311".isnumeric())
print("' '.isspace()", " ".isspace())
print("Hello.istitle()", "Hello".istitle())
print("HELLO.isupper()", "HELLO".isupper(), "\n")

print("'-'.join('hello')", "-".join("hello"))
print("string.replace('p', 'T')", string.replace('T', 'p'))
print("'hello there learner'.rfind('e')", "hello there learner".rfind('e')) # find last position of a specified value
print("'hello there learner'.rindex('e')", "hello there learner".rindex('e')) # find last position of a specified value
print("'hello there hello here'.partion('hello')", "hello there hello here".partition("hello"))
print("'hello there hello here'.rpartion('hello')", "hello there hello here".rpartition("hello"))

print("string.swapecase()", string.swapcase())
print("string.title()", string.title())
print("'Ha He Hi Ho Hu'.translate(str.maketrans('aeiou','12345'))", "Ha He Hi Ho Hu".translate(str.maketrans("aeiou", "12345")))
print("'10'.zfill(5)", "10".zfill(5))
print("string.split()", string.split())