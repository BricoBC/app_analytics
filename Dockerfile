# app/Dockerfile

FROM python:3.9-slim-bullseye

WORKDIR /app

COPY . .

RUN  pip install --upgrade pip

RUN pip install -r requirements.txt 

RUN pip	install streamlit --upgrade

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]