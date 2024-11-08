---
title: Convertir PDF a Documentos de Microsoft Word en Python
linktitle: Convertir PDF a Word 2003/2019
type: docs
weight: 10
url: /es/python-net/convert-pdf-to-word/
lastmod: "2022-12-23"
description: Aprende a escribir código Python para la conversión de formatos de PDF a Microsoft Word con Aspose.PDF para Python a través de .NET. y optimizar la conversión de PDF a DOC(DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Descripción General

Este artículo explica cómo **convertir PDF a Documentos de Microsoft Word usando Python**. Cubre estos temas.

_Formato_: **DOC**
- [Python PDF a DOC](#python-pdf-to-doc)
- [Python Convertir PDF a DOC](#python-pdf-to-doc)
- [Python Cómo convertir archivo PDF a DOC](#python-pdf-to-doc)

_Formato_: **DOCX**
- [Python PDF a DOCX](#python-pdf-to-docx)
- [Python Convertir PDF a DOCX](#python-pdf-to-docx)
- [Python Cómo convertir archivo PDF a DOCX](#python-pdf-to-docx)

_Formato_: **Word**
- [Python PDF a Word](#python-pdf-to-docx)
- [Python Convertir PDF a Word](#python-pdf-to-doc)

- [Python Cómo convertir archivo PDF a Word](#python-pdf-to-docx)

## Conversión de PDF a DOC y DOCX en Python

Una de las características más populares es la conversión de PDF a Microsoft Word DOC, lo que facilita la gestión de contenido. **Aspose.PDF para Python** te permite convertir archivos PDF no solo a DOC sino también al formato DOCX, de manera fácil y eficiente.

## Convertir PDF a archivo DOC (Word 97-2003)

Convierte archivos PDF al formato DOC con facilidad y control total. Aspose.PDF para Python es flexible y admite una amplia variedad de conversiones. La conversión de páginas de documentos PDF a imágenes, por ejemplo, es una característica muy popular.

Una conversión que muchos de nuestros clientes han solicitado es de PDF a DOC: convertir un archivo PDF a un documento de Microsoft Word. Los clientes desean esto porque los archivos PDF no se pueden editar fácilmente, mientras que los documentos Word sí. Algunas empresas quieren que sus usuarios puedan manipular texto, tablas e imágenes en archivos que comenzaron como PDFs.

Manteniendo viva la tradición de hacer las cosas simples y comprensibles, Aspose.PDF para Python te permite transformar un archivo PDF de origen en un archivo DOC con dos líneas de código.
 Para lograr esta característica, hemos introducido una enumeración llamada SaveFormat y su valor .Doc te permite guardar el archivo fuente en formato Microsoft Word.

El siguiente fragmento de código en Python muestra el proceso de convertir un archivo PDF en formato DOC.

<a name="csharp-pdf-to-doc"><strong>Pasos: Convertir PDF a DOC en Python</strong></a>

1. Crea una instancia del objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) con el documento PDF fuente.
2. Guárdalo en formato [SaveFormat](https://reference.aspose.com/pdf/python-net/aspose.pdf/saveformat/) llamando al método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_doc.doc"
    # Abre el documento PDF
    document = ap.Document(input_pdf)
    # Guarda el archivo en formato de documento MS Word
    document.save(output_pdf, ap.SaveFormat.DOC)
```

### Usando la Clase DocSaveOptions

La clase [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) proporciona numerosas propiedades que mejoran el proceso de convertir archivos PDF a formato DOC. Entre estas propiedades, el Modo te permite especificar el modo de reconocimiento para el contenido PDF. Puedes especificar cualquier valor de la enumeración RecognitionMode para esta propiedad. Cada uno de estos valores tiene beneficios y limitaciones específicas:

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_doc_with_options.doc"
    # Abrir documento PDF
    document = ap.Document(input_pdf)

    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC
    # Establecer el modo de reconocimiento como Flow
    save_options.mode = ap.DocSaveOptions.RecognitionMode.FLOW
    # Establecer la proximidad horizontal como 2.5
    save_options.relative_horizontal_proximity = 2.5
    # Activar el valor para reconocer viñetas durante el proceso de conversión
    save_options.recognize_bullets = True

    # Guardar el archivo en formato de documento MS Word
    document.save(output_pdf, save_options)
```

{{% alert color="success" %}}
**Intenta convertir PDF a DOC en línea**

Aspose.PDF para Python te presenta una aplicación en línea gratuita ["PDF a DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.
[![Convert PDF to DOC](/pdf/es/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Convertir PDF a DOCX

Aspose.PDF para Python API te permite leer y convertir documentos PDF a DOCX usando Python a través de .NET. DOCX es un formato bien conocido para documentos de Microsoft Word cuya estructura se cambió de binario simple a una combinación de archivos XML y binarios. Los archivos Docx se pueden abrir con Word 2007 y versiones posteriores, pero no con las versiones anteriores de MS Word que soportan extensiones de archivo DOC.

El siguiente fragmento de código de Python muestra el proceso de conversión de un archivo PDF al formato DOCX.

<a name="csharp-pdf-to-docx"><strong>Pasos: Convertir PDF a DOCX en Python</strong></a>

1. Crea una instancia del objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) con el documento PDF de origen.

2. Guárdelo en el formato [SaveFormat](https://reference.aspose.com/pdf/python-net/aspose.pdf/saveformat/) llamando al método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_docx_options.docx"
    # Abrir documento PDF
    document = ap.Document(input_pdf)

    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    # Establecer el modo de reconocimiento como Flujo
    save_options.mode = ap.DocSaveOptions.RecognitionMode.FLOW
    # Establecer la proximidad horizontal como 2.5
    save_options.relative_horizontal_proximity = 2.5
    # Habilitar el valor para reconocer viñetas durante el proceso de conversión
    save_options.recognize_bullets = True

    # Guardar el archivo en formato de documento de MS Word
    document.save(output_pdf, save_options)
```

La clase [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) tiene una propiedad llamada Format que ofrece la capacidad de especificar el formato del documento resultante, es decir, DOC o DOCX.
 Para convertir un archivo PDF a formato DOCX, por favor pase el valor Docx de la enumeración DocSaveOptions.DocFormat.

{{% alert color="warning" %}}
**Intenta convertir PDF a DOCX en línea**

Aspose.PDF para Python te presenta la aplicación gratuita en línea ["PDF a Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Aspose.PDF Conversión PDF a Word App Gratuita](/pdf/es/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Ver También 

Este artículo también cubre estos temas. Los códigos son los mismos que los anteriores.

_Formato_: **Word**
- [Código Python PDF a Word](#python-pdf-to-docx)
- [API Python PDF a Word](#python-pdf-to-docx)
- [Python PDF a Word Programáticamente](#python-pdf-to-docx)
- [Biblioteca Python PDF a Word](#python-pdf-to-docx)
- [Python Guardar PDF como Word](#python-pdf-to-docx)
- [Python Generar Word desde PDF](#python-pdf-to-docx)
- [Python Crear Word desde PDF](#python-pdf-to-docx)

- [Convertidor Python PDF a Word](#python-pdf-to-docx)
_Format_: **DOC**
- [Código Python para PDF a DOC](#python-pdf-to-doc)
- [API de Python PDF a DOC](#python-pdf-to-doc)
- [Python PDF a DOC Programáticamente](#python-pdf-to-doc)
- [Biblioteca de Python PDF a DOC](#python-pdf-to-doc)
- [Guardar PDF como DOC en Python](#python-pdf-to-doc)
- [Generar DOC desde PDF en Python](#python-pdf-to-doc)
- [Crear DOC desde PDF en Python](#python-pdf-to-doc)
- [Convertidor de Python PDF a DOC](#python-pdf-to-doc)

_Format_: **DOCX**
- [Código Python para PDF a DOCX](#python-pdf-to-docx)
- [API de Python PDF a DOCX](#python-pdf-to-docx)
- [Python PDF a DOCX Programáticamente](#python-pdf-to-docx)
- [Biblioteca de Python PDF a DOCX](#python-pdf-to-docx)
- [Guardar PDF como DOCX en Python](#python-pdf-to-docx)
- [Generar DOCX desde PDF en Python](#python-pdf-to-docx)
- [Crear DOCX desde PDF en Python](#python-pdf-to-docx)
- [Convertidor de Python PDF a DOCX](#python-pdf-to-docx)