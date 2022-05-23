#!/bin/false
# This file is part of Espruino, a JavaScript interpreter for Microcontrollers
#
# Copyright (C) 2013 Gordon Williams <gw@pur3.co.uk>
# Copyright (C) 2014 Victor Nakoryakov <victor@amperka.ru>
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
    'name' : "Iskra.js",
    'link' :  [ "http://amperka.ru/product/iskra-js" ],
    'default_console' : "EV_SERIAL2",
    'default_busy_pin_indicator' : "B7",
    'variables' : 7423, # (128-12)*1024/16-1
    'bootloader' : 0,
    'flash_base': 0x08008000,
    'binary_name' : 'espruino_%v_iskrajs.bin',
    'images_url_base': 'http://js.amperka.ru/img/',
    'binaries_url_base': 'http://js.amperka.ru/binaries/',
    'json_url': 'http://js.amperka.ru/json/ISKRAJS.json',

    'build' : {
        'optimizeflags' : '-Os -std=c11',
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
            'WRAPPERSOURCES+=targets/iskrajs/jswrap_iskrajs.c',
            'DEFINES+=-DUSE_USB_OTG_FS=1',
            'DEFINES+=-DISKRAJS_LOGO',
            'STLIB=STM32F405xx',
            'PRECOMPILED_OBJS+=$(ROOT)/targetlibs/stm32f4/lib/startup_stm32f40_41xxx.o',
            'JSMODULESOURCES+=libs/js/AT.min.js'
        ]
    }
}

chip = {
    'part' : "STM32F405RGT6",
    'family' : "STM32F4",
    'package' : "LQFP64",
    'ram' : 128,
    'flash' : 1024 - 32,
    'speed' : 168,
    'usart' : 6,
    'spi' : 3,
    'i2c' : 3,
    'adc' : 3,
    'dac' : 2,
    'place_text_section' : 0x00004000,
}

# TODO
board = {
}

devices = {
    'OSC' : { 'pin_1' : 'H0',
              'pin_2' : 'H1' },
    'LED1': { 'pin' : 'B6' },
    'LED2': { 'pin' : 'B7' },
    'BTN1': { 'pin' : 'C4' },
    'USB' : { 'pin_dm' : 'A11',
              'pin_dp' : 'A12',
              'pin_vbus' : 'A9',
              'pin_id' : 'A10', },
    'JTAG': { 'pin_MS' : 'A13',
              'pin_CK' : 'A14', 
              'pin_DI' : 'A15', },
}


# TODO
board["_css"] = """
""";

def get_pins():
    pins = pinutils.scan_pin_file([], 'stm32f40x.csv', 6, 9, 10)
    return pinutils.only_from_package(pinutils.fill_gaps_in_pin_list(pins), chip["package"])

# if __name__ == '__main__':
#     from pprint import pprint
#     pprint(get_pins())
