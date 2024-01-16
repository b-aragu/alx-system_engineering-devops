__`bin`__ ~ where binary files are stored
__`boot`__ ~ boot files and grub(allow you to select os)
__`dev`__ ~ physical devices are mounted / stored
__`etc`__ ~ configuration files are stored.
__`home`__ ~ all user named folders are stored
__`lib`__ ~ where binaries are kept/ files needed for program to work are kept
__`media`__ - external devices mount here 
__`opt`__ ~ optional software for the system
__`proc`__ ~ process folder
__`root`__ ~ home directory for root user
__`sbin`__ ~ similar to bin but allows only certain commands run by root user
__`snap`__ 

------
__`pipes`__
- Enable to run two commands respectively
```bash
ls | 
```
__`grep`__
- Used to scan document and present results in a  format you want 
- `grep <search_string>`
__`sort`__ 
- `sort filename`
__`FILTERS`__
filters output of firstcommand which become input of the second

__`Symbolic link`__ - a file that acts as a reference to another file 
	It contains a path reference to the target file or directory
	 creation is done using  `ln` command
```bash
ln -s /path/to/target /path/to/symlink
```
__`awk`__ extract first field (column) from lines in files matching a pattern
__`tr`__ (translate) - cmd used to perform character based translation or deletion of characters.
```shell
tr [OPTION] [set1] [SET2]
```
- Option - optional command line options
- set1 - set of characters to be replaced
- SET2 - set of characters to replace those in set1
__`sed`__ - used for text processing and manipulation. It reads text from a file or stream perfom specified operations on the text and outputs the result
```shell
sed [OPTIONS] 'COMMAND' [INPUTFILE]

```

_e.g substituting text 
 ```shell
 echo "Hello, World" | sed 's/world/universe/'
```

