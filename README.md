# GamerKids Books — Landing pages

Landings estáticas para los 6 libros del catálogo. HTML puro, sin build step, listo para Vercel.

## Estructura

```
landing/
├── build_landing.py     ← generador (fuente única de verdad)
├── index.html           ← catálogo /
├── minecraft/index.html ← /minecraft
├── minecraft-en/
├── roblox/
├── roblox-en/
├── clash/
├── clash-en/
├── assets/
│   ├── covers/          ← 6 portadas
│   └── logo.png
├── vercel.json          ← routing (cleanUrls)
└── README.md
```

## Editar copy / precios / links Bold

**Todo se edita en `build_landing.py`**, en el dict `BOOKS` arriba del archivo. Después corres:

```bash
python build_landing.py
```

Y los 7 archivos HTML se regeneran. Nunca edites los `index.html` a mano — se sobrescriben.

## Antes del primer deploy

En `build_landing.py`, reemplaza los 6 `REEMPLAZAR_BOLD_*` con los links reales de Bold:

```python
"bold_link": "https://checkout.bold.co/payment/LNK_XXXX",
```

Y vuelve a correr `python build_landing.py`.

## Deploy a Vercel

### Opción 1 — CLI (más rápido)

```bash
npm i -g vercel
cd landing
vercel
```

Al primer deploy Vercel te pregunta el nombre del proyecto → pon `gamerkidsbooks` → la URL queda `gamerkidsbooks.vercel.app`.

Los deploys siguientes son:
```bash
vercel --prod
```

### Opción 2 — drag & drop

1. Entra a `vercel.com/new`
2. Importa la carpeta `landing/` (puedes zipearla y subirla)
3. Framework preset: **Other** (es HTML estático)
4. Deploy

### Opción 3 — GitHub

1. Crea un repo con el contenido de `landing/`
2. Conecta en Vercel
3. Cada push redeploya automáticamente

## Probar local

Basta con abrir `landing/index.html` en el navegador, o:

```bash
cd landing
python -m http.server 8000
```

Luego abres `http://localhost:8000` — los clean URLs no funcionan local (necesitas `/minecraft/` con slash), pero sí después del deploy en Vercel.

## Añadir un libro nuevo

1. Añade un dict al array `BOOKS` en `build_landing.py`
2. Añade la portada en `assets/covers/<slug>.png`
3. Añade el link de Bold
4. `python build_landing.py`
5. Deploy

## Integración con flujo TikTok

```
TikTok: "Comenta MINECRAFT y te lo paso"
  ↓
DM automático con link:
  gamerkidsbooks.vercel.app/minecraft
  ↓
Usuario ve la landing → clic en "Comprar ahora"
  ↓
Bold checkout (Nequi, PSE, TC, transferencia)
  ↓
Mientras btn001 está abierto en Bold:
  tú recibes notificación de venta → respondes con PDF
  ↓
(Cuando Bold resuelva): redirect automático a /gracias/<slug>
  con link de descarga directa del PDF
```
