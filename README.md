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
uvicorn src.app:app --host '0.0.0.0' --port 8000
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
