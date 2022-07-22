# CodeJam 2022 Project Repository

This is the app We're making.

## Running/developing

## with Virutalenv

Just fork and clone this and open the folder then run the below to build,
```bash
#windows
.\venv\Scripts\activate
```

To run the project run this,
```bash
uvicorn app.main:main --host '0.0.0.0' --port '80'
```

### With Docker

just fork and clone this and open this folder.
then run this to build,
```bash
$ docker build -t projectImage .
```

After it's built use this to run it.
```bash
$ docker run -d --name projectContainer -p 80:80 projectImage
```
