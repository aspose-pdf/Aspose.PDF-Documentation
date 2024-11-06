---
title: Anotaciones Adhesivas en PDF
linktitle: Anotación Adhesiva
type: docs
weight: 50
url: es/php-java/sticky-annotations/
description: Este tema trata sobre anotaciones adhesivas, como ejemplo mostramos la Anotación de Marca de Agua en el texto. Se usa para representar gráficos en la página. Consulte el fragmento de código para resolver esta tarea.
lastmod: "2024-06-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Añadir Anotación de Marca de Agua

Una anotación de marca de agua se utilizará para representar gráficos que se imprimirán en un tamaño y posición fijos en una página, independientemente de las dimensiones de la página impresa.

Puede añadir texto de marca de agua usando [WatermarkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/WatermarkAnnotation) en una posición específica de la página PDF. La opacidad de la marca de agua también se puede controlar utilizando la propiedad de opacidad.

Por favor, consulte el siguiente fragmento de código para añadir WatermarkAnnotation.

```php

    // Abrir documento
    $document = new Document($inputFile);
    $fontRepository = new FontRepository();
    $colors = new Color();
    // obtener página en particular
    $page = $document->getPages()->get_Item(1);
    
    //Crear Anotación
    $wa = new WatermarkAnnotation($page, new Rectangle(100, 500, 400, 600));

    //Añadir anotación a la colección de anotaciones de la página
    $page->getAnnotations()->add($wa);

    //Crear TextState para configuraciones de fuente
    $ts = new TextState();

    $ts->setForegroundColor($colors->getBlue());
    $ts->setFont($fontRepository->findFont("Times New Roman"));
    $ts->setFontSize(32);

    //Establecer nivel de opacidad del texto de la anotación
    $wa->setOpacity(0.5);
            
    $watermarkStrings = ["Aspose.PDF", "Marca de Agua", "Demo"];
    //Añadir texto a la anotación
    $wa->setTextAndState($watermarkStrings, $ts);

    // Guardar el documento PDF resultante.
    $document->save($outputFile);
    $document->close();
```