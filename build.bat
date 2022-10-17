@echo off
rd /s /q build
rd /s /q dist
del zipf.spec
del zipf.aen
pyinstaller --name=zipf main.py
adk main.py
ren main.aen zipf.aen