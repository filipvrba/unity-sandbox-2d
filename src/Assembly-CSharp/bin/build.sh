#!/bin/bash
. ./bin/common.lib
 
build_dll()
{
    dotnet build &&\
    copy_dll
}
 
copy_dll()
{
    echo "Copy Assembly-CSharp.dll to the original game."
 
    cp bin/Debug/net35/Assembly-CSharp.dll \
    $PATH_GAME/Sandbox_Data/Managed/Assembly-CSharp.dll &&\
    open_windows
}
 
build_dll
