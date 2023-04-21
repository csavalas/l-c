# This contains the list of files from the last run of the l command
$pathToJson = "$Home\Documents\WindowsPowerShell\l\l.json"
# Read content into a list
$json = Get-Content $pathToJson | ConvertFrom-Json
# If the user entered a CLA...
if ($($args.Length) -gt 0) {
    # The user entered a number, so cd to that number's corresponding dir   
    if ($args[0] -is [int]) {
        $choice = $args[0]
        Set-Location $json[$choice]
    # The user did not enter a number, so cd to their literal input           
    } else {
        Set-Location $args[0]
    }
# If no CLA, cd to the directory stored on the clipboard
} else {
    $choice = Get-Clipboard
    $choice = $choice.Substring(1)
    $choice = $choice.Substring(0,$choice.Length-1)
    Set-Location "$choice"
}
