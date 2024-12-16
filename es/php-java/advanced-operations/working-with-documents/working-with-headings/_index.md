---
title: Trabajando con Encabezados en PDF
type: docs
weight: 70
url: /es/php-java/working-with-headings/
lastmod: "2024-06-05"
description: Crea numeración en el encabezado de tu documento PDF usando PHP. Aspose.PDF para PHP vía Java ofrece diferentes tipos de estilos de numeración.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Aplicar Estilo de Numeración en Encabezado

Los encabezados son las partes importantes de cualquier documento. Los escritores siempre intentan hacer que los encabezados sean más prominentes y significativos para sus lectores. Si hay más de un encabezado en un documento, un escritor tiene varias opciones para organizar estos encabezados. Uno de los enfoques más comunes para organizar encabezados es escribirlos en Estilo de Numeración.

Aspose.PDF para PHP vía Java ofrece muchos estilos de numeración predefinidos. Estos estilos de numeración predefinidos se almacenan en una enumeración, NumberingStyle. Los valores predefinidos de la enumeración NumberingStyle y sus descripciones se dan a continuación:

|**Tipos de Encabezado**|**Descripción**|
| :- | :- |

|NumeralsArabic|Tipo árabe, por ejemplo, 1,1.1,...|
|NumeralsRomanUppercase|Tipo romano mayúsculas, por ejemplo, I,I.II, ...|
|NumeralsRomanLowercase|Tipo romano minúsculas, por ejemplo, i,i.ii, ...|
|LettersUppercase|Tipo inglés mayúsculas, por ejemplo, A,A.B, ...|
|LettersLowercase|Tipo inglés minúsculas, por ejemplo, a,a.b, ...|
La propiedad [setStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) de la clase [com.aspose.pdf.Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) se utiliza para establecer los estilos de numeración de los encabezados.

El código fuente, para obtener la salida mostrada en la figura anterior, se proporciona a continuación en el ejemplo.

```php

    // Abrir documento
    $document = new Document($inputFile);
    $document->getPageInfo()->setWidth(612.0);
    $document->getPageInfo()->setHeight(792.0);
    $document->getPageInfo()->setMargin(new MarginInfo());
    $document->getPageInfo()->getMargin()->setLeft(72);
    $document->getPageInfo()->getMargin()->setRight(72);
    $document->getPageInfo()->getMargin()->setTop(72);
    $document->getPageInfo()->getMargin()->setBottom(72);

    $page = $document->getPages()->add();
    $page->getPageInfo()->setWidth(612.0);
    $page->getPageInfo()->setHeight(792.0);
    $document->getPageInfo()->setMargin(new MarginInfo());
    $document->getPageInfo()->getMargin()->setLeft(72);
    $document->getPageInfo()->getMargin()->setRight(72);
    $document->getPageInfo()->getMargin()->setTop(72);
    $document->getPageInfo()->getMargin()->setBottom(72);

    $floatBox = new FloatingBox();
    $floatBox->setMargin($page->getPageInfo()->getMargin());

    $page->getParagraphs()->add($floatBox);

    $heading = new Heading(1);
    $heading->setInList(true);
    $heading->setStartNumber(1);
    $heading->setText("Lista 1");
    $heading->setStyle(NumberingStyle::$NumeralsRomanLowercase);
    $heading->setAutoSequence(true);

    $floatBox->getParagraphs()->add($heading);
    $heading2 = new Heading(1);
    $heading2->setInList(true);
    $heading2->setStartNumber(13);
    $heading2->setText("Lista 2");
    $heading2->setStyle(NumberingStyle::$NumeralsRomanLowercase);
    $heading2->setAutoSequence(true);

    $floatBox->getParagraphs()->add($heading2);

    $heading3 = new Heading(2);
    $heading3->setInList(true);
    $heading3->setStartNumber(1);
    $heading3->setText("el valor, a partir de la fecha de vigencia del plan, de la propiedad que se distribuirá bajo el plan en razón de cada permitido");
    $heading3->setStyle (NumberingStyle::$LettersLowercase);
    $heading3->setAutoSequence(true);

    $floatBox->getParagraphs()->add($heading3);
    
    $document->save($outputFile);
    $document->close();
```