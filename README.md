# Welcome to the Sandbox repo!
A safe place to try random and small stuff that is not worth a dedicated repo (yet).

## Getting Started
To use this repository, simply clone it to your local machine:

```sh
    git clone https://github.com/pjg0707/sandbox.git
    cd sandbox
    git checkout dev
```
Feel free to add, modify, or experiment with any files as needed. No special setup is required.

To set up the virtual environment run, run:
```sh
    uv sync --extra dev
```

And then activate it:
```sh
    .venv\Scripts\activate.bat
```

The first time you need to run:
```sh
    uv tool install pre-commit
    pre-commit install
    pre-commit run -a
```

## :wheelchair: Support
For more info contact me at [gardellapablo@gmail.com](mailto:gardellapablo@gmail.com).
