---
title: Establecer privilegios en un archivo PDF existente
linktitle: Establecer privilegios en un archivo PDF existente
type: docs
weight: 40
url: /es/python-net/set-privileges/
description: Establezca y administre los privilegios de documentos PDF para controlar acciones del usuario como imprimir, copiar y editar.
lastmod: "2026-03-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Administrar permisos y controles de acceso de PDF
Abstract: Aprenda cómo controlar lo que los usuarios pueden hacer con un PDF estableciendo privilegios de documento usando Aspose.PDF for Python via .NET. Esta guía cubre la aplicación de permisos con o sin contraseñas para restringir acciones como imprimir, copiar o editar.
---

## Establecer privilegios de PDF sin contraseñas

Verifique cómo aplicar privilegios de documento a un PDF sin especificar contraseñas de usuario o propietario utilizando Aspose.PDF for Python via .NET. Este fragmento de código muestra cómo controlar las acciones permitidas mientras se mantiene el documento accesible.

1. Crear un objeto 'PdfFileSecurity'.
1. Vincular el PDF de entrada.
1. Definir privilegios del documento.
1. Llame al método 'set_privilege()' sin pasar contraseñas.
1. Guarde el PDF actualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Set PDF Privileges Without Passwords
def set_pdf_privileges_without_passwords(infile, outfile):
    """Set PDF privileges without specifying user and owner passwords."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Apply privileges (owner password will be generated automatically)
    file_security.set_privilege(privilege)

    # Save updated PDF
    file_security.save(outfile)
```

## Establecer privilegios de PDF con contraseñas de usuario y propietario

Para asegurar completamente un documento PDF, a menudo se necesita tanto control de acceso (contraseñas) como restricciones de uso (permisos). Al combinar estos, puedes garantizar que solo los usuarios autorizados puedan abrir el documento y realizar acciones específicas.

Usando el método set_privilege con parámetros de contraseña, puedes:

- Proteger el documento con una contraseña de usuario
- Definir una contraseña de propietario para control total
- Configurar acciones permitidas y restringidas
- Aplicar políticas de seguridad a nivel de documento

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Set PDF Privileges with User and Owner Passwords
def set_pdf_privileges_with_passwords(infile, outfile):
    """Set PDF privileges using user and owner passwords."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True
    privilege.allow_copy = False

    # Apply privileges with passwords
    file_security.set_privilege("user_password", "owner_password", privilege)

    # Save updated PDF
    file_security.save(outfile)
```

## Intenta establecer privilegios de PDF sin excepción

Este fragmento de código explica cómo controlar el acceso y restringir acciones como copiar, mientras se permiten otras como imprimir.

1. Cree un objeto 'PdfFileSecurity'.
1. Carga el PDF de origen usando el método 'bind_pdf()'.
1. Definir privilegios del documento.
1. Aplicar privilegios con contraseñas.
1. Guarde el PDF actualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Try Set PDF Privileges Without Exception
def try_set_pdf_privileges_without_exception(infile, outfile):
    """Attempt to set PDF privileges without throwing an exception on failure."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Attempt to apply privileges
    result = file_security.try_set_privilege(
        "user_password", "owner_password", privilege
    )

    # Save only if operation succeeded
    if result:
        file_security.save(outfile)
    else:
        print("Setting privileges failed. Check passwords or document state.")
```
