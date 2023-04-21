echo "Installing xclip..."  
sudo apt-get update
sudo apt-get install xclip
echo "Installing jq..."  
sudo apt-get install jq

cp -R ./l ~/l
cd ~

printf "\nalias l='python3 ~/l/l.py'\n" >> .bashrc
printf "alias c='. ~/l/c.sh'\n" >> .bashrc

echo "Please restart terminal for changes to take effect"
echo "[Press any key to continue]"
read nil