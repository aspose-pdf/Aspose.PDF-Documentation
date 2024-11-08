---
title: Añadir sellos de imagen en PDF programáticamente
linktitle: Sellos de imagen en archivo PDF
type: docs
weight: 10
url: /es/php-java/image-stamps-in-pdf-page/
description: Añade el sello de imagen en tu documento PDF usando la clase ImageStamp con la biblioteca Aspose.PDF para PHP vía Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Añadir sello de imagen en archivo PDF

Puedes usar la clase [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) para añadir una imagen como sello en un documento PDF. La clase [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) proporciona métodos para especificar altura, ancho y opacidad, etc.

Para añadir un sello de imagen:

1. Crea un objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) y un objeto ImageStamp usando las propiedades requeridas.

1. Llama al método [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) de la clase [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) para añadir el sello al PDF.

El siguiente fragmento de código muestra cómo añadir un sello de imagen en el archivo PDF.

```php

    // Abrir documento
    $document = new Document($inputFile);        
    $pages = $document->getPages();
  
    // Crear sello de imagen
    $imageStamp = new ImageStamp($inputImageFile);
    $imageStamp->setBackground(true);
    $imageStamp->setXIndent(100);
    $imageStamp->setYIndent(100);
    $imageStamp->setHeight(48);
    $imageStamp->setWidth(225);
    $imageStamp->setRotate((new Rotation())->getOn270());
    $imageStamp->setOpacity(0.5);

    // Añadir el sello a una página en particular
    $document->getPages()->get_Item(1)->addStamp($imageStamp);

    // Guardar documento de salida
    $document->save($outputFile);
    $document->close()
```

## Controlar la Calidad de la Imagen al Añadir el Sello

La clase [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) te permite añadir una imagen como sello en un documento PDF.
 También le permite controlar la calidad de la imagen al agregar una imagen como marca de agua en un archivo PDF. Para permitir esto, se ha añadido un método llamado setQuality(...) a la clase [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp). Un método similar también se puede encontrar en la clase [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/Stamp) del paquete com.aspose.pdf.facades.

El siguiente fragmento de código le muestra cómo controlar la calidad de la imagen al agregarla como sello en el archivo PDF.

```php

    // Abrir documento
    $document = new Document($inputFile);        
    $pages = $document->getPages();

    // Crear sello de imagen
    $imageStamp = new ImageStamp($inputImageFile);
    $imageStamp->setQuality(10);

    $document->getPages()->get_Item(1)->addStamp($imageStamp);

    // Guardar documento de salida
    $document->save($outputFile);
    $document->close();        
```

## Sello de Imagen como Fondo en Caja Flotante

La API Aspose.PDF le permite agregar un sello de imagen como fondo en una caja flotante. La propiedad BackgroundImage de la clase FloatingBox se puede usar para establecer la imagen de fondo para un cuadro flotante como se muestra en el siguiente ejemplo de código.

Este fragmento de código demuestra el proceso de creación de un documento PDF y la adición de un FloatingBox. El FloatingBox contiene un fragmento de texto, un borde, una imagen de fondo y un color de fondo. El documento resultante se guarda en un archivo de salida.

```php

    // Abrir documento
    $document = new Document($inputFile);
    $colors = new Color();
    $pages = $document->getPages();

    // Agregar página al documento PDF
    $page = $pages->add();

    // Crear objeto FloatingBox
    $aBox = new FloatingBox(200, 100);

    // Establecer la posición izquierda para FloatingBox
    $aBox->setLeft(40);

    // Establecer la posición superior para FloatingBox
    $aBox->setTop(80);

    // Establecer la alineación horizontal para FloatingBox
    $aBox->setHorizontalAlignment((new HorizontalAlignment())->getCenter());

    // Agregar fragmento de texto a la colección de párrafos de FloatingBox
    $aBox->getParagraphs()->add(new TextFragment("texto principal"));

    // Establecer borde para FloatingBox
    $aBox->setBorder(new BorderInfo(BorderSide::$All, $colors->getRed()));

    // Agregar imagen de fondo
    $img = new Image();
    $img->setFile($inputImageFile);
    $aBox->setBackgroundImage($img);

    // Establecer color de fondo para FloatingBox
    $aBox->setBackgroundColor($colors->getYellow());

    // Agregar FloatingBox a la colección de párrafos del objeto página
    $page->getParagraphs()->add($aBox);
    
    // Guardar documento de salida
    $document->save($outputFile);
    $document->close();
```