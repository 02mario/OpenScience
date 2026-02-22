# OpenScience
Repository for Open Science and Artificial Intelligence


[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18723896.svg)](https://doi.org/10.5281/zenodo.18723896)

## Description
This is a project to perform papers analysis with grobid.
This program allows to extract info from the papers and create some visualizations to analyze the results.

### Funcionalities
- Extract links from papers
- Create a word cloud with the abstracts of the papers
- Create a bar chart with the number of figures per paper

## Requirements
- Python >=3.10
- Poetry >=2.0.0
    - `https://python-poetry.org/docs/#installation`
- A running GROBID service instance
    - `docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.8.2`

## Installation Instructions
Clone the repository and install dependencies:
```sh
git clone https://github.com/02mario/OpenScience.git
cd OpenScience
poetry install
```

## Execution Instructions
First, make sure you have GROBID locally running andthe necessary files in PDF format in the `dataset/` directory.
The application will save the figures in the `output/` directory by default.

To run the application:
```sh
poetry run openscience
```

You can also specify an output directory for the figures:
```sh
poetry run openscience --output output
```

You can also specify a custom dataset directory:
```sh
poetry run openscience --dataset my_dataset
```

You can choose to show the figures in addition to saving them:
```sh
poetry run openscience --show
```

### Test execution
To run unit tests:
```sh
poetry run python -m unittest discover -s tests -p "test_*.py"
```

## Running Examples

To run the application with a custom dataset and save the figures to an output directory:
```sh
poetry run openscience --dataset my_papers --output results
```

## Preferred Citation
If you use this project, please cite:
> Mario, J. G. (2026). Python program for paper analysis with grobid. (Version 0.1.0) [Computer software]. https://github.com/02mario/OpenScience

## Where to Get Help
https://github.com/02mario/OpenScience/issues
