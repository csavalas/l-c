# <code>l</code>/<code>c</code> (fast <code>ls</code>/<code>cd</code> replacements)

<hr>

# Installation Instructions
* Install Python <span style="color:red">3.\*</span>
* run <code>./setup.sh</code> (or <code>./setup.ps1</code> for Windows) then restart your terminal.
## Supported Platforms
* Linux _(bash)_
* macOS _(zsh)_
* Windows _(Terminal:Powershell)_
# Usage Instructions
## General note
* Since <code>l</code> can quickly copy an entry to the clipboard, it can be used in conjunction  
with other commands to avoid mouse input or slow transcription, eg, <code>code \<clipboard-contents\></code>.
## <code>l</code> command
* General
    * The output of <code>l</code> will enumerate the result of the query (detailed below)
    * The selected number will copy the corresponding dir/file to clipboard
    * Directories are listed 
    * _NOTE: All entries are accessible to cx by number regardless of selection_
* Query Examples (inexhaustive)
    * NOTE: <code>*</code>'s must be escaped in macOS/Linux
        * eg. <code>l dir/subdir/\*.png</code> would be written <code>l dir/subdir/<span style="color:red">\\</span>\*.png</code> 
    * <code>l</code>
        * Lists contents of current directory
        * Items copied to the clipboard will not include full path
    * <code>l .</code>
        * Lists contents of current directory
        * Items copied to the clipboard will include full path        
    * <code>l \*.png</code>
        * lists all pngs in current directory
        * Items copied to the clipboard will not include full path
    * <code>l \<dir name\>/*/</code>
        * lists all directories contained within \<dir name\>
        * Items copied to the clipboard will include full path

## <code>c</code> command
* Examples
    * <code>c</code>
        * Changes to the directory stored in the clipboard
    * <code>c \<index #\></code>
        * Changes to the directory corresponding an index # in the last run of <code>l</code>
    * <code>c \<dir name/path\></code>
        * Changes to \<dir name/path\>
    * <code>c ..</code>
        * Changes to the parent directory

<hr>