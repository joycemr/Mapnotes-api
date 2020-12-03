# This has to be at the top to prevent the cache directories
import sys
sys.dont_write_bytecode = True

from api import app, api

if __name__ == '__main__':
    app.run(debug=True, port=8080)
