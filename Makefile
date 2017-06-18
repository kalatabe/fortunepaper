run_path = "$(CURDIR)/run.py"
user = "$(shell whoami)"

requirements:
	@sudo apt-get install wkhtmltopdf

cron:
	@chmod u+x $(run_path)
	@echo "@hourly $(user) $(run_path)" | crontab -
 
