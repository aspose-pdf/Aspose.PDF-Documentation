---
title: Eliminar páginas de PDF programáticamente 
linktitle: Eliminar páginas de PDF
type: docs
weight: 40
url: /es/php-java/delete-pages/
description: Puede eliminar páginas de su archivo PDF usando PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Eliminar página de archivo PDF

1. Llame al método de eliminación y especifique el índice de la página
1. Llame al método de guardar para guardar el archivo PDF actualizado
El siguiente fragmento de código muestra cómo eliminar una página en particular del archivo PDF usando PHP.

```php

    // Abrir documento
    $document = new Document($inputFile);      

    $pages = $document->getPages();

    // Eliminar una página en particular
    $pages->delete(2);

    // Guardar documento de salida
    $document->save($outputFile);
    $document->close();
```