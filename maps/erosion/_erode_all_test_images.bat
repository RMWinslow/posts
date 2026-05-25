@echo off
setlocal

set "SCRIPT_DIR=%~dp0"
pushd "%SCRIPT_DIR%" || exit /b 1

call :process "test_blob.png" || goto :fail
call :process "test_blob_large.png" || goto :fail
call :process "blurry continent.png" || goto :fail

popd
echo Done.
exit /b 0

:process
call :erode "%~1" || exit /b %ERRORLEVEL%
call :render "eroded_%~1" || exit /b %ERRORLEVEL%
exit /b 0

:erode
echo Eroding %~1
python "%SCRIPT_DIR%_erode_heightmap.py" "%~1"
exit /b %ERRORLEVEL%

:render
echo Rendering %~1
python "%SCRIPT_DIR%_render_heightmap.py" "%~1"
exit /b %ERRORLEVEL%

:fail
set "STATUS=%ERRORLEVEL%"
popd
exit /b %STATUS%
