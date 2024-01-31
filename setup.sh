if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi

if [ "$(uname)" == "Darwin" ]; then
    # Do something under Mac OS X platform
    source .venv/bin/activate
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    # Do something under Linux platform
    source .venv/bin/activate
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
    # Do something under Windows NT platform
    source .venv/Scripts/activate
fi

pip install -r requirements.txt
pip install -e .
