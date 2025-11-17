# sudo apt-get install -y python3-pip
# sudo apt install --upgrade python3-setuptools 


# cd ~
# sudo apt install python3-venv
# python3 -m venv env --system-site-packages

# source env/bin/activate

# cd ~
# pip3 install --upgrade adafruit-python-shell
# wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
# sudo -E env PATH=$PATH python3 raspi-blinka.py

# --- 
# sudo pip3 install adafruit-circuitpython-rfm9x


# --- 
curl -fsSL https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/main/raspi-spi-reassign.py -o raspi-spi-reassign.py
sudo -E env PATH=$PATH python3 raspi-spi-reassign.py --ce0=disabled --ce1=disabled

