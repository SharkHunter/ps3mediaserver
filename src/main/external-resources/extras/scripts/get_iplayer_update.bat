@echo off
set str=%0
set str=%str:bat=pl%
set str=%str:_update=%
del c:\tmp\list
extras\perl\bin\perl.exe %str% --xml-alpha --mythtv c:\tmp\list 