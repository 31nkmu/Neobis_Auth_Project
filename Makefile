.SILENT:
.PHONY: compose-up
compose-up:
	docker-compose -f docker-compose.prod.yml --env-file .env/.env.prod up -d --build

.PHONY: compose-start
compose-start: compose-up
	docker-compose -f docker-compose.prod.yml --env-file .env/.env.prod exec -u 0 web python manage.py collectstatic --no-input --clear

.PHONY: compose-down
compose-down:
	docker-compose -f docker-compose.prod.yml --env-file .env/.env.prod down -v

.PHONY: compose-logs
compose-logs:
	docker-compose -f docker-compose.prod.yml --env-file .env/.env.prod logs -f




.PHONY: up
up:
	docker-compose -f docker-compose.yml --env-file .env/.env.dev up -d --build

.PHONY: down
down:
	docker-compose -f docker-compose.yml --env-file .env/.env.dev down -v

.PHONY: logs
logs:
	docker-compose -f docker-compose.yml --env-file .env/.env.dev logs -f

.PHONY: ps
ps:
	docker-compose -f docker-compose.yml --env-file .env/.env.dev ps -a
