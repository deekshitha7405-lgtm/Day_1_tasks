from deep_translator import GoogleTranslator

while True:
    text = input("Enter English text (or type 'exit' to stop): ")

    if text.lower() == "exit":
        print("Program Ended.")
        break

    translated = GoogleTranslator(source='english', target='kannada').translate(text)

    print("Kannada:", translated)
    print("-" * 40)