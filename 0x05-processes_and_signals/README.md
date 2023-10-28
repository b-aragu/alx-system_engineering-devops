Processes and signals
___________
# PID (Process Identification Number)
- A process is a running instance of a program and is guaranteed a unique pid which is a non negative integer
- A PID, or process identification number, is a unique non-negative integer assigned to each process when it's created in a Unix-like operating system.

- The process named "init" always has PID 1 and is the ancestor of all other processes.

- A large PID doesn't necessarily mean many processes are running; PIDs aren't immediately reused to prevent errors.

- The default maximum PID value is 32,767, limiting the number of simultaneous processes.

- The "pid_max" file specifies the PID wrap-around value, with a default of 32,768 and a maximum of about four million, depending on system memory.

- Use the `ps`, `pstree`, `top`, and `pidof` commands to view PIDs of processes on the system.

- PIDs are needed to terminate misbehaving programs with the `kill` command, enhancing system stability.

- Process information is stored in the /proc filesystem, and each process has a numbered directory containing various files in /proc.

- Read the "cmdline" file in a process's directory to find the command and its arguments, e.g., `cat /proc/1/cmdline` for PID 1.

To read files in the /proc directory, you may need root access (using "su").

For detailed information about a process, read its "status" file in the /proc directory, e.g., `cat /proc/1/status" for PID 1.`



1. **PID Assignment and "init" Process:**
   
   - A PID is automatically assigned to each process.
   - The "init" process always has PID 1 and is the ancestor of all other processes.

   Example:
   ```css
   $ ps -p 1
   PID TTY          TIME CMD
     1 ?        00:00:03 init
   ```

2. **Large PIDs and PID Wrap-Around:**

   - A large PID doesn't necessarily mean many processes are running.
   - PIDs are not immediately reused to prevent errors.

   Example:
   ```css
   $ ps -p 99999
   99999 ?        00:00:00 ps
   ```

3. **Default and Custom "pid_max" Value:**

   - The default maximum PID value is 32,767.
   - "pid_max" specifies the PID wrap-around value (default is 32,768).

   Example:
   ```shell
   $ cat /proc/sys/kernel/pid_max
   32768
   ```

4. **Viewing Process Information:**

   - Use commands like "ps," "pstree," "top," and "pidof" to view PIDs and process information.

   Example (using "ps"):
   ```shell
   $ ps -e
   ```

5. **Using PIDs to Terminate Processes:**

   - PIDs are needed to terminate misbehaving processes with the "kill" command.

   Example:
   ```shell
   $ kill -9 12345
   ```

6. **/proc Filesystem:**

   - Process information is stored in the "/proc" filesystem.
   - Each process has a numbered directory containing files with information.

   Example:
   ```shell
   $ ls /proc | head -5
   1
   2
   3
   5
   ```

7. **Reading "cmdline" and "status" Files:**

   - Use the "cmdline" file to find the command and its arguments.
   - The "status" file provides detailed information about the process.

   Example (reading "cmdline"):
   ``` shell
   $ cat /proc/1/cmdline
   /sbin/init
   ```

   Example (reading "status"):
   ``` shell
   $ cat /proc/1/status
   ```

8. **Root Access for Reading /proc:**

   - Root (admin) access, often obtained using the "su" command, may be required to read files in the "/proc" directory.

   Example (using "su" to access root):
   ``` shell
   $ su
   Password:
   # cat /proc/1/cmdline
   ```

These examples demonstrate the concepts related to PIDs and the management of processes on a Unix-like operating system, including how to access process information and terminate processes using PIDs.
_______________
# Linux Processes – Environment extern, environ, getenv, setenv
- processes can access and manipulate their environment variables through a set of functions and variables that allows them to interact with the environment.
#### Environment Variables
- They are variables that are set in the environment of a process and can be used by a process and its child process.
- Common environment variables include:
	`PATH` - specifying directories to search for executable files.
	`HOME` - user home directory
	`LANG`- language and localization settings
#### `extern` keyword
- The `extern` keyword in c / c++ is used to declare a variable that is defined in another file (global variable). Often used when a program need to access a global variable defined in  external libraries or modules.
	```c
	extern int globarvar; // declare global variable defined elsewhere
	```
#### `environ` Variable
- The `environ` variable is a global variable defined in the C library (glibc) that holds the process's environment variables as an array of strings.
declared as :
```c
extern char **environ;
int main() {
	for (int i = 0; environ[i] != NULL; i++)
	{
		printf("%S\n", environ[i])
		return 0;
	}
}
```
#### `Get env variable`
- It is used to retrieve the value of a specific environment variable by providing its name. It returns a pointer to the value as a C string (null-terminated character)
- if variable does not exist it returns NULL
```c
#include <stdio.h>
#include <stdlib.h>

int main(){
	char *path = getenv("PATH")
	if ( path != NULL){
		printf("PATH = %S\n", path)
	}
	return 0;
}
```
#### `Setenv` function
- It allows a process to set the value of an environment  variable or create a new one, it takes the variable name , value, and an optional flag to indicate whether to overwrite the variable if it already exist.
```c
#include <stdio.h>
#include <stdlib.h>

int main(){
	setenv("MYVAR", "Hello, World!", 1 );// overwrite if myvar exist
	printf("MYVAR=%S\n", getenv("MYVAR"));
	return 0;
}
```
---------------------
## Linux Signals
- A signal is an event generated by a unix or linux system, in response to some condition. Upon receipt of a signal, a process may take action.
- A signal is just like an interrupt; when generated at user level, a call is made to the kernel of the OS which then acts accordingly.
1. Maskable: signals which can be changed or ignored by the user.
2. Non-Maskable: signals which cant be change or ignored by the user.
```
| Signal  | Description                                                                                           |
| ------- | ----------------------------------------------------------------------------------------------------- |
| SIGHUP  | Hang-up detected on controlling terminal or death of controlling process.                             |
| SIGINT  | Issued if the user sends an interrupt signal (Ctrl + C).                                            |
| SIGQUIT | Issued if the user sends a quit signal (Ctrl + D).                                                   |
| SIGFPE  | Issued if an illegal mathematical operation is attempted.                                            |
| SIGKILL | If a process gets this signal, it must quit immediately and will not perform any clean-up operations. |
| SIGTERM | Software termination signal (sent kill by default).                                                  |
| SIGALRM | Alarm clock signal (used for timers).                                                                |

```
--------------------
## Commands for process management in Linux
- A process in linux is a program in execution.
###### Types of processes
1. Foreground process
	- depends on user for input
	- also referred to as interactive process
2. Background process
  - run independently of the user
  - referred to as non-interactive or automatic process

###### process States in Linux
- A process in linux can go through different states after its created and before its terminated.
- The states are:
	__`Running`__
	__`Sleeping`__
	   - `interruptible sleep`
	   - `uninterruptible sleep`
	__`Stopped`__
	__`Zombie`__
- A process in a running state means that it is running or ready to run.
- A process is in a sleeping state when it is waiting for a resource to be available.
- A process in interruptible sleep  will wake up to handle signals, whereas a process in uninterruptible sleep will not.
- A process enters a stopped state when it receives a stop signal.
- _zombie_ state is when a process is dead but the entry for the process is present in the table.

###### commands for process management in Linux
1. top - track running process on your machine
	```shell
	$ top
	```
- it displays a list of processes running in real time along with their memory and cpu usage
	PID: unique process ID given to each process
	User: username of the process owner
	PR: priority given to a process while scheduling
	NL: nice value of a process
	VIRT: amoint of virtual memory used by a process
	RES: amount of physical memory used by a process
	SHR: amount of memory shared with other process
	S: state of the process
          - `D` = uninterruptible sleep
          - `R` = running
          - `S` = sleeping
          - `T`= traced or stopped
          - `Z` = zombie
	%CPU: % of cpu used by process
	%MEM: percentage of RAM used by the process
	TIME+: total CPU time consumed by the process
	Command: command used to activate the process

1. ps command
	- short for process status. It display the current-running processes. However output generated aint realtime unlike top command.
	   PID - process ID
	   TTY - terminal type
	   TIME - total time the process has been running
	   CMD - name of command that launches the process
3. Stop a process

To stop a process in Linux, use the '**kill’** command. [kill command](https://www.digitalocean.com/community/tutorials/kill-command-in-linux) sends a signal to the process.

There are different types of signals that you can send. However, the most common one is ‘kill -9’ which is ‘**SIGKILL**’.

You can list all the signals using:
```shell
$ kill L
```
The default signal is 15, which is **SIGTERM**. Which means if you just use the kill command without any number, it sends the SIGTERM signal.

The syntax for killing a process is:
```shell
kill [pid]
```
alternatively use 
 ```shell
 kill -9 [pid]
```
this command 'SIGKILL' signal to process. this shd be used in cale the process ignores aa normal kill request
4. Change priority of a process

In Linux, you can prioritize between processes. The priority value for a process is called the ‘Niceness’ value. Niceness value can range from -**20** to **19**. **0** is the default value.

The fourth column in the output of top command is the column for niceness value.

![Niceness](https://journaldev.nyc3.digitaloceanspaces.com/2020/08/niceness.png)

To start a process and give it a nice value other than the default one, use:
```shell
$ nice -n [value] [process name]
```
To change nice value of process that is already running use
```shell
nice value -p 'PID' 
```

-------------
1. **`ps` Command:**
    
    - `ps` stands for "process status."
    - It is used to view information about running processes.
    - Example: `ps aux` lists all running processes.
2. **`pgrep` Command:**
    
    - `pgrep` is used to search for processes based on their names or other attributes.
    - Example: `pgrep apache` finds the process IDs of processes with "apache" in their names.
3. **`pkill` Command:**
    
    - `pkill` is used to send signals to processes based on their names or other attributes.
    - Example: `pkill -SIGTERM apache` sends the SIGTERM signal to processes with "apache" in their names.
4. **`kill` Command:**
    
    - `kill` is used to send signals to processes.
    - It can be used to terminate or signal a process to perform various actions.
    - Example: `kill -9 1234` sends the SIGKILL signal to process ID 1234.
5. **`exit` Command:**
    
    - The `exit` command is used to exit the current shell or script.
    - It's commonly used to exit a shell session or terminate a script.
    - Example: `exit` exits the current shell session.
6. **`trap` Command:**
    
    - `trap` is used to set up signal handling routines in a shell script.
    - It allows you to specify actions to be taken when specific signals are received.
    - Example: `trap 'echo Signal received' SIGINT` sets up a trap to execute a command when the SIGINT signal is received.

---------------
1. **PID (Process Identification Number):**
    
    - A PID is a unique identification number assigned to each running process in a Unix-like operating system (including Linux). It helps the system and users manage and interact with processes.
2. **Process:**
    
    - A process is an executing instance of a program. It's a running task that has its own memory space, state, and system resources. Processes are the fundamental units of work in an operating system.
3. **How to Find a Process's PID:**
    
    - You can find a process's PID using various commands, such as `ps`, `pgrep`, or `pidof`. For example, `ps aux` displays a list of running processes along with their PIDs.
4. **How to Kill a Process:**
    
    - To terminate a process, you can use the `kill` command followed by the process's PID. For example, `kill -9 PID` sends the SIGKILL signal to the specified process, forcing it to terminate.
5. **Signal:**
    
    - A signal is a software interrupt delivered to a process to notify it of a specific event or request it to perform a certain action. Signals are a means of inter-process communication in Unix-like systems.
6. **Two Signals That Cannot Be Ignored:**
    
    - The two signals that cannot be ignored or caught by a process are:
        - **SIGKILL (signal number 9):** This signal forces the immediate termination of a process without allowing it to perform cleanup operations.
        - **SIGSTOP (signal number 19 or 17):** This signal suspends (pauses) a process, and the process remains in a stopped state until it receives a SIGCONT signal.
