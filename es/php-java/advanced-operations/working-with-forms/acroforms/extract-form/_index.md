---
title: Extraer Datos de AcroForms
linktitle: Extraer Datos de AcroForms
type: docs
weight: 30
url: es/php-java/extract-form/
description: Esta sección explica cómo extraer formularios de su documento PDF con Aspose.PDF para PHP a través de Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtener Valor de un Campo Individual del Documento PDF

El [método getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) del campo de formulario le permite obtener el valor de un campo particular.

Para obtener el valor, obtenga el campo de formulario de la colección Form del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Este ejemplo selecciona un [textBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) y recupera su valor utilizando el [método getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```php

    // Abrir un documento
    $document = new Document($inputFile);

    // Obtener un campo
    $textBoxField = $document->getForm()->get("textbox1");

    // Obtener el nombre del campo
    $responseData = "PartialName: " . $textBoxField->getPartialName();

    // Obtener el valor del campo
    $responseData = $responseData . " Value: " . $textBoxField->getValue();
    $document->close();
```