<div align="center">
 <img style="width: 50%; mix-blend-mode: multiply;" src="https://user-images.githubusercontent.com/52632898/181664653-e2a64fb2-35f2-47d3-8af6-8451d3fbe305.png" alt="Quranic Search">
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
    *   [What is Quranic Search](#microphone-what-is-quranic-search)
    *   [Why Quranic Search](#mag-why-quranic-search)
        *   [The Problem with Traditional Lexical Search](#1-the-problem-with-traditional-lexical-search)
        *   [The Solution with Semantic Search](#1-the-solution-with-semantic-search)
        *   [Features](#see_no_evil-features)
    *   [How Quranic Search Works](#closed_lock_with_key-how-quranic-search-works)
    *   [Tech stack and Tools](#hammer_and_wrench-tech-stack-and-tools)
*   [Source Code Directory Structure](#ladder-source-code-directory-structure)
*   [Getting Started](#biking_man-getting-started)
    *   [Prerequisites](#yellow_circle-prerequisites)
    *   [Run for Development](#wrench-run-for-development)
*   [License](#warning-license)

## :tada: About the Project

Retrieving information from the Holy Quran is an important field for Quran scholars, Muslim researchers, and Arabic enthusiasts in general. There are two popular types of Quran searching techniques: lexical or keyword-based and semantic or concept-based that is a challenging task, especially in a complex corpus such as the Holy Quran. `Quranic Search` stands for lexical and semantic search in the Holy Quran.

### :camera: Screenshots

|                                       |                                             |
|:-------------------------------------:|:-------------------------------------------:|
| ![Home](/assets/screenshots/home.png) | ![Results](/assets/screenshots/results.png) |


## :microphone: What is Quranic Search

Quranic Search is developed to help all people, especially Muslims to deal with the Holy Quran easier and faster, allowing them to search in the Holy Quran for specific Verses, by a keyword or a conceptual topic.

### :mag: Why Quranic Search

The Holy Quran is considered the primary reference to approximately 1.6 billion Muslims around the world and as the leading resource for classical Arabic language. Muslims, as well as non-Muslims, need to search for certain information from the Holy Quran or retrieve verses that discuss a specific topic, having various topics to discuss, for example; ethics, Islamic law, marital and family law, monetary transactions, morals, and the relationship between Islam/Muslims and other world religions.

#### :-1: The Problem with Traditional Lexical Search

*   Incomplete results using key-words
*   Lexical search is not based on the meaning of the search query

#### :+1: The Solution with Semantic Search

*   Relevant verses based on meaning, improving the accuracy of search
*   Best ranking of the most similar verses, based on Word Embedding Representation

#### :see\_no\_evil: Features

*   Natural Language Processing based
*   Displaying the first 50 results based on the best ranking
*   Using the best pre-trained Word2Vec models
*   Building a sentence embedding model based on Word2Vec (CBOW Architecture)
*   Using different methods to represent the sentence vector
    *   Max similarity score between two words (A word in a query and a word in a Verse)
    *   Max frequency score of a specific similarity (0.3) between two words
    *   Average similarity score between two words
    *   Pooling; max pooling and average pooling
*   Preprocessing of the queries is done based on the preprocessing of models' training to o seek the best comparison of vectors
*   Working first on the single word level
    *   Then we iterated over the whole query and sentence, maximizing all Verses words with the results by summing up the result of the method for every two words (in a query and a verse), to finally compare with the whole document of the Holy Quran text.
*   Combining methods results and models to get the best results
*   Fast with low cost, unlike using Transformers
*   Open-source

### :closed\_lock\_with\_key: How Quranic Search Works

**When you make a lexical search:**

*   Lexical Search Django API interacts with the React UI
*   Verses are retrieved based on the sequence of keywords using the Lexical Search API
*   Verses are displayed in the results page lexicographically by Surah number and the Verse number in the Surah

**When you make a semantic search:**

*   Semantic Search API interacts with the UI
*   Verses IDs are retrieved based on the meaning/topic of words using the Semantic Search API
*   A set of Word2Vec pre-trained models are used to get the word vectors of the words of Verses and search queries
*   Computing sentence vectors is done using the several methods
    *   Combining the results of all methods by all models
*   Verses are retrieved based on the similarity score between the query and the verse
*   Computing distances by cosine similarity to retrieve the most similar verses
*   Verses' all props are retrieved from the Lexical Search API

### :hammer\_and\_wrench: Tech Stack and Tools

The tools used in this project.

|                                                                       | Tool                                                 | Description                             |
|:---------------------------------------------------------------------:|:----------------------------------------------------:|:---------------------------------------:|
| <img src="/assets/tools/vscode.png" width="40px" height="32px" />     | [Visual Studio Code](https://code.visualstudio.com/) | IDE                                     |
| <img src="/assets/tools/reactdotjs.png" width="40px" height="32px" /> | [React.js](https://reactjs.org/)                     | Frontend framework                      |
| <img src="/assets/tools/django.png" width="42px" height="32px" />     | [django](https://www.djangoproject.com/)             | Lexical Search Backend Framework        |
| <img src="/assets/tools/flask.png" width="45px" height="32px" />      | [Flask](https://flask.palletsprojects.com/en/2.1.x/) | Semantic Search API Backend Framework   |
| <img src="/assets/tools/gensim.png" width="45px" height="32px" />     | [Gensim](https://radimrehurek.com/gensim/)           | Topic Modeling (Word2Vec, KeyedVectors) |
| <img src="/assets/tools/sqlite3.png" width="45px" height="32px" />    | [SQLite3](https://www.sqlite.org/)                   | For the Holy Quran Database             |

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
│   │   │   ├── api/                            <- Lexical Django project with settings
│   │   │   ├── db/                             <- Used databases in the project
│   │   │   ├── search/                         <- Search application (static, templates, models, serializers, urls, views, tests, ..etc) 
│   │   │   ├── db.sqlite3                      <- Migrated database
│   │   │   ├── manage.py                       <- A command-line utility to interact with this Django project 
│   │   │   └── requirements.txt                <- All needed for installing the lexical search API
│   │   └── semantic
│   │       ├── data                    
│   │       │   ├── external/                   <- Data from third-party sources
│   │       │   └── processed/                  <- The final, canonical data sets for modeling
│   │       ├── models/                         <- Trained and serialized models, model predictions, or model summaries
│   │       ├── notebooks/                      <- All Jupyter notebooks
│   │       ├── src                             <- Source code for use in this project
│   │       │   ├── __init__.py                 <- Makes src a Python module
│   │       │   └── models                      <- Scripts to train models and then use trained models to make predictions
│   │       │       ├── pooling.py              <- Pooling algorithms for sentence embeddings
│   │       │       ├── predict.py              <- Resources of the semantic search API
│   │       │       ├── preprocess.py           <- The frequent preprocessing methods 
│   │       │       └── semantic_methods.py     <- The semantic (word/sentence) search methods
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
│   ├── package-lock.json                       <- Used to install dependencies
│   └── package.json                            <- Used to install dependencies
├── .github  
│   └── workflows                               <- GitHub Actions workflows
│       ├── django.yml
│       └── node.js.yml
└── .gitignore
```

## :biking\_man: Getting Started

### :yellow\_circle: Prerequisites

This project uses multiple pre-trained models, besides the requirements to run (backend/frontend). You can start by using the helper scripts to download a light model and install all requirements, before running:

```sh
sh scripts/start.sh
```

### :wrench: Run for Development

*   Clone this repository

```sh
git clone https://github.com/ahr9n/quranic-search-v2.git
cd quranic-search-v2
```

:red\_circle: *All commands must be executed in the root of the project.*

*   Run all services (lexical API, semantic API, then frontend)

```sh
sh scripts/run.sh
```

*   Navigate to `http://localhost:3000` <br/>

:green\_circle: *Now you are good to go!*

:red\_circle: *Notice that all servers shall be running in the background using the scripts, so you can close all of them using the following command:*

```sh
sh scripts/down.sh
```

## :hatching\_chick: Contributors
<table>
  <tr>
    <td align="center"><a href="https://github.com/OmarShamkh"><img src="https://avatars.githubusercontent.com/u/44472968?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Omar Shamkh</b></sub></a><br /><a href="https://github.com/ahr9n/quranic-search-v2/commits?author=OmarShamkh">💻</a></td>
    <td align="center"><a href="https://github.com/mograby3500"><img src="https://avatars.githubusercontent.com/u/25778262?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ahmad Almaghraby</b></sub></a><br /><a href="https://github.com/ahr9n/quranic-search-v2/commits?author=mograby3500">💻</a></td>
    <td align="center"><a href="https://github.com/ahr9n"><img src="https://avatars.githubusercontent.com/u/52632898?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ahmad Abdulrahman</b></sub></a><br /><a href="https://github.com/ahr9n/quranic-search-v2/commits?author=ahr9n">💻</a></td>
    <td align="center"><a href="https://github.com/AbdeltwabMF"><img src="https://avatars.githubusercontent.com/u/55063723?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Abd El-Twab M. Fakhry</b></sub></a><br /><a href="https://github.com/ahr9n/quranic-search-v2/commits?author=AbdeltwabMF">💻</a></td>
    <td align="center"><a href="https://github.com/ahmadateya"><img src="https://avatars.githubusercontent.com/u/32394857?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ahmad Ateya</b></sub></a><br /><a href="https://github.com/ahr9n/quranic-search-v2/commits?author=ahmedateya">💻</a></td>
  </tr>
</table>

## :warning: License

Licensed under the [GPL-v3](LICENSE) License.
