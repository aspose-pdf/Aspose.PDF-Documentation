---
title: Rellenar AcroForms
linktitle: Rellenar AcroForms
type: docs
weight: 20
url: /es/php-java/fill-form/
description: Esta sección explica cómo rellenar un campo de formulario en un documento PDF con Aspose.PDF para PHP vía Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Los documentos PDF son maravillosos, y realmente el tipo de archivo preferido, para crear formularios.

Aspose.PDF para PHP vía Java te permite rellenar un campo de formulario, obtener el campo de la colección de formularios del objeto Documento.

Veamos el siguiente ejemplo de cómo resolver esta tarea:

```php

    // Cargar formulario XFA
    $document = new Document($inputFile);
    
    // Obtener nombres de los campos del formulario XFA
    $names = $document->getForm()->getXFA()->getFieldNames();
        
    // Establecer valores de los campos        
    $document->getForm()->getXFA()->set_Item($names[0],"Campo 0");
    $document->getForm()->getXFA()->set_Item($names[1],"Campo 1");
        
    // Guardar el documento actualizado
    $document->save($outputFile);
    
    // Guardar el PDF modificado    
    $document->close();
```