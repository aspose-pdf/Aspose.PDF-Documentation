---
title: Proteger y firmar archivos PDF en Python
linktitle: Protección y firma en PDF
type: docs
weight: 210
url: /es/python-net/securing-and-signing/
description: Aprenda a firmar, cifrar, descifrar y proteger archivos PDF en Python, incluidas firmas digitales, tarjetas inteligentes y permisos de documentos.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Firme, cifre, descifre y proteja documentos PDF en Python
Abstract: Esta sección explica cómo proteger y firmar documentos PDF usando Aspose.PDF for Python via .NET. Aprenda cómo aplicar firmas digitales, usar tarjetas inteligentes y certificados, extraer información de firmas y gestionar el cifrado de PDF, contraseñas y privilegios de acceso en Python.
---

Esta sección explica cómo aplicar de forma segura firmas digitales a documentos PDF usando Python Library. Mientras que los términos firma electrónica y firma digital a veces se usan indistintamente, no son lo mismo. Una firma digital está respaldada por un [autoridad certificadora](https://en.wikipedia.org/wiki/Certificate_authority), proporcionando un sello de confianza que protege el documento contra la manipulación. En contraste, una firma electrónica se utiliza típicamente para indicar la intención de una persona de firmar un documento, sin el mismo nivel de validación de seguridad.

Utilice estas guías cuando necesite proteger el contenido de PDF, controlar los permisos del documento, verificar la confianza o aplicar firmas basadas en certificados en flujos de trabajo de Python.

## Tareas de seguridad y firma cubiertas

Aspose.PDF admite firmas digitales:

- PKCS1 con algoritmo de firma RSA y resumen SHA-1.
- PKCS7 con algoritmo de firma RSA y resumen SHA-1.
- PKCS7 separado con algoritmos de firma DSA, RSA y ECDSA. Los algoritmos de resumen admitidos dependen del algoritmo de firma.
- Firma de sello de tiempo.

Algoritmos de resumen para PKCS7 separado:

- DSA - SHA-1.
- RSA - SHA-1, SHA-256, SHA-384, SHA-512.
- ECDSA - SHA-256, SHA-384, SHA-512, SHA3-256, SHA3-384, SHA3-512.

Se recomienda evitar firmas digitales con el algoritmo de resumen SHA-1 debido a su inseguridad.

- [Firmar digitalmente archivo PDF](/pdf/es/python-net/digitally-sign-pdf-file/)
- [Establecer privilegios, cifrar y descifrar archivo PDF](/pdf/es/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)
- [Extraer información de imagen y firma](/pdf/es/python-net/extract-image-and-signature-information/)
- [Firmar documento PDF desde tarjeta inteligente](/pdf/es/python-net/sign-pdf-document-from-smart-card/)
