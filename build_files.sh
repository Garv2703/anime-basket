# build_files.sh
python -m ensurepip
pip install -r requirements.txt

# make migrations
python3.12 manage.py migrate 
python3.12 manage.py collectstatic