---
title: Cifrar archivo PDF
linktitle: Cifrar archivo PDF
type: docs
weight: 30
url: /es/python-net/encrypt-pdf-file/
description: Cifre un documento PDF y configure los permisos para controlar lo que los usuarios pueden hacer con el archivo.
lastmod: "2026-03-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cifre PDF y controle las acciones del usuario
Abstract: Aprenda cómo cifrar un PDF mientras define permisos específicos de usuario utilizando Aspose.PDF for Python via .NET. Esta guía muestra cómo permitir o restringir acciones como imprimir y copiar, mientras mantiene el documento seguro.
---

## Cifrar PDF con contraseña de usuario y de propietario

Proteger los documentos PDF es esencial al compartir contenido sensible o restringido. El cifrado le permite proteger un documento con contraseñas y definir qué acciones pueden realizar los usuarios. Este fragmento de código muestra cómo aplicar contraseñas de usuario y propietario, junto con permisos de acceso, para asegurar un archivo PDF.

1. Crear un objeto PdfFileSecurity.
1. Vincular el PDF de entrada.
1. Definir privilegios de documento.
1. Cifrar el PDF.
1. Guardar el PDF cifrado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Encrypt PDF with User and Owner Password
def encrypt_pdf_with_user_owner_password(infile, outfile):
    """Encrypt a PDF document using user and owner passwords."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define document privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Encrypt the PDF
    file_security.encrypt_file(
        "user_password", "owner_password", privilege, pdf_facades.KeySize.X128
    )

    # Save encrypted PDF
    file_security.save(outfile)
```

## Encriptar PDF con permisos

El siguiente fragmento de código explica cómo permitir acciones seleccionadas como imprimir y copiar mientras se restringen otras.

1. Inicializar el [PdfFileSecurity](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) clase.
1. Vincular el PDF de entrada.
1. Configurar privilegios del documento.
1. Llamar al método 'encrypt_file()'.
1. Guardar el PDF cifrado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Encrypt PDF with Permissions
def encrypt_pdf_with_permissions(infile, outfile):
    """Encrypt a PDF document and configure specific permissions."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Configure privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True
    privilege.allow_copy = True

    # Encrypt the PDF
    file_security.encrypt_file(
        "user_password", "owner_password", privilege, pdf_facades.KeySize.X128
    )

    # Save encrypted PDF
    file_security.save(outfile)
```

## Cifrar PDF con algoritmo de encriptación

El cifrado de PDF no solo protege los documentos con contraseñas, sino que también permite elegir el algoritmo de cifrado y su robustez. Seleccionar el algoritmo apropiado garantiza una seguridad más fuerte para documentos sensibles.

1. Cree un objeto PdfFileSecurity.
1. Vincular el PDF de entrada.
1. Definir privilegios de documento.
1. Cifre el PDF con el algoritmo.
1. Guardar el PDF cifrado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Encrypt PDF with Encryption Algorithm
def encrypt_pdf_with_encryption_algorithm(infile, outfile):
    """Encrypt a PDF document using a specific encryption algorithm."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Encrypt the PDF using AES algorithm
    file_security.encrypt_file(
        "user_password",
        "owner_password",
        privilege,
        pdf_facades.KeySize.X256,
        pdf_facades.Algorithm.AES,
    )

    # Save encrypted PDF
    file_security.save(outfile)
```
