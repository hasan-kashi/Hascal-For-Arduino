# Hascal For Arduino
Compiler for [Hascal Programming Language](https://github.com/hascal) for programming Arduino
## Example 
blink :
```
function setup
  pinMode(LED_BUILTIN, OUTPUT);
end;

function loop
  digitalWrite(LED_BUILTIN, HIGH);   
  delay(1000);                       
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
end;
```

to compile this code enter following command in your terminal :
```
python hascal.py blink.has
arduino --upload tmp.ino
```

## Build
Prerequisites :
- arduino v1.8 or higher
- python v3.X

and you must have the pyinstaller library installed , if not installed enter following command for install it :
```
# on linux :
pip3 install pyinstaller

# on windows :
pip install pyinstaller
```

then enter the following command in the terminal :
```
pyinstaller hascal.py --onefile
```

that compiles in `src/dist` folder.
## License
GNU general public license

## About
Copyright © 2019-2020 **Hascal Development Team**, all rights reserved.
