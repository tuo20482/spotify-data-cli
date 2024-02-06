# Spotify Data CLI

## Introduction
This project is a command-line interface (CLI) application that allows users to fetch the top tracks of a given artist on Spotify. It utilizes the Spotipy library to interact with the Spotify Web API and Typer for the CLI component.

## Prerequisites
- Python 3.8 or higher
- A Spotify Developer account and your own Client ID and Client Secret for accessing the Spotify Web API

## Installation
1. Clone this repository to your local machine.
2. Navigate to the cloned directory.
3. It is recommended to create a virtual environment for this project:
```
python -m venv venv
```
4. Activate the virtual environment:
- On Windows:
  ```
  .\venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```
5. Install the required dependencies:
```
pip install spotipy typer
```

## Configuration
Before running the application, you need to set up your Spotify API credentials. Set your Client ID and Client Secret as environment variables:
- On Windows:
```
set SPOTIPY_CLIENT_ID=your_client_id_here
set SPOTIPY_CLIENT_SECRET=your_client_secret_here
```
- On macOS and Linux:
```
export SPOTIPY_CLIENT_ID=your_client_id_here
export SPOTIPY_CLIENT_SECRET=your_client_secret_here
```

## Running the Application
To run the application, use the following command:
```
python main.py "artist name"
```
