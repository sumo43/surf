cp ext/native_messaging.json ~/Library/"Application Support"/Google/Chrome/NativeMessagingHosts/_com.surf.surf_search.json
echo "installed chrome native messaging host..."

chmod o+r ~/Library/"Application Support"/Google/Chrome/NativeMessagingHosts/_com.surf.surf_search.json
echo "fixed permissions for native host..."

alias "surf_start"="python3 $(pwd)/main.py"
echo "created alias for surf client..."
