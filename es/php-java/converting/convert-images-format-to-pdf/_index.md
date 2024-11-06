---
title: Convertir varios formatos de imágenes a PDF
linktitle: Convertir Imágenes a PDF
type: docs
weight: 60
url: es/php-java/convert-images-format-to-pdf/
lastmod: "2024-05-20"
description: Este tema muestra cómo la biblioteca Aspose.PDF para PHP permite convertir varios formatos de imágenes a PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF para PHP** te permite convertir diferentes formatos de imágenes a archivos PDF. Nuestra biblioteca demuestra fragmentos de código para convertir los formatos de imagen más populares, tales como - BMP, CGM, DMF, JPG, PNG, SVG y formatos TIFF.

## Convertir BMP a PDF

Convierte archivos BMP a documentos PDF usando la biblioteca **Aspose.PDF para PHP**.

Las imágenes <abbr title="Bitmap Image File">BMP</abbr> son archivos con extensión .BMP que representan archivos de imagen de mapa de bits que se utilizan para almacenar imágenes digitales de mapa de bits. Estas imágenes son independientes del adaptador gráfico y también se llaman formato de archivo de mapa de bits independiente del dispositivo (DIB).
Puedes convertir BMP a PDF con la API Aspose.PDF para PHP.
 Por lo tanto, puede seguir los siguientes pasos para convertir imágenes BMP:

1. Crear un nuevo objeto Document
1. Agregar una nueva página al documento
1. Establecer los márgenes de la página a 0 (si es necesario)
1. Crear un nuevo objeto Image y establecer el archivo BMP de entrada
1. Agregar la imagen a la página
1. Guardar el documento en el archivo PDF de salida

Así que el siguiente fragmento de código sigue estos pasos y muestra cómo convertir BMP a PDF usando PHP:

```php
// Crear un nuevo objeto Document
$document = new Document();

// Agregar una nueva página al documento
$page = $document->getPages()->add();

// Establecer los márgenes de la página a 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Crear un nuevo objeto Image y establecer el archivo BMP de entrada
$image = new Image();
$image->setFile($inputFile);

// Agregar la imagen a la página
$page->getParagraphs()->add($image);

// Guardar el documento en el archivo PDF de salida
$document->save($outputFile);
```

## Convertir CGM a PDF

<abbr title="Metarchivo de Gráficos por Computadora">CGM</abbr> es un estándar ISO que proporciona un formato de archivo de imagen 2D basado en vectores para el almacenamiento y recuperación de información gráfica. CGM es un formato independiente del dispositivo. CGM es un formato de gráficos vectoriales que admite tres métodos diferentes de codificación: binario (mejor para la velocidad de lectura del programa), basado en caracteres (produce el tamaño de archivo más pequeño y permite transferencias de datos más rápidas) o codificación de texto claro (permite a los usuarios leer y modificar el archivo con un editor de texto).

El siguiente fragmento de código le muestra cómo convertir archivos CGM al formato PDF usando Aspose.PDF para PHP.

1. Cree una instancia de [CgmLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/) para especificar cualquier opción específica para cargar el archivo CGM.
1. Cree una instancia de la clase [Document](https://reference.aspose.com/page/java/com.aspose.page/Document) con el nombre de archivo de origen mencionado y las opciones.
1. Guarde el documento con el nombre de archivo deseado.

```php
$options = new CgmLoadOptions();

// Crear un objeto Document y cargar el archivo CGM usando las opciones especificadas
$document = new Document($inputFile, $options);

// Guardar el documento como un archivo PDF
$document->save($outputFile);
```


## Convertir DICOM a PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> es un estándar para manejar, almacenar, imprimir y transmitir información en imágenes médicas. Incluye una definición de formato de archivo y un protocolo de comunicación en red.

Aspose.PDF for PHP te permite convertir archivos DICOM a formato PDF, revisa el siguiente fragmento de código:

1. Crear un nuevo objeto Document
1. Añadir una nueva página al documento
1. Establecer los márgenes de la página a 0 (si es necesario)
1. Crear un nuevo objeto Image y establecer el archivo BMP de entrada
1. Establecer el archivo DICOM como el archivo fuente para la imagen
1. Establecer el tipo de archivo de la imagen a DICOM
1. Añadir la imagen a la página
1. Guardar el documento en el archivo PDF de salida

```php
// Crear un nuevo objeto Document
$document = new Document();

// Añadir una nueva página al documento
$page = $document->getPages()->add();

// Establecer los márgenes de la página a 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Crear un nuevo objeto Image
$image = new Image();

// Establecer el archivo DICOM como el archivo fuente para la imagen
$image->setFile($inputFile);

// Establecer el tipo de archivo de la imagen a DICOM
$image->setFileType(ImageFileType::$Dicom);

// Añadir la imagen a la página
$page->getParagraphs()->add($image);

// Guardar el documento como un archivo PDF
$document->save($outputFile);
```


{{% alert color="success" %}}
**Intenta convertir DICOM a PDF en línea**

Aspose te presenta la aplicación gratuita en línea ["DICOM a PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Conversión Aspose.PDF de DICOM a PDF usando la aplicación gratuita](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## Convertir EMF a PDF

El formato de metarchivo mejorado (<abbr title="Enhanced metafile format">EMF</abbr>) almacena imágenes gráficas de manera independiente del dispositivo. Los metarchivos de EMF comprenden registros de longitud variable en orden cronológico que pueden representar la imagen almacenada después de ser analizados en cualquier dispositivo de salida.

Tenemos varios enfoques para convertir EMF en PDF.

## Usando la clase Image

Un documento PDF comprende páginas y cada página contiene uno o más objetos de párrafo. Un párrafo puede ser un texto, imagen, tabla, cuadro flotante, gráfico, encabezado, campo de formulario o un archivo adjunto.

Para convertir un archivo de imagen en formato PDF, encierra la imagen en un párrafo.

Es posible convertir imágenes en una ubicación física en el disco duro local, encontradas en una URL web o en una instancia de Stream.

Para agregar una imagen:

1. Crea un objeto de la clase com.aspose.pdf.Image.
1. Añade la imagen a una colección de [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/paragraphs) de una instancia de página.
1. Especifica la ruta o fuente de la Imagen.
    - Si una imagen está en una ubicación en el disco duro, especifica la ubicación de la ruta usando el método [Image.setFile(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image).
    - Si una imagen está colocada en un FileInputStream, pasa el objeto que contiene la imagen al método [Image.setImageStream(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image).

El siguiente fragmento de código muestra cómo cargar un objeto de imagen, establecer el margen de la página, colocar la imagen en la página y guardar el resultado como PDF.

```php
$inputFile = "sample.emf";

// Crea un nuevo objeto Document
$document = new Document();

// Añade una nueva página al documento
$page = $document->getPages()->add();

// Establece los márgenes de la página a 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Crea un nuevo objeto Image y establece el archivo de entrada
$image = new Image();
$image->setFile($inputFile);

// Añade la imagen a la página
$page->getParagraphs()->add($image);

// Guarda el documento como un archivo PDF
$document->save($outputFile);
```


## Convertir JPG a PDF

No necesitas preguntarte cómo convertir JPG a PDF, porque Apose.PDF para PHP tiene la mejor solución.

Puedes convertir fácilmente imágenes JPG a PDF con Aspose.PDF para PHP siguiendo estos pasos:

1. Inicializa un objeto de la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. Añade una nueva página al documento
1. Establece los márgenes de la página a 0
1. Crea un nuevo objeto de imagen y establece el archivo de entrada
1. Guarda el PDF de salida

El siguiente fragmento de código muestra cómo convertir una imagen JPG a PDF usando PHP:

```php
$inputFile = "sample.jpg";

// Crea un nuevo objeto Document
$document = new Document();

// Añade una nueva página al documento
$page = $document->getPages()->add();

// Establece los márgenes de la página a 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Crea un nuevo objeto de imagen y establece el archivo de entrada
$image = new Image();
$image->setFile($inputFile);

// Añade la imagen a la página
$page->getParagraphs()->add($image);

// Guarda el documento como un archivo PDF
$document->save($outputFile);
```


{{% alert color="success" %}}
**Intenta convertir JPG a PDF en línea**

Aspose te presenta una aplicación gratuita en línea ["JPG to PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/), donde puedes probar la funcionalidad y la calidad con que trabaja.

[![Aspose.PDF Conversión JPG a PDF usando Aplicación Gratuita](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## Convertir PNG a PDF

**Aspose.PDF para PHP** admite la función de convertir imágenes PNG al formato PDF. Consulta el siguiente fragmento de código para realizar tu tarea.

<abbr title="Portable Network Graphics">PNG</abbr> se refiere a un tipo de formato de archivo de imagen rasterizada que utiliza compresión sin pérdida, lo que lo hace popular entre sus usuarios.

Puedes convertir una imagen PNG a PDF utilizando los siguientes pasos:

1. Inicializa un objeto de la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. Añade una nueva página al documento
1. Establece los márgenes de la página en 0
1. Crea un nuevo objeto Image y establece el archivo de entrada
1. Guarda el PDF de salida

Además, el siguiente fragmento de código muestra cómo convertir PNG a PDF en tus aplicaciones PHP:

```php
$inputFile = "sample.png";

// Crear un nuevo objeto Document
$document = new Document();

// Añadir una nueva página al documento
$page = $document->getPages()->add();

// Establecer los márgenes de la página a 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Crear un nuevo objeto Image y establecer el archivo de entrada
$image = new Image();
$image->setFile($inputFile);

// Añadir la imagen a la página
$page->getParagraphs()->add($image);

// Guardar el documento como un archivo PDF
$document->save($outputFile);
```

{{% alert color="success" %}}
**Intenta convertir PNG a PDF en línea**

Aspose te presenta la aplicación gratuita en línea ["PNG a PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Conversión Aspose.PDF de PNG a PDF usando la aplicación gratuita](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)

{{% /alert %}}

## Convertir SVG a PDF

Gráficos Vectoriales Escalables (SVG) es una familia de especificaciones de un formato de archivo basado en XML para gráficos vectoriales bidimensionales, tanto estáticos como dinámicos (interactivos o animados). La especificación SVG es un estándar abierto que ha estado en desarrollo por el Consorcio World Wide Web (W3C) desde 1999.

Las imágenes SVG y sus comportamientos están definidos en archivos de texto XML. Esto significa que pueden ser buscados, indexados, con guiones y, si es necesario, comprimidos. Como archivos XML, las imágenes SVG pueden ser creadas y editadas con cualquier editor de texto, pero a menudo es más conveniente crearlas con programas de dibujo como Inkscape.

## Cómo convertir un archivo SVG a formato PDF

Para convertir archivos SVG a PDF, use la clase llamada [SvgLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions) que se utiliza para inicializar el objeto [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions).
 Más tarde, este objeto se pasa como un argumento durante la inicialización del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) y ayuda al motor de renderizado PDF a determinar el formato de entrada del documento fuente.

El siguiente fragmento de código muestra el proceso de conversión de un archivo SVG al formato PDF.

```php
// Crear un nuevo objeto SvgLoadOptions
$loadOption = new SvgLoadOptions();

// Crear un nuevo objeto Document y cargar el archivo SVG
$document = new Document($inputFile, $loadOption);

// Guardar el documento como un archivo PDF
$document->save($outputFile);
```

{{% alert color="success" %}}
**Intenta convertir el formato SVG a PDF en línea**

Aspose.PDF para PHP te presenta una aplicación gratuita en línea ["SVG a PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Conversión Aspose.PDF de SVG a PDF con aplicación gratuita](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

## Convertir TIFF a PDF

**Aspose.PDF para PHP** formato de archivo soportado, ya sea una imagen <abbr title="Formato de Archivo de Imagen Etiquetada">TIFF</abbr> de un solo cuadro o de múltiples cuadros. Esto significa que puedes convertir la imagen TIFF a PDF en tus aplicaciones Java.

TIFF o TIF, Formato de Archivo de Imagen Etiquetada, representa imágenes rasterizadas que están destinadas para su uso en una variedad de dispositivos que cumplen con este estándar de formato de archivo. La imagen TIFF puede contener varios cuadros con diferentes imágenes. El formato de archivo Aspose.PDF también es compatible, ya sea una imagen TIFF de un solo cuadro o de múltiples cuadros. Por lo tanto, puedes convertir la imagen TIFF a PDF en tus aplicaciones Java. Por lo tanto, consideraremos un ejemplo de conversión de una imagen TIFF de varias páginas a un documento PDF de varias páginas con los siguientes pasos:

1. Crear un nuevo objeto Document
1. Añadir una nueva página al documento
1. Establecer los márgenes de la página a 0
1. Crear un nuevo objeto Image
1. Establecer la ruta del archivo de la imagen TIFF de entrada
1. Añadir la imagen a la página
1. Guardar el documento como un archivo PDF

Además, el siguiente fragmento de código muestra cómo convertir una imagen TIFF de varias páginas o múltiples cuadros a PDF:

```php
// Crear un nuevo objeto Document
$document = new Document();

// Añadir una nueva página al documento
$page = $document->getPages()->add();

// Establecer los márgenes de la página a 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Crear un nuevo objeto Image
$image = new Image();

// Establecer la ruta del archivo de la imagen TIFF de entrada
$image->setFile($inputFile);

// Añadir la imagen a la página
$page->getParagraphs()->add($image);

// Guardar el documento como un archivo PDF
$document->save($outputFile);
```