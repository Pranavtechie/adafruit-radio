sudo apt-get install -y python3-pip
sudo apt install --upgrade python3-setuptools 


cd ~
sudo apt install python3-venv
python3 -m venv env --system-site-packages

source env/bin/activate

cd ~
pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo -E env PATH=$PATH python3 raspi-blinka.py