---
title: Fill AcroForms
linktitle: Fill AcroForms
type: docs
weight: 20
url: es/php-java/fill-form/
description: Esta sección explica cómo rellenar un campo de formulario en un documento PDF con Aspose.PDF para PHP a través de Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Los documentos PDF son maravillosos, y realmente el tipo de archivo preferido, para crear Formularios.

Aspose.PDF para PHP a través de Java te permite rellenar un campo de formulario, obtener el campo de la colección de Formularios del objeto Documento.

Veamos el siguiente ejemplo de cómo resolver esta tarea:

```php

    // Abrir documento
    $document = new Document($inputFile);
    $page = $document->getPages()->get_Item(1);
    
    // Obtener un campo    
    $textBoxField = $document->getForm()->get("textbox1");

    // Modificar el valor del campo
    $textBoxField->setValue("Valor a ser llenado en el campo");
        
    // Guardar documento actualizado
    $document->save($outputFile);
    $document->close();
```