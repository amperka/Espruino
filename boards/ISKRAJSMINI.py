#!/bin/false
# This file is part of Espruino, a JavaScript interpreter for Microcontrollers
#
# Copyright (C) 2013 Gordon Williams <gw@pur3.co.uk>
# Copyright (C) 2022 Roman Samusevich (kekcheburec) for Amperka Robots LLC
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# ----------------------------------------------------------------------------------------
# This file contains information for a specific board - the available pins, and where LEDs,
# Buttons, and other in-built peripherals are. It is used to build documentation as well
# as various source and header files for Espruino.
# ----------------------------------------------------------------------------------------

import pinutils;

info = {
 'name' : "Iskra JS Mini",
 'link' :  [ "http://amperka.ru/product/iskra-js-mini" ],
 'default_console' : "EV_SERIAL1",
 'default_console_tx' : "B6",
 'default_console_rx' : "B7",
 'variables' : 7423, # (128-12)*1024/16-1
 'bootloader' : 1,
 'binary_name' : 'espruino_%v_iskrajs_mini.bin',
 'build' : {
   'optimizeflags' : '-Os',
   'libraries' : [
     'USB_HID',
     'NET',
     'GRAPHICS',
     'TV',
     'FILESYSTEM',
     'WIZNET',
     'CRYPTO','SHA256','SHA512',
     'TLS',
     'NEOPIXEL'
   ],
   'makefile' : [
     'DEFINES+=-DUSE_USB_OTG_FS=1',
     'DEFINES+=-DPIN_NAMES_DIRECT=1',
     'DEFINES+=-DISKRAJS_MINI_LOGO',
     'STLIB=STM32F411xE',
     'PRECOMPILED_OBJS+=$(ROOT)/targetlibs/stm32f4/lib/startup_stm32f401xx.o',
     'JSMODULESOURCES+=libs/js/AT.min.js',
   ]
  }
};

chip = {
  'part' : "STM32F411CEU6",
  'family' : "STM32F4",
  'package' : "UQFN48",
  'ram' : 128,
  'flash' : 512,
  'speed' : 100,
  'usart' : 6,
  'spi' : 3,
  'i2c' : 3,
  'adc' : 1,
  'dac' : 0,
  'saved_code' : {
    'address' : 0x08060000,
    'page_size' :  131072,
    'pages' : 1,
    'flash_available' : 384
  },
};

devices = {
  'OSC' : { 'pin_in' :  'H0', # checked
            'pin_out' : 'H1' }, # checked
  # 'OSC_RTC' : { 'pin_in' :  'C14', # checked
  #               'pin_out' : 'C15' }, # checked
  'LED1' : { 'pin' : 'B2' },
  'LED2' : { 'pin' : 'B12' },
  'USB' : { 'pin_vsense' :  'A9',
            'pin_dm' : 'A11',   # checked
            'pin_dp' : 'A12' }, # checked
  'JTAG' : {
        'pin_MS' : 'A13',
        'pin_CK' : 'A14',
#        'pin_DI' : 'A15'
          },
};

# TODO
board = {
};

# TODO
board["_css"] = """
""";

def get_pins():
  pins = pinutils.scan_pin_file([], 'stm32f401.csv', 5, 8, 9)
  pins = pinutils.scan_pin_af_file(pins, 'stm32f401_af.csv', 0, 1)
  return pinutils.only_from_package(pinutils.fill_gaps_in_pin_list(pins), chip["package"])

# if __name__ == '__main__':
#     from pprint import pprint
#     pprint(get_pins())
