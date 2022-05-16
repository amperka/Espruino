#!/bin/bash

# This file is part of Espruino, a JavaScript interpreter for Microcontrollers
#
# Copyright (C) 2013 Gordon Williams <gw@pur3.co.uk>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# ----------------------------------------------------------------------------------------
# Creates a binary file containing both Espruino and the bootloader
# ----------------------------------------------------------------------------------------

cd `dirname $0` # scripts
cd ..            # main dir
BASEDIR=`pwd`

BOARDNAME=ISKRAJS
ESPRUINOFILE=`python scripts/get_board_info.py $BOARDNAME "common.get_board_binary_name(board)"`
IMGFILE=espruino_iskrajs.uf2
rm -f $ESPRUINOFILE $BOOTLOADERFILE $IMGFILE

export ISKRAJS=1
export BOARD=ISKRAJS
# export USB_PRODUCT_ID=0x5741 # For test harness board only
# export DEBUG=1
export RELEASE=1

make clean
make || { echo 'Build failed (espruino)' ; exit 1; }

echo Create UF2 file
echo ---------------------
./scripts/uf2conv.py -c -b 0x08010000 -f STM32F4 $ESPRUINOFILE -o $IMGFILE  || { echo 'Build failed (uf2)' ; exit 1; }

echo ---------------------
echo Finished!
echo ---------------------

