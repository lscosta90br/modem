# Como clonar o repositorio
```
git clone git@github.com:lscosta90br/modem-timlive.git
cd modem-timlive
poetry install
poetry shell
```

## Colocando em produção
```
# criando o diretório da aplicação
mkdir /u00/app/modem-timlive

# copiando os arquivos para o diretorio de produção
cp requirements.txt verifica_modem-timlive.py config.py /u00/app/modem-timlive
cp .secrets-exemplo.toml /u00/app/modem-timlive/.secrets.toml
cp settings-exemplo.toml /u00/app/modem-timlive/settings.toml

# Criando o arquivo requirements.txt
poetry export -f requirements.txt --output requirements.txt
```

## Baixando versao Selenoid
```
baixar https://github.com/aerokube/cm/releases/tag/1.7.2
$ mv cm_linux_amd64 cm
$ chmod +x cm
```

## iniciando ambiente remoto Selenoid
```
./cm selenoid start
./cm selenoid-ui start
```

## Criando ambiente virtual python
```
python -m venv .venv  
source .venv/bin/activate                
pip install -r requirements.txt 
```

## criando arquivo /usr/local/bin
```
#!/usr/bin/env bash

#variaveis da aplicação
#DIR_APPS="/home/lc/projects/py/modem-timlive"
DIR_APPS="/u00/app/modem-timlive"
PYTHON_VENV="$DIR_APPS/.venv/bin/python"
APLICACAO="$DIR_APPS/verifica_modem-timlive.py"

#execucao da aplicação
cd $DIR_APPS
$PYTHON_VENV $APLICACAO
```

## Create a new repository on the command line
```
echo "# modem-timlive" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:lscosta90br/modem-timlive.git
git push -u origin main
                
## Push an existing repository from the command line
…or push an existing repository from the command line
git remote add origin git@github.com:lscosta90br/modem-timlive.git
git branch -M main
git push -u origin main
```