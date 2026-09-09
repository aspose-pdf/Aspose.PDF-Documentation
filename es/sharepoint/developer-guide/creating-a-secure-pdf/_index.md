---
title: Crear un PDF seguro en SharePoint
linktitle: Crear un PDF seguro
type: docs
weight: 60
url: /es/sharepoint/creating-a-secure-pdf/
lastmod: "2026-09-09"
description: Usando la API PDF SharePoint, puedes producir PDFs seguros y cifrados y especificar sus contraseñas en SharePoint.
---

{{% alert color="primary" %}}

Aspose.PDF for SharePoint admite la creación de PDFs seguros. Instalar Aspose.PDF for SharePoint agrega una opción **PDF Secure Settings** en Site Setting. Aquí, puedes establecer la contraseña de usuario, la contraseña del propietario y cualquier valor de la lista de algoritmos para cifrar el PDF de salida. La lista de algoritmos proporciona diferentes combinaciones de algoritmos de cifrado y tamaños de clave. Proporciona el valor que elijas.

Este artículo demuestra cómo usar Aspose.PDF for SharePoint para generar un PDF cifrado.

{{% /alert %}}

## Crear un PDF seguro

Para demostrar la característica, primero configuramos la opción **PDF Secure Setting** para la contraseña de propietario y de usuario y el algoritmo de cifrado. El ejemplo luego combina dos documentos de una biblioteca de documentos.

### Configuración de opciones de PDF Secure Setting

Abra la opción **PDF Secure Settings** desde Configuración del sitio y establezca el algoritmo, la contraseña de propietario y la contraseña de usuario.

Especifique diferentes contraseñas de usuario y de propietario al cifrar el archivo PDF.

- La contraseña de usuario, si está establecida, es lo que necesita proporcionar para abrir un PDF. Acrobat Reader solicita al usuario que introduzca la contraseña de usuario. Si es incorrecta, el documento no se abre.
- La contraseña del propietario, si se establece, controla permisos como imprimir, editar, extraer, comentar, etc. Acrobat Reader impide estas funciones según la configuración de permisos. Acrobat requiere esta contraseña si deseas establecer/cambiar permisos.

![Configuración segura de PDF](creating-a-secure-pdf_1.png)

### Combinar documentos

Combina dos documentos usando la opción **Convert to PDF**. Esta función combina varios archivos que no son PDF (HTML, texto o imagen) en un archivo PDF.

1. Abre una biblioteca de documentos y selecciona los documentos deseados de la lista.

![Combinar documentos](creating-a-secure-pdf_2.png)

1. Utiliza la opción **Merge to PDF** de Library Tools para guardar el archivo de salida. Se te pedirá que guardes el archivo de salida en el disco.

![Combinar a PDF](creating-a-secure-pdf_3.png)

### Salida

El archivo de salida está cifrado.

![Salida](creating-a-secure-pdf_4.png)

