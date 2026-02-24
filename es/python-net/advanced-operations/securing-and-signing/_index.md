---
title: Asegurar y firmar PDF en Python
linktitle: Asegurar y firmar en PDF
type: docs
weight: 210
url: /es/python-net/securing-and-signing/
description: Esta sección describe las características de usar una firma y asegurar su documento PDF utilizando Python
lastmod: "2025-06-23"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Firmar documentos PDF con Python
Abstract: Esta sección de la documentación de Aspose.PDF para Python via .NET brinda una guía completa sobre cómo asegurar y firmar documentos PDF de forma programática. Cubre temas esenciales, incluyendo protección con contraseña, algoritmos de cifrado, aplicación y verificación de firmas digitales, gestión de certificados y permisos de documentos. Los desarrolladores aprenderán a implementar varios niveles de seguridad para proteger contenido sensible, garantizar la integridad del documento y cumplir con normas regulatorias. Los ejemplos y referencias de API permiten una integración rápida de las funciones de seguridad en aplicaciones Python, facilitando la protección de flujos de trabajo PDF con confianza.
---

Esta sección explica cómo aplicar de manera segura firmas digitales a documentos PDF usando la biblioteca Python. Aunque los términos firma electrónica y firma digital a veces se usan indistintamente, no son lo mismo. Una firma digital está respaldada por una [autoridad certificadora](https://en.wikipedia.org/wiki/Certificate_authority), que proporciona un sello de confianza que protege el documento contra manipulaciones. En contraste, una firma electrónica se utiliza típicamente para indicar la intención de una persona de firmar un documento, sin el mismo nivel de validación de seguridad.

Aspose.PDF admite firmas digitales:

- PKCS1 con algoritmo de firma RSA y digest SHA-1.
- PKCS7 con algoritmo de firma RSA y digest SHA-1.
- PKCS7 detached con algoritmos de firma DSA, RSA y ECDSA. Los algoritmos de digestión compatibles dependen del algoritmo de firma.
- Firma de marca de tiempo.

Algoritmos de digestión para PKCS7 detached:

- DSA - SHA-1.
- RSA - SHA-1, SHA-256, SHA-384, SHA-512.
- ECDSA - SHA-256, SHA-384, SHA-512, SHA3-256, SHA3-384, SHA3-512.

Se recomienda evitar firmas digitales con el algoritmo de digestión SHA-1 debido a su inseguridad.

- [Firmar digitalmente archivo PDF](/pdf/python-net/digitally-sign-pdf-file/)
- [Establecer privilegios, cifrar y descifrar archivo PDF](/pdf/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)
- [Extraer información de imagen y firma](/pdf/python-net/extract-image-and-signature-information/)
- [Firmar documento PDF desde tarjeta inteligente](/pdf/python-net/sign-pdf-document-from-smart-card/)
