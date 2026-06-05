<div align="center">

# Panda Akira

### Developer · Linux · Ciberseguridad

<a href="https://github.com/PandaAkiraNakai">
  <img src="https://readme-typing-svg.demolab.com?font=Inter&weight=500&size=20&pause=1200&color=0071E3&center=true&vCenter=true&width=620&height=42&lines=Backend+%C2%B7+Python+%2F+Django;Android+%C2%B7+Kotlin+%2F+Compose;Redes+y+ciberseguridad;Automatizaci%C3%B3n+sobre+Linux" alt="typing" />
</a>

<br/>

<img src="https://komarev.com/ghpvc/?username=PandaAkiraNakai&label=Profile%20views&color=0071e3&style=flat" />
<img src="https://img.shields.io/github/followers/PandaAkiraNakai?label=Followers&style=flat&color=0071e3" />
<img src="https://img.shields.io/github/stars/PandaAkiraNakai?label=Stars&style=flat&color=0071e3" />

</div>

<br/>

## Hola

Construyo herramientas que conectan el teléfono con el escritorio Linux, daemons de automatización y proyectos de redes y seguridad. Me muevo entre **Python/Django** en el backend y **Kotlin/Compose** en Android, casi siempre sobre un setup Linux minimalista.

<br/>

## Toolkit

#### Lenguajes
![Python](https://img.shields.io/badge/Python-f5f5f7?style=flat&logo=python&logoColor=1d1d1f)
![TypeScript](https://img.shields.io/badge/TypeScript-f5f5f7?style=flat&logo=typescript&logoColor=1d1d1f)
![Kotlin](https://img.shields.io/badge/Kotlin-f5f5f7?style=flat&logo=kotlin&logoColor=1d1d1f)
![JavaScript](https://img.shields.io/badge/JavaScript-f5f5f7?style=flat&logo=javascript&logoColor=1d1d1f)
![C++](https://img.shields.io/badge/C++-f5f5f7?style=flat&logo=cplusplus&logoColor=1d1d1f)
![PHP](https://img.shields.io/badge/PHP-f5f5f7?style=flat&logo=php&logoColor=1d1d1f)

#### Frameworks
![Django](https://img.shields.io/badge/Django-f5f5f7?style=flat&logo=django&logoColor=1d1d1f)
![Next.js](https://img.shields.io/badge/Next.js-f5f5f7?style=flat&logo=nextdotjs&logoColor=1d1d1f)
![Astro](https://img.shields.io/badge/Astro-f5f5f7?style=flat&logo=astro&logoColor=1d1d1f)
![Jetpack Compose](https://img.shields.io/badge/Jetpack%20Compose-f5f5f7?style=flat&logo=jetpackcompose&logoColor=1d1d1f)
![Tailwind](https://img.shields.io/badge/Tailwind-f5f5f7?style=flat&logo=tailwindcss&logoColor=1d1d1f)
![Prisma](https://img.shields.io/badge/Prisma-f5f5f7?style=flat&logo=prisma&logoColor=1d1d1f)

#### Infra
![Linux](https://img.shields.io/badge/Linux-f5f5f7?style=flat&logo=linux&logoColor=1d1d1f)
![Docker](https://img.shields.io/badge/Docker-f5f5f7?style=flat&logo=docker&logoColor=1d1d1f)
![Nginx](https://img.shields.io/badge/Nginx-f5f5f7?style=flat&logo=nginx&logoColor=1d1d1f)
![MySQL](https://img.shields.io/badge/MySQL-f5f5f7?style=flat&logo=mysql&logoColor=1d1d1f)
![SQLite](https://img.shields.io/badge/SQLite-f5f5f7?style=flat&logo=sqlite&logoColor=1d1d1f)
![Git](https://img.shields.io/badge/Git-f5f5f7?style=flat&logo=git&logoColor=1d1d1f)

<br/>

## Proyectos

**[Panda Control](https://github.com/PandaAkiraNakai/PandaControl)** &nbsp;·&nbsp; Kotlin · Python · Compose
<!-- excerpt:PandaControl -->
**Panel Android + backend Python** para controlar tu PC Linux desde el celu vía **Tailscale**. Kotlin/Compose con tema cyberpunk, Ktor 3 + SSE para push en vivo, ForegroundService para notifs en background. Daemon stdlib que expone REST/SSE bajo polkit narrow-scope: poder, kill, services, inhibir suspensión, mini-terminal opt-in, audio maestro/por-app/mic (pactl), portapapeles (wl-clipboard), pantallas niri + DPMS + escenas (presets), MPRIS con seek±15/fullscreen, lanzar/cerrar juegos Steam, gestor de archivos (navegar/subir/bajar/renombrar/borrar/abrir, anti path-traversal), journal, updates `pacman`. Auth dual: identidad Tailscale (`tailscale whois`) o Bearer token. Cero servicios externos, cero telemetría. `// linux-control · phone-rig · tailnet-native`
<!-- /excerpt:PandaControl -->

**[OpenCodeAndroid](https://github.com/PandaAkiraNakai/OpenCodeAndroid)** &nbsp;·&nbsp; Kotlin · Compose · Ktor
<!-- excerpt:OpenCodeAndroid -->
**Cliente Android para [OpenCode](https://opencode.ai)** — chatea con tu agente de IA de código desde el celu. Kotlin/Compose con tema cyberpunk: sesiones, **selector de modelos** (providers del server), explorador de archivos del workspace, **adjuntos** (imágenes con reescalado + archivos vía `data:` URL, con guardar/compartir lo recibido) y **dictado por voz on-device** (Speech-to-Text del sistema → texto, sin tokens ni audio al server). Ktor 3 + OkHttp, **SSE** para streaming de respuestas, Basic Auth. Habla por HTTP con cualquier server `opencode serve` en tu LAN/tailnet. `// agent-deck · phone-rig · voice-to-text`
<!-- /excerpt:OpenCodeAndroid -->

**[Cerebro Virtual · Ciberseguridad](https://github.com/PandaAkiraNakai/Cerebro-Virtual-Ciberseguridad)** &nbsp;·&nbsp; Obsidian · Cisco · MikroTik
<!-- excerpt:Cerebro-Virtual-Ciberseguridad -->
Vault Obsidian de **redes y ciberseguridad** — 130 notas en 27 secciones: **Cisco IOS / MikroTik**, administración **Linux**, **reconocimiento** (OSINT, Nmap, nuclei), **pentesting** y defensa (firewalls, **IDS/IPS**, criptografía, phishing), **seguridad web** (45 vulns OWASP), **post-explotación** (escalada Linux/Windows, pivoting, **Active Directory**), **monitoreo** (Zabbix / Splunk / Wireshark), **IoT / Meshtastic**, **cloud** y servicios. Grafo de conocimiento navegable con nota índice **MOC** como cabeza del cerebro. `// net-codex · blue+red · knowledge-graph`
<!-- /excerpt:Cerebro-Virtual-Ciberseguridad -->

**[DerivaShield](https://github.com/PandaAkiraNakai/DerivaShield)** &nbsp;·&nbsp; Python
<!-- excerpt:DerivaShield -->
Detector de anomalías de red basado en **cálculo diferencial**. Trata `paquetes/seg` como señal discreta, calcula primera y segunda derivada, y dispara alerta cuando `f'(t) > μ+kσ` **AND** `f''(t) > 0`. Caza DDoS y port-scans con baja tasa de falsos positivos. `// firewall · IDS · math-as-weapon`
<!-- /excerpt:DerivaShield -->

**[Bots Telegram](https://github.com/PandaAkiraNakai/Bots-Telegram)** &nbsp;·&nbsp; Python
<!-- excerpt:Bots-Telegram -->
Tres daemons que se complementan sobre un deck Linux: **aprobación out-of-band para `sudo`** (askpass + socket UNIX), **chat con Claude Code desde el teléfono** (streaming, voice-notes, documentos) y **panel de control remoto** (procesos, servicios, power-cycle con doble confirmación, updates de sistema vía oneshot polkit, MPRIS con seek). Cero secretos en el repo, deploy idempotente con `systemd` + `polkit`.
<!-- /excerpt:Bots-Telegram -->

**[mem-cli](https://github.com/PandaAkiraNakai/mem-cli)** &nbsp;·&nbsp; Shell · SQLite
<!-- excerpt:mem-cli -->
CLI minimal en bash sobre **SQLite** para **memorias** (hechos persistentes inyectables al inicio de sesión) y **pedidos** (TODOs con estado y prioridad). Pensado como capa de memoria local para **Claude Code** vía hook `SessionStart`, pero sirve para cualquier flujo que necesite estado persistente accesible por CLI. Bootstrap automático del schema, XDG-compliant, cero dependencias más allá de `bash` + `sqlite3`.
<!-- /excerpt:mem-cli -->

**[gamescope-auto](https://github.com/PandaAkiraNakai/gamescope-auto)** &nbsp;·&nbsp; Shell
<!-- excerpt:gamescope-auto -->
Wrapper de **gamescope** para juegos de Steam en niri: detecta el modo exacto del monitor enfocado (ancho × alto × refresh), arranca en pantalla completa nested y auto-focusea la ventana nueva del juego. Recupera el ~1 cm perdido por los indicadores de columna de niri y elimina el "abro el juego pero queda en otra columna sin foco". `// drop-in en Steam Launch Options`
<!-- /excerpt:gamescope-auto -->

**[gamdl-portable](https://github.com/PandaAkiraNakai/gamdl-portable)** &nbsp;·&nbsp; Shell · Apple Music
<!-- excerpt:gamdl-portable -->
Setup portable de **gamdl** para rippear tu música de **Apple Music** en **AAC 256 kbps** sobre cualquier PC Linux Debian/Ubuntu. Un solo `setup.sh` idempotente instala `pipx` + `ffmpeg` + `gamdl`, genera el `config.ini` con tus rutas y descarga en `~/Música/{artista}/{álbum}` con tags y carátula. Las cookies (≈ tu sesión Apple) nunca tocan el repo — las pones a mano en el PC nuevo. `// audio-heist · one-shot · zero-creds-in-repo`
<!-- /excerpt:gamdl-portable -->

**[Cerebro Virtual · Ciencias](https://github.com/PandaAkiraNakai/Cerebro-Virtual-Ciencias)** &nbsp;·&nbsp; Obsidian · Quartz v4
<!-- excerpt:Cerebro-Virtual-Ciencias -->
Vault Obsidian construido como **cerebro virtual de ciencias** — ~375 notas N0→N5 con eje en **paleontología** y ramas en **biología, geología, antropología y química** (expansión taxonómica completa de Dinosauria y Hominoidea). Publicado con **Quartz v4 + nginx en Docker** → [paleo.sergiocubelli.space](https://paleo.sergiocubelli.space).
<!-- /excerpt:Cerebro-Virtual-Ciencias -->

**[obsidian-quartz-publish](https://github.com/PandaAkiraNakai/obsidian-quartz-publish)** &nbsp;·&nbsp; Template · Docker
<!-- excerpt:obsidian-quartz-publish -->
**Template público** extraído del rig anterior: publica tu vault Obsidian como sitio estático con **Quartz v4 + nginx + Docker**, listo para Coolify u otra plataforma docker-compose. Build multi-stage (Quartz se clona en build, el repo del usuario queda chico), magic env `SERVICE_FQDN_SITE` para auto-domain, contenido de ejemplo incluido. `// use this template · plug-in tu vault · burn`
<!-- /excerpt:obsidian-quartz-publish -->

**[Tetris](https://github.com/PandaAkiraNakai/Tetris)** &nbsp;·&nbsp; JavaScript
<!-- excerpt:Tetris -->
Clon de Tetris en HTML5/JS puro, sin frameworks de juego. `// 4 a.m. coding · no deps`
<!-- /excerpt:Tetris -->

<br/>

## Stats

<div align="center">

<img height="160em" src="https://github-readme-stats-nine-tan-12.vercel.app/api?username=PandaAkiraNakai&show_icons=true&hide_border=true&bg_color=00000000&title_color=0071e3&icon_color=0071e3&text_color=8a8a8e" />
<img height="160em" src="https://github-readme-stats-nine-tan-12.vercel.app/api/top-langs/?username=PandaAkiraNakai&layout=compact&hide_border=true&bg_color=00000000&title_color=0071e3&text_color=8a8a8e&langs_count=8" />

<br/><br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/PandaAkiraNakai/PandaAkiraNakai/output/github-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/PandaAkiraNakai/PandaAkiraNakai/output/github-snake.svg" />
  <img alt="Snake" src="https://raw.githubusercontent.com/PandaAkiraNakai/PandaAkiraNakai/output/github-snake.svg" />
</picture>

</div>

<br/>

## Links

<div align="center">

<a href="https://github.com/PandaAkiraNakai">
  <img src="https://img.shields.io/badge/GitHub-f5f5f7?style=flat&logo=github&logoColor=1d1d1f" />
</a>
<a href="https://paleo.sergiocubelli.space">
  <img src="https://img.shields.io/badge/paleo.sergiocubelli.space-f5f5f7?style=flat&logo=obsidian&logoColor=1d1d1f" />
</a>

</div>
