# OpenScience
Repository for Open Science and Artificial Intelligence

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18875351.svg)](https://doi.org/10.5281/zenodo.18875351)

[![Documentation](https://readthedocs.org/projects/open-science-paper-analysis/badge/?version=latest)](https://open-science-paper-analysis.readthedocs.io/en/latest/)

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
- Docker
- A GROBID service instance
    - `docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.8.2`

## Installation Instructions
Clone the repository and install dependencies:
```sh
git clone https://github.com/02mario/OpenScience.git
cd OpenScience
```

## Execution Instructions
There are two ways to run the application installing locally with poetry or using Docker, both ways require Docker installed. 

**Notice that running with Docker doesn't allow to specify custom dataset or output directories nor to show the figures.**

### Execution with Docker
To run the application with Docker, first put your PDF files (.pdf extension needed) in the `dataset/` directory, then run:
Omit `-d` to see the execution and logs of the app.
```sh
docker compose up -d
```

The process may take 1-2 minutes depending on the number of files. 
The application will save the figures in the `output/` directory by default.

When finished, you can stop the application with:
```sh
docker compose down
```

You can delete the docker image if you are not going to use it anymore with:
```sh
docker rmi openscience-openscience:latest
```

### Execution with Poetry

First, make sure you have GROBID locally running andthe necessary files in PDF format in the `dataset/` directory.
The application will save the figures in the `output/` directory by default.

Install the dependencies with poetry:
```sh
poetry install
```

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

You can specify the URL of the GROBID service:
```sh
poetry run openscience --grobid_url http://localhost:8070
```

### Test execution

The tests verify that the information is correctly extracted from a TEI and that the figures contain the correct information.
The application has also been tested with some files to verify full functionality with Grobid.

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
> Mario, J. G. (2026). Python program for paper analysis with grobid. (Version 1.0.0) [Computer software]. https://github.com/02mario/OpenScience

## Where to Get Help
https://github.com/02mario/OpenScience/issues
