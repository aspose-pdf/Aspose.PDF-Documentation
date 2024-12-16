---
title: Convertir documentos PDF a documentos de Microsoft Word en .NET
linktitle: Convertir PDF a Word
type: docs
weight: 10
url: /es/net/convert-pdf-to-word/
lastmod: "2022-08-04"
description: Aprenda cómo escribir código en C# para la conversión de formatos PDF a Microsoft Word con Aspose.PDF para .NET. y ajuste la conversión de PDF a DOC(DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Visión general

Este artículo explica cómo **convertir documentos PDF a documentos de Microsoft Word usando C#**. Cubre estos temas.

_Formato_: **DOC**

- [C# PDF a DOC](#csharp-pdf-to-doc)
- [C# Convertir PDF a DOC](#csharp-pdf-to-doc)
- [C# Cómo convertir un archivo PDF a DOC](#csharp-pdf-to-doc)

_Formato_: **DOCX**

- [C# PDF a DOCX](#csharp-pdf-to-docx)
- [C# Convertir PDF a DOCX](#csharp-pdf-to-docx)
- [C# Cómo convertir un archivo PDF a DOCX](#csharp-pdf-to-docx)

_Formato_: **Word**

- [C# PDF a Word](#csharp-pdf-to-docx)
- [C# Convertir PDF a Word](#csharp-pdf-to-doc)
- [C# Cómo convertir un archivo PDF a Word](#csharp-pdf-to-docx)

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).
El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

## Conversión de PDF a DOC y DOCX

Una de las características más populares es la conversión de PDF a Microsoft Word DOC, lo que hace que la gestión de contenido sea más sencilla. **Aspose.PDF para .NET** te permite convertir archivos PDF a formato DOC y DOCX de manera rápida y eficiente.

## Convertir PDF a archivo DOC (Microsoft Word 97-2003)

Convierte archivos PDF a formato DOC con facilidad y control total. Aspose.PDF para .NET es flexible y soporta una amplia variedad de conversiones. Convertir páginas de documentos PDF a imágenes, por ejemplo, es una característica muy popular.

Muchos de nuestros clientes han solicitado una conversión de PDF a DOC: convertir un archivo PDF a un documento de Microsoft Word. Los clientes desean esto porque los archivos PDF no se pueden editar fácilmente, mientras que los documentos Word sí. Algunas empresas quieren que sus usuarios puedan manipular texto, tablas e imágenes en archivos que comenzaron como PDFs.

Manteniendo viva la tradición de hacer las cosas simples y comprensibles, Aspose.PDF para .NET te permite transformar un archivo PDF fuente en un archivo DOC con solo dos líneas de código.
Manteniendo viva la tradición de hacer las cosas simples y comprensibles, Aspose.PDF para .NET te permite transformar un archivo PDF fuente en un archivo DOC con dos líneas de código.

El siguiente fragmento de código C# muestra cómo convertir un archivo PDF en formato DOC.

<a name="csharp-pdf-to-doc"><strong>Pasos: Convertir PDF a DOC en C#</strong></a>

1. Crea una instancia del objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) con el documento PDF fuente.
2. Guárdalo en formato **SaveFormat.Doc** llamando al método **Document.Save()**.

```csharp
public static void ConvertPDFtoWord()
{
    // Abre el documento PDF fuente
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");
    // Guarda el archivo en formato de documento de MS
    pdfDocument.Save(_dataDir + "PDFToDOC_out.doc", SaveFormat.Doc);

}
```

### Usando la clase DocSaveOptions

La clase [`DocSaveOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) proporciona numerosas propiedades que mejoran la conversión de archivos PDF a formato DOC.
La clase [`DocSaveOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) proporciona numerosas propiedades que mejoran la conversión de archivos PDF a formato DOC.

- El modo [`Textbox`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) es rápido y bueno para preservar la apariencia original del archivo PDF, pero la capacidad de edición del documento resultante podría ser limitada. Cada bloque de texto visualmente agrupado en el PDF original se convierte en un cuadro de texto en el documento de salida. Esto logra una máxima similitud con el original, por lo que el documento de salida se ve bien, pero consiste enteramente en cuadros de texto, lo que podría ser editado en Microsoft Word, lo cual es bastante desafiante.
- El modo [`Flow`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) es un modo de reconocimiento completo, donde el motor realiza agrupaciones y análisis multinivel para restaurar el documento original según la intención del autor mientras produce un documento fácilmente editable.
- [`Flow`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) es el modo de reconocimiento completo, donde el motor realiza agrupamientos y análisis de múltiples niveles para restaurar el documento original según la intención del autor mientras produce un documento fácilmente editable.

La propiedad [`RelativeHorizontalProximity`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/properties/relativehorizontalproximity) se puede utilizar para controlar la proximidad relativa entre elementos textuales. Esto significa que la distancia está normalizada por el tamaño de la fuente. Las fuentes más grandes pueden tener espacios más grandes entre sílabas y aún considerarse un todo único. Se especifica como un porcentaje del tamaño de la fuente; por ejemplo, 1 = 100%. Esto significa que dos caracteres de 12pt colocados a 12 pt de distancia están próximos.
- [`RecognitionBullets`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/properties/recognizebullets) se utiliza para activar el reconocimiento de viñetas durante la conversión.

```csharp
public static void ConvertPDFtoWordDocAdvanced()
{
    var pdfFile = Path.Combine(_dataDir, "PDF-to-DOC.pdf");
    var docFile = Path.Combine(_dataDir, "PDF-to-DOC.doc");
    Document pdfDocument = new Document(pdfFile);
    DocSaveOptions saveOptions = new DocSaveOptions
    {
        Format = DocSaveOptions.DocFormat.Doc,
        // Establecer el modo de reconocimiento como Flow
        Mode = DocSaveOptions.RecognitionMode.Flow,
        // Establecer la proximidad horizontal como 2.5
        RelativeHorizontalProximity = 2.5f,
        // Habilitar el valor para reconocer viñetas durante el proceso de conversión
        RecognizeBullets = true
    };
    pdfDocument.Save(docFile, saveOptions);
}
```
{{% alert color="success" %}}
**Intenta convertir PDF a DOC en línea**

Aspose.PDF para .NET te presenta una aplicación gratuita en línea ["PDF a DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), donde puedes explorar la funcionalidad y la calidad con la que trabaja.

[![Convertir PDF a DOC](/pdf/es/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Convertir PDF a DOCX (archivo Microsoft Word 2007-2021)

Aspose.PDF para .NET API te permite leer y convertir documentos PDF a DOCX usando C# y cualquier lenguaje .NET. DOCX es un formato bien conocido para documentos de Microsoft Word cuya estructura cambió de binario plano a una combinación de archivos XML y binarios. Los archivos Docx se pueden abrir con Word 2007 y versiones posteriores, pero no con versiones anteriores de MS Word, que admiten extensiones de archivo DOC.

El siguiente fragmento de código C# muestra cómo convertir un archivo PDF en formato DOCX.

<a name="csharp-pdf-to-docx"><strong>Pasos: Convertir PDF a DOCX en C#</strong></a>

1.
1.
2. Guárdalo en formato **SaveFormat.DocX** llamando al método **Document.Save()**.

```csharp
public static void ConvertPDFtoWord_DOCX_Format()
{
    // Abrir el documento PDF fuente
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");
    // Guardar el archivo DOC resultante
    pdfDocument.Save(_dataDir + "saveOptionsOutput_out.doc", SaveFormat.DocX);
}
```

### Convertir PDF a DOCX en Modo Mejorado

Para obtener mejores resultados de la conversión de PDF a DOCX, puedes usar el modo `EnhancedFlow`.
La principal diferencia entre Flow y Enhanced Flow es que las tablas (tanto con bordes como sin ellos) se reconocen como tablas reales, no como texto con una imagen de fondo.
También se incluye el reconocimiento de listas numeradas y muchas otras cosas menores.

```csharp
public static void ConvertPDFtoWord_Advanced_DOCX_Format()
{    
    // Abrir el documento PDF fuente
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");

    // Instanciar el objeto DocSaveOptions
    DocSaveOptions saveOptions = new DocSaveOptions
    {
        // Especificar el formato de salida como DOCX
        Format = DocSaveOptions.DocFormat.DocX
        // Establecer otros parámetros de DocSaveOptions
        Mode = DocSaveOptions.RecognitionMode.EnhancedFlow
    };
    // Guardar el documento en formato docx
    pdfDocument.Save("ConvertToDOCX_out.docx", saveOptions);
}
```
{{% alert color="warning" %}}
**Intenta convertir PDF a DOCX en línea**

Aspose.PDF para .NET te presenta la aplicación gratuita en línea ["PDF a Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), donde puedes probar a investigar la funcionalidad y calidad con la que trabaja.

[![Aspose.PDF Conversión PDF a Word Aplicación Gratuita](/pdf/es/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Ver También

Este artículo también cubre estos temas. Los códigos son los mismos que arriba.

_Format_: **Word**

- [Código C# PDF a Word](#csharp-pdf-to-docx)
- [API C# PDF a Word](#csharp-pdf-to-docx)
- [C# PDF a Word Programáticamente](#csharp-pdf-to-docx)
- [Biblioteca C# PDF a Word](#csharp-pdf-to-docx)
- [C# Guardar PDF como Word](#csharp-pdf-to-docx)
- [C# Generar Word desde PDF](#csharp-pdf-to-docx)
- [C# Crear Word desde PDF](#csharp-pdf-to-docx)
- [Convertidor C# PDF a Word](#csharp-pdf-to-docx)

_Format_: **DOC**

- [Código C# PDF a DOC](#csharp-pdf-to-doc)
- [API C# PDF a DOC](#csharp-pdf-to-doc)
- [API de C# PDF a DOC](#csharp-pdf-to-doc)
- [C# PDF a DOC Programáticamente](#csharp-pdf-to-doc)
- [Biblioteca C# PDF a DOC](#csharp-pdf-to-doc)
- [C# Guardar PDF como DOC](#csharp-pdf-to-doc)
- [C# Generar DOC desde PDF](#csharp-pdf-to-doc)
- [C# Crear DOC desde PDF](#csharp-pdf-to-doc)
- [Convertidor C# PDF a DOC](#csharp-pdf-to-doc)

_Formato_: **DOCX**

- [Código C# PDF a DOCX](#csharp-pdf-to-docx)
- [API de C# PDF a DOCX](#csharp-pdf-to-docx)
- [C# PDF a DOCX Programáticamente](#csharp-pdf-to-docx)
- [Biblioteca C# PDF a DOCX](#csharp-pdf-to-docx)
- [C# Guardar PDF como DOCX](#csharp-pdf-to-docx)
- [C# Generar DOCX desde PDF](#csharp-pdf-to-docx)
- [C# Crear DOCX desde PDF](#csharp-pdf-to-docx)
- [Convertidor C# PDF a DOCX](#csharp-pdf-to-docx)
