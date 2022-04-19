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

| Test Name | Description |
| ----------- | ----------- |
| test_signin_pass | test to check user login with correct credntials |
| test_signout_pass | test to check user can logout after successfull login |
| test_signin_fail | test to check user login with wrong credentials |

Article Test cases are covered in ==test_article.py== file

| Test Name | Description |
| ----------- | ----------- |
| test_create_new_article | test to check if user can login and create new article |
| test_create_new_article_with_same_name | test to check if user can login and create new article with not unique title |
| test_comment_on_article | test to check if user can comment on the article |
| test_tags_on_article | test to check if clicking on tag gives article with same tags |
| test_fav_count_on_article | test for checking user can click fav button and check the count change |

SignUp Test cases are covered in ==test_signup.py== file

| Test Name | Description |
| ----------- | ----------- |
| test_signup_pass | test to check if user can register with fresh username and email |
| test_signup_fail | test to check if user uses already taken username then it should not get registered |