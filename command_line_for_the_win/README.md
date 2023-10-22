# Bash Scripting for CMD CHALLENGE

## Introduction
Welcome to the CMD CHALLENGE Bash Scripting project! CMD CHALLENGE is an engaging game designed to test and improve your command line skills. In this repository, you'll find Bash scripts and examples to help you level up your command line prowess.

## Background Context
CMD CHALLENGE is a unique game that presents increasingly complex command line challenges. It provides an excellent opportunity to sharpen your Bash scripting abilities and tackle real-world problems through the terminal.

## Getting Started
To get started with Bash scripting for CMD CHALLENGE, make sure you have a working Bash environment on your system. If you're using Linux or macOS, you're good to go. For Windows users, consider using a Bash terminal like Git Bash, Windows Subsystem for Linux (WSL), or Cygwin.

## Examples

### 1. Basic Command Execution
Execute simple commands in your Bash terminal. For instance, the following command lists files in the current directory:
```bash
ls
```
2. Command Pipelines
Leverage pipes to chain commands together. This example counts the number of lines in a text file:
```bash
cat sample.txt | wc -l
```
3. Shell Scripting
Create and run Bash scripts. This script calculates the sum of numbers from 1 to 10:
```bash
#!/bin/bash
sum=0
for i in {1..10}
do
    sum=$((sum + i))
done
echo "Sum of numbers from 1 to 10: $sum"

```
4. Command Substitution
Use command substitution to capture the output of a command and use it as a variable. This script displays the current date:
```bash
current_date=$(date)
echo "Todays date is $current_date"

```
