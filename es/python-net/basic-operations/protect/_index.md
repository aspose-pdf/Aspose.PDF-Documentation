---
title: Proteger archivos PDF en Python
linktitle: Cifrar y descifrar archivo PDF
type: docs
weight: 70
url: /es/python-net/protect-pdf-file/
description: Aprende cómo cifrar archivos, descifrar PDFs protegidos y cambiar contraseñas en Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Establecer permisos de PDF y gestionar el cifrado en Python
Abstract: >
    Esta página de documentación explica cómo establecer privilegios de documento, aplicar cifrado y descifrar archivos PDF usando Aspose.PDF for Python. Guía a los desarrolladores a través de la configuración de contraseñas de usuario y de propietario, definiendo restricciones de acceso (como imprimir, copiar o editar). Los ejemplos de código ilustran cómo proteger contenido sensible y gestionar la seguridad de PDF de manera eficaz dentro de aplicaciones Python, garantizando un acceso controlado y la confidencialidad de los datos.
---

## Cifrar PDF con contraseña y permisos

Aspose.PDF for Python muestra cómo asegurar un documento PDF usando cifrado basado en contraseña:

1. Cargar el documento PDF.
1. Crear un objeto de permisos.
1. Permitir permisos específicos.
1. Establecer contraseñas de usuario y propietario.
1. Seleccionar el algoritmo de cifrado.
1. Aplicar cifrado al documento.
1. Guardar el PDF cifrado.

```python
import aspose.pdf as ap
import sys
from os import path

def encrypt_password(infile, outfile):
    """
    Encrypt PDF with password and permissions.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        encrypt_password("sample.pdf", "sample_protected.pdf")

    Note:
        Uses AES 128-bit encryption. Allows screen readers, forbids all other operations.
        User password: "userpassword", Owner password: "ownerpassword".
    """
    document = ap.Document(infile)
    document_privilege = ap.facades.DocumentPrivilege.forbid_all
    document_privilege.allow_screen_readers = True

    document.encrypt(
        "userpassword",
        "ownerpassword",
        document_privilege,
        ap.CryptoAlgorithm.AESx128,
        False,
    )
    document.save(outfile)
```

## Cifrar PDF con permisos completos

Encripta un documento PDF mientras permite permisos de acceso completo usando Aspose.PDF for Python. El ejemplo utiliza cifrado RC4 de 128 bits, lo que garantiza una seguridad básica manteniendo la compatibilidad con lectores PDF más antiguos.

1. Cargar el documento PDF.
1. Define contraseñas de usuario y propietario.
1. Establece permisos de acceso completo.
1. Seleccionar el algoritmo de cifrado.
1. Llama al método encrypt() con contraseñas, permisos y algoritmo.
1. Guardar el PDF cifrado.

```python
import aspose.pdf as ap
import sys
from os import path

def encrypt_pdf_file(infile, outfile):
    """
    Encrypt PDF with full permissions.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        encrypt_pdf_file("sample.pdf", "sample_protected.pdf")

    Note:
        Uses RC4 128-bit encryption with allow_all privileges.
    """
    document = ap.Document(infile)
    document.encrypt(
        "userpassword",
        "ownerpassword",
        ap.facades.DocumentPrivilege.allow_all,
        ap.CryptoAlgorithm.RC4x128,
        False,
    )
    document.save(outfile)
```

## Descifrar archivo PDF usando la contraseña del propietario

Para eliminar la protección por contraseña y restaurar el acceso completo:

1. Cargue el PDF encriptado usando la contraseña correcta ('password' es la contraseña de usuario o de propietario).
1. Elimine toda la protección con contraseña y los ajustes de encriptación del documento.
1. Guarde el PDF ahora sin protección en el archivo de salida especificado.

```python
import aspose.pdf as ap
import sys
from os import path

def decrypt_pdf_file(infile, outfile):
    """
    Decrypt password-protected PDF.

    Args:
        infile (str): Input encrypted PDF filename
        outfile (str): Output decrypted PDF filename

    Returns:
        None

    Example:
        decrypt_pdf_file("sample_protected.pdf", "sample_unprotected.pdf")

    Note:
        Requires user password to open document.
    """
    document = ap.Document(infile, "userpassword")
    document.decrypt()
    document.save(outfile)
```

## Cambiar la contraseña de un archivo PDF

Actualizar las credenciales de seguridad (contraseñas de usuario y propietario) de un documento PDF mientras se preservan su contenido y estructura.

1. Abra el PDF utilizando la contraseña de propietario existente ('owner'), que otorga acceso total, incluida la posibilidad de cambiar la configuración de seguridad.
1. Reemplace las contraseñas antiguas con una nueva contraseña de usuario ('newuser') y una nueva contraseña de propietario ('newowner').
1. Guarde el PDF con la configuración de contraseñas actualizada.

```python
import aspose.pdf as ap
import sys
from os import path

def change_password(infile, outfile):
    """
    Change user and owner passwords.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        change_password("sample_protected.pdf", "sample_changepassword.pdf")

    Note:
        Changes from ownerpassword to newuser/newowner.
    """
    document = ap.Document(infile, "ownerpassword")
    document.change_passwords("ownerpassword", "newuser", "newowner")
    document.save(outfile)

```

## Determinar la contraseña correcta del array

En algunos escenarios, es posible que necesite identificar la contraseña correcta de una lista de posibles candidatos para acceder a un PDF protegido. El fragmento de código a continuación muestra cómo comprobar si un archivo PDF está protegido con contraseña y luego intentar desbloquearlo iterando a través de una lista predefinida de contraseñas utilizando Aspose.PDF for Python via .NET.

El proceso incluye:

1. Usando PdfFileInfo para detectar si el PDF está encriptado.
1. Abra el PDF con cada contraseña usando ap.Document().
1. Si tiene éxito, imprime el número de páginas.
1. Si no, captura la excepción y reporta la contraseña fallida.

```python
import aspose.pdf as ap
import sys
from os import path

def determine_correct_password_from_list(infile):
    """
    Test multiple passwords to find correct one.

    Args:
        infile (str): Input encrypted PDF filename

    Returns:
        None

    Example:
        determine_correct_password_from_list("sample_protected.pdf")

    Note:
        Tries passwords: test, test1, test2, test3, userpassword.
        Prints page count if password is correct.
    """
    info = ap.facades.PdfFileInfo(infile)
    print(f"File is password protected {info.is_encrypted}")

    passwords = "test", "test1", "test2", "test3", "userpassword"

    for password in passwords:
        try:
            document = ap.Document(infile, password)
            count = len(document.pages)
            if count > 0:
                print(f"Number of Page in document are = {count}")
        except RuntimeError as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
```
