# Simple Blog

This is an imaginary blog built in Django entirely for educational purposes. It is traditional MVC style application.

### How to run it locally?

It is fairly simple thanks to docker. Simply run this command after **cloning the repository**.

```sh
docker compose -f docker-compose.dev.yml up --build --watch
```

If you want to seed the database with sample data you can also run this command.

```sh
docker compose -f docker-compose.dev.yml exec app python manage.py seed_db
```

That's all! Now simply hit [http://localhost:8000](http://localhost:8000) and explore.
