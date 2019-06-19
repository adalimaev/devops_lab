#!/bin/bash

if [ ! -d "$HOME/.pyenv/versions/2.7.0" ]
then
	pyenv install 2.7.0;
fi
if [ ! -d "$HOME/.pyenv/versions/3.7.0" ]
then
	pyenv install 3.7.0;
fi
if [ ! -d "$HOME/.pyenv/versions/2.7.0/envs/python2env" ]
then
	pyenv virtualenv 2.7.0 python2env;
fi
if [ ! -d "$HOME/.pyenv/versions/3.7.0/envs/python3env" ]
then
	pyenv virtualenv 3.7.0 python3env;
fi

echo "Checking:";
pyenv versions | grep python.env

