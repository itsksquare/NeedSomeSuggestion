from fastapi import FastAPI
from API.utils.DBConnection import DBConnection

app=FastAPI(title="Recommender System Website API")

from API import fwapp