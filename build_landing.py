"""
build_landing.py — Genera las 6 landing pages de GamerKids Books.

Lee la configuracion BOOKS de abajo y produce:
  - index.html            (catalogo con los 6 libros)
  - <slug>/index.html     (una landing por libro)

Uso:
    python build_landing.py

Las landings usan HTML + Tailwind CDN + CSS inline. No requiere npm ni build step.
Se despliega directo a Vercel arrastrando la carpeta `landing/` o con `vercel deploy`.
"""

from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).parent

# ---------------------------------------------------------------------------
# Configuracion global de contacto
# ---------------------------------------------------------------------------

WA_NUMBER = "573214536735"  # Colombia, sin + ni espacios (formato wa.me)


def wa_link(book_title_for_msg, lang):
    """Construye el enlace wa.me con mensaje pre-llenado por libro."""
    if lang == "es":
        msg = (
            f"Hola GamerKids! 🎮 Compré *{book_title_for_msg}* y adjunto "
            f"el comprobante de pago. ¿Me envían el PDF? ¡Gracias!"
        )
    elif lang == "pt":
        msg = (
            f"Oi GamerKids! 🎮 Comprei *{book_title_for_msg}* e envio "
            f"o comprovante de pagamento. Podem me mandar o PDF? Obrigado!"
        )
    else:
        msg = (
            f"Hi GamerKids! 🎮 I just bought *{book_title_for_msg}* and "
            f"I'm attaching my payment receipt. Can you send me the PDF? Thanks!"
        )
    return f"https://wa.me/{WA_NUMBER}?text={quote(msg)}"


# ---------------------------------------------------------------------------
# Datos de los 6 libros — fuente unica de verdad
# ---------------------------------------------------------------------------

BOOKS = [
    {
        "slug": "minecraft",
        "lang": "es",
        "title": "El Gran Libro de Aventuras en Minecraft",
        "subtitle": "Guía para Pequeños Exploradores 7-10 años",
        "theme": "minecraft",
        "price_usd": 7,
        "price_cop": "25.000",
        "cover": "/assets/covers/minecraft-es.png",
        "bold_link_cop": "https://checkout.bold.co/payment/LNK_ZCXX893OSL",
        "bold_link_usd": "https://checkout.bold.co/payment/LNK_1HZ6LB90I2",
        "age": "7-10 años",
        "pages": 48,
        "illustrations": 10,
        "color_primary": "#4CAF50",
        "color_accent": "#8BC34A",
        "color_dark": "#1B5E20",
        "tagline": "De jugador novato a explorador experto: la guía paso a paso que convierte a tu hijo en un verdadero sobreviviente de Minecraft.",
        "hook_pain": "¿Tu hijo juega Minecraft todos los días pero no sabe qué hacer? ¿Se pierde, muere y se frustra?",
        "hook_promise": "Este libro lo lleva por niveles como en el juego. Aprende a sobrevivir, construir y jugar como un verdadero explorador.",
        "benefits": [
            "Entender el mundo de Minecraft (biomas, bloques, mobs)",
            "Sobrevivir la primera noche sin morir",
            "Conseguir comida, herramientas y refugio",
            "Encontrar minerales (carbón, hierro, diamante)",
            "Defenderse de creepers, zombies y esqueletos",
            "Construir su primera casa como experto",
        ],
        "includes": [
            "6 capítulos paso a paso (del principiante al experto)",
            "10 ilustraciones originales a todo color estilo Pixar",
            "Tips de seguridad online para jugar sin riesgos",
            "Glosario con todos los términos del juego",
            "Sección especial para padres con controles parentales",
        ],
    },
    {
        "slug": "minecraft-en",
        "lang": "en",
        "title": "The Big Book of Minecraft Adventures",
        "subtitle": "A Guide for Young Explorers Ages 7-10",
        "theme": "minecraft",
        "price_usd": 9,
        "price_cop": "36.000",
        "cover": "/assets/covers/minecraft-en.png",
        "bold_link_usd": "https://checkout.bold.co/payment/LNK_L2ERT0E2QJ",
        "age": "7-10 years",
        "pages": 48,
        "illustrations": 10,
        "color_primary": "#4CAF50",
        "color_accent": "#8BC34A",
        "color_dark": "#1B5E20",
        "tagline": "From beginner to expert explorer: the step-by-step guide that turns your child into a true Minecraft survivor.",
        "hook_pain": "Does your kid play Minecraft every day but doesn't know what to do? Gets lost, dies, and gives up?",
        "hook_promise": "This book takes them level by level like the game. They learn to survive, build, and play like a real explorer.",
        "benefits": [
            "Understand the Minecraft world (biomes, blocks, mobs)",
            "Survive the first night without dying",
            "Get food, tools, and shelter",
            "Find ores (coal, iron, diamond)",
            "Defend against creepers, zombies, and skeletons",
            "Build their first house like an expert",
        ],
        "includes": [
            "6 step-by-step chapters (from beginner to expert)",
            "10 original full-color Pixar-style illustrations",
            "Online safety tips for risk-free play",
            "Glossary with every game term explained",
            "Special parents section with parental controls",
        ],
    },
    {
        "slug": "clash",
        "lang": "es",
        "title": "Clash Royale para Pequeños Campeones",
        "subtitle": "Guía Estratégica para Niños 7-9 años",
        "theme": "clash",
        "price_usd": 7,
        "price_cop": "25.000",
        "cover": "/assets/covers/clash-es.png",
        "bold_link_cop": "https://checkout.bold.co/payment/LNK_Y8XM0TUUNH",
        "bold_link_usd": "https://checkout.bold.co/payment/LNK_M47D2F2UL8",
        "age": "7-9 años",
        "pages": 69,
        "illustrations": 11,
        "color_primary": "#0D3B7F",
        "color_accent": "#FFC107",
        "color_dark": "#06194A",
        "tagline": "La primera guía en español que enseña a los niños a jugar Clash Royale con cabeza: defender, construir mazos ganadores y pensar como un campeón.",
        "hook_pain": "¿Tu hijo pierde partida tras partida en Clash Royale y se frustra? ¿Gasta gemas sin estrategia y llora cuando lo eliminan?",
        "hook_promise": "Este libro le enseña a pensar como un verdadero campeón: defender antes de atacar, armar mazos equilibrados y nunca más perder por impaciencia.",
        "benefits": [
            "Entender cómo funciona Clash Royale de verdad (torres, cartas, elixir)",
            "Defender como un campeón antes de atacar (el secreto de los ganadores)",
            "Construir un mazo equilibrado que funcione como equipo",
            "Usar la paciencia como un superpoder estratégico",
            "No frustrarse cuando pierde: aprender de cada derrota",
            "Reconocer estafas (gemas gratis, hacks) y jugar con seguridad",
        ],
        "includes": [
            "4 capítulos paso a paso (mundo del juego, defensa, mazos, mentalidad)",
            "11 ilustraciones a todo color estilo Supercell",
            "Quiz del Pequeño Campeón con respuestas al final",
            "Glosario gamer con todos los términos del juego",
            "Diploma final imprimible",
            "Sección especial para padres con controles parentales",
        ],
    },
    {
        "slug": "clash-en",
        "lang": "en",
        "title": "Clash Royale for Little Champions",
        "subtitle": "Strategy Guide for Kids Ages 7-9",
        "theme": "clash",
        "price_usd": 9,
        "price_cop": "36.000",
        "cover": "/assets/covers/clash-en.png",
        "bold_link_usd": "https://checkout.bold.co/payment/LNK_5HFAZI9957",
        "age": "7-9 years",
        "pages": 69,
        "illustrations": 11,
        "color_primary": "#0D3B7F",
        "color_accent": "#FFC107",
        "color_dark": "#06194A",
        "tagline": "The first English strategy guide that teaches kids to play Clash Royale smart: defend, build winning decks, and develop a true champion's mindset.",
        "hook_pain": "Does your kid lose match after match in Clash Royale and get frustrated? Spend gems with no strategy and cry when they get eliminated?",
        "hook_promise": "This book teaches them to think like a real champion: defend before attacking, build balanced decks, and never lose to impatience again.",
        "benefits": [
            "How Clash Royale really works (towers, cards, elixir)",
            "Defending like a champion before attacking (the winners' secret)",
            "Building a balanced deck that works as a team",
            "Using patience as a strategic superpower",
            "Bouncing back from losses: learning from every defeat",
            "Spotting scams (free gems, hacks) and playing safe online",
        ],
        "includes": [
            "4 step-by-step chapters (game world, defense, decks, mindset)",
            "11 full-color Supercell-style illustrations",
            "Little Champion's Quiz with answers at the end",
            "Gamer glossary with every game term explained",
            "Printable final diploma",
            "Special parents section with parental controls",
        ],
    },
    {
        "slug": "roblox",
        "lang": "es",
        "title": "Crea tu Primer Juego en Roblox",
        "subtitle": "Guía para Jóvenes Creadores 9-13 años",
        "theme": "roblox",
        "price_usd": 9,
        "price_cop": "35.000",
        "cover": "/assets/covers/roblox-es.png",
        "bold_link_cop": "https://checkout.bold.co/payment/LNK_UYBSTLW3SD",
        "bold_link_usd": "https://checkout.bold.co/payment/LNK_QDY7ZWFO3L",
        "age": "9-13 años",
        "pages": 66,
        "illustrations": 11,
        "color_primary": "#0B3D91",
        "color_accent": "#00A2FF",
        "color_dark": "#061E48",
        "tagline": "De jugador a creador: la guía paso a paso que enseña a los niños a construir y publicar su propio juego en Roblox, con código real.",
        "hook_pain": "¿Tu hijo pasa horas jugando Roblox y sueña con crear su propio juego, pero no sabe por dónde empezar? ¿Los tutoriales están en inglés o son demasiado técnicos?",
        "hook_promise": "Al terminar este libro, tu hijo tendrá su propio juego publicado en Roblox, jugable por sus amigos. Sin experiencia previa. Paso a paso.",
        "benefits": [
            "Instalar y dominar Roblox Studio desde cero",
            "Crear un mundo 3D completo con ambiente, plataformas y trampas",
            "Implementar checkpoints, monedas coleccionables y leaderboard",
            "Diseñar un estilo visual profesional (materiales, luces, partículas)",
            "Escribir sus primeras líneas de código en Luau (lenguaje oficial)",
            "Publicar su juego para que cualquier persona del mundo lo juegue",
        ],
        "includes": [
            "10 capítulos paso a paso con proyecto real (obby completo)",
            "Scripts de Luau listos para copiar/pegar y modificar",
            "11 ilustraciones originales en estilo Pixar 3D",
            "Sección completa de seguridad online y controles parentales",
            "Glosario con todos los términos técnicos de Roblox Studio",
        ],
    },
    {
        "slug": "roblox-en",
        "lang": "en",
        "title": "Create Your First Game in Roblox",
        "subtitle": "A Guide for Young Creators Ages 9-13",
        "theme": "roblox",
        "price_usd": 11,
        "price_cop": "44.000",
        "cover": "/assets/covers/roblox-en.png",
        "bold_link_usd": "https://checkout.bold.co/payment/LNK_W4Q1PTEJMQ",
        "age": "9-13 years",
        "pages": 64,
        "illustrations": 11,
        "color_primary": "#0B3D91",
        "color_accent": "#00A2FF",
        "color_dark": "#061E48",
        "tagline": "From player to creator: the step-by-step guide that teaches kids to build and publish their own Roblox game, with real code.",
        "hook_pain": "Does your kid spend hours playing Roblox and dream of making their own game, but doesn't know where to start? Are tutorials too technical or confusing?",
        "hook_promise": "By the end of this book, your child will have their own game published on Roblox, playable by their friends. No prior experience needed. Step by step.",
        "benefits": [
            "Install and master Roblox Studio from zero",
            "Build a complete 3D world with atmosphere, platforms and traps",
            "Implement checkpoints, collectible coins and a leaderboard",
            "Design a professional visual style (materials, lights, particles)",
            "Write their first lines of real code in Luau (Roblox's official language)",
            "Publish their game so anyone in the world can play it",
        ],
        "includes": [
            "10 step-by-step chapters with a real project (complete obby)",
            "Ready-to-use Luau scripts to copy, paste and modify",
            "11 original Pixar-style 3D illustrations",
            "Complete online safety section with parental controls",
            "Glossary of all Roblox Studio technical terms",
        ],
    },
]


# Strings localizados (labels UI, no copy del libro)
UI = {
    "es": {
        "lang_code": "es",
        "nav_catalogo": "Catálogo",
        "nav_sobre": "Sobre el autor",
        "badge_author": "Escrito por un adolescente gamer de verdad",
        "section_aprende": "Lo que tu hijo va a aprender",
        "section_incluye": "Qué incluye el libro",
        "section_porque": "Por qué este libro es diferente",
        "section_autor": "¿Quién escribió este libro?",
        "why_title_1": "Lenguaje de niños",
        "why_desc_1": "No es un manual aburrido. Está escrito en un lenguaje que los niños entienden y disfrutan leer.",
        "why_title_2": "Paso a paso",
        "why_desc_2": "Cada capítulo lleva al lector de la mano desde lo más básico hasta el resultado final.",
        "why_title_3": "Ilustraciones reales",
        "why_desc_3": "Cada capítulo tiene ilustraciones originales a todo color que refuerzan lo que aprenden.",
        "why_title_4": "Para padres también",
        "why_desc_4": "Incluye una sección especial para padres con consejos de seguridad y controles parentales.",
        "cta_primary": "Comprar ahora",
        "cta_pay_cop": "Pagar en COP",
        "cta_pay_usd": "Pagar en USD",
        "cta_note": "Descarga inmediata · Pago seguro con Bold",
        "delivery_note_title": "📬 ¿Cómo recibo mi PDF?",
        "delivery_note_body": "Después de pagar en Bold, contáctanos por WhatsApp con tu comprobante y te enviamos el PDF en menos de 1 hora (horario hábil Colombia).",
        "delivery_note_cta": "Escríbenos por WhatsApp",
        "wa_tooltip": "¿Dudas? Chatea con nosotros",
        "delivery_title": "Cómo recibes el libro",
        "delivery_step_1": "Haces clic en el botón de compra",
        "delivery_step_2": "Pagas con Nequi, PSE, transferencia o tarjeta",
        "delivery_step_3": "Recibes el PDF al instante en tu correo",
        "faq_title": "Preguntas frecuentes",
        "faq_q_1": "¿Cómo recibo el libro?",
        "faq_a_1": "Al completar el pago, recibirás el PDF por email en máximo 5 minutos. Listo para leer en tablet, computadora, celular o imprimir en casa.",
        "faq_q_2": "¿Qué métodos de pago aceptan?",
        "faq_a_2": "Nequi, PSE, transferencia bancaria, tarjeta de crédito/débito y más. Todo a través de Bold, la pasarela de pagos más segura de Colombia.",
        "faq_q_3": "¿Funciona en cualquier dispositivo?",
        "faq_a_3": "Sí. Es un PDF que se abre en cualquier celular, tablet, computadora o lector de ebooks. También se puede imprimir.",
        "faq_q_4": "¿Hay garantía?",
        "faq_a_4": "Sí. Si el libro no cumple con lo que prometemos, te devolvemos el 100% de tu dinero dentro de los primeros 7 días. Solo escríbenos.",
        "author_title": "Escrito por un adolescente gamer",
        "author_body": "Los libros de GamerKids Books no los escribe una editorial aburrida: los escribe un adolescente de 15 años que lleva años jugando Minecraft, Roblox y Clash Royale. Sabe cómo piensa un niño gamer, qué lo frustra, qué lo motiva y qué le funciona. Por eso sus libros conectan.",
        "catalogo_title": "Libros para niños gamers",
        "catalogo_subtitle": "Guías escritas por un adolescente gamer de verdad, para niños que quieren aprender, crear y divertirse.",
        "footer_tagline": "Libros para niños gamers que quieren aprender, crear y divertirse.",
        "pages_label": "páginas",
        "ages_label": "Edad",
        "format_label": "Formato",
        "illustrations_label": "ilustraciones a color",
        "price_prefix": "Desde",
        "cop_note": "También pagas en COP con Nequi o PSE",
    },
    "en": {
        "lang_code": "en",
        "nav_catalogo": "Catalog",
        "nav_sobre": "About the author",
        "badge_author": "Written by a real teen gamer",
        "section_aprende": "What your child will learn",
        "section_incluye": "What's included",
        "section_porque": "Why this book is different",
        "section_autor": "Who wrote this book?",
        "why_title_1": "Kid-friendly language",
        "why_desc_1": "Not a boring manual. Written in a language kids actually understand and enjoy reading.",
        "why_title_2": "Step by step",
        "why_desc_2": "Every chapter guides the reader from the very basics to the final result.",
        "why_title_3": "Real illustrations",
        "why_desc_3": "Every chapter includes original full-color illustrations that reinforce what they learn.",
        "why_title_4": "For parents too",
        "why_desc_4": "Includes a special parents section with safety tips and parental controls.",
        "cta_primary": "Buy now",
        "cta_note": "Instant download · Secure payment with Bold",
        "delivery_note_title": "📬 How do I get my PDF?",
        "delivery_note_body": "After paying with Bold, send us your receipt via WhatsApp and we will email you the PDF within 1 hour (Colombia business hours).",
        "delivery_note_cta": "Message us on WhatsApp",
        "wa_tooltip": "Questions? Chat with us",
        "delivery_title": "How you get the book",
        "delivery_step_1": "Click the buy button",
        "delivery_step_2": "Pay with credit card, bank transfer, or local methods",
        "delivery_step_3": "Get the PDF instantly in your inbox",
        "faq_title": "Frequently asked questions",
        "faq_q_1": "How do I receive the book?",
        "faq_a_1": "After completing payment, you'll get the PDF by email within 5 minutes. Ready to read on tablet, computer, phone, or print at home.",
        "faq_q_2": "What payment methods do you accept?",
        "faq_a_2": "Credit/debit card, bank transfer, and more through Bold, a secure payment gateway. International cards accepted.",
        "faq_q_3": "Does it work on any device?",
        "faq_a_3": "Yes. It's a PDF that opens on any phone, tablet, computer, or ebook reader. Also printable.",
        "faq_q_4": "Is there a guarantee?",
        "faq_a_4": "Yes. If the book doesn't deliver what we promise, we refund 100% of your money within the first 7 days. Just email us.",
        "author_title": "Written by a real teen gamer",
        "author_body": "GamerKids Books aren't written by a boring publisher: they're written by a 15-year-old teenager who's been playing Minecraft, Roblox, and Clash Royale for years. He knows how a young gamer thinks, what frustrates them, what motivates them, and what works. That's why his books connect.",
        "catalogo_title": "Books for young gamers",
        "catalogo_subtitle": "Guides written by a real teen gamer, for kids who want to learn, create, and have fun.",
        "footer_tagline": "Books for young gamers who want to learn, create, and have fun.",
        "pages_label": "pages",
        "ages_label": "Age",
        "format_label": "Format",
        "illustrations_label": "color illustrations",
        "price_prefix": "From",
        "cop_note": "",
    },
}


# ---------------------------------------------------------------------------
# Template HTML de cada landing de libro
# ---------------------------------------------------------------------------


def render_book_page(book):
    ui = UI[book["lang"]]
    benefits_html = "\n".join(
        f'            <li class="benefit-item"><span class="check">✓</span><span>{b}</span></li>'
        for b in book["benefits"]
    )
    includes_html = "\n".join(
        f'            <li class="include-item"><span class="dot">●</span><span>{i}</span></li>'
        for i in book["includes"]
    )

    cop_line = (
        f'<div class="price-cop">${book["price_cop"]} COP</div>'
        if book["lang"] == "es"
        else ""
    )

    if book["lang"] == "es":
        cta_group_html = (
            f'<div class="cta-group">'
            f'<a href="{book["bold_link_cop"]}" class="cta-button cta-cop">{ui["cta_pay_cop"]}</a>'
            f'<a href="{book["bold_link_usd"]}" class="cta-button cta-usd">{ui["cta_pay_usd"]}</a>'
            f'</div>'
        )
    else:
        cta_group_html = (
            f'<div class="cta-group">'
            f'<a href="{book["bold_link_usd"]}" class="cta-button">{ui["cta_primary"]} → ${book["price_usd"]} USD</a>'
            f'</div>'
        )

    return f"""<!DOCTYPE html>
<html lang="{ui['lang_code']}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{book['title']} | GamerKids Books</title>
<meta name="description" content="{book['tagline']}">
<meta property="og:title" content="{book['title']}">
<meta property="og:description" content="{book['tagline']}">
<meta property="og:image" content="{book['cover']}">
<meta property="og:type" content="product">
<link rel="icon" type="image/png" href="/assets/logo.png">
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&family=Bungee&display=swap" rel="stylesheet">
<style>
:root {{
  --primary: {book['color_primary']};
  --accent: {book['color_accent']};
  --dark: {book['color_dark']};
  --text: #1a1a1a;
  --bg: #ffffff;
  --bg-soft: #f7f7fb;
  --muted: #6b7280;
}}

* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html {{ scroll-behavior: smooth; }}
body {{
  font-family: 'Fredoka', -apple-system, sans-serif;
  color: var(--text);
  background: var(--bg);
  line-height: 1.6;
}}

.container {{ max-width: 1100px; margin: 0 auto; padding: 0 24px; }}

header {{
  background: var(--dark);
  padding: 16px 0;
  position: sticky;
  top: 0;
  z-index: 100;
  border-bottom: 3px solid var(--accent);
}}
header .container {{ display: flex; justify-content: space-between; align-items: center; }}
header a {{ color: white; text-decoration: none; font-weight: 600; }}
header .logo {{ display: flex; align-items: center; gap: 12px; font-family: 'Bungee', sans-serif; font-size: 18px; }}
header .logo img {{ height: 40px; }}

.hero {{
  background: linear-gradient(135deg, var(--dark) 0%, var(--primary) 100%);
  color: white;
  padding: 60px 0 80px;
  position: relative;
  overflow: hidden;
}}
.hero::before {{
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background-image: radial-gradient(circle at 20% 30%, rgba(255,255,255,0.1) 0%, transparent 50%),
                    radial-gradient(circle at 80% 70%, var(--accent) 0%, transparent 40%);
  opacity: 0.4;
  pointer-events: none;
}}
.hero .container {{ display: grid; grid-template-columns: 1.2fr 1fr; gap: 48px; align-items: center; position: relative; }}

.badge {{
  display: inline-block;
  background: var(--accent);
  color: var(--dark);
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 700;
  margin-bottom: 20px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}}

.hero h1 {{
  font-family: 'Bungee', sans-serif;
  font-size: 44px;
  line-height: 1.1;
  margin-bottom: 12px;
  text-shadow: 2px 2px 0 rgba(0,0,0,0.3);
}}
.hero h2 {{
  font-size: 20px;
  font-weight: 400;
  opacity: 0.92;
  margin-bottom: 24px;
}}
.hero .tagline {{
  font-size: 17px;
  margin-bottom: 32px;
  opacity: 0.95;
  max-width: 540px;
}}

.hero-cover {{
  display: flex;
  justify-content: center;
}}
.hero-cover img {{
  max-width: 320px;
  width: 100%;
  border-radius: 12px;
  box-shadow: 0 20px 60px rgba(0,0,0,0.5), 0 0 0 6px rgba(255,255,255,0.1);
  transform: rotate(-3deg);
  transition: transform 0.3s;
}}
.hero-cover img:hover {{ transform: rotate(0deg) scale(1.02); }}

.price-box {{
  display: inline-flex;
  flex-direction: column;
  background: rgba(255,255,255,0.12);
  backdrop-filter: blur(8px);
  padding: 14px 22px;
  border-radius: 12px;
  margin-bottom: 24px;
  border: 2px solid var(--accent);
}}
.price-label {{ font-size: 12px; opacity: 0.8; text-transform: uppercase; letter-spacing: 1px; }}
.price-main {{ font-family: 'Bungee', sans-serif; font-size: 36px; color: var(--accent); }}
.price-cop {{ font-size: 14px; opacity: 0.85; margin-top: 2px; }}

.cta-button {{
  display: inline-block;
  background: var(--accent);
  color: var(--dark);
  font-family: 'Bungee', sans-serif;
  font-size: 20px;
  padding: 18px 36px;
  border-radius: 12px;
  text-decoration: none;
  box-shadow: 0 6px 0 rgba(0,0,0,0.3), 0 10px 30px rgba(0,0,0,0.2);
  transition: all 0.2s;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}}
.cta-button:hover {{
  transform: translateY(-2px);
  box-shadow: 0 8px 0 rgba(0,0,0,0.3), 0 14px 40px rgba(0,0,0,0.25);
}}
.cta-button:active {{ transform: translateY(2px); box-shadow: 0 2px 0 rgba(0,0,0,0.3); }}
.cta-button.cta-cop {{
  background: #14b8a6;
  color: white;
}}
.cta-button.cta-cop:hover {{ background: #0f9e8e; }}
.cta-button.cta-usd {{
  background: #f59e0b;
  color: white;
}}
.cta-button.cta-usd:hover {{ background: #d97f06; }}
.cta-note {{ display: block; font-size: 13px; margin-top: 12px; opacity: 0.85; }}
.cta-group {{
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
  align-items: center;
}}

.cta-inline {{
  padding: 40px 0;
  text-align: center;
  background: linear-gradient(90deg, transparent 0%, var(--bg-soft) 20%, var(--bg-soft) 80%, transparent 100%);
}}
.cta-inline .cta-button {{ font-size: 18px; padding: 16px 32px; }}
.cta-inline .cta-group {{ justify-content: center; }}
.cta-inline .cta-note {{ color: var(--muted); }}

.final-cta .cta-group {{ justify-content: center; }}

.hook-section {{
  background: var(--bg-soft);
  padding: 60px 0;
  text-align: center;
}}
.hook-section .pain {{
  font-size: 24px;
  font-weight: 600;
  max-width: 720px;
  margin: 0 auto 20px;
  color: var(--text);
}}
.hook-section .promise {{
  font-size: 18px;
  max-width: 680px;
  margin: 0 auto;
  color: var(--muted);
}}

section.features {{ padding: 80px 0; }}
section.features h2 {{
  font-family: 'Bungee', sans-serif;
  font-size: 32px;
  color: var(--dark);
  text-align: center;
  margin-bottom: 48px;
}}

.benefits-grid {{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  max-width: 900px;
  margin: 0 auto;
}}
.benefit-item {{
  list-style: none;
  display: flex;
  gap: 14px;
  align-items: flex-start;
  background: white;
  padding: 18px 20px;
  border-radius: 12px;
  border-left: 4px solid var(--accent);
  box-shadow: 0 2px 10px rgba(0,0,0,0.05);
  font-size: 16px;
}}
.benefit-item .check {{
  color: var(--primary);
  font-weight: 900;
  font-size: 22px;
  line-height: 1;
  flex-shrink: 0;
}}

.includes-section {{
  background: var(--bg-soft);
  padding: 80px 0;
}}
.includes-section .container {{ max-width: 820px; }}
.includes-section h2 {{
  font-family: 'Bungee', sans-serif;
  font-size: 32px;
  color: var(--dark);
  text-align: center;
  margin-bottom: 40px;
}}
.includes-list {{ list-style: none; }}
.include-item {{
  display: flex;
  gap: 14px;
  align-items: flex-start;
  padding: 16px 0;
  border-bottom: 1px dashed #d1d5db;
  font-size: 17px;
}}
.include-item:last-child {{ border-bottom: none; }}
.include-item .dot {{
  color: var(--accent);
  font-size: 18px;
  line-height: 1.4;
  flex-shrink: 0;
}}

.meta-row {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  margin: 40px auto 0;
  max-width: 640px;
}}
.meta-item {{
  background: white;
  padding: 20px;
  border-radius: 12px;
  text-align: center;
  box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}}
.meta-item .num {{ font-family: 'Bungee', sans-serif; font-size: 28px; color: var(--primary); }}
.meta-item .lbl {{ font-size: 12px; color: var(--muted); text-transform: uppercase; letter-spacing: 0.5px; }}

.why-section {{
  padding: 80px 0;
}}
.why-section h2 {{
  font-family: 'Bungee', sans-serif;
  font-size: 32px;
  color: var(--dark);
  text-align: center;
  margin-bottom: 48px;
}}
.why-grid {{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
}}
.why-card {{
  background: linear-gradient(135deg, white 0%, var(--bg-soft) 100%);
  padding: 28px;
  border-radius: 16px;
  border-top: 4px solid var(--accent);
  box-shadow: 0 4px 20px rgba(0,0,0,0.06);
}}
.why-card h3 {{
  font-family: 'Bungee', sans-serif;
  color: var(--primary);
  font-size: 20px;
  margin-bottom: 10px;
}}
.why-card p {{ color: var(--muted); }}

.author-section {{
  background: var(--dark);
  color: white;
  padding: 80px 0;
  text-align: center;
}}
.author-section h2 {{
  font-family: 'Bungee', sans-serif;
  font-size: 32px;
  margin-bottom: 24px;
  color: var(--accent);
}}
.author-section p {{
  max-width: 680px;
  margin: 0 auto;
  font-size: 17px;
  opacity: 0.92;
}}

.delivery-section {{
  padding: 80px 0;
  background: var(--bg-soft);
}}
.delivery-section h2 {{
  font-family: 'Bungee', sans-serif;
  font-size: 32px;
  color: var(--dark);
  text-align: center;
  margin-bottom: 48px;
}}
.delivery-steps {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  max-width: 900px;
  margin: 0 auto;
}}
.delivery-step {{
  background: white;
  padding: 30px 24px;
  border-radius: 16px;
  text-align: center;
  box-shadow: 0 4px 20px rgba(0,0,0,0.06);
  position: relative;
}}
.delivery-step .step-num {{
  font-family: 'Bungee', sans-serif;
  font-size: 48px;
  color: var(--accent);
  line-height: 1;
  margin-bottom: 12px;
}}
.delivery-step p {{ font-size: 16px; color: var(--text); font-weight: 600; }}

.faq-section {{ padding: 80px 0; }}
.faq-section h2 {{
  font-family: 'Bungee', sans-serif;
  font-size: 32px;
  color: var(--dark);
  text-align: center;
  margin-bottom: 48px;
}}
.faq-list {{ max-width: 760px; margin: 0 auto; }}
.faq-item {{
  background: var(--bg-soft);
  border-radius: 12px;
  padding: 22px 26px;
  margin-bottom: 14px;
  border-left: 4px solid var(--primary);
}}
.faq-item h3 {{
  font-size: 18px;
  color: var(--dark);
  margin-bottom: 8px;
}}
.faq-item p {{ color: var(--muted); }}

.final-cta {{
  background: linear-gradient(135deg, var(--primary) 0%, var(--dark) 100%);
  color: white;
  padding: 80px 0;
  text-align: center;
}}
.final-cta h2 {{
  font-family: 'Bungee', sans-serif;
  font-size: 36px;
  margin-bottom: 16px;
}}
.final-cta p {{ font-size: 18px; opacity: 0.92; margin-bottom: 32px; }}

footer {{
  background: #0a0a0a;
  color: #9ca3af;
  padding: 40px 0;
  text-align: center;
  font-size: 14px;
}}
footer a {{ color: var(--accent); text-decoration: none; }}

.delivery-note {{
  margin-top: 40px;
  background: #f0fdf4;
  border: 2px solid #25D366;
  border-radius: 14px;
  padding: 24px 28px;
  text-align: center;
  max-width: 640px;
  margin-left: auto;
  margin-right: auto;
}}
.delivery-note strong {{
  display: block;
  font-size: 18px;
  color: #0f9e47;
  margin-bottom: 6px;
}}
.delivery-note p {{
  color: #374151;
  font-size: 15px;
  margin-bottom: 14px;
  line-height: 1.5;
}}
.wa-button-inline {{
  display: inline-block;
  background: #25D366;
  color: white !important;
  padding: 12px 24px;
  border-radius: 10px;
  text-decoration: none;
  font-weight: 700;
  font-size: 15px;
  box-shadow: 0 4px 12px rgba(37, 211, 102, 0.3);
  transition: transform 0.15s, box-shadow 0.15s;
}}
.wa-button-inline:hover {{
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(37, 211, 102, 0.4);
}}

.wa-float {{
  position: fixed;
  bottom: 24px;
  right: 24px;
  width: 60px;
  height: 60px;
  background: #25D366;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 6px 20px rgba(37, 211, 102, 0.4), 0 2px 6px rgba(0,0,0,0.15);
  z-index: 9999;
  text-decoration: none;
  transition: transform 0.2s, box-shadow 0.2s;
}}
.wa-float:hover {{
  transform: scale(1.08);
  box-shadow: 0 8px 28px rgba(37, 211, 102, 0.55), 0 3px 8px rgba(0,0,0,0.2);
}}
.wa-float .wa-tooltip {{
  position: absolute;
  right: 72px;
  background: #1f2937;
  color: white;
  font-size: 13px;
  padding: 8px 14px;
  border-radius: 8px;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s;
  font-family: inherit;
}}
.wa-float:hover .wa-tooltip {{ opacity: 1; }}
@media (max-width: 768px) {{
  .wa-float {{ width: 54px; height: 54px; bottom: 18px; right: 18px; }}
  .wa-float .wa-tooltip {{ display: none; }}
}}

@media (max-width: 768px) {{
  .hero {{ padding: 40px 0 60px; }}
  .hero .container {{ grid-template-columns: 1fr; gap: 32px; text-align: center; }}
  .hero h1 {{ font-size: 30px; }}
  .hero h2 {{ font-size: 17px; }}
  .hero-cover img {{ max-width: 240px; }}
  .benefits-grid {{ grid-template-columns: 1fr; }}
  .why-grid {{ grid-template-columns: 1fr; }}
  .delivery-steps {{ grid-template-columns: 1fr; }}
  .meta-row {{ grid-template-columns: 1fr; }}
  header .logo {{ font-size: 14px; }}
  header .logo img {{ height: 32px; }}
  section.features h2, .includes-section h2, .why-section h2, .delivery-section h2, .faq-section h2 {{ font-size: 24px; }}
  .final-cta h2 {{ font-size: 26px; }}
}}
</style>
</head>
<body>

<header>
  <div class="container">
    <a href="/" class="logo">
      <img src="/assets/logo.png" alt="GamerKids Books">
      <span>GAMERKIDS BOOKS</span>
    </a>
    <a href="/">{ui['nav_catalogo']}</a>
  </div>
</header>

<section class="hero">
  <div class="container">
    <div class="hero-text">
      <span class="badge">⭐ {ui['badge_author']}</span>
      <h1>{book['title']}</h1>
      <h2>{book['subtitle']}</h2>
      <p class="tagline">{book['tagline']}</p>
      <div class="price-box">
        <span class="price-label">{ui['price_prefix']}</span>
        <span class="price-main">${book['price_usd']} USD</span>
        {cop_line}
      </div>
      <div>
        {cta_group_html}
        <span class="cta-note">⚡ {ui['cta_note']}</span>
      </div>
    </div>
    <div class="hero-cover">
      <img src="{book['cover']}" alt="{book['title']}">
    </div>
  </div>
</section>

<section class="hook-section">
  <div class="container">
    <p class="pain">{book['hook_pain']}</p>
    <p class="promise">{book['hook_promise']}</p>
  </div>
</section>

<section class="cta-inline">
  <div class="container">
    {cta_group_html}
    <span class="cta-note">⚡ {ui['cta_note']}</span>
  </div>
</section>

<section class="features">
  <div class="container">
    <h2>🎯 {ui['section_aprende']}</h2>
    <ul class="benefits-grid">
{benefits_html}
    </ul>
  </div>
</section>

<section class="includes-section">
  <div class="container">
    <h2>📖 {ui['section_incluye']}</h2>
    <ul class="includes-list">
{includes_html}
    </ul>
    <div class="meta-row">
      <div class="meta-item">
        <div class="num">{book['pages']}</div>
        <div class="lbl">{ui['pages_label']}</div>
      </div>
      <div class="meta-item">
        <div class="num">{book['illustrations']}</div>
        <div class="lbl">{ui['illustrations_label']}</div>
      </div>
      <div class="meta-item">
        <div class="num">{book['age'].split()[0]}</div>
        <div class="lbl">{ui['ages_label']}</div>
      </div>
    </div>
    <div class="delivery-note">
      <strong>{ui['delivery_note_title']}</strong>
      <p>{ui['delivery_note_body']}</p>
      <a href="{wa_link(book['title'], book['lang'])}" target="_blank" rel="noopener" class="wa-button-inline">
        💬 {ui['delivery_note_cta']}
      </a>
    </div>
  </div>
</section>

<section class="cta-inline">
  <div class="container">
    {cta_group_html}
    <span class="cta-note">⚡ {ui['cta_note']}</span>
  </div>
</section>

<section class="why-section">
  <div class="container">
    <h2>✨ {ui['section_porque']}</h2>
    <div class="why-grid">
      <div class="why-card"><h3>{ui['why_title_1']}</h3><p>{ui['why_desc_1']}</p></div>
      <div class="why-card"><h3>{ui['why_title_2']}</h3><p>{ui['why_desc_2']}</p></div>
      <div class="why-card"><h3>{ui['why_title_3']}</h3><p>{ui['why_desc_3']}</p></div>
      <div class="why-card"><h3>{ui['why_title_4']}</h3><p>{ui['why_desc_4']}</p></div>
    </div>
  </div>
</section>

<section class="author-section">
  <div class="container">
    <h2>🎮 {ui['author_title']}</h2>
    <p>{ui['author_body']}</p>
  </div>
</section>

<section class="cta-inline">
  <div class="container">
    {cta_group_html}
    <span class="cta-note">⚡ {ui['cta_note']}</span>
  </div>
</section>

<section class="delivery-section">
  <div class="container">
    <h2>📬 {ui['delivery_title']}</h2>
    <div class="delivery-steps">
      <div class="delivery-step"><div class="step-num">1</div><p>{ui['delivery_step_1']}</p></div>
      <div class="delivery-step"><div class="step-num">2</div><p>{ui['delivery_step_2']}</p></div>
      <div class="delivery-step"><div class="step-num">3</div><p>{ui['delivery_step_3']}</p></div>
    </div>
  </div>
</section>

<section class="faq-section">
  <div class="container">
    <h2>❓ {ui['faq_title']}</h2>
    <div class="faq-list">
      <div class="faq-item"><h3>{ui['faq_q_1']}</h3><p>{ui['faq_a_1']}</p></div>
      <div class="faq-item"><h3>{ui['faq_q_2']}</h3><p>{ui['faq_a_2']}</p></div>
      <div class="faq-item"><h3>{ui['faq_q_3']}</h3><p>{ui['faq_a_3']}</p></div>
      <div class="faq-item"><h3>{ui['faq_q_4']}</h3><p>{ui['faq_a_4']}</p></div>
    </div>
  </div>
</section>

<section class="final-cta">
  <div class="container">
    <h2>{book['title']}</h2>
    <p>{ui['cta_note']}</p>
    {cta_group_html}
  </div>
</section>

<footer>
  <div class="container">
    <p>© 2026 GamerKids Books · {ui['footer_tagline']}</p>
  </div>
</footer>

<a href="{wa_link(book['title'], book['lang'])}" target="_blank" rel="noopener" class="wa-float" aria-label="WhatsApp"><svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.67-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg><span class="wa-tooltip">{ui['wa_tooltip']}</span></a>

</body>
</html>
"""


# ---------------------------------------------------------------------------
# Template del home/catalogo
# ---------------------------------------------------------------------------


def render_index():
    # Usamos UI en espanol para el home (mercado principal)
    ui = UI["es"]
    cards_html = "\n".join(
        f'''      <a href="/{book['slug']}" class="book-card" style="--card-primary: {book['color_primary']}; --card-accent: {book['color_accent']}; --card-dark: {book['color_dark']};">
        <div class="book-card-cover"><img src="{book['cover']}" alt="{book['title']}"></div>
        <div class="book-card-body">
          <span class="book-card-lang">{'🇪🇸' if book['lang'] == 'es' else '🇬🇧'} {book['lang'].upper()}</span>
          <h3>{book['title']}</h3>
          <p>{book['subtitle']}</p>
          <div class="book-card-footer">
            <span class="book-card-price">${book['price_usd']} USD</span>
            <span class="book-card-cta">Ver libro →</span>
          </div>
        </div>
      </a>'''
        for book in BOOKS
    )

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GamerKids Books · Libros para niños gamers</title>
<meta name="description" content="Libros para niños gamers escritos por un adolescente gamer de verdad. Minecraft, Roblox, Clash Royale. Descarga inmediata.">
<meta property="og:title" content="GamerKids Books">
<meta property="og:description" content="Libros para niños gamers escritos por un adolescente gamer de verdad.">
<meta property="og:image" content="/assets/logo.png">
<link rel="icon" type="image/png" href="/assets/logo.png">
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&family=Bungee&display=swap" rel="stylesheet">
<style>
:root {{
  --primary: #1645A6;
  --accent: #FFC107;
  --dark: #0C0E27;
  --text: #1a1a1a;
  --bg: #f7f7fb;
  --muted: #6b7280;
}}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html {{ scroll-behavior: smooth; }}
body {{
  font-family: 'Fredoka', -apple-system, sans-serif;
  color: var(--text);
  background: var(--bg);
  line-height: 1.6;
}}
.container {{ max-width: 1200px; margin: 0 auto; padding: 0 24px; }}

header {{
  background: var(--dark);
  padding: 16px 0;
  border-bottom: 3px solid var(--accent);
}}
header .container {{ display: flex; justify-content: space-between; align-items: center; }}
header .logo {{ display: flex; align-items: center; gap: 12px; color: white; font-family: 'Bungee', sans-serif; font-size: 18px; text-decoration: none; }}
header .logo img {{ height: 40px; }}

.hero {{
  background: linear-gradient(135deg, var(--dark) 0%, var(--primary) 100%);
  color: white;
  padding: 80px 0 100px;
  text-align: center;
  position: relative;
  overflow: hidden;
}}
.hero::before {{
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background-image: radial-gradient(circle at 20% 30%, rgba(255,255,255,0.1) 0%, transparent 50%),
                    radial-gradient(circle at 80% 70%, var(--accent) 0%, transparent 40%);
  opacity: 0.3;
}}
.hero .container {{ position: relative; }}
.hero h1 {{
  font-family: 'Bungee', sans-serif;
  font-size: 52px;
  line-height: 1.05;
  margin-bottom: 16px;
  text-shadow: 3px 3px 0 rgba(0,0,0,0.3);
}}
.hero p {{
  font-size: 20px;
  max-width: 680px;
  margin: 0 auto;
  opacity: 0.92;
}}

.catalogo {{ padding: 80px 0; }}
.catalogo h2 {{
  font-family: 'Bungee', sans-serif;
  font-size: 32px;
  color: var(--dark);
  text-align: center;
  margin-bottom: 48px;
}}
.books-grid {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px;
}}
.book-card {{
  background: white;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(0,0,0,0.08);
  text-decoration: none;
  color: var(--text);
  transition: all 0.3s;
  border-top: 4px solid var(--card-accent);
  display: flex;
  flex-direction: column;
}}
.book-card:hover {{
  transform: translateY(-6px);
  box-shadow: 0 20px 50px rgba(0,0,0,0.15);
}}
.book-card-cover {{
  background: linear-gradient(135deg, var(--card-dark), var(--card-primary));
  padding: 24px;
  display: flex;
  justify-content: center;
}}
.book-card-cover img {{
  max-width: 200px;
  width: 100%;
  border-radius: 8px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.4);
}}
.book-card-body {{
  padding: 24px;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}}
.book-card-lang {{
  display: inline-block;
  background: var(--card-accent);
  color: var(--card-dark);
  font-size: 12px;
  font-weight: 700;
  padding: 4px 10px;
  border-radius: 12px;
  margin-bottom: 12px;
  align-self: flex-start;
}}
.book-card-body h3 {{
  font-family: 'Bungee', sans-serif;
  font-size: 18px;
  color: var(--card-primary);
  line-height: 1.2;
  margin-bottom: 8px;
}}
.book-card-body p {{
  color: var(--muted);
  font-size: 14px;
  margin-bottom: 18px;
  flex-grow: 1;
}}
.book-card-footer {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 16px;
  border-top: 1px dashed #e5e7eb;
}}
.book-card-price {{
  font-family: 'Bungee', sans-serif;
  font-size: 22px;
  color: var(--card-primary);
}}
.book-card-cta {{
  font-weight: 700;
  color: var(--card-accent);
  font-size: 14px;
}}

.about {{
  background: var(--dark);
  color: white;
  padding: 80px 0;
  text-align: center;
}}
.about h2 {{
  font-family: 'Bungee', sans-serif;
  font-size: 32px;
  margin-bottom: 24px;
  color: var(--accent);
}}
.about p {{
  max-width: 680px;
  margin: 0 auto;
  font-size: 17px;
  opacity: 0.92;
}}

footer {{
  background: #0a0a0a;
  color: #9ca3af;
  padding: 40px 0;
  text-align: center;
  font-size: 14px;
}}

@media (max-width: 900px) {{
  .books-grid {{ grid-template-columns: repeat(2, 1fr); }}
  .hero h1 {{ font-size: 36px; }}
  .hero p {{ font-size: 17px; }}
}}
@media (max-width: 600px) {{
  .books-grid {{ grid-template-columns: 1fr; }}
  .hero h1 {{ font-size: 28px; }}
}}
</style>
</head>
<body>

<header>
  <div class="container">
    <a href="/" class="logo">
      <img src="/assets/logo.png" alt="GamerKids Books">
      <span>GAMERKIDS BOOKS</span>
    </a>
  </div>
</header>

<section class="hero">
  <div class="container">
    <h1>🎮 {ui['catalogo_title']}</h1>
    <p>{ui['catalogo_subtitle']}</p>
  </div>
</section>

<section class="catalogo">
  <div class="container">
    <h2>📚 Nuestro catálogo</h2>
    <div class="books-grid">
{cards_html}
    </div>
  </div>
</section>

<section class="about">
  <div class="container">
    <h2>🎮 {ui['author_title']}</h2>
    <p>{ui['author_body']}</p>
  </div>
</section>

<footer>
  <div class="container">
    <p>© 2026 GamerKids Books · GamerKids Books para niños gamers</p>
  </div>
</footer>

<a href="https://wa.me/573214536735?text=Hola%20GamerKids!%20Quiero%20informacion%20sobre%20los%20libros" target="_blank" rel="noopener" class="wa-float" aria-label="WhatsApp"><svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.67-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg><span class="wa-tooltip">Escríbenos por WhatsApp</span></a>

</body>
</html>
"""


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main():
    print(f"[landing] building in {ROOT}")

    # Home
    index_html = render_index()
    (ROOT / "index.html").write_text(index_html, encoding="utf-8")
    print(f"  [ok] index.html ({len(index_html)} bytes)")

    # 6 libros
    for book in BOOKS:
        html = render_book_page(book)
        out_dir = ROOT / book["slug"]
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(html, encoding="utf-8")
        print(f"  [ok] {book['slug']}/index.html ({len(html)} bytes)")

    print(f"[landing] done. 7 pages generated.")
    print(f"[landing] next: reemplaza los 'REEMPLAZAR_BOLD_*' en build_landing.py con tus links de Bold y corre de nuevo.")


if __name__ == "__main__":
    main()
