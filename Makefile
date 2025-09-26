SHELL := /bin/zsh
.SHELLFLAGS := -c
up:
	source ~/.zshre && workon erb7 && \
	work
	python manage.py runserver

static:
	python manage.py collectstatic