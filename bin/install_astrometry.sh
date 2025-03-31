#!/usr/bin/bash
# echo "Installing Astrometry.net 0.94"
# wget -nc https://github.com/dstndstn/astrometry.net/releases/download/0.94/astrometry.net-0.94.tar.gz
# tar -xzvf astrometry.net-0.94.tar.gz
# cd astrometry.net-0.94

cd /home/hnut/workspace/code/astrometry.net

sudo apt update
sudo apt install -y build-essential curl git file pkg-config \
                    swig libcairo2-dev libnetpbm10-dev netpbm \
                    libpng-dev libjpeg-dev zlib1g-dev libbz2-dev libcfitsio-dev wcslib-dev \
                    python3 python3-pip python3-distutils python3-dev python3-scipy python3-pil python3-venv \
                    libatlas-base-dev

sudo apt install astrometry.net

pip3 install numpy pyfits

make
make extra
sudo make install
# echo "export PATH=/usr/local/astrometry/bin:$PATH" >> ~/.profile
# sudo echo "export PATH=/usr/local/astrometry/bin:$PATH" >> /root/.profile
# cd ../
# Back in install dir
# ./catalog-install.sh
