##

Update for new api returns for Pocket API

## Get AccessToken and ConsumerKey
1. https://getpocket.com/developer/apps/
2. copy consumer key

## Install

Source installl

    python setup.py install

or Package install

    pip3 install --upgrade pokuz buku

## Setup

- Help
    >poku --help

- Open browser from cli to authrize and get Access Key

    > poku --consumer CONSUMER_KEY

p.s.
    
    Make ~/.config/poku/*.cfg to look like
    access YOUR_ACCESS
    consumer YOUR_CONSUMER_KEY

## Importing
poku

## Wrap and Ship
python setup.py sdist

## Based on 

(poku)
https://github.com/shanedabes/poku

(package)
https://github.com/cookiecutter/cookiecutter
https://github.com/audreyr/cookiecutter-pypackage