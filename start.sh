#!/bin/bash
# ------------------------
# Start React + Django app
# ------------------------

cd backend || exit
# activate virtual environment
ls
source ./venv/bin/activate
# apply migrations
python manage.py migrate

cd ..
cd frontend || exit
npm install

echo "Starting Django backend..."
echo "$PWD" | pbcopy
# go to backend folder
cd backend || exit
# activate virtual environment
source ./venv/bin/activate
# run backend in background
python manage.py runserver &
BACKEND_PID=$!

echo "Django backend started with PID $BACKEND_PID"
cd ..
echo "Starting React frontend..."
cd frontend || exit
npm start &
FRONTEND_PID=$!

echo "React frontend started with PID $FRONTEND_PID"

# Wait for both processes
wait $BACKEND_PID $FRONTEND_PID

%cd%
%cd%
