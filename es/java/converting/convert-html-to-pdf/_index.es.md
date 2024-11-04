---
title: Convertir archivo HTML a PDF en Java
linktitle: Convertir archivo HTML a PDF
type: docs
weight: 40
url: /java/convert-html-to-pdf/
lastmod: "2021-11-19"
description: Este tema muestra cómo Aspose.PDF permite convertir formatos HTML y MHTML a archivo PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Descripción general

Este artículo explica cómo convertir HTML a PDF usando Java. El código es muy simple, solo carga HTML en la clase Document y guárdalo como PDF de salida. Convertir MHTML a PDF en Java es también similar. Cubre los siguientes temas

- [Java HTML a PDF](#convert-html-to-pdf)
- [Java MHTML a PDF](#convert-mhtml-to-pdf)
- [Java Convertir HTML a PDF](#convert-html-to-pdf)
- [Java Convertir MHTML a PDF](#convert-mhtml-to-pdf)
- [Java PDF desde HTML](#convert-html-to-pdf)
- [Java PDF desde MHTML](#convert-mhtml-to-pdf)
- [Java Convertidor HTML a PDF - Cómo Convertir Página Web a PDF](#convert-html-to-pdf)

- [Java Biblioteca HTML a PDF, API o Código para Renderizar, Guardar, Generar o Crear PDF Programáticamente desde HTML](#convert-html-to-pdf)

## Biblioteca de Conversión de HTML a PDF en Java

**Aspose.PDF para Java** es una API de manipulación de PDF que te permite convertir cualquier documento HTML existente a PDF sin problemas. El proceso de convertir HTML a PDF se puede personalizar de manera flexible.

## Convertir HTML a PDF

El siguiente ejemplo de código Java muestra cómo convertir un documento HTML a un PDF.

1. Crea una instancia de la clase [HtmlLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions).
1. Inicializa el objeto [Document](https://reference.aspose.com/page/java/com.aspose.page/document).
1. Guarda el documento PDF de salida llamando al método **Document.save(String)**.

```java
// Abre el documento PDF de origen
Document document = new Document(DATA_DIR + "PDFToHTML.pdf")

// Instanciar objeto de opciones de guardado HTML
HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();

// Guarda el documento
document.save(DATA_DIR + "MultiPageHTML_out.html", htmlsaveOptions);
```

{{% alert color="success" %}}
**Intenta convertir HTML a PDF en línea**

Aspose te presenta la aplicación en línea gratuita ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Conversión de Aspose.PDF de HTML a PDF usando la aplicación gratuita](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## Conversión avanzada de HTML a PDF

El motor de conversión HTML tiene varias opciones que nos permiten controlar el proceso de conversión.

### Soporte para Media Queries

1. Crear un [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) de HTML.
1. Establecer modo de impresión o pantalla.
1. Inicializar el [objeto Document](<https://reference.aspose.com/page/java/com.aspose.page/document>).
1. Guardar el documento PDF de salida.

Las consultas de medios son una técnica popular para entregar una hoja de estilo adaptada a diferentes dispositivos. Podemos establecer el tipo de dispositivo usando la propiedad [HtmlMediaType](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlMediaType).

```java
// Crear un LoadOptions de HTML
HtmlLoadOptions options = new HtmlLoadOptions();

// Establecer modo de impresión o pantalla
options.setHtmlMediaType(HtmlMediaType.Print);

// Inicializar objeto documento
String htmlFileName = Paths.get(DATA_DIR.toString(), "test.html").toString();
Document document = new Document(htmlFileName, options);

// Guardar el documento PDF de salida
document.save(Paths.get(DATA_DIR.toString(), "HTMLtoPDF.pdf").toString());
document.close();
```


### Habilitar (deshabilitar) la incrustación de fuentes

1. Agregar nuevas [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) Html.
1. Habilitar/Deshabilitar la incrustación de fuentes.
1. Guardar un nuevo Documento.

Las páginas HTML a menudo usan fuentes (por ejemplo, fuentes de una carpeta local, Google Fonts, etc.). También podemos controlar la incrustación de fuentes en un documento usando la propiedad [IsEmbedFonts](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions#isEmbedFonts--).

```java
HtmlLoadOptions options = new HtmlLoadOptions();
// Habilitar/Deshabilitar la incrustación de fuentes
options.setEmbedFonts(true);

Document document = new Document(DATA_DIR + "test_fonts.html", options);
document.save(DATA_DIR + "html_test.PDF");
document.close();
```

### Administrar la carga de recursos externos

El Motor de Conversión proporciona un mecanismo que te permite controlar la carga de ciertos recursos asociados con el documento HTML.

La clase [HtmlLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) tiene la propiedad [CustomLoaderOfExternalResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions#setCustomLoaderOfExternalResources-com.aspose.pdf.LoadOptions.ResourceLoadingStrategy-) con la cual podemos definir el comportamiento del cargador de recursos.

```java
HtmlLoadOptions options = new HtmlLoadOptions();

options.setCustomLoaderOfExternalResources(
        new LoadOptions.ResourceLoadingStrategy() {
            public LoadOptions.ResourceLoadingResult invoke(String resourceURI) {
                // Crear recurso de plantilla vacío para reemplazar:
                LoadOptions.ResourceLoadingResult res = new LoadOptions.ResourceLoadingResult(new byte[] {});
                // Devolver un arreglo de bytes vacío en caso de servidor i.imgur.com
                if (resourceURI.contains("i.imgur.com")) {
                    return res;
                } else {
                    // Procesar recursos con el cargador de recursos predeterminado
                    res.setLoadingCancelled(true);
                    return res;
                }
            }   
});

Document document = new Document(DATA_DIR + "test.html", options);
document.save(DATA_DIR + "html_test.PDF");
document.close();    
```

## Convertir MHTML a PDF

{{% alert color="success" %}}
**Intenta convertir MHTML a PDF en línea**


Aspose.PDF para Java te presenta la aplicación en línea gratuita ["MHTML a PDF"](https://products.aspose.app/pdf/conversion/mhtml-to-pdf), donde puedes tratar de investigar la funcionalidad y calidad con la que funciona.

[![Conversión de Aspose.PDF de MHTML a PDF usando la aplicación gratuita](mhtml.png)](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)
{{% /alert %}}

<abbr title="MIME encapsulation of aggregate HTML documents">MHTML</abbr>, abreviatura de MIME HTML, es un formato de archivo de archivo de página web utilizado para combinar recursos que normalmente se representan mediante enlaces externos (como imágenes, animaciones Flash, applets de Java y archivos de audio) con código HTML en un solo archivo. El contenido de un archivo MHTML se codifica como si fuera un mensaje de correo electrónico en HTML, utilizando el tipo MIME multipart/related.

El siguiente fragmento de código muestra cómo convertir archivos MHTML al formato PDF con Java:

```java
// Crear una instancia de MhtLoadOptions para especificar las opciones de carga para el
// archivo MHTML.
MhtLoadOptions options = new MhtLoadOptions();

// Establecer la ruta del archivo MHTML.
String mhtmlFileName = Paths.get(DATA_DIR.toString(), "samplefile.mhtml").toString();

// Cargar el archivo MHTML en un objeto Document.
Document document = new Document(mhtmlFileName, options);

// Guardar el documento como un archivo PDF.
document.save(Paths.get(DATA_DIR.toString(), "MarkdowntoPDF.pdf").toString());

// Cerrar el documento.
document.close();
```