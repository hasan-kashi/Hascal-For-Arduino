# Hascal For Arduino
A Compiler for [Hascal Programming Language](https://github.com/hascal) for programming Arduino
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

## License
GNU general public license

## About
Copyright © 2019-2020 **Hascal Development Team**, all rights reserved.
