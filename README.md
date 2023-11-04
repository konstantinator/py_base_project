# Py_base_project

## Files and Folders

- `app.py`: streamlit app file
- `requirements.txt`: package requirements files
- `Dockerfile` for docker deployment
- `notebook` data extractor and model learning
- `data` source data
- `models` tf-idf transform and catboost model


## Run Demo Locally 

### Shell

For directly run streamlit locally in the repo root folder as follows:

```shell
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ streamlit run app.py
```
Open http://localhost:8501 to view the app.

### Docker

For build and run the docker image named `st-demo`:

```
$ docker build -t st-demo .
$ docker run -it --rm -p '8501:8501' st-demo
```

`-it` keeps the terminal interactive

`--rm` removes the image once the command is stopped (e.g. using control + c)

Open http://localhost:8501/ to view the app.

## Streamlit Cloud Deployment
 
1. Put your app on GitHub (like this repo)
Make sure it's in a public folder and that you have a `requirements.txt` file.
 
2. Sign into Streamlit Cloud
Sign into share.streamlit.io with your GitHub email address, you need to have access to Streamlit Cloud service.
 
3. Deploy and share!  
Click "New app", then fill in your repo, branch, and file path, choose a Python version (3.10 for this demo) and click "Deploy", then you should be able to see your app.