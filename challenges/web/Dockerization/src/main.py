from flask import Flask
from cffi import FFI

app = Flask(__name__)

# You can ignore all the FFI parts of this challenge
# it's just to prevent yall from seeing the flag directly
ffi = FFI()
ffi.cdef("""
    char* get_flag();
""")

# Ignore this too
lib = ffi.dlopen("lib.so")

# But don't ignore this
@app.route("/")
def index():
    return f"<h1>Congratulations!</h1><p>Flag: {ffi.string(lib.get_flag()).decode()}</p>"

# This is kinda needed too
app.run(host="0.0.0.0", port=6969)
