# Pokuz

For people want to hack on awesome Buku bookmark CLI and Pocket !!

## Contributions:

* Update poku python package for new Pocket API

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

## Work best with

1. Chrome extension: Bukubrow
https://chrome.google.com/webstore/detail/bukubrow/ghniladkapjacfajiooekgkfopkjblpn?hl=en


2. Chrome browser native messaging for connecting CLI and Chrome
https://github.com/SamHH/bukubrow-host
bukubrow --install-chrome

## Based on 

(poku)
https://github.com/shanedabes/poku

(package)
https://github.com/cookiecutter/cookiecutter
https://github.com/audreyr/cookiecutter-pypackage
