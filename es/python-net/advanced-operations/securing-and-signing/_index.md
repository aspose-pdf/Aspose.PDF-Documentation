---
title: Seguridad y firma de archivos PDF en Python
linktitle: Seguridad y firma en PDF
type: docs
weight: 210
url: /es/python-net/securing-and-signing/
description: Aprenda cómo firmar, cifrar, descifrar y asegurar archivos PDF en Python, incluyendo firmas digitales, tarjetas inteligentes y permisos de documentos.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Firme, cifre, descifre y proteja documentos PDF en Python
Abstract: Esta seccion explica como asegurar y firmar documentos PDF usando Aspose.PDF para Python a traves de .NET. Aprenda como aplicar firmas digitales, usar tarjetas inteligentes y certificados, extraer informacion de firmas y gestionar el cifrado de PDF, las contraseñas y los privilegios de acceso en Python.
---

Esta seccion explica como aplicar de forma segura firmas digitales a documentos PDF usando Python. Aunque los terminos firma electronica y firma digital a veces se usan indistintamente, no son lo mismo. Una firma digital esta respaldada por una [autoridad certificadora](https://en.wikipedia.org/wiki/Certificate_authority), lo que proporciona un sello de confianza que protege el documento contra la manipulacion. En cambio, una firma electronica suele utilizarse para indicar la intencion de una persona de firmar un documento, sin el mismo nivel de validacion de seguridad.

Utilice estas guías cuando necesite proteger el contenido PDF, controlar los permisos del documento, verificar la confianza o aplicar firmas basadas en certificados en flujos de trabajo de Python.

## Tareas de seguridad y firma cubiertas

Aspose.PDF admite firmas digitales:

- PKCS1 con algoritmo de firma RSA y resumen SHA-1.
- PKCS7 con algoritmo de firma RSA y resumen SHA-1.
- PKCS7 independiente con algoritmos de firma DSA, RSA y ECDSA. Los algoritmos de resumen admitidos dependen del algoritmo de firma.
- Firma de sello de tiempo.

Algoritmos de resumen para PKCS7 independiente:

- DSA - SHA-1.
- RSA - SHA-1, SHA-256, SHA-384, SHA-512.
- ECDSA - SHA-256, SHA-384, SHA-512, SHA3-256, SHA3-384, SHA3-512.

Se recomienda evitar firmas digitales con el algoritmo de resumen SHA-1 debido a su inseguridad.

- [Firmar digitalmente un archivo PDF](/pdf/es/python-net/digitally-sign-pdf-file/)
- [Establecer privilegios, cifrar y descifrar un archivo PDF](/pdf/es/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)
- [Extraer informacion de imagen y firma](/pdf/es/python-net/extract-image-and-signature-information/)
- [Firmar un documento PDF desde una tarjeta inteligente](/pdf/es/python-net/sign-pdf-document-from-smart-card/)
