@echo off

set uploaddir=src

( 
    echo ===============================================================
    echo  GAEBot uploader
    echo ===============================================================
    echo.
    echo please input your appid
) && (
    @cd /d "%~dp0" 
) && (
    set PYTHONSCRIPT="import sys;sys.path.insert(0, 'uploader.zip');import appcfg;appcfg.main()"
) && (
    ".\py.exe"
) && (
    echo.
    echo GAEBot uploaded, press any to exit.
)

@pause>NUL

@echo off