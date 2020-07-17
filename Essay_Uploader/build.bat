@ECHO OFF

REM Check for administrator Priviledges
net session >nul 2>&1
if %errorLevel% NEQ 0 (
	echo #############################
	echo  Please Run as Administrator
	echo #############################
	echo.
	pause
	exit
) 

set app_name=Essay_Uploader
set location=D:\Personal\Github_Essays_Repository\Essays\Essay_Uploader\

set rel_location=D:\Personal\Github_Essays_Repository\Essays\
set executable_location=D:\Personal\Github_Essays_Repository\Essays\Essay_Uploader\dist\%app_name%\%app_name%.exe


if exist %location%\build\ (

	del %location%*.spec
	rmdir %location%build /Q /S 
	rmdir %location%dist /Q /S
	
	del %rel_location%%app_name%.exe
)

py -m PyInstaller src\__main__.py --name %app_name% --noconsole --hidden-import=pkg_resources.py2_warn 

mklink %rel_location%%app_name%.exe %executable_location%
