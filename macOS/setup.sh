echo "Installing jq..."  
brew install jq

cp -R ./l ~/l
cd ~

printf "\nalias l='python3 ~/l/l.py'\n" >> .zprofile
printf "alias c='. ~/l/c.sh'\n" >> .zprofile

echo "Please restart terminal for changes to take effect"
echo "[Press any key to continue]"
read nil