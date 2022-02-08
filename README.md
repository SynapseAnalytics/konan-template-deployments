# konan-template-deployments

[Konan](https://konan.ai) is your one-stop platform to bring your AI models to life. Typically, one would be required to do some tedious boring work in order to prepare the machine learning or data science model for deployment. Not with us! With **Konan**, gone are the days of worrying about a model's *dependencies*, battling with *containerization* or obsessively hand-holding the *infrastructure*. This repo will guide you in preparing your machine learning model in as seamless a manner as possible! Of course, don't forget to also checkout **Konan's** rich [documentation](https://docs.konan.ai) for additional info.

To get started, clone this repo by typing in the command
``` bash
git clone https://github.com/SynapseAnalytics/konan-template-deployments.git
```

## Objective

The aim of this repository is to guide a data scientist, software engineer, or inquisitive tinkerer into *packaging* their already-prepared AI-powered model into a format that will be easily deployable on [Konan](https://app.konan.ai). More specifically, a **Konan Model**-compatible docker image will be created, with all required dependencies installed and an appropriate webserver initialized to help serve your AI logic.

## Directory Structure

The template deployments inside this repo are organized by *Programming language*. In each `<programming-language>` folder, you should find the following subfolders and files:

- `src/` should contain the source code of your AI model and its logic
- `models/` is a folder in which you can add ready-made models to your logic. They can, for example, be picked files of models trained and saved.
- `scripts/` folder is provided so that you can add any extra scripts, in any programming language of your chosing, as helper files for your main source code.
- `data/` should contain any data files (CSVs and such) needed by your machine learning model.
- The `.konan` file should contain the environment variables needed in order to generate your docker image and prepare your **Konan** model. For example, you should specify your docker credentials in there.
- The `.dockerignore`, `Dockerfile`, `Makefile` and other scary sounding files are used to automtically generate your docker image and Konan-based model. Of course, feel free to check them out, but you shouldn't need to interact with them.

## Usage

For a complete walk-through on how to use this repo for generating your **Konan**-powered deployments, head on to the [Quick Start Guide](https://docs.konan.ai/getting-started/quick-start) in **Konan's** documentation for more instructions.

## Support

If you have any questions, or feel that this repo needs some improvement, feel free to raise an **issue** with the repository's [Issue Tracker](https://github.com/SynapseAnalytics/konan-template-deployments/issues).
