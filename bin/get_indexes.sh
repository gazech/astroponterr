#!/usr/bin/bash

INSTALL_DIR="/home/hnut/workspace/data/astrometry-indexes/"

mkdir -p "${INSTALL_DIR}"

# Wide field indexes
for i in $( seq -w 7 19 ); do
    wget http://data.astrometry.net/4100/index-41$i.fits -P "${INSTALL_DIR}";
done
