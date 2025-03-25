# Обязательно в реализации
# - Цели НЕ менять
# - Зависимости и сценарии поменять на необходимые

# Рекомендуется проект выстраивать вокруг собственных сценариев сборки
# Рекомендуется в этом файле оставить только свои вызовы "make build",
# "cmake .", "msBuild proj1.sln ./out" и операции копирования

# Сценарий интерфейса специально не носит название "makefile" -
# Вы можете отсюда обращаться к своим сценариям


# Положить на проверку ИЛИ собрать на сервере pdf отчёта
# Допускается использование libreoffice, latex, xelatex
ready/report.pdf: report/report.pdf
	mkdir -p ./ready
	cp report/report.pdf ready/report.pdf

# Положить на проверку уже загруженный в репозиторий отчёт тестирования
#
# Пример содержимого:
#
# {
#     "timestamp": "2024-07-14T19:46:32+03:00",
#     "coverage": 0.1,
#     "passed": 1,
#     "failed": 0
# }
#
# "timestamp" - дататаймштамп в формате UTC с указанием зоны dtst=$(date +"%Y-%m-%dT%H:%M:%S%:z")
# "coverage" - покрытие в процентах
# "passed" - число пройденных модульных тестов при последнем тестировании
# "failed" - число проваленных модульных тестов при последнем тестировании
#
# При невозможности/нежелании генерировать такой файл автоматически допускается ручное заполнение "на глаз" с одним тестом и минимальным покрытием

ready/stud-unit-test-report-prev.json: code/stud-unit-test-report-prev.json
	mkdir -p ./ready
	cp code/stud-unit-test-report-prev.json ready/stud-unit-test-report-prev.json

ready/stud-unit-test-report.json:
	mkdir -p ./ready
	cp code/stud-unit-test-report-prev.json ready/stud-unit-test-report.json


# Собрать приложение на компилируемом языке прямо на сервере
ready/app-cli-debug:
	mkdir -p ./ready


# Очистка
.PHONY: clean
clean:
	echo OK

# --

# Если хочется добавить в образ на сервере что-то,
# можно обратиться к @alexodnodvorcev прямо в комментарии к MR.

# --

# Реализация по желанию - удалить цели, если нет реализации

# Сборка и запуск модульных тестов прямо на сервере


