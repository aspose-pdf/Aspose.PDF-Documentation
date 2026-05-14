---
title: Cifrar y descifrar archivos PDF en Python
linktitle: Cifrar y descifrar archivo PDF
type: docs
weight: 70
url: /es/python-net/set-privileges-encrypt-and-decrypt-pdf-file/
description: Aprende cómo establecer privilegios de PDF, encriptar archivos, descifrar PDFs protegidos y cambiar contraseñas en Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Establece permisos de PDF y gestiona el cifrado en Python.
Abstract: Esta página de documentación explica cómo establecer privilegios de documento, aplicar cifrado y descifrar archivos PDF usando Aspose.PDF for Python. Guía a los desarrolladores a través de la configuración de contraseñas de usuario y propietario, definiendo restricciones de acceso (como imprimir, copiar o editar). Los ejemplos de código ilustran cómo proteger contenido sensible y gestionar la seguridad de PDF de manera eficaz dentro de aplicaciones Python, garantizando un acceso controlado y la confidencialidad de los datos.
---

Gestionar la seguridad de documentos es esencial al trabajar con contenido sensible o crítico para el negocio. Aspose.PDF for Python via .NET ofrece una API robusta para aplicar encriptación de forma programática, controlar el acceso mediante permisos y descifrar archivos PDF protegidos.

Este artículo guía a los desarrolladores de Python a través de ejemplos prácticos para establecer privilegios, aplicar y eliminar encriptación, cambiar contraseñas y detectar estados de protección — todo dentro de un flujo de trabajo de PDF.

Aspose.PDF for Python via .NET brinda a los desarrolladores un control total sobre la seguridad de PDF:

**Establecer privilegios** - Control de acceso granular mediante permisos.
**Cifrar archivo** - Aplicar cifrado AES o RC4 con contraseñas personalizadas.
**Desencriptar archivo** - Eliminar la seguridad usando la contraseña del propietario.
**Cambiar contraseñas** - Rotar o actualizar credenciales sin alterar el contenido.
**Inspect Security** - Detectar estado de cifrado o tipos de contraseña requeridos.

Utilice esta página cuando necesite proteger documentos PDF con contraseñas, restringir la impresión o la copia, rotar credenciales o inspeccionar si un documento está cifrado.

## Establecer privilegios en un archivo PDF existente

Puede restringir o permitir operaciones específicas (p. ej., imprimir, copiar, rellenar formularios) asignando contraseñas de usuario y de propietario junto con privilegios de acceso.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def set_privileges_on_existing_pdf_file(infile: str, outfile: str) -> None:
    """Set restricted privileges on an existing PDF document."""
    with ap.Document(infile) as document:
        document_privilege = ap.facades.DocumentPrivilege.forbid_all
        document_privilege.allow_screen_readers = True
        document.encrypt(
            "user",
            "owner",
            document_privilege,
            ap.CryptoAlgorithm.AESx128,
            False,
        )
        document.save(outfile)
```

## Cifrar archivo PDF usando diferentes tipos y algoritmos de cifrado

Cifrar un PDF asegura que solo los usuarios con credenciales válidas puedan abrir o modificar el archivo.

>Términos clave:

- Contraseña de usuario. Requerida para abrir el documento.

- Contraseña del propietario. Necesaria para cambiar permisos o eliminar el cifrado.

- KeySize. Use AE_SX128 para obtener la máxima seguridad en flujos de trabajo modernos.

El siguiente fragmento de código le muestra cómo cifrar archivos PDF.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def encrypt_pdf_file(infile: str, outfile: str) -> None:
    """Encrypt a PDF document with user and owner passwords."""
    with ap.Document(infile) as document:
        document.encrypt(
            "user",
            "owner",
            ap.Permissions.EXTRACT_CONTENT,
            ap.CryptoAlgorithm.AESx128,
        )
        document.save(outfile)
```

## Descifrar archivo PDF usando la contraseña del propietario

Para eliminar la protección con contraseña y restaurar el acceso completo:

1. Carga el PDF cifrado usando la contraseña correcta ('password' es la contraseña de usuario o de propietario).
1. Elimina toda la protección con contraseña y la configuración de cifrado del documento.
1. Guarda el PDF ahora sin protección en el archivo de salida especificado.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def decrypt_pdf_file(infile: str, outfile: str) -> None:
    """Decrypt a password-protected PDF document."""
    with ap.Document(infile, "password") as document:
        document.decrypt()
        document.save(outfile)
```

## Cifrar y descifrar un PDF con certificados de clave pública

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def pub_sec_encryption(
    crypto_algorithm,
    pub_cert: str,
    in_pfx: str,
    outfile: str,
) -> None:
    """Demonstrate public-key encryption and decryption."""
    pfx_password = "12345"

    with ap.Document() as document:
        document.info.title = "TestTitle"
        document.info.author = "TestAuthor"
        page = document.pages.add()
        page.paragraphs.add(ap.text.TextFragment("Hello World!"))

        with open(pub_cert, "rb") as file_stream:
            byte_content = file_stream.read()

        document.encrypt(
            ap.Permissions.PRINT_DOCUMENT,
            crypto_algorithm,
            [byte_content],
        )
        document.save(outfile)

    with ap.Document(
        outfile,
        ap.security.CertificateEncryptionOptions(pub_cert, in_pfx, pfx_password),
    ) as document:
        print(document.info.title)
        print(document.info.author)

        text_absorber = ap.text.TextAbsorber()
        document.pages[1].accept(text_absorber)
        print(text_absorber.text)

        document.decrypt()
        document.save(path.join(path.dirname(outfile), "pubsec_decrypted_out.pdf"))
```

## Cambiar la contraseña de un archivo PDF

Actualizar las credenciales de seguridad (contraseñas de usuario y propietario) de un documento PDF mientras se preserva su contenido y estructura.

1. Abre el PDF usando la contraseña de propietario existente ('owner'), lo que brinda acceso total, incluida la autorización para cambiar la configuración de seguridad.
1. Reemplaza las contraseñas antiguas con una nueva contraseña de usuario ('newuser') y una nueva contraseña de propietario ('newowner').
1. Guarda el PDF con la configuración de contraseña actualizada.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def change_password(infile: str, outfile: str) -> None:
    """Change the passwords of a password-protected PDF document."""
    with ap.Document(infile, "owner") as document:
        document.change_passwords("owner", "newuser", "newowner")
        document.save(outfile)
```

## Cómo - determinar si el PDF de origen está protegido con contraseña

### Determinar la contraseña correcta del array

En algunos escenarios, es posible que necesite identificar la contraseña correcta de una lista de candidatos potenciales para acceder a un PDF protegido. El fragmento de código a continuación demuestra cómo verificar si un archivo PDF está protegido con contraseña y luego intentar desbloquearlo iterando a través de una lista predefinida de contraseñas usando Aspose.PDF for Python via .NET.

El proceso incluye:

1. Usando PdfFileInfo para detectar si el PDF está encriptado.
1. Intenta abrir el PDF con cada contraseña usando ap.Document().
1. Si tiene éxito, imprime el número de páginas.
1. Si no, captura la excepción y reporta la contraseña fallida.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def determine_correct_password_from_array(infile: str) -> None:
    """Try a list of passwords until the document opens successfully."""
    with ap.facades.PdfFileInfo() as pdf_file_info:
        pdf_file_info.bind_pdf(infile)
        print(f"File is password protected {pdf_file_info.is_encrypted}")

    passwords = ["test", "test1", "test2", "test3", "sample"]

    for password in passwords:
        try:
            with ap.Document(infile, password) as document:
                if len(document.pages) > 0:
                    print(f"Password = {password} is correct")
                    print(f"Number of pages in document = {len(document.pages)}")
                    break
        except Exception:
            print(f"Password = {password} is not correct")
```

## Temas de Seguridad Relacionados

- [Protege y firma archivos PDF en Python](/pdf/es/python-net/securing-and-signing/)
- [Firmar digitalmente archivos PDF en Python](/pdf/es/python-net/digitally-sign-pdf-file/)
- [Extraer información de la firma del PDF en Python](/pdf/es/python-net/extract-image-and-signature-information/)
- [Firmar documentos PDF desde una tarjeta inteligente en Python](/pdf/es/python-net/sign-pdf-document-from-smart-card/)

