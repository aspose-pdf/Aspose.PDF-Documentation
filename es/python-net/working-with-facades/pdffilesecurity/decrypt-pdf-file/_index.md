---
title: Descifrar archivo PDF
linktitle: Descifrar archivo PDF
type: docs
weight: 20
url: /es/python-net/decrypt-pdf-file/
description: Esta guía explica cómo eliminar restricciones como imprimir, copiar y editar para obtener acceso total a su documento PDF.
lastmod: "2026-03-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar protección con contraseña de un PDF
Abstract: Este artículo muestra cómo descifrar un archivo PDF usando una contraseña de propietario. Cubre el proceso de eliminación de restricciones de seguridad que limitan acciones como imprimir, editar o copiar contenido. Al aplicar la contraseña de propietario correcta, los usuarios pueden desbloquear el documento y recuperar el control total de sus funciones.
---

## Descifrar PDF con contraseña de propietario

Descifre un documento PDF protegido con contraseña usando la contraseña de propietario con Aspose.PDF for Python via .NET. Esta operación elimina el cifrado y permite el acceso sin restricciones al documento.

1. Cree un objeto 'PdfFileSecurity'.
1. Cargue el PDF cifrado usando el método 'bind_pdf()'.
1. Desencripte el documento.
1. Guarde el PDF desencriptado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Decrypt PDF with Owner Password
def decrypt_pdf_with_owner_password(infile, outfile):
    """Decrypt a PDF document using the owner password."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Decrypt the PDF
    file_security.decrypt_file("owner_password")

    # Save decrypted PDF
    file_security.save(outfile)
```

## Intentar descifrar PDF sin excepción

Los documentos PDF a menudo están protegidos con contraseñas para restringir el acceso y el uso. Para acceder o modificar completamente dichos documentos, puede ser necesario eliminar el cifrado. Desencripte un documento PDF asegurado usando la contraseña del propietario para eliminar el cifrado y las restricciones de acceso con Aspose.PDF for Python via .NET.

1. Cree un objeto 'PdfFileSecurity'.
1. Vincular el PDF de entrada.
1. Desencripte el PDF.
1. Guarde el PDF de salida.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Try Decrypt PDF Without Exception
def try_decrypt_pdf_without_exception(infile, outfile):
    """Attempt to decrypt a PDF without throwing an exception on failure."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Attempt to decrypt the PDF
    result = file_security.try_decrypt_file("owner_password")

    # Save only if decryption was successful
    if result:
        file_security.save(outfile)
    else:
        print("Decryption failed. Check password or document security.")
```
