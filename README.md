# How to set up pyenv

To Create a new evnv

```sh
pyenv virtualenv <python-version> myenv
```

To activate

```sh
pyenv activate myenv
```

To Deactivate

```sh
pyenv deactivate
```

How to delete

```sh
pyenv virtualenv-delete <name-of-virtual-enve>
```

# How to isntall

Dependecies

```sh
sudo apt-get update; sudo apt-get install --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

clone pyenv

```sh
curl https://pyenv.run | zsh
```

Defining environment variable

```sh
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
```

Add pyenv init to the shell which enables shims and autocompletion

```sh
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc
```

Restart your shell

```sh
exec "$SHELL"
```

show version

```sh
pyenv --version

```

list version

```sh
pyenv install --list
```

install any version you want

```sh
pyenv install <your-verion>
```
