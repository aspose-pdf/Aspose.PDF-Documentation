---
title: Agregar Encabezado y Pie de Página en PDF
linktitle: Agregar Encabezado y Pie de Página en PDF
type: docs
weight: 70
url: /es/php-java/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF para PHP a través de Java le permite agregar encabezados y pies de página a su archivo PDF usando la clase TextStamp.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Los sellos PDF se utilizan a menudo en contratos, informes y materiales restringidos, para demostrar que los documentos han sido revisados y marcados como "leído", "calificado" o "confidencial", etc. Este artículo le mostrará cómo podemos agregar sellos de imagen y sellos de texto a documentos PDF utilizando **Aspose.PDF para PHP a través de Java**.

Si lee los fragmentos de código anteriores línea por línea, debe encontrar que la sintaxis y la lógica del código son bastante fáciles de entender.

## Agregar Texto en el Encabezado del Archivo PDF

Puede utilizar la clase [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) para agregar texto en el encabezado de un archivo PDF.
 TextStamp class proporciona las propiedades necesarias para crear un sello basado en texto como tamaño de fuente, estilo de fuente, color de fuente, etc. Para agregar texto en el encabezado, necesitas crear un objeto Document y un objeto TextStamp utilizando las propiedades requeridas. Después de eso, puedes llamar al método AddStamp de la Page para agregar el texto en el encabezado del PDF.

Necesitas configurar la propiedad TopMargin de tal manera que ajuste el texto en el área del encabezado de tu PDF. También necesitas configurar HorizontalAlignment a Center y VerticalAlignment a Top.

El siguiente fragmento de código te muestra cómo agregar texto en el encabezado de un archivo PDF con PHP.

```php

    // Abrir documento
    $document = new Document($inputFile);

    // Crear encabezado
    $textStamp = new TextStamp("Texto del Encabezado");
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // Establecer propiedades del sello
    $textStamp->setTopMargin(10);
    $textStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $textStamp->setVerticalAlignment($verticalAlignment->Top);

    $pages = $document->getPages();

    // Agregar pie de página en la 1ª página
    $page = $pages->get_Item(1);
    $page->addStamp($textStamp);
    
    // Guardar documento de salida
    $document->save($outputFile);
    $document->close();
```

## Añadiendo Texto en el Pie de Página de un Archivo PDF

Puedes usar la clase TextStamp para agregar texto en el pie de página de un archivo PDF. La clase TextStamp proporciona las propiedades necesarias para crear un sello basado en texto como tamaño de fuente, estilo de fuente y color de fuente, etc. Para agregar texto en el pie de página, necesitas crear un objeto Document y un objeto TextStamp usando las propiedades requeridas. Después de eso, puedes llamar al método addStamp de la Página para agregar el texto en el pie de página del PDF.

El siguiente fragmento de código te muestra cómo agregar texto en el pie de página de un archivo PDF con PHP.

```php

    // Abrir documento
    $document = new Document($inputFile);

    // Crear encabezado
    $textStamp = new TextStamp("Texto del Encabezado");
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // Establecer propiedades del sello
    $textStamp->setBottomMargin(10);
    $textStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $textStamp->setVerticalAlignment($verticalAlignment->Bottom);

    $pages = $document->getPages();

    // Agregar pie de página en la 1ra página
    $page = $pages->get_Item(1);
    $page->addStamp($textStamp);
    
    // Guardar documento de salida
    $document->save($outputFile);
    $document->close();
```


## Añadiendo Imagen en el Encabezado del Archivo PDF

Puede usar la clase [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp) para agregar una imagen en el encabezado de un archivo PDF. La clase Image Stamp proporciona las propiedades necesarias para crear un sello basado en imagen como el tamaño de fuente, estilo de fuente, y color de fuente, etc. Para agregar una imagen en el encabezado, necesita crear un objeto Document y un objeto Image Stamp usando las propiedades requeridas. Después de eso, puede llamar al método [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) de la Página para agregar la imagen en el encabezado del PDF.

```php

    // Abrir documento
    $document = new Document($inputFile);
    
    // Crear pie de página
    $imageStamp = new ImageStamp($inputImage);
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // Establecer propiedades del sello
    $imageStamp->setTopMargin(10);
    $imageStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $imageStamp->setVerticalAlignment($verticalAlignment->Top);

    $pages = $document->getPages();

    // Agregar pie de página a la 1ra página
    $page = $pages->get_Item(1);
    $page->addStamp($imageStamp);

    // Guardar documento de salida
    $document->save($outputFile);
    $document->close();
```


El siguiente fragmento de código te muestra cómo agregar una imagen en el encabezado de un archivo PDF con PHP.

## Agregar Imagen en el Pie de Página de un Archivo PDF

Puedes usar la clase Image Stamp para agregar una imagen en el pie de página de un archivo PDF. La clase Image Stamp proporciona las propiedades necesarias para crear un sello basado en imagen como el tamaño de la fuente, el estilo de la fuente y el color de la fuente, etc. Para agregar una imagen en el pie de página, necesitas crear un objeto Document y un objeto Image Stamp usando las propiedades requeridas. Después de eso, puedes llamar al método AddStamp de la página para agregar la imagen en el pie de página del PDF.

{{% alert color="primary" %}}

Necesitas ajustar la propiedad BottomMargin de tal manera que ajuste la imagen en el área del pie de página de tu PDF. También necesitas establecer [HorizontalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/HorizontalAlignment) en `Center` y [VerticalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/VerticalAlignment) en `Bottom`.

{{% /alert %}}

El siguiente fragmento de código te muestra cómo agregar una imagen en el pie de página de un archivo PDF con PHP.

```php

    // Abrir documento
    $document = new Document($inputFile);
    
    // Crear pie de página
    $imageStamp = new ImageStamp($inputImage);
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // Establecer propiedades del sello
    $imageStamp->setBottomMargin(10);
    $imageStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $imageStamp->setVerticalAlignment($verticalAlignment->Bottom);

    $pages = $document->getPages();

    // Agregar pie de página a la primera página
    $page = $pages->get_Item(1);
    $page->addStamp($imageStamp);

    // Guardar documento de salida
    $document->save($outputFile);
    $document->close();
```

## Agregar diferentes encabezados en un archivo PDF

Sabemos que podemos agregar TextStamp en la sección de Encabezado/Pie de página del documento usando las propiedades TopMargin o Bottom Margin, pero a veces podemos tener el requisito de agregar múltiples encabezados/pies de página en un solo documento PDF. **Aspose.PDF para PHP a través de Java** explica cómo hacer esto.

Para cumplir con este requisito, crearemos objetos [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) individuales (el número de objetos depende de la cantidad de encabezados/pies de página requeridos) y los agregaremos al documento PDF.

 Podemos especificar también información de formato diferente para cada objeto de sello individual. En el siguiente ejemplo, hemos creado un objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) y tres objetos [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) y luego hemos utilizado el método [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) de la Página para añadir el texto en la sección del encabezado del PDF. El siguiente fragmento de código te muestra cómo añadir una imagen en el pie de un archivo PDF con Aspose.PDF para PHP a través de Java.

```php

    // Abrir documento
    $document = new Document($inputFile);

    // Crear tres sellos
    $stamp1 = new TextStamp("Header 1");
    $stamp2 = new TextStamp("Header 2");
    $stamp3 = new TextStamp("Header 3");
    
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();
    $fontStyles = new FontStyles();

    // Establecer alineación del sello (colocar sello en la parte superior de la página, centrado horizontalmente)
    $stamp1->setVerticalAlignment ($verticalAlignment->Top);
    $stamp1->setHorizontalAlignment($horizontalAlignment->Center);

    // Especificar el estilo de fuente como Negrita
    $stamp1->getTextState()->setFontStyle($fontStyles->Bold);
    // Establecer la información del color de primer plano del texto como rojo
    $stamp1->getTextState()->setForegroundColor((new Color())->getRed());
    // Especificar el tamaño de fuente como 14
    $stamp1->getTextState()->setFontSize(14);

    // Ahora necesitamos establecer la alineación vertical del segundo objeto de sello como Superior
    $stamp2->setVerticalAlignment($verticalAlignment->Top);
    // Establecer la información de alineación horizontal para el sello como Centro
    $stamp2->setHorizontalAlignment($horizontalAlignment->Center);
    // Establecer el factor de zoom para el objeto de sello
    $stamp2->setZoom(10);

    // Establecer el formato del tercer objeto de sello
    // Especificar la información de alineación vertical para el objeto de sello como SUPERIOR
    $stamp3->setVerticalAlignment($verticalAlignment->Top);
    // Establecer la información de alineación horizontal para el objeto de sello como Centro
    $stamp3->setHorizontalAlignment ($horizontalAlignment->Center);
    // Establecer el ángulo de rotación para el objeto de sello
    $stamp3->setRotateAngle(35);
    // Establecer rosa como color de fondo para el sello
    $stamp3->getTextState()->setBackgroundColor ((new Color())->getPink());  
    // Cambiar la información de tipo de letra para el sello a Verdana
    $stamp3->getTextState()->setFont ((new FontRepository())->findFont("Verdana"));

    // El primer sello se añade en la primera página;
    $document->getPages()->get_Item(1)->addStamp($stamp1);
    // El segundo sello se añade en la segunda página;
    $document->getPages()->get_Item(2)->addStamp($stamp2);
    // El tercer sello se añade en la tercera página.
    $document->getPages()->get_Item(3)->addStamp($stamp3);
    
    // Guardar documento de salida
    $document->save($outputFile);
    $document->close();
```