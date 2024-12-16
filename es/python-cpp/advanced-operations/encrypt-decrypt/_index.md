---
title: Encrypt and Decrypt PDF
linktitle: Encrypt and Decrypt PDF File
type: docs
weight: 30
url: /es/python-cpp/set-privileges-encrypt-and-decrypt-pdf-file/
description: Encriptar y Desencriptar Archivo PDF con Python a través de una aplicación C++.
lastmod: "2024-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Encriptar Archivo PDF usando Diferentes Tipos de Encriptación y Algoritmos

Una forma efectiva de proteger archivos PDF es mediante encriptación. En este artículo, exploraremos cómo encriptar documentos PDF usando Python con la ayuda de la biblioteca Aspose.PDF.

La encriptación de PDF implica cifrar el contenido de un documento PDF usando algoritmos criptográficos para prevenir el acceso no autorizado. Los archivos PDF encriptados requieren una contraseña para abrirse y pueden tener restricciones en acciones como imprimir, copiar y editar.

- La **contraseña de usuario**, si se establece, es la que necesitas proporcionar para abrir un PDF. Acrobat/Reader solicitará al usuario que ingrese la contraseña de usuario. Si no es correcta, el documento no se abrirá.
- La **contraseña de propietario**, si se establece, controla permisos, como imprimir, editar, extraer, comentar, etc.
 Acrobat/Reader deshabilitará estas cosas basándose en la configuración de permisos. Acrobat requerirá esta contraseña si deseas establecer/cambiar permisos.

El siguiente fragmento de código te muestra cómo encriptar archivos PDF.

1. Crear la ruta de archivo de entrada y salida
1. Cargar el documento PDF usando AsposePDFPythonWrappers
1. Definir los permisos para el documento encriptado
1. Definir el algoritmo de encriptación que se utilizará
1. Encriptar el documento con las contraseñas de usuario y propietario, permisos y algoritmo de encriptación especificados usando el método 'document.encrypt'
1. Guardar el documento encriptado en el archivo de salida especificado con el método 'document.save'.

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # Establecer la ruta del directorio para los archivos de muestra
    dataDir = os.path.join(os.getcwd(), "samples")

    # Establecer la ruta del archivo de entrada
    input_file = os.path.join(dataDir, "sample.pdf")

    # Establecer la ruta del archivo de salida
    output_file = os.path.join(dataDir, "results", "sample-enc.pdf")

    # Cargar el documento PDF usando AsposePDFPythonWrappers
    document = apw.Document(inputFile)

    # Definir los permisos para el documento encriptado
    permission = apCore.Permissions(apCore.Permissions.ExtractContent | apCore.ModifyContent)

    # Definir el algoritmo de encriptación que se utilizará
    cryptoAlgorithm = apCore.CryptoAlgorithm.RC4x128

    # Encriptar el documento con las contraseñas de usuario y propietario, permisos y algoritmo de encriptación especificados
    document.encrypt("user", "owner", permission, cryptoAlgorithm)

    # Guardar el documento encriptado en el archivo de salida especificado
    document.save(output_file)
```

## Desencriptar archivo PDF usando contraseña de propietario

1. Crear la ruta del archivo de entrada y salida
1. Crear una nueva instancia de la clase Document del módulo AsposePDFPythonWrappers
1. Desencriptar el documento usando el método [document_decrypt](https://reference.aspose.com/pdf/python-cpp/core/document_decrypt/)
1. Guardar el documento desencriptado en la ruta del archivo de salida usando el método save() con la función [document_save](https://reference.aspose.com/pdf/python-cpp/core/document_save/).

```Python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # Establecer la ruta del directorio para los archivos de muestra
    dataDir = os.path.join(os.getcwd(), "samples")

    # Establecer la ruta del archivo de entrada
    input_file = os.path.join(dataDir, "sample_enc.pdf")

    # Establecer la ruta del archivo de salida
    output_file = os.path.join(dataDir, "results", "sample-dec.pdf")

    # Crear una nueva instancia de la clase Document del módulo AsposePDFPythonWrappers
    document = apw.Document(input_file, "owner")

    # Desencriptar el documento usando el método decrypt()
    document.decrypt()

    # Guardar el documento desencriptado en la ruta del archivo de salida usando el método save()
    document.save(output_file)
```