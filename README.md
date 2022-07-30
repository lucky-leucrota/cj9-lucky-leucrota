<img src="https://github.com/lucky-leucrota/cj9-lucky-leucrota/blob/a05fbdd57ca5c576d1937ee868c1316f220f04e7/src/static/images/logo.png" alt="Dis-Code" width="256" height="256">

# Dis-Code

A chat app made with FastAPI under 10 days, which has tendancy(20%) to forget to decrpyt the messages.

## Running/developing

> Also remember to rename the `chat.log.example` file to `chat.log`

## with Virutalenv

Just fork and clone this and open the folder then run the below to build,
```bash
#windows
.\venv\Scripts\activate
```

To run the project run this,
```bash
uvicorn src.main:app --host '0.0.0.0' --port 8000
```

### With Docker

just fork and clone this and open this folder.
then run this to build,
```bash
$ docker build -t projectimage .
```

After it's built use this to run it.
```bash
$ docker run -d --name projectcontainer -p 80:80 projectimage
```

## Authors

[Lucky-Leucrota]("https://github.com/lucky-leucrota")
