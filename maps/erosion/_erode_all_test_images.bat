@echo off
setlocal

set "SCRIPT_DIR=%~dp0"
pushd "%SCRIPT_DIR%" || exit /b 1

call :erode "test_blob.png" || goto :fail
call :erode "test_blob_large.png" || goto :fail
call :erode "blurry continent.png" || goto :fail

popd
echo Done.
exit /b 0

:erode
echo Eroding %~1
python "%SCRIPT_DIR%_erode_heightmap.py" "%~1"
exit /b %ERRORLEVEL%

:fail
set "STATUS=%ERRORLEVEL%"
popd
exit /b %STATUS%
