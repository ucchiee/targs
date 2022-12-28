# targs
tmux + xargs

## Install

```bash
git clone https://github.com/ucchiee/targs.git
cd targs
pip install -e .
```

## Usage

`targs` reads newline delimited strings from the standard input and executes each of them in the tmux panes.

e.g.:

```bash
$ cat scripts
# echo 1
# echo 2
# echo 3
# echo 4

$ tmux
$ cat scripts | targs
```
