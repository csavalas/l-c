pip3 install -r requirements.txt
Copy-Item -Path .\WindowsPowerShell\ -Destination "$Home\Documents\WindowsPowerShell\" -Recurse
Write-Output "Please restart terminal for changes to take effect."
Write-Output "[Press any key to continue]"
Read-Host