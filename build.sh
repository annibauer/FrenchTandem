cd backend || exit
# activate virtual environment
pip install requirements.txt
source ./venv/bin/activate
# apply migrations
python manage.py migrate

cd ..
cd frontend || exit
npm install