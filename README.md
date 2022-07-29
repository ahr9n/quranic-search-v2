<div align="center">
 <img style="width: 35%; mix-blend-mode: multiply;" src="https://user-images.githubusercontent.com/52632898/181664653-e2a64fb2-35f2-47d3-8af6-8451d3fbe305.png" alt="Quranic Search">
</div>

<h1 align="center">Quranic Lexical/Semantic Search</h1>
<h4 align="center">A Machine Learning Based Web Application of Retrieving Information from the Holy Quran Using NLP</h4>

<div align="center">
    <a href="https://github.com/ahr9n/quranic-search-v2/graphs/commit-activity">
        <img src="https://img.shields.io/badge/Maintained%3F-YES-green.svg" alt="maintenance" />
    </a>
    <a href="https://github.com/ahr9n/quranic-search-v2/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/ahr9n/quranic-search-v2?logo=gnu&.svg" alt="license" />
    <a>
    <a href="http://makeapullrequest.com">
        <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="pull-request" />
    </a>
    <a href="https://standardjs.com">
        <img src="https://img.shields.io/badge/code_style-standard-brightgreen.svg" alt="style" />
    </a>
</div>

## :scroll: Table of Contents

*   [About the Project](#tada-about-the-project)
    *   [Screenshots](#camera-screenshots)
    *   [What is Quranic Search](#microphone-what-is-devault)
    *   [Why Quranic Search](#mag-why-devault)
        *   [The Problem with Traditional Lexical Search](#-1-the-problem-with-traditional-cloud-storage)
        *   [Solution with Semantic Search](#1-the-solution-with-devault)
        *   [Features](#see_no_evil-features)
    *   [How Quranic Search Works](#closed_lock_with_key-how-devault-works)
    *   [Tech stack and Tools](#hammer_and_wrench-tech-stack-and-tools)
*   [Source Code Directory Structure](#ladder-source-code-directory-structure)
*   [Getting Started](#biking_man-getting-started)
    *   [Prerequisites](#yellow_circle-prerequisites)
        *   [Package Manager](#package-package-manager)
    *   [Run for Development](#wrench-run-for-development)
        *   [Run the Tests](#syringe-run-the-tests)
*   [Usage](#thinking-usage)
*   [FAQ](#bulb-faq)
*   [Future Work](#rescue_worker_helmet-future-work)
*   [Contributors](#hatching_chick-contributors)
*   [License](#warning-license)

## :tada: About the Project

`Quranic Search` stands for lexical and semantic search in the Holy Quran.

### :camera: Screenshots

|                                               |                                               |
|:---------------------------------------------:|:---------------------------------------------:|
| ![Home](/assets/screenshots/home.png) | ![Results](/assets/screenshots/results.png) |


## :microphone: What is Quranic Search

Quranic Search is developed to help all people, especially Muslims to deal with the Holy Quran easier and faster, allowing them to search in the Holy Quran for specific Verses, by a key-word or a conceptual topic.

### :mag: Why Quranic Search

#### :-1: The Problem with Traditional Lexical Search

*   Incomplete results using key-words
*   Lexical search is not based on meaning of the search query

#### :+1: The Solution with Semantic Search

*   Relevant verses based on meaning
*   Best ranking of the most similar verses

#### :see\_no\_evil: Features

*   Natural Language Processing based
*   Using of the best pre-trained word2vec models
*   Building a sentence embedding model based on word2vec
*   Fast with low cost, unlike using Transformers
*   Open-source

### :closed\_lock\_with\_key: How Quranic Search Works

Verses are shown lexographically by Surah number and the Verse number in the Surah

**When you make a lexical search:**

*   Lexical Search API interacts with the UI
*   Verses are retrieved based on the sequence of key-words using the Lexical Search API

**When you make a semantic search:**

*   Semantic Search API interacts with the UI
*   Verses IDs are retrieved based on the meaning/topic of words using the Semantic Search API
*   Verses all props are retrieved from the Lexical Search API

### :hammer\_and\_wrench: Tech Stack and Tools

The tools used in this project.

|                                                                       | Tool                                                 | Description                             |
|:---------------------------------------------------------------------:|:----------------------------------------------------:|:---------------------------------------:|
| <img src="/assets/tools/vscode.png" width="32px" height="32px" />     | [Visual Studio Code](https://code.visualstudio.com/) | IDE                                     |
| <img src="/assets/tools/reactdotjs.png" width="32px" height="32px" /> | [React.js](https://reactjs.org/)                     | Frontend framework                      |
| <img src="/assets/tools/django.png" width="32px" height="32px" />     | [django](https://www.djangoproject.com/)             | Lexical Search Backend Framework        |
| <img src="/assets/tools/flask.png" width="32px" height="32px" />      | [Flask](https://flask.palletsprojects.com/en/2.1.x/) | Semantic Search API Backend Framework   |
| <img src="/assets/tools/gensim.png" width="32px" height="32px" />     | [Gensim](https://radimrehurek.com/gensim/)           | Topic Modeling (Word2Vec, KeyedVectors) |
| <img src="/assets/tools/sqlite3.png" width="32px" height="32px" />    | [SQLite3](https://www.sqlite.org/)                   | For the Holy Quran Database             |

## :ladder: Source Code Directory Structure

```sh
quranic-search-v2
├── README.md                                   <- This top-level README for this project
├── LICENSE
├── assets
│   ├── screenshots                             <- Screenshots from the project
│   └── tools                                   <- Used tools in the project
├── backend                                     
│   ├── api
│   │   ├── lexical
│   │   │   ├── api/                            <- Lexical django project with settings
│   │   │   ├── db/                             <- Used databases in the project
│   │   │   ├── search/                         <- Search application (static, templates, models, serializers, urls, views, tests, ..etc) 
│   │   │   ├── db.sqlite3                      <- Migrated database
│   │   │   ├── manage.py                       <- A command-line utility to interact with this Django project 
│   │   │   └── requirements.txt                <- All needed for installing the lexical search API
│   │   └── semantic
│   │       ├── data                    
│   │       │   ├── external/                   <- Data from third party sources
│   │       │   └── processed/                  <- The final, canonical data sets for modeling
│   │       ├── models/                         <- Trained and serialized models, model predictions, or model summaries
│   │       ├── notebooks/                      <- All Jupyter notebooks
│   │       ├── src                             <- Source code for use in this project
|   │       |   ├── __init__.py                 <- Makes src a Python module
|   │       │   └── models                      <- Scripts to train models and then use trained models to make predictions
|   │       │       ├── pooling.py              <- Pooling algorithms for sentence embeddings
|   │       │       ├── predict.py              <- Resources of the semantic search API
|   │       │       ├── preprocess.py           <- The frequent preprocessing methods 
|   │       │       └── semantic_methods.py     <- The semantic (word/sentence) search methods
│   │       ├── app.py                          <- The Flask application (entry point)
│   │       └── requirements.txt                <- All needed for installing the semantic search API
│   └── run.sh                                  <- Bootstrapping script to run the APIs
├── frontend
│   ├── node_modules                            <- Node.js modules
│   ├── public                                  
│   │   ├── fonts                               <- Fonts used in the project
│   │   │   ├── amiri/ 
│   │   │   └── kufi/ 
│   │   ├── images
│   │   │   └── quran-logo.png 
│   │   ├── 404.html 
│   │   ├── index.html 
│   │   ├── manifest.json
│   │   └── robots.txt  
│   ├── src
│   │   ├── components                          <- React components
│   │   │   ├── HomeForm  
│   │   │   │   ├── HomeForm.css  
│   │   │   │   └── HomeForm.js  
│   │   │   ├── Navbar/
│   │   │   ├── ResultsForm/
│   │   │   └── Verse/
│   │   ├── containers                          <- React containers/pages
│   │   │   ├── About
│   │   │   │   ├── About.css  
│   │   │   │   └── About.js  
│   │   │   ├── Bookmarks/
│   │   │   ├── Home/
│   │   │   └── Results/
│   │   ├── App.css                             <- CSS for the application
│   │   ├── App.js                              <- The application file
│   │   ├── App.test.js                         <- The application file for testing
│   │   ├── index.css                           <- CSS for the root (entire application)
│   │   ├── index.js                            <- The root application file
│   │   ├── reportWebVitals.js                  <- WebVitals reporting script
│   │   └── setupTests.js                       <- Setup script for testing
|   ├── package-lock.json                       <- Used to install dependencies
|   └── package.json                            <- Used to install dependencies
├── .github  
│   └── workflows                               <- GitHub Actions workflows
│       ├── django.yml
│       └── node.js.yml
└── .gitignore
```

## :warning: License

Licensed under the [GPL-v3](LICENSE) License.