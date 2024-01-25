### File Test operators
__`-a`__
if file exist
__`-f`__
The file is a regular file (not directory or device file)
__`-d`__
file is a directory
__`-b`__
file is a block device
__`-c`__
file is a character device
__`-p`__
file is a pipe
__`-h`__
file is a symbolic link
__`-r`__
file has read permission (for user running the test)
__`-w`__
file has write permission
__`-x`__
file has execute permission
__`-O`__
you are the owner of the file

###  `#!/usr/bin/env`
- Make sure a script is portable across different UNIX like operating systems.
- The `env` command allows you to run a program in a modified environment
- Example instead of  `#!/usr/bin/bash` use `#!/usr/bin/env bash` the advantage of this is that it will use whatever bash executable appears first in the running users path variable.
- To show current environment variables defined by your shell , you can run `env` command.
