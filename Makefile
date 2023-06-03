compose-up-d:
	docker-compose -f docker-compose.prod.yml up -d --build
compose-down:
	docker-compose -f docker-compose.prod.yml down -v
compose-up:
	docker-compose -f docker-compose.prod.yml up --build
collect:
	docker-compose -f docker-compose.prod.yml exec -u 0 web python manage.py collectstatic --no-input --clear
compose-logs:
	docker-compose -f docker-compose.prod.yml logs
