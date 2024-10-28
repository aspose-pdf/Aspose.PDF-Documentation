---
title: Convertir archivo PDF a otros formatos 
linktitle: Convertir PDF a otros formatos 
type: docs
weight: 90
url: /java/convert-pdf-to-other-files/
lastmod: "2021-11-19"
description: Este tema muestra cómo Aspose.PDF permite convertir un archivo PDF a otros formatos de archivo.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convertir PDF a EPUB

{{% alert color="success" %}}
**Intenta convertir PDF a EPUB en línea**

Aspose.PDF para Java te presenta una aplicación gratuita en línea ["PDF a EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), donde puedes investigar la funcionalidad y la calidad con la que trabaja.

[![Conversión de PDF a EPUB de Aspose.PDF con Aplicación Gratuita](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Electronic Publication">EPUB</abbr>** (abreviatura de publicación electrónica) es un estándar de libro electrónico libre y abierto del Foro Internacional de Publicaciones Digitales (IDPF).
 Los archivos tienen la extensión .epub. EPUB está diseñado para contenido adaptable, lo que significa que un lector de EPUB puede optimizar el texto para un dispositivo de visualización en particular. EPUB también admite contenido de diseño fijo. El formato está diseñado como un único formato que los editores y las casas de conversión pueden usar internamente, así como para distribución y venta. Sustituye al estándar Open eBook.

Aspose.PDF para Java admite la función de convertir documentos PDF al formato EPUB. Aspose.PDF para Java tiene una clase llamada [EpubSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubSaveOptions) que se puede usar como segundo argumento en el método [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..), para generar un archivo EPUB. Intente usar el siguiente fragmento de código para cumplir con este requisito.

```java
// Cargar documento PDF
Document document = new Document(DATA_DIR + "PDFToEPUB.pdf");
// Instanciar opciones de guardado Epub
EpubSaveOptions options = new EpubSaveOptions();
// Especificar el diseño para los contenidos
options.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.Flow);
// Guardar el documento ePUB
document.save(DATA_DIR + "PDFToEPUB_out.epub", options);
document.close();
```

## Convertir PDF a LaTeX/TeX

**Aspose.PDF para Java** admite la conversión de PDF a LaTeX/TeX. El formato de archivo LaTeX es un formato de archivo de texto con el marcado especial y se utiliza en el sistema de preparación de documentos basado en TeX para la composición tipográfica de alta calidad.

Para convertir archivos PDF a TeX, Aspose.PDF tiene la clase [TeXSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TeXSaveOptions) que proporciona el método `setOutDirectoryPath` para guardar imágenes temporales durante el proceso de conversión.

El siguiente fragmento de código muestra el proceso de conversión de archivos PDF al formato TEX con Java.

```java
String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToTeX.pdf").toString();
String texDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToTeX_out.tex").toString();

// Crear objeto Document
Document document = new Document(documentFileName);

// Instanciar opción de guardado LaTex
TeXSaveOptions saveOptions = new TeXSaveOptions();

// Especificar el directorio de salida
String pathToOutputDirectory = DATA_DIR.toString();

// Establecer la ruta del directorio de salida para el objeto de opción de guardado
saveOptions.setOutDirectoryPath(pathToOutputDirectory);

// Guardar archivo PDF en formato LaTex
document.save(texDocumentFileName, saveOptions);
document.close();
```


{{% alert color="success" %}}
**Intenta convertir PDF a LaTeX/TeX en línea**

Aspose.PDF para Java te presenta la aplicación gratuita en línea ["PDF a LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Conversión de Aspose.PDF PDF a LaTeX/TeX con aplicación gratuita](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Convertir PDF a Texto

**Aspose.PDF para Java** soporta convertir un documento PDF completo y una sola página a un archivo de texto.

### Convertir un documento PDF completo a un archivo de texto

Puedes convertir un documento PDF a un archivo TXT utilizando el método Visit de la clase [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber).

El siguiente fragmento de código explica cómo extraer los textos de todas las páginas.

```java
// Abrir documento
String pdfFileName = Paths.get(DATA_DIR.toString(), "demo.pdf").toString();
String txtFileName = Paths.get(DATA_DIR.toString(), "PDFToTXT_out.txt").toString();

// Cargar documento PDF
Document document = new Document(pdfFileName);
TextAbsorber ta = new TextAbsorber();
ta.visit(document);
// Guardar el texto extraído en un archivo de texto
BufferedWriter writer = new BufferedWriter(new FileWriter(txtFileName));
writer.write(ta.getText());
writer.close();
```


{{% alert color="success" %}}
**Intente convertir Convertir PDF a Texto en línea**

Aspose.PDF para Java le presenta la aplicación gratuita en línea ["PDF a Texto"](https://products.aspose.app/pdf/conversion/pdf-to-txt), donde puede intentar investigar la funcionalidad y la calidad con la que trabaja.

[![Aspose.PDF Conversión PDF a Texto con Aplicación Gratuita](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

### Convertir página PDF a archivo de texto

Puede convertir un documento PDF a un archivo TXT con Aspose.PDF para Java. Debe usar el método Visit de la clase [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) para resolver esta tarea.

El siguiente fragmento de código explica cómo extraer los textos de las páginas particulares.

```java
String pdfFileName = Paths.get(DATA_DIR.toString(), "demo.pdf").toString();
String txtFileName = Paths.get(DATA_DIR.toString(), "PDFToTXT_out.txt").toString();

// Cargar documento PDF
Document document = new Document(pdfFileName);

TextAbsorber ta = new TextAbsorber();
int[] pages = new int[] { 1, 3, 4 };

for (int page : pages) {
    ta.visit(document.getPages().get_Item(page));
}

// Guardar el texto extraído en un archivo de texto
BufferedWriter writer = new BufferedWriter(new FileWriter(txtFileName));
writer.write(ta.getText());
writer.close();
document.close();
```


## Convertir PDF a XPS

**Aspose.PDF para Java** ofrece la posibilidad de convertir archivos PDF al formato <abbr title="Especificación de Papel XML">XPS</abbr>. Intentemos usar el fragmento de código presentado para convertir archivos PDF al formato XPS con Java.

{{% alert color="success" %}}
**Intenta convertir PDF a XPS en línea**

Aspose.PDF para Java te presenta la aplicación gratuita en línea ["PDF a XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), donde puedes investigar la funcionalidad y la calidad de su funcionamiento.

[![Conversión de Aspose.PDF de PDF a XPS con aplicación gratuita](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

El tipo de archivo XPS está principalmente asociado con la Especificación de Papel XML de Microsoft Corporation. La Especificación de Papel XML (XPS), anteriormente con nombre en clave Metro y que subsume el concepto de marketing Next Generation Print Path (NGPP), es la iniciativa de Microsoft para integrar la creación y visualización de documentos en el sistema operativo Windows.

Para convertir archivos PDF a XPS, Aspose.PDF tiene la clase [XpsSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsSaveOptions) que se utiliza como el segundo argumento en el constructor Document.save(..) para generar el archivo XPS.
 El siguiente fragmento de código muestra el proceso de conversión de archivos PDF al formato XPS.

```java
String documentFileName = Paths.get(DATA_DIR.toString(), "sample.pdf").toString();
String xpsDocumentFileName = Paths.get(DATA_DIR.toString(), "sample-res-xps.xps").toString();

// Crear objeto Document
Document document = new Document(documentFileName);

// Instanciar opciones de guardado XPS
XpsSaveOptions saveOptions = new XpsSaveOptions();

// Guardar salida en formato XML
document.save(xpsDocumentFileName, saveOptions);
document.close();
```