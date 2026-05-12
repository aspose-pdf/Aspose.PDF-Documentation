---
title: Proteger archivos PDF en Python
linktitle: Cifrar y descifrar archivo PDF
type: docs
weight: 70
url: /es/python-net/protect-pdf-file/
description: Aprenda cómo cifrar archivos, descifrar PDFs protegidos y cambiar contraseñas en Python.
lastmod: "2026-05-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Establecer permisos de PDF y gestionar el cifrado en Python
Abstract: Esta página explica cómo establecer privilegios de documento, aplicar cifrado, descifrar archivos PDF y cambiar contraseñas utilizando Aspose.PDF for Python via .NET. Cubre la configuración de contraseñas de usuario y propietario, la definición de restricciones de acceso (como imprimir, copiar y editar), y la gestión de la seguridad de PDF en aplicaciones Python.
---

## Cifrar PDF con contraseña y permisos

Utilice Aspose.PDF for Python via .NET para proteger un documento PDF con cifrado basado en contraseña y permisos restringidos.

1. Cargue el documento PDF.
1. Cree un objeto de permisos `DocumentPrivilege`.
1. Habilite los permisos requeridos.
1. Establezca las contraseñas de usuario y de propietario.
1. Elija el algoritmo de cifrado.
1. Aplique el cifrado al documento.
1. Guarde el PDF cifrado.

```python
import aspose.pdf as ap

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

Cifre un documento PDF mientras permite permisos de acceso completo usando Aspose.PDF for Python via .NET. Este ejemplo usa cifrado RC4 de 128 bits para compatibilidad con visores PDF más antiguos.

1. Cargue el documento PDF.
1. Defina las contraseñas de usuario y propietario.
1. Establezca permisos de acceso completo.
1. Elija el algoritmo de cifrado.
1. Llame a `encrypt()` con contraseñas, permisos y algoritmo.
1. Guarde el PDF cifrado.

```python
import aspose.pdf as ap

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

Para eliminar la protección con contraseña y restaurar el acceso completo:

1. Cargue el PDF cifrado usando la contraseña correcta (usuario o propietario).
1. Elimine toda la protección con contraseña y los ajustes de cifrado del documento.
1. Guarde el PDF ahora desprotegido en el archivo de salida especificado.

```python
import aspose.pdf as ap

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

Actualice las credenciales de seguridad (contraseñas de usuario y propietario) de un documento PDF mientras preserva su contenido y estructura.

1. Abra el PDF usando la contraseña de propietario existente, que brinda acceso completo a la configuración de seguridad.
1. Reemplace las contraseñas antiguas por una nueva contraseña de usuario y una nueva contraseña de propietario.
1. Guarde el PDF con la configuración de contraseñas actualizada.

```python
import aspose.pdf as ap

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

## Determinar la contraseña correcta de una lista

En algunos escenarios, es posible que necesite identificar la contraseña correcta de una lista de candidatos para acceder a un PDF protegido. El fragmento a continuación verifica si un archivo PDF está cifrado y luego intenta abrirlo iterando a través de una lista predefinida de contraseñas.

El proceso incluye:

1. Use `PdfFileInfo` para detectar si el PDF está cifrado.
1. Abra el PDF con cada contraseña usando `ap.Document()`.
1. Si tiene éxito, imprima el número de páginas.
1. Si no, captura la excepción e informa la contraseña fallida.

```python
import aspose.pdf as ap

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
