# If there is a CLA...
if [ $# -ne 0 ]; then
    re='^[0-9]+$'
    # It's a path, so cd directly into it...
    if ! [[ $1 =~ $re ]]; then
        cd "${1}"
    # It's a number, so cd into the corresponding directory in l.json
    else
        name="$(jq -r ".[$1]" < ~/l/l.json)" 
        cd "$name"
    fi
# There is no CLA...
else
    # Get data from clipboard
    choice="$(xclip -o -sel clip)"
    # Cut trailing '
    choice=${choice%?}
    # Cut leading '
    choice="${choice:1}"    
    # Change directory
    cd "${choice}"
fi