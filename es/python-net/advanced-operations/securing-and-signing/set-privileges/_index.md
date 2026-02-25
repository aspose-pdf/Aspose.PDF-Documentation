---
title: Establecer privilegios, encriptar y desencriptar PDF
linktitle: Encriptar y desencriptar archivo PDF
type: docs
weight: 70
url: /es/python-net/set-privileges-encrypt-and-decrypt-pdf-file/
description: Encripta un archivo PDF con Python usando diferentes tipos y algoritmos de encriptación. También, desencripta archivos PDF usando la contraseña del propietario.
lastmod: "2025-06-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Encripta o desencripta un archivo PDF con Python
Abstract: Esta página de documentación explica cómo establecer privilegios de documento, aplicar encriptación y desencriptar archivos PDF usando Aspose.PDF para Python. Guía a los desarrolladores a través de la configuración de contraseñas de usuario y propietario, definiendo restricciones de acceso (como imprimir, copiar o editar). Los ejemplos de código ilustran cómo proteger contenido sensible y gestionar la seguridad de PDF de manera efectiva dentro de aplicaciones Python, garantizando acceso controlado y confidencialidad de los datos.
---

Gestionar la seguridad de documentos es esencial al trabajar con contenido sensible o crítico para el negocio. Aspose.PDF para Python a través de .NET ofrece una API robusta para aplicar encriptación de forma programática, controlar el acceso mediante permisos y desencriptar archivos PDF protegidos.

Este artículo guía a los desarrolladores Python a través de ejemplos prácticos para establecer privilegios, aplicar y eliminar encriptación, cambiar contraseñas y detectar estados de protección, todo dentro de un flujo de trabajo con PDF.

Aspose.PDF para Python a través de .NET brinda a los desarrolladores control total sobre la seguridad de PDF:

**Establecer privilegios** - Control de acceso granular mediante permisos.
**Encriptar archivo** - Aplicar encriptación AES o RC4 con contraseñas personalizadas.
**Desencriptar archivo** - Eliminar la seguridad usando la contraseña del propietario.
**Cambiar contraseñas** - Rotar o actualizar credenciales sin alterar el contenido.
**Inspeccionar seguridad** - Detectar el estado de encriptación o los tipos de contraseñas requeridos.

## Establecer privilegios en un archivo PDF existente

Puedes restringir o permitir operaciones específicas (p. ej., impresión, copia, rellenado de formularios) asignando contraseñas de usuario y propietario junto con privilegios de acceso.

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
        document.encrypt("user", "owner", document_privilege, ap.CryptoAlgorithm.AE_SX128, False)
        # Save PDF document
        document.save(path_outfile)
```

## Encriptar archivo PDF usando diferentes tipos y algoritmos de encriptación

Encriptar un PDF asegura que solo los usuarios con credenciales válidas puedan abrir o modificar el archivo.

>Términos clave:

- Contraseña de usuario. Necesaria para abrir el documento.

- Contraseña del propietario. Necesaria para cambiar permisos o eliminar la encriptación.

- Tamaño de clave. Use AE_SX128 para máxima seguridad en flujos de trabajo modernos.

El siguiente fragmento de código muestra cómo encriptar archivos PDF.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Encrypt PDF
        document.encrypt("user", "owner", ap.Permissions.EXTRACT_CONTENT, ap.CryptoAlgorithm.AE_SX128)
        # Save PDF document
        document.save(path_outfile)
```

## Desencriptar archivo PDF usando la contraseña del propietario

Para eliminar la protección por contraseña y restaurar el acceso completo:

1. Carga el PDF encriptado usando la contraseña correcta ('password' es la contraseña de usuario o propietario).
1. Elimina toda la protección por contraseña y la configuración de encriptación del documento.
1. Guarda el PDF ahora desprotegido al archivo de salida especificado.

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

Para actualizar las credenciales de seguridad (contraseñas de usuario y propietario) de un documento PDF mientras se preserva su contenido y estructura.

1. Abre el PDF usando la contraseña de propietario existente ('owner'), lo que brinda acceso total incluyendo permiso para cambiar la configuración de seguridad.
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

## Cómo determinar si el PDF origen está protegido por contraseña

### Determinar la contraseña correcta a partir de una matriz

En algunos escenarios, puede que necesites identificar la contraseña correcta a partir de una lista de candidatos potenciales para acceder a un PDF protegido. El fragmento de código a continuación demuestra cómo verificar si un archivo PDF está protegido por contraseña y luego intentar desbloquearlo iterando a través de una lista predefinida de contraseñas usando Aspose.PDF para Python a través de .NET.

El proceso incluye:

1. Usar PdfFileInfo para detectar si el PDF está encriptado.
1. Intenta abrir el PDF con cada contraseña usando ap.Document().
1. Si tiene éxito, imprime el número de páginas.
1. Si no, captura la excepción y reporta la contraseña fallida.

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
                        print("Number of Pages in document are = " + str(len(document.pages)))
                    password_index = password_index + 1
            except Exception as e:
                print("Password = " + passwords[password_index] + " is not correct")
                password_index = password_index + 1
```


