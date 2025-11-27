- ==***command + ,***==  key for open General Setting in Obsidian
- ==***option + D***== key (may change in the setting) for open daily notes
## This is a heading

`#!/bin/bash`


<<<<<<< HEAD
```sh
=======
```python
>>>>>>> b04cc49e8db0deabb74e6ef260dd2495db7731c2
#bash/python/sh     
#!/bin/bash

echo `This is some code`
```

## Task1: The chmod Command

The chmod Command
- Read - *`r`*
- Write - *`w`*
- Execute - *`x`*

|   |   |   |   |
|---|---|---|---|
|RIGHT​|LETTER​|OCTAL VALUE​|MEANING​|
|Read​|r​|4​|Can view the file’s contents.​|
|Write​|w​|2​|Can modify or delete the file.​|
|Execute​|x​|1​|Can run the file (if it’s a script/program).​



```
xcci2071e1125b:week4 up2519096$ touch newfil.txt

xcci2071e1125b:week4 up2519096$ chmod 600 newfil.txt

xcci2071e1125b:week4 up2519096$ ls-l

-bash: ls-l: command not found

xcci2071e1125b:week4 up2519096$ ls -l

total 0

-rw-------  1 up2519096  UNI\Domain Users  0 23 Oct 15:47 newfil.txt

xcci2071e1125b:week4 up2519096$ chmod 755 newfil.txt

xcci2071e1125b:week4 up2519096$ ls -l

total 0

-rwxr-xr-x  1 up2519096  UNI\Domain Users  0 23 Oct 15:47 newfil.txt
```

## Task2: Bash Variables Script


```
#!/bin/bash
read -p "What are you heaving for tea? : " SANDWICH

echo "hey $USER, you are heaving $SANDWICH for tea"
```

RESULT in Terminal
```
xcci2071e1125b:week4 up2519096$ ./interactive.sh

What are you heaving for tea? : Sweet

hey up2519096, you are heaving Sweet for tea
```

#### Small notes & improvements

- **Typo:** You probably meant **“having”** instead of “heaving”.
- **Read robustness:** Add `-r` to `read` to avoid interpreting backslashes as escapes.
- **Default / empty input:** You might want to handle the case where the user just presses Enter.
- **Portability / style:** If you want the script to run with whichever bash is first in `PATH`, use `#!/usr/bin/env bash`. Not necessary on many systems, but a common pattern.