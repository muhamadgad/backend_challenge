	<h1  align="center">backend-challenge</h1>

Muhammad Gad ([muhammadabdelfattah](https://github.com/muhammadabdelfattah))

## Table of Contents <!-- omit in toc -->

- [About the challenge](#about-the-challenge)
- [App overview](#app-overview)
- [Technologies used](Technologies-used)
- [Quick Start](#Quick-Start)
  - [Requirements](#requirements)
  - [Install](#Install)
- [Documentation](#Documentation)
- [End Points](#Entry-points)


## About the challenge

[Gemography backend-coding-challenge](https://github.com/hiddenfounders/backend-coding-challenge) is about creating REST microservice that list the languages used by the 100 trending public repos on GitHub.
- For every language, we need to calculate the attributes below 👇:
    - Number of repos using this language
    - The list of repos using the language
    - Framework popularity over the 100 repositories

## App overview

This is a simple REST API that lists the list of the languages used by the 100 based on a straightforward algorithm which is the most starred repositories created last month.

## Technologies used

	- Flask			    : lightweight WSGI web application framework
	- Flask-swagger-ui	: for the documentation

## Quick Start

### Requirements
	- Docker
	- Web browser (chrome)
### Install
1. clone the project
	`git clone https://github.com/muhammadabdelfattah/backend_challenge.git`
2. cd into project directory
	`cd backend_challenge`
3. Build docker image of the API
	`docker build -t app_flask .`
4. Run the docker container
	`docker run -it -d -p 5000:5000 app_flask`

Now the API is working on [http://localhost:5000/trending_languages](http://localhost:5000/trending_languages)

## Documentation

The documenation is built with Swagger UI, A beautiful and interactive documentation
check this url [documentation](http://localhost:5000/docs)

## Entry points
| Entry point | description|
|-------------|-----------|
|/trending_languages   | list all languages in 100 trending github repos
|/docs				   | swagger documentation for the api