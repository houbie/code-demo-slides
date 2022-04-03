# Python project demo slides
* embedded code snippets
* demo project code from within your slides
* add a Jupyter (slides) notebook to a Python project

## Getting started

```shell
cd python
# windows: .\pw start
./pw start
```

<div class="alert alert-block alert-info">
    <b>NOTE:</b> Make sure Python >=3.8 is available on your path by running <em>python --version</em></div>

## Python Project
This example project uses [PDM](https://pdm.fming.dev/) for dependency management.
PDM is automatically installed as dev dependency inside the project dir (cfg. npm dev dependencies).

Run any PDM command by typing `./pw` in front, ex. `./pw pdm add matplotlib`.

Or add aliases to _pyproject.toml_, ex. `./pw test`. You don't need to type all of it, ex. try `./pw t`.
