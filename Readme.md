# Readme

PLease flow the steps to setup this project

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirement list. In the downloaded folder you can see requirement.txt file.

First create virtualenv named realworld

```bash

cd realworldautomation
python3 -m realworld

```
Now go the script directory in newly created folder realworld and activate the virtual environment

```bash

cd realworld/Scripts
activate

```

Here all dependencies can be installed via requirements.txt file

```bash

pip install -r requirements.txt

```

Running the a single test

```bash

cd realworldautomation
python test_articles.py

```

Running all test from the project will use pytest

```bash

pytest

```

Running all test from particular test module and particular test case

```bash

pytest test_file.py::TestClass::test_method

pytest test_articles.py::QureAIArticleTest::test_create_new_article_with_same_name

```

## Test Cases

Login Test cases are covered in ==test_login.py== file

| Syntax | Description |
| ----------- | ----------- |
| Header | Title |
| Paragraph | Text |

Article Test cases are covered in ==test_article.py== file

| Syntax | Description |
| ----------- | ----------- |
| Header | Title |
| Paragraph | Text |

SignUp Test cases are covered in ==test_signup.py== file

| Syntax | Description |
| ----------- | ----------- |
| Header | Title |
| Paragraph | Text |