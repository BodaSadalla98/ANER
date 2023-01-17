#!/bin/bash
fuser -k 7777/tcp



aner_dir=$PWD/model/ours
camel_dir=$HOME/.camel_tools


# ## Check for our model
# if [ ! -d "$aner_dir" ]; then
#   echo "ANER dir does not exist. creating it now"
#   mkdir -p $aner_dir
# fi


## checks is the dir is empy
if [ -z "$(ls -A $aner_dir)" ]; then
echo "Downloading ANER model"
#V2 model
gdown https://drive.google.com/file/d/1Ebvc67HJQ5I9M6LfdzAiOVx5iiyVO9LN/view?usp=share_link -O $aner_dir/model.pt --fuzzy
# V5 model
# gdown https://drive.google.com/file/d/1JkL0-o3WIR1bOHTKZd38pFDOqEplb4ng/view?usp=sharing -O $aner_dir/model.pt --fuzzy
fi


## check for Camel model
if [ ! -d "$camel_dir" ]; then
    echo "Camel tools dir does not exist. creating it now"
fi

if [ -z "$(ls -A $camel_dir)" ]; then
gdown https://drive.google.com/file/d/1k5595oEmAq7qcM6aEBQMWfQ2TiFDRExo/view?usp=share_link --fuzzy -O camel_tools.tar.xz
tar -xvf camel_tools.tar.xz 
mv camel_tools $camel_dir
# mkdir -p $camel_dir

fi

# mkdir -p $camel_dir
# cp -r model/camel/camel_tools/* $camel_dir/

# # ls $camel_dir
# # ls /root/.camel_tools 
# # cp -r   $camel_dir /root/.camel_tools 
# # ls $camel_dir
# # ls /root/.camel_tools 


export CAMELTOOLS_DATA=$camel_dir
## Run
python app.py 