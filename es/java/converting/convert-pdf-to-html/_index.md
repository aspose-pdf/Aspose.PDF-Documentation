---
title: Convertir archivo PDF a formato HTML 
linktitle: Convertir archivo PDF a formato HTML
type: docs
weight: 50
url: es/java/convert-pdf-to-html/
lastmod: "2021-11-19"
description: Este tema muestra cómo Aspose.PDF permite convertir un archivo PDF a formato HTML con la biblioteca Java.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Aspose.PDF para Java ofrece muchas características para convertir varios formatos de archivo a documentos PDF y convertir archivos PDF en varios formatos de salida. Este artículo discute cómo convertir un archivo PDF en formato HTML y guardar las imágenes del archivo PDF en una carpeta particular.

{{% alert color="success" %}}
**Intenta convertir PDF a HTML en línea**

Aspose.PDF para Java te presenta una aplicación en línea gratuita ["PDF a HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Aspose.PDF Conversión PDF a HTML con Aplicación Gratuita](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)

{{% /alert %}}

Cuando se convierte un archivo PDF grande con varias páginas a formato HTML, el resultado aparece como una sola página HTML. Puede terminar siendo muy largo. Para controlar el tamaño de la página, es posible dividir la salida en varias páginas durante la conversión de PDF a HTML.

## Convertir páginas PDF a HTML

Aspose.PDF para Java proporciona muchas características para convertir varios formatos de archivos a documentos PDF y convertir archivos PDF en varios formatos de salida. Este artículo discute cómo convertir un archivo PDF a formato HTML y guardar las imágenes del archivo PDF en una carpeta particular.

El siguiente fragmento de código te muestra todas las opciones posibles que puedes usar al convertir PDF a HTML.

```java
// Abrir el documento PDF de origen
Document pdfDocument = new Document(_dataDir + "PDFToHTML.pdf");

// Guardar el archivo en formato de documento MS
pdfDocument.save(_dataDir + "output_out.html", SaveFormat.Html);
```

## Convertir PDF a HTML - Dividir salida en HTML de varias páginas

Aspose.PDF para Java soporta la función de convertir documentos PDF a varios formatos de salida, incluido HTML.
 Sin embargo, al convertir archivos PDF grandes (compuestos de múltiples páginas), puede tener un requisito de guardar cada página PDF individual en un archivo HTML separado.

Al convertir un archivo PDF grande con varias páginas al formato HTML, la salida aparece como una sola página HTML. Puede terminar siendo muy larga. Para controlar el tamaño de la página, es posible dividir la salida en varias páginas durante la conversión de PDF a HTML. Por favor, intente usar el siguiente fragmento de código.

```java
// Abrir el documento PDF de origen
Document document = new Document(_dataDir + "PDFToHTML.pdf");

// Instanciar un objeto HtmlSaveOptions
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();

// Especificar dividir la salida en varias páginas
htmlOptions.setSplitIntoPages(true);

// Guardar el documento
document.save(_dataDir + "MultiPageHTML_out.html", htmlOptions);    
```

## Convertir PDF a HTML - Evitar Guardar Imágenes en Formato SVG

El formato de salida predeterminado para guardar imágenes al convertir de PDF a HTML es SVG. Durante la conversión, algunas imágenes de PDF se transforman en imágenes vectoriales SVG. Esto podría ser lento. En su lugar, las imágenes podrían transformarse en PNG. Para permitir esto, Aspose.PDF tiene la opción de usar SVG para vectores o crear PNGs.

Para eliminar completamente la representación de imágenes en formato SVG al convertir archivos PDF a formato HTML, por favor intente usar el siguiente fragmento de código.

```java
 // Cargar el archivo PDF
Document document = new Document(DATA_DIR + "PDFToHTML.pdf")

// Instanciar objeto de opciones de guardado HTML
HtmlSaveOptions saveOptions = new HtmlSaveOptions();

// Especificar la carpeta donde se guardan las imágenes SVG durante la conversión de PDF a HTML
saveOptions.setSpecialFolderForSvgImages(DATA_DIR.toString());

// Guardar el archivo de salida
document.save(DATA_DIR + "SaveSVGFiles_out.html", saveOptions);
```

## Comprimir Imágenes SVG Durante la Conversión

Para comprimir imágenes SVG durante la conversión de PDF a HTML, por favor intente usar el siguiente código:

```java
// Cargar el archivo PDF
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");

// Crear HtmlSaveOption con la función probada
HtmlSaveOptions saveOptions = new HtmlSaveOptions();

// Comprimir las imágenes SVG si las hay
saveOptions.setCompressSvgGraphicsIfAny(true);
document.save(DATA_DIR + "SaveSVGFiles_out.html", saveOptions);
document.close();
```

## Convertir PDF a HTML - Especificar Carpeta de Imágenes

Por defecto, al convertir un archivo PDF a HTML, las imágenes en el PDF se guardan en una carpeta separada creada en el mismo directorio donde se crea el HTML de salida. Pero a veces es necesario especificar una carpeta diferente para guardar las imágenes al generar archivos HTML. Para lograr esto, introdujimos el [SaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SaveOptions). El método [SpecialFolderForAllImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/#setSpecialFolderForAllImages-java.lang.String-) se utiliza para especificar la carpeta de destino para almacenar imágenes.

```java
// Cargar el archivo PDF
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");
HtmlSaveOptions saveOptions = new HtmlSaveOptions();

// Especificar la carpeta separada para guardar imágenes
saveOptions.setSpecialFolderForAllImages(DATA_DIR.toString());
document.save(DATA_DIR + "SaveSVGFiles_out.html", saveOptions);
document.close();
```

## Crear Archivos Subsiguientes Solo con el Contenido del Cuerpo

Con el siguiente fragmento de código simple, puede dividir el HTML de salida en páginas. En las páginas de salida, todos los objetos HTML deben ir exactamente donde van ahora (procesamiento y salida de fuentes, creación y salida de CSS, creación y salida de imágenes), excepto que el HTML de salida contendrá contenidos actualmente colocados dentro de las etiquetas (ahora se omitirán las etiquetas "body").

```java
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");

HtmlSaveOptions saveOptions = new HtmlSaveOptions();

saveOptions.setHtmlMarkupGenerationMode(HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent);
saveOptions.setSplitIntoPages(true);

document.save(DATA_DIR + "CreateSubsequentFiles_out.html", saveOptions);
document.close();
```

## Renderizado de Texto Transparente

En caso de que el archivo PDF de origen/entrada contenga textos transparentes sombreado por imágenes de primer plano, entonces puede haber problemas de renderizado de texto. Así que para atender tales escenarios, se pueden usar los métodos `setSaveShadowedTextsAsTransparentTexts` y `setSaveTransparentTexts`.

```java
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");

// Instanciar objeto de opciones de guardado HTML
HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();
htmlsaveOptions.setSaveShadowedTextsAsTransparentTexts(true);
htmlsaveOptions.setSaveTransparentTexts(true);

// Guardar el documento
document.save(DATA_DIR + "TransparentTextRendering_out.html", htmlsaveOptions);
document.close();
```


## Renderizado de capas de documentos PDF

Podemos renderizar capas de documentos PDF en un elemento de tipo capa separado durante la conversión de PDF a HTML:

```java
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");
// Instanciar objeto HTML SaveOptions

HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();

// Especificar renderizar capas de documentos PDF por separado en el HTML de salida
htmlsaveOptions.setConvertMarkedContentToLayers(true);

// Guardar el documento
document.save(DATA_DIR + "LayersRendering_out.html", htmlsaveOptions);
document.close();
```

La conversión de PDF a HTML es una de las características más populares de Aspose.PDF porque permite ver el contenido de archivos PDF en varias plataformas sin usar un visor de documentos PDF. El HTML de salida cumple con los estándares WWW y puede mostrarse fácilmente en todos los navegadores web. Usando esta característica, los archivos PDF pueden verse en dispositivos portátiles porque no necesitas instalar ninguna aplicación de visualización de PDF, sino que puedes usar un navegador web simple.

## PDF a HTML - Excluir recursos de fuentes

Si tiene la intención de excluir todos o algunos recursos de fuentes durante la conversión de PDF a HTML, Aspose.PDF para Java API le permite lograr esto con la ayuda de la clase HtmlSaveOptions. La API ofrece dos opciones para este propósito.

- `htmlOptions.FontSavingMode = HTmlSaveOptions.FontSavingModes.DontSave` - para evitar exportar todas las fuentes
- `htmlOptions.ExcludeFontNameList = (new String[] { "ArialMT", "SymbolMT" });` - es para evitar exportar fuentes específicas (nombres de fuentes a especificar sin hash)

Para convertir PDF a HTML excluyendo recursos de fuentes, utilice los siguientes pasos:

1. Defina un nuevo objeto de la clase HtmlSaveOptions
1. Defina y establezca los nombres de las fuentes que se deben evitar exportar en HtmlSaveOptions.ExcludeFontNameList
1. Convierta el PDF a HTML usando el método save

```java
HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();
htmlsaveOptions.setExplicitListOfSavedPages(
        new int[]{
                1
        }
);
htmlsaveOptions.setFixedLayout(true);
htmlsaveOptions.setCompressSvgGraphicsIfAny(false);
htmlsaveOptions.setSaveTransparentTexts(true);
htmlsaveOptions.setSaveShadowedTextsAsTransparentTexts(true);
htmlsaveOptions.setExcludeFontNameList(new String[]{"ArialMT", "SymbolMT"});
htmlsaveOptions.setFontSavingMode(HtmlSaveOptions.FontSavingModes.DontSave);
htmlsaveOptions.setDefaultFontName("Comic Sans MS");
htmlsaveOptions.setUseZOrder(true);
htmlsaveOptions
        .setLettersPositioningMethod(LettersPositioningMethods.UseEmUnitsAndCompensationOfRoundingErrorsInCss);
htmlsaveOptions
        .setPartsEmbeddingMode(HtmlSaveOptions.PartsEmbeddingModes.NoEmbedding);
htmlsaveOptions
        .setRasterImagesSavingMode(HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
htmlsaveOptions.setSplitIntoPages(false);

Document document = new Document(DATA_DIR + "sample.pdf");
document.save(DATA_DIR + "output_out.html", htmlsaveOptions);
document.close();
```