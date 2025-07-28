# glyph_runner.py
from echo_core import EchoGlyph

if __name__ == "__main__":
    eg = EchoGlyph()

    print("EchoGlyph Protocol Initialized.\n")
    while True:
        prompt = input("Enter glyph command (e.g., mutate::self) or type 'exit': ")
        if prompt.lower() == "exit":
            break
        output = eg.process(prompt)
        print(f"[Echo Response] {output}\n")
