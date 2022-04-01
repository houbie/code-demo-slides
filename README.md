# Slides with embedded, runnable code 
* embedded code snippets
* executable Python, Java, JavaScript, shell instructions, etc.
* give demos without leaving your slide show
* basic code completion during live coding demos (depending on language)

## Getting started

```shell
git checkout https://github.com/houbie/code-demo-slides.git
cd code-demo-slides/demo-slides
# windows: pw start (without ./)
./pw start
```

<div class="alert alert-block alert-info">
    <b>NOTE:</b> Make sure Python >=3.7 is available on your path by running <em>python --version</em></div>

## Language Specific Examples
### Python
Using the default Python kernel.

```shell
cd code-demo-slides/python
# windows: pw start (without ./)
./pw start
```

### Node.js (TypeScript, JavaScript)
Using the [tslab](https://github.com/yunabe/tslab) kernel.

```shell
cd code-demo-slides/nodejs
# windows: pw start (without ./)
./pw start
```

### Java
Using the [IJava](https://github.com/SpencerPark/IJava) kernel.

```shell
cd code-demo-slides/java
# windows: pw start (without ./)
./pw start
```

### Combining languages
The nodejs slides use the [Script of Scripts (SoS) kernel](https://github.com/vatlab/SOS)
to enable both TypeScript and JavaScript execution in the same notebook.

This can easily be extended with other kernels by copying the relevant bits of each _pypproject.toml_.

## Other programming languages
_I would like to demo my favourite language, but it's not yet included._

Checkout if there is a [Jupyter kernel](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels) available.
I so, submit a [github issue](https://github.com/houbie/code-demo-slides/issues), and I'll see what I can do 😃

**Let's do some live coding demos!**
