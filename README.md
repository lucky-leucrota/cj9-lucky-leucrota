<img src="src/static/images/logo-256.png" alt="Dis-Code" style="display: block; margin: 0 auto" />

# Dis-Code

A chat app made with FastAPI under 10 days, which has tendancy to forget to decrpyt the messages.

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

## Authors

[Lucky-Leucrota](https://github.com/lucky-leucrota)
