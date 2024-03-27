call config.cmd

@REM Startup
doskey init=%IDEA_HOME%\bin\idea64.exe $T notepad++.exe $T code

@REM GIT COMMANDS
doskey gpod=git pull origin develop
doskey gp=git pull
doskey gco=git checkout $*
doskey gpc=git pull $T git checkout $*
doskey gcp=git checkout $* $T git pull
doskey gss=git stash save $*
doskey gsa=git stash apply $*

@REM CREATE PYTHON VENV
doskey cpyvenv=i:\ds\tools\python3.10\latest\python.exe -m venv "venv_$1"

@REM NPM COMMANDS
doskey nrs=npm run start
doskey nrb=npm run build
doskey nrbs=npm run build $T npm run start

@REM RUN PYTHON UNIT TEST
doskey rput=coverage run -m unittest discover tests $T coverage xml $T nosetests --with-xunit $T coverage html
