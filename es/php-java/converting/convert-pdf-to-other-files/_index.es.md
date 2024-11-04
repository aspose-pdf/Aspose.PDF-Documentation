---
title: Convertir archivo PDF a otros formatos
linktitle: Convertir PDF a otros formatos
type: docs
weight: 90
url: /php-java/convert-pdf-to-other-files/
lastmod: "2024-05-20"
description: Este tema muestra cómo Aspose.PDF permite convertir un archivo PDF a otros formatos de archivo.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convertir PDF a EPUB

{{% alert color="success" %}}
**Prueba a convertir PDF a EPUB en línea**

Aspose.PDF para PHP te presenta la aplicación gratuita en línea ["PDF a EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), donde puedes probar e investigar la funcionalidad y la calidad con la que trabaja.

[![Aspose.PDF Conversión de PDF a EPUB con Aplicación Gratuita](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Electronic Publication">EPUB</abbr>** (abreviatura de publicación electrónica) es un estándar de libro electrónico libre y abierto del International Digital Publishing Forum (IDPF).
 Los archivos tienen la extensión .epub. EPUB está diseñado para contenido adaptativo, lo que significa que un lector EPUB puede optimizar el texto para un dispositivo de visualización en particular. EPUB también admite contenido de diseño fijo. El formato está destinado como un único formato que los editores y las casas de conversión pueden usar internamente, así como para distribución y venta. Sustituye al estándar Open eBook.

Aspose.PDF para PHP admite la función de convertir documentos PDF al formato EPUB. Aspose.PDF para PHP tiene una clase llamada [EpubSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubSaveOptions) que se puede usar como el segundo argumento del método [Document.save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#save-java.lang.String-), para generar un archivo EPUB. Por favor, intente usar el siguiente fragmento de código para lograr este requisito.

```php
// Crear una nueva instancia de la clase Document y cargar el archivo PDF de entrada
$document = new Document($inputFile);

// Crear una nueva instancia de la clase EpubSaveOptions
$saveOption = new EpubSaveOptions();

// Guardar el documento en formato EPUB usando las opciones de guardado especificadas
$document->save($outputFile, $saveOption);
```

## Convertir PDF a LaTeX/TeX

**Aspose.PDF para PHP** admite la conversión de PDF a LaTeX/TeX.
El formato de archivo LaTeX es un formato de archivo de texto con un marcado especial y se utiliza en el sistema de preparación de documentos basado en TeX para la composición tipográfica de alta calidad.

Para convertir archivos PDF a TeX, Aspose.PDF tiene la clase [LaTeXSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LaTeXSaveOptions) que proporciona el método `setOutDirectoryPath` para guardar imágenes temporales durante el proceso de conversión.

El siguiente fragmento de código muestra el proceso de conversión de archivos PDF al formato TEX con Java.

```php
// Crear un nuevo objeto Document y cargar el archivo PDF de entrada
$document = new Document($inputFile);

// Crear un nuevo objeto LaTeXSaveOptions
$saveOption = new LaTeXSaveOptions();
$saveOption->setOutDirectoryPath ($pathToOutputDirectory)

// Guardar el documento como LaTeX
$document->save($outputFile, $saveOption);
```

{{% alert color="success" %}}
**Intenta convertir PDF a LaTeX/TeX en línea**

Aspose.PDF para PHP te presenta la aplicación gratuita en línea ["PDF a LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), donde puedes intentar investigar la funcionalidad y la calidad con la que trabaja.

[![Aspose.PDF Conversión de PDF a LaTeX/TeX con App Gratis](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Convertir PDF a Texto

**Aspose.PDF para PHP** soporta convertir un documento PDF completo y una sola página a un archivo de Texto.

### Convertir documento PDF completo a archivo de Texto

Puede convertir un documento PDF a un archivo TXT usando el método Visit de la clase [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber).

El siguiente fragmento de código explica cómo extraer los textos de todas las páginas.

```php
// Cargar el documento PDF
$document = new Document($inputFile);

// Crear un objeto TextAbsorber para extraer texto del documento
$textAbsorber = new TextAbsorber();

// Extraer el texto del documento
$textAbsorber->visit($document);
$content = $textAbsorber->getText();

// Guardar el texto extraído en el archivo de salida
file_put_contents($outputFile, $content);

// Obtener el tamaño del archivo de salida
$fileSize = filesize($outputFile);
```


{{% alert color="success" %}}
**Intenta convertir Convertir PDF a Texto en línea**

Aspose.PDF para PHP te presenta una aplicación gratuita en línea ["PDF a Texto"](https://products.aspose.app/pdf/conversion/pdf-to-txt), donde puedes intentar investigar la funcionalidad y la calidad con la que trabaja.

[![Aspose.PDF Conversión PDF a Texto con Aplicación Gratuita](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

### Convertir página de PDF a archivo de texto

Puedes convertir un documento PDF a un archivo TXT con Aspose.PDF para PHP. Debes usar el método Visit de la clase [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) para resolver esta tarea.

El siguiente fragmento de código explica cómo extraer los textos de páginas particulares.

```php
// Cargar el documento PDF
$document = new Document($inputFile);

// Crear un objeto TextAbsorber para extraer texto del documento
$textAbsorber = new TextAbsorber();

$array = array(1, 3, 4);

foreach ($array as $page) {
    $textAbsorber->visit($document->getPages()->get_Item($page));
    $content = $textAbsorber->getText();
    
    $outputFile = $dataDir . DIRECTORY_SEPARATOR . 'result-pdf-to-text'. $page . '.txt';
    // Guardar el texto extraído en el archivo de salida
    file_put_contents($outputFile, $content);
}
```


## Convertir PDF a XPS

**Aspose.PDF para PHP** brinda la posibilidad de convertir archivos PDF al formato <abbr title="XML Paper Specification">XPS</abbr>. Vamos a intentar usar el fragmento de código presentado para convertir archivos PDF al formato XPS con Java.

{{% alert color="success" %}}
**Intenta convertir PDF a XPS en línea**

Aspose.PDF para PHP te presenta una aplicación gratuita en línea ["PDF a XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), donde puedes investigar la funcionalidad y calidad con la que trabaja.

[![Conversión de PDF a XPS de Aspose.PDF con aplicación gratuita](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

El tipo de archivo XPS está principalmente asociado con la Especificación de Papel XML de Microsoft Corporation. La Especificación de Papel XML (XPS), anteriormente con el nombre en clave Metro y subsumiendo el concepto de marketing Next Generation Print Path (NGPP), es la iniciativa de Microsoft para integrar la creación y visualización de documentos en el sistema operativo Windows.

Para convertir archivos PDF a XPS, Aspose.PDF tiene la clase [XpsSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsSaveOptions) que se utiliza como segundo argumento en el constructor Document.save(..) para generar el archivo XPS.
 El siguiente fragmento de código muestra el proceso de conversión de archivos PDF a formato XPS.

```php
// Crear un nuevo objeto Document y cargar el archivo PDF de entrada
$document = new Document($inputFile);

// Crear un nuevo objeto XpsSaveOptions
$saveOption = new XpsSaveOptions();

// Guardar el documento como XPS usando las opciones de guardado especificadas
$document->save($outputFile, $saveOption);
```