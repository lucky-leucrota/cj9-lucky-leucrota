<img src="src/static/images/logo-256.png" alt="Dis-Code" style="display: block; margin: 0 auto" />

# Dis-Code

A chat app made with FastAPI under 10 days, which has tendancy to forget to decrpyt the messages.

> Production is just to view the UI and the Code Runner. WebSockets don't work in Vercel.

### Features

- A full UI, with member count and an editor to write python code
- A full python code runner with the standard library

## Running / Development 🤖

### With Virutal Environment

Just fork or clone this repo and open the folder, then run the below to commands,

```bash
#windows
py -m venv venv
```

```bash
#linux
python3 -m venv venv
```

Activate virutal environment

```bash
.\venv\Scripts\activate
```

Install dependencies

```bash
pip install -r dev-requirements.txt
```

To run the project,

```bash
uvicorn src.main:app --host '0.0.0.0' --port <any-port-number-you-want>
```

Now visit `localhost:<the-port-you-have-chosen>`

### With Docker

Just fork or clone this repo and open the folder,
then run this to build,

```bash
$ docker build -t projectimage .
```

After it's built use this to run it.

```bash
$ docker run -d --name project_container_name -p 80:80 projectimage
```

Now visit `localhost`

### With Heroku

Just fork or clone this repo and open the folder, and uncomment line `45` and comment out line `47` in the `src/static/js/script.js` file,
And rename `dev-requirements.txt` to `requirements.txt`

### With Vercel

> Vercel can't do WebSockets so you can't use this with Vercel.
> but if your gonna do it anyway here are some instructions.

Fork and clone this. Edit the `src/static/js/script.js` file and uncomment line `47` and comment out line `45` and rename `dev-requirements.txt` to `requirements.txt`

then run this to deploy it to vercel,

```bash
$ vercel
```

## Authors

[Lucky-Leucrota](https://github.com/lucky-leucrota)
