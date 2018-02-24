clear
echo "
██████╗  ██████╗ ██████╗ ███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗
██╔══██╗ ██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║  ██║ ██████╔╝██████╔╝█████╗  ██║  ██║███████║   ██║   ██║   ██║██████╔╝
██║  ██║ ██╔═══╝ ██╔══██╗██╔══╝  ██║  ██║██╔══██║   ██║   ██║   ██║██╔══██╗
██████╔╝ ██║     ██║  ██║███████╗██████╔╝██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═════╝  ╚═╝     ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝

██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗     ███████╗██████╗
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     ██╔════╝██╔══██╗
██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     █████╗  ██████╔╝
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     ██╔══╝  ██╔══██╗
██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗███████╗██║  ██║
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
";

if [ "$PREFIX" = "/data/data/com.termux/files/usr" ]; then
    INSTALL_DIR="$PREFIX/usr/share/doc/dpredator"
    BIN_DIR="$PREFIX/bin/"
    BASH_PATH="$PREFIX/bin/bash"
    TERMUX=true

    pkg install -y git python3
elif [ "$(uname)" = "Darwin" ]; then
    INSTALL_DIR="/usr/local/dpredator"
    BIN_DIR="/usr/local/bin/"
    BASH_PATH="/bin/bash"
    TERMUX=false
else
    INSTALL_DIR="$HOME/.dpredator"
    BIN_DIR="/usr/local/bin/"
    BASH_PATH="/bin/bash"
    TERMUX=false

    sudo apt-get install -y git python3.6
fi

echo "[✔] Checking directories...";
if [ -d "$INSTALL_DIR" ]; then
    echo "[◉] A directory dpredator was found! Do you want to replace it? [Y/n]:" ;
    read mama
    if [ "$mama" = "y" ]; then
        if [ "$TERMUX" = true ]; then
            rm -rf "$INSTALL_DIR"
            rm "$BIN_DIR/dpredator*"
        else
            sudo rm -rf "$INSTALL_DIR"
            sudo rm "$BIN_DIR/dpredator*"
        fi
    else
        echo "[✘] If you want to install you must remove previous installations [✘] ";
        echo "[✘] Installation failed! [✘] ";
        exit
    fi
fi
echo "[✔] Cleaning up old directories...";
if [ -d "$ETC_DIR/Mfr12" ]; then
    echo "$DIR_FOUND_TEXT"
    if [ "$TERMUX" = true ]; then
        rm -rf "$ETC_DIR/Mfr12"
    else
        sudo rm -rf "$ETC_DIR/Mfr12"
    fi
fi

echo "[✔] Installing ...";
echo "";
git clone --depth=1 https://github.com/Mfr12/dpredator "$INSTALL_DIR";
echo "#!$BASH_PATH
python3 $INSTALL_DIR/DPredator.py" '${1+"$@"}' > "$INSTALL_DIR/dpredator";
chmod +x "$INSTALL_DIR/dpredator";
if [ "$TERMUX" = true ]; then
    cp "$INSTALL_DIR/dpredator" "$BIN_DIR"
    cp "$INSTALL_DIR/dpredator.cfg" "$BIN_DIR"
else
    sudo cp "$INSTALL_DIR/dpredator" "$BIN_DIR"
    sudo cp "$INSTALL_DIR/dpredator.cfg" "$BIN_DIR"
fi
rm "$INSTALL_DIR/dpredator";

pip3 install -r require.txt

if [ -d "$INSTALL_DIR" ] ;
then
    clear
    echo "Tool installed ;-)";
    echo "Just type dpredator in your terminal.";
    echo "";
else
    clear
    echo "Installation failed!";
    exit
fi
