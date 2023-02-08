docker-compose up -d --build

# docker-compose exec web 
# python py_kakeibo/manage.py migrate
# docker-compose exec web bash | curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh
exit

docker-compose exec web nvm install --lts 
docker-compose exec web nvm use --lts