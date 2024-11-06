---
title: Convertir PDF a formatos de imágenes
linktitle: Convertir PDF a Imágenes
type: docs
weight: 70
url: es/php-java/convert-pdf-to-images-format/
lastmod: "2024-05-20"
description: Este tema te muestra cómo Aspose.PDF permite convertir PDF a varios formatos de imágenes. Convierte páginas PDF a imágenes PNG, JPEG, BMP con unas pocas líneas de código.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF para PHP** te permite convertir documentos PDF a formatos de imagen como BMP, JPEG, GIF, PNG, EMF, TIFF y SVG usando dos enfoques. La conversión se realiza usando `Device` y usando `SaveOption`.

Hay varias clases en la biblioteca que te permiten usar un dispositivo virtual para transformar imágenes. `DocumentDevice` está orientado a la conversión de todo el documento, pero `ImageDevice` - para una página en particular.

## Convertir PDF usando la clase DocumentDevice

**Aspose.PDF para PHP** hace posible convertir páginas PDF a imágenes TIFF.

La [clase TiffDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) te permite convertir páginas PDF a imágenes TIFF.
 Esta clase proporciona un método llamado Process que te permite convertir todas las páginas de un archivo PDF en una única imagen TIFF.

### Convertir Páginas de PDF a Una Imagen TIFF

Aspose.PDF para PHP explica cómo convertir todas las páginas de un archivo PDF en una única imagen TIFF:

1. Crea un objeto de la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Llama al método [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/DocumentDevice#process-com.aspose.pdf.IDocument-int-int-java.io.OutputStream-) para convertir el documento.
1. Para establecer las propiedades del archivo de salida, utiliza la clase [TiffSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/TiffSettings).

El siguiente fragmento de código muestra cómo convertir todas las páginas del PDF en una única imagen TIFF.

```php
// Cargar el documento PDF
$document = new Document($inputFile);

// Crear un nuevo objeto TiffSettings
$tiffSettings = new devices_TiffSettings();

// Descomenta las siguientes líneas para personalizar las configuraciones de TIFF
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);

// Establecer la resolución para la imagen TIFF
$resolution = new devices_Resolution(300);

// Crear un nuevo objeto TiffDevice con la resolución y configuraciones especificadas
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// Convertir el documento PDF a TIFF utilizando el TiffDevice
$tiffDevice->process($document, $outputFile);
```

### Convertir una sola página a imagen TIFF

Aspose.PDF para PHP permite convertir una página en particular de un archivo PDF a una imagen TIFF, usando una versión sobrecargada del método Process(..) que toma un número de página como argumento para la conversión. El siguiente fragmento de código muestra cómo convertir la primera página de un PDF al formato TIFF.

```php
// Cargar el documento PDF
$document = new Document($inputFile);

// Crear un nuevo objeto TiffSettings
$tiffSettings = new devices_TiffSettings();

// Descomentar las siguientes líneas para personalizar la configuración de TIFF
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);

// Establecer la resolución para la imagen TIFF
$resolution = new devices_Resolution(300);

// Crear un nuevo objeto TiffDevice con la resolución y configuración especificadas
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// Convertir el documento PDF a TIFF usando el TiffDevice
$tiffDevice->process($document, 1, 1, $outputFile);
```


### Usar el algoritmo de Bradley durante la conversión

Aspose.PDF para PHP ha estado apoyando la función de convertir PDF a TIFF usando compresión LZW y luego con el uso de AForge, se puede aplicar Binarización. Sin embargo, uno de los clientes solicitó que para algunas imágenes, necesitan obtener el Umbral usando Otsu, por lo que también les gustaría usar Bradley.

```php
// Crear un nuevo objeto TiffSettings
$tiffSettings = new devices_TiffSettings();

// Descomentar las siguientes líneas para personalizar la configuración de TIFF
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);

$outputImageFile = new java("java.io.FileOutputStream", $outputImageFileName);
$outputBinImageFile = new java("java.io.FileOutputStream", $outputBinImageFileName);

// Establecer la resolución para la imagen TIFF
$resolution = new devices_Resolution(300);

// Crear un nuevo objeto TiffDevice con la resolución y configuración especificadas
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// Convertir el documento PDF a TIFF usando el TiffDevice
$tiffDevice->process($document, 1, 1, $outputFile);

// Crear objeto de flujo para guardar la imagen de salida
$inStream = new java("java.io.FileInputStream",$outputImageFileName);
$tiffDevice->binarizeBradley($inStream, $outputBinImageFile, 0.1);
```


### Convertir Páginas de PDF a Imágenes TIFF Pixeladas

Para convertir todas las páginas de un archivo PDF al formato TIFF Pixelado, utiliza la opción Pixelated de IndexedConversionType

```php
// Crear un nuevo objeto TiffSettings
$tiffSettings = new devices_TiffSettings();

// Descomenta las siguientes líneas para personalizar la configuración de TIFF
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);
// establecer el brillo de la imagen
$tiffSettings->setBrightness(0.5f);
// establecer el Tipo de Conversión Indexada, el valor predeterminado es simple
$tiffSettings->setIndexedConversionType(IndexedConversionType::Pixelated);


$outputImageFile = new java("java.io.FileOutputStream", $outputImageFileName);
$outputBinImageFile = new java("java.io.FileOutputStream", $outputBinImageFileName);

// Establecer la resolución para la imagen TIFF
$resolution = new devices_Resolution(300);

// Crear un nuevo objeto TiffDevice con la resolución y configuración especificadas
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// Convertir el documento PDF a TIFF usando el TiffDevice
$tiffDevice->process($document, 1, 1, $outputFile);

// Crear objeto de flujo para guardar la imagen de salida
$inStream = new java("java.io.FileInputStream",$outputImageFileName);
$tiffDevice->binarizeBradley($inStream, $outputBinImageFile, 0.1);
```


{{% alert color="success" %}}
**Intenta convertir PDF a TIFF en línea**

Aspose.PDF para PHP te presenta la aplicación gratuita en línea ["PDF a TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), donde puedes investigar la funcionalidad y la calidad con la que funciona.

[![Conversión de Aspose.PDF de PDF a TIFF con App Gratis](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## Convertir PDF usando la clase ImageDevice

`ImageDevice` es el antecesor de `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` y `EmfDevice`.

- La clase [BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) te permite convertir páginas PDF a imágenes <abbr title="Archivo de Imagen de Mapa de Bits">BMP</abbr>.
- La clase [EmfDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/EmfDevice) te permite convertir páginas PDF a imágenes <abbr title="Archivo de Meta Mejorado">EMF</abbr>.

- La clase [JpegDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/JpegDevice) te permite convertir páginas PDF a imágenes JPEG.
- La clase [PngDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/PngDevice) te permite convertir páginas PDF a imágenes <abbr title="Portable Network Graphics">PNG</abbr>.
- La clase [GifDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/GifDevice) te permite convertir páginas PDF a imágenes <abbr title="Graphics Interchange Format">GIF</abbr>.

Veamos cómo convertir una página PDF a una imagen.

La clase [BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) proporciona un método llamado [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice#process-com.aspose.pdf.Page-com.aspose.ms.System.Drawing.Graphics-) que te permite convertir una página particular del archivo PDF al formato de imagen BMP. Las otras clases tienen el mismo método. Entonces, si necesitamos convertir una página PDF a una imagen, simplemente instanciamos la clase requerida.

El siguiente fragmento de código muestra esta posibilidad:

```php
// Cargar el documento PDF
$document = new Document($inputFile);

// Obtener la colección de páginas en el documento
$pages = $document->getPages();

// Obtener el número total de páginas en el documento
$count = $pages->size();

// Establecer la resolución para las imágenes PNG
$resolution = new devices_Resolution(300);

// Crear un nuevo dispositivo PNG con la resolución especificada
$imageDevice = new devices_PngDevice($resolution);

// Recorrer cada página en el documento
for ($pageCount = 1; $pageCount <= $document->getPages()->size(); $pageCount++) {
    // Establecer el nombre del archivo de imagen de salida para la página actual
    $imageFileName = $imageFileNameTemplate . $pageCount . '.png';

    // Obtener la página actual de la colección
    $page = $document->getPages()->get_Item($pageCount);

    // Procesar la página actual y guardarla como una imagen PNG
    $imageDevice->process($page, $imageFileName);
}
```


{{% alert color="success" %}}
**Intenta convertir PDF a PNG en línea**

Como ejemplo de cómo funcionan nuestras aplicaciones gratuitas, por favor revisa la siguiente característica.

Aspose.PDF para PHP te presenta la aplicación gratuita en línea ["PDF a PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Cómo convertir PDF a PNG usando la aplicación gratuita](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Convertir PDF usando la clase SaveOptions

Esta parte del artículo te muestra cómo convertir PDF a <abbr title="Scalable Vector Graphics">SVG</abbr> usando Java y la clase SaveOptions.

{{% alert color="success" %}}
**Intenta convertir PDF a SVG en línea**

Aspose.PDF para PHP te presenta la aplicación gratuita en línea ["PDF a SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Conversión de PDF a SVG con Aspose.PDF usando la aplicación gratuita](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Gráficos Vectoriales Escalables (SVG)** es una familia de especificaciones de un formato de archivo basado en XML para gráficos vectoriales bidimensionales, tanto estáticos como dinámicos (interactivos o animados). La especificación SVG es un estándar abierto que ha estado en desarrollo por el Consorcio World Wide Web (W3C) desde 1999.

Las imágenes SVG y sus comportamientos se definen en archivos de texto XML. Esto significa que pueden ser buscados, indexados, programados y, si es necesario, comprimidos. Como archivos XML, las imágenes SVG pueden ser creadas y editadas con cualquier editor de texto, pero a menudo es más conveniente crearlas con programas de dibujo como Inkscape.

### Convertir páginas PDF a imágenes SVG

Aspose.PDF para PHP admite la función de convertir archivos PDF al formato SVG.
 Para cumplir con este requisito, la clase [SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions) ha sido introducida en el paquete com.aspose.pdf. Instancie un objeto de [SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions) y páselo como segundo argumento al método [Document.save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

El siguiente fragmento de código muestra los pasos para convertir un archivo PDF a formato SVG.

```php
// Cargar el documento PDF
$document = new Document($inputFile);

// Crear una instancia de la clase SvgSaveOptions
$saveOption = new SvgSaveOptions();

// Guardar el documento PDF como SVG
$document->save($outputFile, $saveOption);
```