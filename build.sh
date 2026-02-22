cd backend || exit
# activate virtual environment
source ./venv/bin/activate
# apply migrations
python manage.py migrate

cd ..
cd frontend || exit
npm install