Loops, condition and Parsing
_______________
## Making linux script portable with  #!/usr/bin/env as shebang
- `#!` is called a shebang followed by the full path to the intepreter such as `/bin/bash`
- most unix like system executes using the intepreter specified on the first line
- However there is a small problem since bash / perl is not always on the same location path e.g `/usr/bin/bash`
- If you want to make sure the script is portable across different unix like os you need to use __`#!/usr/bin/env`__ command as shebang
e.g 
``` bash
#!/usr/bin/env bash
x=5
y=10
echo "$x and $Y"
```
- The main advantage of using __`#!/usr/bin/env bash`__ is that it will use whatever bash executable appears first in the running users `$PATH variable`

#### Using env in the shebang of a script
- `env` is a shell command for unix like os. and we can use it for various purpose e.g
	- display list of environment variables
_____________________________

1. **`env` Command:**
   - **Purpose:** The `env` command is used to display environment variables or run a command in a modified environment.
   - **Usage:**
     - To display all environment variables: `env`
     - To run a command in a modified environment: `env VAR_NAME=value command`

2. **`cut` Command:**
   - **Purpose:** The `cut` command is used to extract sections from lines of files or data streams.
   - **Usage:** 
     - To cut characters from a line: `cut -c START-END file`
     - To cut fields from a line (based on a delimiter): `cut -d DELIMITER -f N file`

3. **`for` Loop:**
   - **Purpose:** The `for` loop is used for iterating over a sequence (like a list of items) and performing a set of commands for each item in the sequence.
   - **Usage:**
     ```bash
     for item in item1 item2 item3
     do
         # Commands to be executed for each item
     done
     ```

4. **`while` Loop:**
   - **Purpose:** The `while` loop is used to execute a set of commands as long as a specified condition is true.
   - **Usage:**
     ```bash
     while [ condition ]
     do
         # Commands to be executed while the condition is true
     done
     ```

5. **`until` Loop:**
   - **Purpose:** The `until` loop is used to execute a set of commands as long as a specified condition is false.
   - **Usage:**
     ```bash
     until [ condition ]
     do
         # Commands to be executed until the condition is true
     done
     ```

6. **`if` Statement:**
   - **Purpose:** The `if` statement is used for conditional branching. It allows you to execute different commands based on whether a specified condition is true or false.
   - **Usage:**
     ```bash
     if [ condition ]
     then
         # Commands to be executed if the condition is true
     else
         # Commands to be executed if the condition is false
     fi
     ```

Refer to the manual pages for each command by running `man command_name` to get detailed information and options.
_____________________

Let's explore each of your questions one by one:

1. **How to Create SSH Keys:**
   - To create SSH keys, you can use the `ssh-keygen` command. Here's a basic example of how to generate an SSH key pair:
     ```bash
     ssh-keygen -t rsa -b 2048 -f ~/.ssh/id_rsa
     ```
   - This command generates an RSA key pair with a bit length of 2048 and saves the private key to `~/.ssh/id_rsa` and the public key to `~/.ssh/id_rsa.pub`.

2. **Advantage of `#!/usr/bin/env bash` over `#!/bin/bash`:
   - Using `#!/usr/bin/env bash` is more portable because it relies on the `env` command to find the `bash` executable in the system's `PATH`. This is especially useful when the location of the `bash` executable may vary across different systems.

3. **How to Use `while`, `until`, and `for` Loops:**
   - You can use `while` and `until` loops to repeat a set of commands as long as or until a condition is met, respectively. For example:
     ```bash
     while [ condition ]
     do
         # Commands to be executed while the condition is true
     done

     until [ condition ]
     do
         # Commands to be executed until the condition is true
     done
     ```
   - You can use a `for` loop to iterate over a sequence of items. For example:
     ```bash
     for item in item1 item2 item3
     do
         # Commands to be executed for each item
     done
     ```

4. **How to Use `if`, `else`, `elif`, and `case` Condition Statements:**
   - You can use `if`, `else`, and `elif` statements for conditional branching. Here's an example:
     ```bash
     if [ condition1 ]
     then
         # Commands to be executed if condition1 is true
     elif [ condition2 ]
     then
         # Commands to be executed if condition2 is true
     else
         # Commands to be executed if none of the conditions are true
     fi
     ```
   - The `case` statement is used to perform different actions based on the value of a variable. For example:
     ```bash
     case $variable in
         pattern1)
             # Commands to be executed for pattern1
             ;;
         pattern2)
             # Commands to be executed for pattern2
             ;;
         *)
             # Commands to be executed if no patterns match
             ;;
     esac
     ```

5. **How to Use the `cut` Command:**
   - The `cut` command is used to extract sections from lines of files or data streams. For example:
     ```bash
     echo "John,Doe,30" | cut -d ',' -f 1
     ```
   - This command extracts the first field (delimited by a comma) from the input line and prints "John."

6. **File and Other Comparison Operators:**
   - File comparison operators in Bash include `-e`, `-f`, and `-d`, which check for existence, regular file, and directory, respectively.
   - Other comparison operators include `-eq`, `-ne`, `-lt`, `-le`, `-gt`, and `-ge` for numeric comparisons, and `=`, `!=`, `<`, and `>` for string comparisons.
   - You can use these operators in `if` statements to make decisions based on conditions.


___________________
# File test Operators
- In bash you can use various file test operators to check various attributes and conditions of files and directories 
- These operators help determine if a file or directory exist, is readable, writable, executable and more
1. -e (existence): check if a file or directory exist
```bash
if [ -e "path/to/file"]; then
	echo "file exist"
fi
```

2. -f (Regular file): checks if the given path is a regular file(not directory or special file)
```bash
if [-f "path/to/file"]; then
	echo "It is a regular file"
fi
```
3. -d (Directory): checks if the given path is a directory
```bash
if [ -d "path/to/directory" ]; then 
	echo "It is a directory"
fi
```
4. -x (execute permission, checks if the file or directory is executable)
``` bash
if [-x "path/to/file"]; then 
echo "It is executable"
fi
```
5. -r (read permission): checks if file or directory is readable
``` bash
if [-r "path/to/file" ]; then 
	echo "it is readable"
fi
```
6. -w (write permission) checks if the file or directory is writtable.
``` bash
if [-w "path/to/file"]; then
echo "It is writabble"
fi```
7. -s(size >0))checks  if the file is  not empty
``` bash
if [-s "path/to/file" ]; then
 echo "file is not empty"
fi
```
8. -z (size = o): check if file list is empty
``` bash
if [-s "path/to/file"]; then
echo "file list is empty

"
```
