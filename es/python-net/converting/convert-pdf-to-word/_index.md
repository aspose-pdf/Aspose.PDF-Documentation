---
title: Convertir PDF a documentos Microsoft Word en Python
linktitle: Convertir PDF a Word
type: docs
weight: 10
url: /python-net/convert-pdf-to-word/
lastmod: "2025-09-27"
description: Aprenda cómo convertir documentos PDF al formato Word en Python usando Aspose.PDF para una edición de documentos sencilla.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Cómo convertir PDF a Word en Python
Abstract: Este artículo proporciona una guía completa sobre cómo convertir archivos PDF a formatos de Microsoft Word (DOC y DOCX) usando Python, específicamente utilizando la biblioteca Aspose.PDF. Describe las ventajas de convertir PDFs a documentos Word editables, lo que permite una manipulación de contenido más fácil, como texto, tablas e imágenes. El artículo detalla el proceso de conversión de PDF a DOC (formato Word 97-2003) y DOCX, con fragmentos de código que demuestran estas conversiones mediante Python. El proceso implica crear un `Document` objeto a partir del PDF y guardarlo en el formato deseado usando el método `save()` y la enumeración `SaveFormat`. Además, introduce la clase `DocSaveOptions`, que permite una mayor personalización del proceso de conversión, como especificar modos de reconocimiento. El artículo también destaca aplicaciones en línea proporcionadas por Aspose.PDF para probar la calidad y funcionalidad de la conversión. El contenido incluye una visión estructurada y enlaces a las secciones correspondientes para cada formato.
---

## Convertir PDF a DOC

Una de las funciones más populares es la conversión de PDF a Microsoft Word DOC, lo que facilita la gestión de contenido. **Aspose.PDF for Python via .NET** le permite convertir archivos PDF no solo a DOC sino también a formato DOCX, de manera fácil y eficiente.

El [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) la clase proporciona numerosas propiedades que mejoran el proceso de conversión de archivos PDF a formato DOC. Entre estas propiedades, Mode le permite especificar el modo de reconocimiento para el contenido PDF. Puede especificar cualquier valor de la enumeración RecognitionMode para esta propiedad. Cada uno de estos valores tiene beneficios y limitaciones específicos:

Pasos: Convertir PDF a DOC en Python

1. Cargue el PDF en un objeto 'ap.Document'.
1. Crea una instancia de 'DocSaveOptions'.
1. Establece la propiedad format a 'DocFormat.DOC' para asegurar que la salida esté en formato .doc (formato Word antiguo).
1. Guarda el PDF como un documento Word usando las opciones de guardado especificadas.
1. Imprime un mensaje de confirmación.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.DocSaveOptions()
    save_options.format = apdf.DocSaveOptions.DocFormat.DOC
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Intenta convertir PDF a DOC en línea**

Aspose.PDF for Python te presenta una aplicación gratuita en línea ["PDF a DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Convertir PDF a DOC](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Convertir PDF a DOCX

Aspose.PDF for Python API le permite leer y convertir documentos PDF a DOCX usando Python a través de .NET. DOCX es un formato bien conocido para documentos de Microsoft Word cuya estructura se cambió de binario simple a una combinación de archivos XML y binarios. Los archivos DOCX pueden abrirse con Word 2007 y versiones posteriores, pero no con las versiones anteriores de MS Word que admiten extensiones de archivo DOC.

El siguiente fragmento de código Python muestra el proceso de conversión de un archivo PDF al formato DOCX.

Pasos: Convertir PDF a DOCX en Python

1. Cargue el PDF de origen usando 'ap.Document'.
1. Cree una instancia de 'DocSaveOptions'.
1. Establezca la propiedad format a 'DocFormat.DOC_X' para generar un archivo .docx (formato Word moderno).
1. Guarde el PDF como un archivo DOCX con las opciones de guardado configuradas.
1. Imprima un mensaje de confirmación después de la conversión.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.DocSaveOptions()
    save_options.format = apdf.DocSaveOptions.DocFormat.DOC_X
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

El [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) class tiene una propiedad llamada Format que brinda la capacidad de especificar el formato del documento resultante, es decir, DOC o DOCX. Para convertir un archivo PDF a formato DOCX, pase el valor Docx de la enumeración DocSaveOptions.DocFormat.

{{% alert color="warning" %}}
**Intenta convertir PDF a DOCX en línea**

Aspose.PDF for Python te presenta una aplicación gratuita en línea ["PDF a Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aplicación gratuita Aspose.PDF Conversión PDF a Word](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}
