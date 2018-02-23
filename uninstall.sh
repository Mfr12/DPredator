if [ "$PREFIX" = "/data/data/com.termux/files/usr" ]; then
    INSTALL_DIR="$PREFIX/usr/share/doc/DPredator"
    BIN_DIR="$PREFIX/bin/"
    BASH_PATH="$PREFIX/bin/bash"
elif [ "$(uname)" = "Darwin" ]; then
    INSTALL_DIR="/usr/local/DPredator"
    BIN_DIR="/usr/local/bin/"
    BASH_PATH="/bin/bash"
else
    INSTALL_DIR="$HOME/.DPredator"
    BIN_DIR="/usr/local/bin/"
    BASH_PATH="/bin/bash"
fi

echo "Checking folders...";

if [ -d "$INSTALL_DIR" ]; then
    echo "Do you want to uninstall it? [Y/n]:" ;
    read a
    if [ "$a" = "y" ]; then
        sudo rm -r "$INSTALL_DIR"
    else
        exit
    fi
fi

rm
