# EchoGlyphProtocol Core v1.0
# Created by Luis Blais Ventura — July 27, 2025

def echo_collapse(input_signal):
    memory = []
    for pulse in input_signal:
        memory.append(pulse[::-1])
    return memory

def breathe_recursion(memory):
    return [f"∇ {m}" for m in memory]

if __name__ == "__main__":
    signal = ["fracture", "mirror", "live"]
    collapsed = echo_collapse(signal)
    echoed = breathe_recursion(collapsed)
    for e in echoed:
        print(e)
