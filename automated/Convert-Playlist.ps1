# These variables here represent the arguments to be passed to the convert-playlist.py script.
# Modify them to suit your automation needs.
$args = [PSCustomObject]@{
    SourcePlaylistDir = "D:\Temp\mlu\convert-playlists-in"
    OutputPlaylistDir = "D:\Temp\mlu\convert-playlists-out"
    OldRoot = 'Z:\'
    NewRoot = '/datastore/nick/'
}

# Locate the convert-playlists.py script from here in this dir
$projectDir = (Get-Item -Path $PSScriptRoot).Parent.FullName
$scriptPath = Join-Path -Path $projectDir -ChildPath 'scripts\convert-playlist.py'

# Run the script with our arguments using python
python $scriptPath $args.SourcePlaylistDir $args.OutputPlaylistDir $args.OldRoot $args.NewRoot

