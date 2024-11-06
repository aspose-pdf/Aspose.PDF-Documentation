---
title: Convertir archivo PDF a formato HTML 
linktitle: Convertir archivo PDF a formato HTML
type: docs
weight: 50
url: es/php-java/convert-pdf-to-html/
lastmod: "2024-05-20"
description: Este tema le muestra cómo Aspose.PDF permite convertir un archivo PDF a formato HTML con la biblioteca PHP.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Aspose.PDF para PHP proporciona muchas características para convertir varios formatos de archivo a documentos PDF y convertir archivos PDF en varios formatos de salida. Este artículo discute cómo convertir un archivo PDF en formato HTML y guardar las imágenes del archivo PDF en una carpeta particular.

{{% alert color="success" %}}
**Pruebe convertir PDF a HTML en línea**

Aspose.PDF para PHP le presenta una aplicación en línea gratuita ["PDF a HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), donde puede probar para investigar la funcionalidad y calidad con la que trabaja.

[![Aspose.PDF Conversión PDF a HTML con Aplicación Gratuita](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)

{{% /alert %}}

Cuando se convierte un archivo PDF grande con varias páginas al formato HTML, la salida aparece como una sola página HTML. Puede terminar siendo muy larga. Para controlar el tamaño de la página, es posible dividir la salida en varias páginas durante la conversión de PDF a HTML.

## Convertir páginas PDF a HTML

Aspose.PDF para PHP ofrece muchas características para convertir varios formatos de archivo a documentos PDF y convertir archivos PDF en varios formatos de salida. Este artículo discute cómo convertir un archivo PDF en formato HTML y guardar las imágenes del archivo PDF en una carpeta particular.

El siguiente fragmento de código muestra todas las posibles opciones que puede utilizar al convertir PDF a HTML.

```php
// Crear un nuevo objeto Document y cargar el archivo PDF de entrada
$document = new Document($inputFile);

// Crear un nuevo objeto HtmlSaveOptions para guardar el documento como HTML
$saveOption = new HtmlSaveOptions();

// Guardar el documento como HTML usando las opciones de guardado especificadas
$document->save($outputFile, $saveOption);
```

## Convertir PDF a HTML - Dividir la salida en HTML de varias páginas

Aspose.PDF para PHP admite la función de convertir documentos PDF a varios formatos de salida, incluido HTML. Sin embargo, al convertir archivos PDF grandes (compuestos por múltiples páginas), puede tener el requisito de guardar cada página PDF individual en un archivo HTML separado.

Al convertir un archivo PDF grande con varias páginas al formato HTML, la salida aparece como una sola página HTML. Puede terminar siendo muy larga. Para controlar el tamaño de la página, es posible dividir la salida en varias páginas durante la conversión de PDF a HTML. Por favor, intente usar el siguiente fragmento de código.

```php
// Crear un nuevo objeto Document y cargar el archivo PDF de entrada
$document = new Document($inputFile);

// Crear un nuevo objeto HtmlSaveOptions para guardar el documento como HTML
$saveOption = new HtmlSaveOptions();

// Especificar dividir la salida en varias páginas
$saveOption->setSplitIntoPages(true);

// Guardar el documento como HTML usando las opciones de guardado especificadas
$document->save($outputFile, $saveOption);
```

## Convertir PDF a HTML - Evitar Guardar Imágenes en Formato SVG


El formato de salida predeterminado para guardar imágenes al convertir de PDF a HTML es SVG. Durante la conversión, algunas imágenes del PDF se transforman en imágenes vectoriales SVG. Esto podría ser lento. En su lugar, las imágenes podrían transformarse en PNG. Para permitir esto, Aspose.PDF tiene la opción de usar SVG para vectores o crear PNG.

Para eliminar completamente el renderizado de imágenes en formato SVG al convertir archivos PDF a formato HTML, intente usar el siguiente fragmento de código.

```php
// Crear un nuevo objeto Document y cargar el archivo PDF de entrada
$document = new Document($inputFile);

// Crear un nuevo objeto HtmlSaveOptions para guardar el documento como HTML
$saveOption = new HtmlSaveOptions();

// Especificar la carpeta donde se guardan las imágenes SVG durante la conversión de PDF a HTML
$saveOption->setSpecialFolderForSvgImages(DATA_DIR);

// Guardar el documento como HTML usando las opciones de guardado especificadas
$document->save($outputFile, $saveOption);
```

## Comprimir Imágenes SVG Durante la Conversión

Para comprimir imágenes SVG durante la conversión de PDF a HTML, por favor intente usar el siguiente código:

```php
// Crear un nuevo objeto Document y cargar el archivo PDF de entrada
$document = new Document($inputFile);

// Crear un nuevo objeto HtmlSaveOptions para guardar el documento como HTML
$saveOptions = new HtmlSaveOptions();
$saveOptions = setCompressSvgGraphicsIfAny(true);

// Guardar el documento como HTML usando las opciones de guardado especificadas
$document->save($outputFile, $saveOptions);
```

## Convertir PDF a HTML - Especificar Carpeta de Imágenes

Por defecto, al convertir un archivo PDF a HTML, las imágenes en el PDF se guardan en una carpeta separada creada en el mismo directorio donde se crea el HTML de salida. Pero a veces, es necesario especificar una carpeta diferente para guardar las imágenes al generar archivos HTML. Para lograr esto, introducimos el [SaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SaveOptions).

El método [setSpecialFolderForAllImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/#setSpecialFolderForSvgImages-java.lang.String-) se utiliza para especificar la carpeta de destino para almacenar imágenes.


```php
// Crea un nuevo objeto de Documento y carga el archivo PDF de entrada
$document = new Document($inputFile);

// Crea un nuevo objeto HtmlSaveOptions para guardar el documento como HTML
$saveOptions = new HtmlSaveOptions();
$saveOptions->setSpecialFolderForAllImages(DATA_DIR);

// Guarda el documento como HTML usando las opciones de guardado especificadas
$document->save($outputFile, $saveOptions);
```

## Renderizado de Texto Transparente

En caso de que el archivo PDF de origen/entrada contenga textos transparentes sombreados por imágenes de primer plano, entonces podría haber problemas de renderizado de texto. Entonces, para atender tales escenarios, se pueden usar las propiedades SaveShadowedTextsAsTransparentTexts y SaveTransparentTexts.

```php
// Crea un nuevo objeto de Documento y carga el archivo PDF de entrada
$document = new Document($inputFile);

// Crea un nuevo objeto HtmlSaveOptions para guardar el documento como HTML
$saveOptions = new HtmlSaveOptions();
$saveOptions->setSaveShadowedTextsAsTransparentTexts(true);
$saveOptions->setTransparentTexts(true);

// Guarda el documento como HTML usando las opciones de guardado especificadas
$document->save($outputFile, $saveOptions);
```


## Renderizado de capas de documentos PDF

Podemos renderizar capas de documentos PDF en un elemento de tipo capa separado durante la conversión de PDF a HTML:

```php
// Crear un nuevo objeto Document y cargar el archivo PDF de entrada
$document = new Document($inputFile);

// Crear un nuevo objeto HtmlSaveOptions para guardar el documento como HTML
$saveOptions = new HtmlSaveOptions();
$saveOptions->setConvertMarkedContentToLayers(true);

// Guardar el documento como HTML usando las opciones de guardado especificadas
$document->save($outputFile, $saveOptions);
```

La conversión de PDF a HTML es una de las características más populares de Aspose.PDF porque permite ver el contenido de archivos PDF en varias plataformas sin usar un visor de documentos PDF. El HTML de salida se ajusta a los estándares de la WWW y puede mostrarse fácilmente en todos los navegadores web. Usando esta función, los archivos PDF pueden visualizarse en dispositivos portátiles porque no necesitas instalar ninguna aplicación para visualizar PDF, sino que puedes usar un simple navegador web.