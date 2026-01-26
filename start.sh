#!/bin/bash
uvicorn backEnd.main:app --host 0.0.0.0 --port $PORT

