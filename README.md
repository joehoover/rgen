# RGen: README Generator for Cog and Replicate

RGen is a utility package designed to simplify the process of creating README files for your machine learning models packaged with Cog and published on Replicate. 

## Installation

You can install RGen directly from its GitHub repository using pip:

```bash
pip install git+https://github.com/joehoover/rgen.git
```

## Quick start

To use the default Cog and Replicate README templates, you can just: 

1. Build a README yaml from the default Cog and Replicate README templates.
```
rgen extract
```
2. Fill out the fields in `readme.yaml`.

3. Run `rgen generate`

## Usage


RGen provides a command-line interface to generate README files. It follows a two-step process:

1. **Extract:** This operation reads the provided README templates, identifies the fields that need to be filled, and writes these fields into a readme.yaml file. If readme.yaml already exists, it will not be overwritten.

```
rgen extract --template1 path_or_url_to_readme_template1 --template2 path_or_url_to_readme_template2
```

By default, rgen uses [cog_readme_template.md](https://github.com/joehoover/rgen/blob/main/data/cog_readme_template.md) and [replicate_readme_template.md](https://github.com/joehoover/rgen/blob/main/data/replicate_readme_template.md) for template1 and template2 respectively.

2. **Generate.** This operation reads the readme.yaml file and populates the fields in the README templates. The populated README files are then written to the disk.

```sh
rgen generate --template1 path_or_url_to_readme_template1 --template2 path_or_url_to_readme_template2
```

# About readme.yaml

`readme.yaml` is a YAML file that holds the values for the fields that need to be filled in the README templates. After running `rgen extract`, you should edit `readme.yaml` to provide appropriate values for the fields.

For multi-line values in YAML, you can use the `|` character for literal block scalars or the `>` character for folded block scalars. For example:

```yaml
multi_line: |
    line 1
    line 2
    line 3
```

or

```yaml
folded_multi_line: >
    line 1
    line 2
    line 3
```
