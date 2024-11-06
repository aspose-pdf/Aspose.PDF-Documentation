---
title: Extraer Formulario XFA
linktitle: Extraer Formulario XFA
type: docs
weight: 30
url: es/php-java/extract-form/
description: Esta sección explica cómo extraer formularios de su documento PDF con Aspose.PDF para PHP a través de Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtener Valor de un Campo de Formulario del Documento PDF

El método [getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) del campo de formulario le permite obtener el valor de un campo en particular.

Para obtener el valor, obtenga el campo de formulario de la colección Form del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Este ejemplo selecciona un [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) y recupera su valor usando el método [getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```php

    // Cargar formulario XFA
    $document = new Document($inputFile);
    
    // Obtener nombres de los campos del formulario XFA
    $names = $document->getForm()->getXFA()->getFieldNames();
        
    // Obtener valores de los campos
    $document->getForm()->getXFA()->get_Item($names[0]);
    $document->getForm()->getXFA()->get_Item($names[1]);
    
    // Guardar PDF modificado    
    $document->close();
```