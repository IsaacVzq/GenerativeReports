FROM python:3.8.4-slim-buster
RUN  pip install requests
RUN  pip install openpyxl
RUN  pip install load_dotenv

WORKDIR /usr/app/src
copy generate_report_OpenSea.py ./
CMD ["python3" ,"./generate_report_OpenSea.py"]
# RUN pip install -r requirements.txt