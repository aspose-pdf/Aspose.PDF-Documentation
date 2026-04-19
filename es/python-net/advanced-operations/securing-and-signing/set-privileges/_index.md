---
title: Cifrar y descifrar archivos PDF en Python
linktitle: Cifrar y descifrar archivo PDF
type: docs
weight: 70
url: /es/python-net/set-privileges-encrypt-and-decrypt-pdf-file/
description: Aprende cómo establecer privilegios PDF, cifrar archivos, descifrar PDFs protegidos y cambiar contraseñas en Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Establecer permisos PDF y gestionar el cifrado en Python
Abstract: Esta página de documentación explica cómo establecer privilegios del documento, aplicar cifrado y descifrar archivos PDF usando Aspose.PDF for Python. Guía a los desarrolladores a través de la configuración de contraseñas de usuario y propietario, definiendo restricciones de acceso (como imprimir, copiar o editar). Los ejemplos de código ilustran cómo proteger contenido sensible y gestionar la seguridad de PDF de manera eficaz dentro de aplicaciones Python, garantizando un acceso controlado y la confidencialidad de los datos.
---

La gestión de la seguridad de documentos es esencial al trabajar con contenido sensible o crítico para el negocio. Aspose.PDF for Python via .NET proporciona una API robusta para aplicar cifrado programáticamente, controlar el acceso mediante permisos y descifrar archivos PDF protegidos.

Este artículo guía a los desarrolladores de Python a través de ejemplos prácticos para establecer privilegios, aplicar y eliminar el cifrado, cambiar contraseñas y detectar estados de protección — todo dentro de un flujo de trabajo PDF.

Aspose.PDF for Python via .NET brinda a los desarrolladores control total sobre la seguridad de PDF:

**Set Privileges** - Control de acceso granulado mediante permisos.
**Encrypt File** - Aplicar cifrado AES o RC4 con contraseñas personalizadas.
**Decrypt File** - Eliminar la seguridad usando la contraseña del propietario.
**Change Passwords** - Rotar o actualizar credenciales sin alterar el contenido.
**Inspect Security** - Detectar el estado de cifrado o los tipos de contraseña requeridos.

Utilice esta página cuando necesite proteger documentos PDF con contraseñas, restringir la impresión o la copia, rotar credenciales o inspeccionar si un documento está cifrado.

## Establecer privilegios en un archivo PDF existente

Puede restringir o permitir operaciones específicas (p. ej., imprimir, copiar, rellenar formularios) asignando contraseñas de usuario y propietario junto con privilegios de acceso.

```python
import aspose.pdf as ap

path_infile = self.data_dir + infile
path_outfile = self.data_dir + outfile

# Open PDF document
with ap.Document(path_infile) as document:
    # Instantiate Document Privileges object
    # Apply restrictions on all privileges
    document_privilege = ap.facades.DocumentPrivilege.forbid_all
    # Only allow screen reading
    document_privilege.allow_screen_readers = True
    # Encrypt the file with User and Owner password
    # Need to set the password, so that once the user views the file with user password
    # Only screen reading option is enabled
    document.encrypt(
        "user", "owner", document_privilege, ap.CryptoAlgorithm.AE_SX128, False
    )
    # Save PDF document
    document.save(path_outfile)
```

## Cifrar archivo PDF usando diferentes tipos y algoritmos de encriptación

Cifrar un PDF garantiza que solo los usuarios con credenciales válidas puedan abrir o modificar el archivo.

>Términos clave:

- Contraseña de usuario. Necesaria para abrir el documento.
- Contraseña del propietario. Necesaria para cambiar permisos o eliminar el cifrado.
- Tamaño de clave. Use AE_SX128 para máxima seguridad en flujos de trabajo modernos.

El siguiente fragmento de código le muestra cómo cifrar archivos PDF.

```python
import aspose.pdf as ap

path_infile = self.data_dir + infile
path_outfile = self.data_dir + outfile

# Open PDF document
with ap.Document(path_infile) as document:
    # Encrypt PDF
    document.encrypt(
        "user", "owner", ap.Permissions.EXTRACT_CONTENT, ap.CryptoAlgorithm.AE_SX128
    )
    # Save PDF document
    document.save(path_outfile)
```

## Descifrar archivo PDF usando la contraseña del propietario

Para eliminar la protección con contraseña y restaurar el acceso completo:

1. Carga el PDF cifrado usando la contraseña correcta ('password' es la contraseña de usuario o del propietario).
1. Elimina toda la protección con contraseña y los ajustes de cifrado del documento.
1. Guarda el PDF ahora sin protección en el archivo de salida especificado.

```python
import aspose.pdf as ap

path_infile = self.data_dir + infile
path_outfile = self.data_dir + outfile

# Open PDF document with password
with ap.Document(path_infile, "password") as document:
    # Decrypt PDF
    document.decrypt()
    # Save PDF document
    document.save(path_outfile)
```

## Cambiar la contraseña de un archivo PDF

Actualizar las credenciales de seguridad (contraseñas de usuario y propietario) de un documento PDF mientras se preserva su contenido y estructura.

1. Abre el PDF utilizando la contraseña de propietario existente ('owner'), lo que otorga acceso total, incluida la autorización para cambiar la configuración de seguridad.
1. Reemplaza las contraseñas antiguas con una nueva contraseña de usuario ('newuser') y una nueva contraseña de propietario ('newowner').
1. Guarda el PDF con la configuración de contraseñas actualizada.

```python
import aspose.pdf as ap

path_infile = self.data_dir + infile
path_outfile = self.data_dir + outfile

# Open PDF document with password
with ap.Document(path_infile, "owner") as document:
    # Change password
    document.change_passwords("owner", "newuser", "newowner")
    # Save PDF document
    document.save(path_outfile)
```

## Cómo - determinar si el PDF de origen está protegido con contraseña

### Determinar la contraseña correcta del Array

En algunos escenarios, puede que necesite identificar la contraseña correcta de una lista de posibles candidatos para acceder a un PDF protegido. El fragmento de código a continuación demuestra cómo verificar si un archivo PDF está protegido con contraseña y luego intentar desbloquearlo iterando a través de una lista predefinida de contraseñas usando Aspose.PDF for Python via .NET.

El proceso incluye:

1. Usando PdfFileInfo para detectar si el PDF está cifrado.
1. Intenta abrir el PDF con cada contraseña usando ap.Document().
1. Si tiene éxito, imprime el número de páginas.
1. Si no, captura la excepción e informa la contraseña fallida.

```python
import aspose.pdf as ap

path_infile = self.data_dir + infile

with ap.facades.PdfFileInfo() as pdf_file_info:
    # Bind PDF document
    pdf_file_info.bind_pdf(path_infile)
    # Determine if the source PDF is encrypted
    print("File is password protected " + str(pdf_file_info.is_encrypted))

    passwords = ["test", "test1", "test2", "test3", "sample"]

    for password_index in range(len(passwords)):
        try:
            with ap.Document(path_infile, passwords[password_index]) as document:
                if len(document.pages) > 0:
                    print(
                        "Number of Pages in document are = " + str(len(document.pages))
                    )
                password_index = password_index + 1
        except Exception as e:
            print("Password = " + passwords[password_index] + " is not correct")
            password_index = password_index + 1
```

## Temas de seguridad relacionados

- [Asegurar y firmar archivos PDF en Python](/pdf/es/python-net/securing-and-signing/)
- [Firmar digitalmente archivos PDF en Python](/pdf/es/python-net/digitally-sign-pdf-file/)
- [Extraer información de la firma del PDF en Python](/pdf/es/python-net/extract-image-and-signature-information/)
- [Firmar documentos PDF desde una tarjeta inteligente en Python](/pdf/es/python-net/sign-pdf-document-from-smart-card/)

