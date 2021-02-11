# Criação do virtual env

```
cd desktop
python -m venv .venv
.venv/Scripts/Activate.ps1
```

Instalação do kivy e dependências para windows.

> https://kivy.org/doc/stable/guide/packaging-windows.html

```
python -m pip install --upgrade pip wheel setuptools

python -m pip install kivy docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew kivy.deps.gstreamer kivy.deps.angle

python -m pip install PyInstaller
```

# Primeiro build

```
PyInstaller --name teste .\desktop\main.py
```

# Configurar o Spec para onefile

No spec gerado, `teste.spec`, Remova o COLL e Deixe o EXE como mostrado abaixo.

```python
# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew
...
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)], #para gerar o SDL2
          name='teste', #substitua pelo nome do seu pacote
          debug=False,
          bootloader_ignore_signals=False,
          upx=True,
          console=False, #Esconde o console que abre junto a janela
          strip=False,
          upx_exclude=[],
          )
```

# Build do teste.spec

```
PyInstaller teste.spec
```

## compatibilidade com opengl 1.1

```python
#main.py
from kivy import Config

Config.set('graphics', 'multisamples', '0')
```

# compilação com kivymd

Alterar .spec para inserir os hooks do kivy md

```python
# -*- mode: python ; coding: utf-8 -*-
from kivymd import hooks_path
a = Analysis(
        ...,
        hookspath=[hooks_path],
        ...
)
```
