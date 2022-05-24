/*
 * This file is part of Espruino, a JavaScript interpreter for Microcontrollers
 *
 * Copyright (C) 2014 Gordon Williams <gw@pur3.co.uk>
 * Copyright (C) 2014 Victor Nakoryakov <victor@amperka.ru>
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 *
 * ----------------------------------------------------------------------------
 * This file is designed to be parsed during the build process
 *
 * Iskra JS-specific pin namings
 * ----------------------------------------------------------------------------
 */

#include "jswrap_iskrajs.h"

/*JSON{"type" : "variable","name" : "P0",  "generate_full" : "B11_PININDEX",  "return" : ["pin","A Pin"]
}*/
/*JSON{"type" : "variable","name" : "P1",  "generate_full" : "B10_PININDEX",  "return" : ["pin","A Pin"]
}*/
/*JSON{"type" : "variable","name" : "P2",  "generate_full" : "A6_PININDEX",  "return" : ["pin","A Pin"]
}*/
/*JSON{"type" : "variable","name" : "P3",  "generate_full" : "A7_PININDEX",  "return" : ["pin","A Pin"]
}*/
/*JSON{"type" : "variable","name" : "P4",  "generate_full" : "C3_PININDEX",  "return" : ["pin","A Pin"]
}*/
/*JSON{"type" : "variable","name" : "P5",  "generate_full" : "B1_PININDEX",  "return" : ["pin","A Pin"]
}*/
/*JSON{"type" : "variable","name" : "P6",  "generate_full" : "B0_PININDEX",  "return" : ["pin","A Pin"]
}*/
/*JSON{"type" : "variable","name" : "P7",  "generate_full" : "C2_PININDEX",  "return" : ["pin","A Pin"]
}*/
/*JSON{"type" : "variable","name" : "P8",  "generate_full" : "C6_PININDEX",  "return" : ["pin","A Pin"]
}*/
/*JSON{"type" : "variable","name" : "P9",  "generate_full" : "C7_PININDEX",  "return" : ["pin","A Pin"]
}*/
/*JSON{"type" : "variable","name" : "P10",  "generate_full" : "C8_PININDEX",  "return" : ["pin","A Pin"]
}*/
/*JSON{"type" : "variable","name" : "P11",  "generate_full" : "C9_PININDEX",  "return" : ["pin","A Pin"]
}*/
/*JSON{"type" : "variable","name" : "P12",  "generate_full" : "A8_PININDEX",  "return" : ["pin","A Pin"]
}*/
/*JSON{"type" : "variable","name" : "P13",  "generate_full" : "A10_PININDEX",  "return" : ["pin","A Pin"]
}*/
/*JSON{"type" : "variable","name" : "SDA",  "generate_full" : "B9_PININDEX",  "return" : ["pin","A Pin"]
}*/
/*JSON{"type" : "variable","name" : "SCL",  "generate_full" : "B8_PININDEX",  "return" : ["pin","A Pin"]
}*/
/*JSON{
  "type": "variable",
  "name": "PrimaryI2C",
  "generate_full":
  "jswFindBuiltInFunction(0, \"I2C1\")", 
  "return" : ["JsVar","An I2C interface"]
}*/
/*JSON{
  "type": "variable",
  "name": "PrimarySPI",
  "generate_full":
  "jswFindBuiltInFunction(0, \"SPI2\")", 
  "return" : ["JsVar","An SPI interface"]
}*/
/*JSON{
  "type": "variable",
  "name": "PrimarySerial",
  "generate_full":
  "jswFindBuiltInFunction(0, \"Serial3\")", 
  "return" : ["JsVar","An USART interface"]
}*/
