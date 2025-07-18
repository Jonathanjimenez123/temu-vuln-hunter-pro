#📄 temu_xss_redirect_report.md

# 🔥 XSS + Open Redirect encadenado en Temu permite robo de sesión o phishing avanzado

## 🧠 Descripción General

Se ha descubierto una vulnerabilidad **crítica** en la plataforma de Temu que permite **inyectar código JavaScript (XSS reflejado)** a través de una redirección abierta (`open redirect`) en uno de sus endpoints. Esta falla puede explotarse para ejecutar scripts maliciosos en el navegador de los usuarios y **redirigirlos a sitios de phishing o robar sus tokens**.

---

## 🎯 Dominio afectado

https://www.temu.com

---

## 📌 Severidad: **Alta (9.1/10)**  

Clasificación según [OWASP Top 10](https://owasp.org/www-project-top-ten/):
- A1:2017 – **Injection (XSS)**
- A10:2017 – **Unvalidated Redirects and Forwards**

---

## 🛠️ Componentes vulnerables

- Endpoint: `https://www.temu.com/redirect?url=...`
- No valida correctamente los parámetros antes de redirigir.
- El contenido HTML donde se carga esta URL refleja la cadena de redirección sin sanitización.

---

## 🔁 Encadenamiento

1. Se usa el parámetro vulnerable `?url=` para redirigir al usuario a un sitio externo controlado.
2. El sitio externo refleja una cadena JavaScript maliciosa en el HTML.
3. Esto permite inyectar y ejecutar código JavaScript directamente en el navegador del usuario.

---

## 🧪 PoC Técnica (Prueba de Concepto)

### Payload completo:

```html
https://www.temu.com/redirect?url=https://attacker.site/xss?payload=%3Cscript%3Ealert('XSS+Redirect')%3C/script%3E
El usuario accede al enlace anterior.

Temu redirige automáticamente sin validar al sitio externo.

El sitio atacante refleja el payload inyectado.

El script se ejecuta en el navegador.

#🖼️ Captura de pantalla

#📉 Impacto técnico

Robo de sesión (session hijacking)

Redirección a phishing con apariencia legítima de Temu

Robo de credenciales o tokens OAuth

Ejecución arbitraria de código en navegador de usuario

#✅ Recomendaciones

Validar y restringir los parámetros url= a una lista blanca de dominios permitidos (whitelist).

Usar una función de escape/sanitización HTML para evitar reflejo directo.

Agregar encabezados de seguridad como Content-Security-Policy.

Auditar otros endpoints con parámetros de redirección similares.

#🧑‍💻 Reportado por

Jonathan Jiménez
https://github.com/Jonathanjimenez123
https://github.com/Jonathanjimenez123/temu-vuln-hunter-pro





