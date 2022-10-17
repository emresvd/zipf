@echo off
rd /s /q build
rd /s /q dist
del zipf.spec
pyinstaller --name=zipf main.py
adk main.py
ren main.aen zipf.aen