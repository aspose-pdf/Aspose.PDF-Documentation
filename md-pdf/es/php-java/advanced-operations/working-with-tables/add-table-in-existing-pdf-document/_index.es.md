---
title: Crear o Añadir Tabla en PDF 
linktitle: Crear o Añadir Tabla
type: docs
weight: 10
url: /php-java/add-table-in-existing-pdf-document/
description: Aprende cómo crear o añadir una tabla a un documento PDF, aplicando estilo a las celdas, dividiendo la tabla en páginas y personalizando las filas y columnas, etc.
lastmod: "2024-05-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Añadiendo Tabla en un Documento PDF Existente

Para añadir una tabla a un archivo PDF existente con Aspose.PDF para PHP, sigue los siguientes pasos:

1. Cargar el archivo fuente.
1. Inicializar una tabla
1. Establecer el color del borde de la tabla como Gris Claro
1. Establecer el borde para las celdas de la tabla
1. Crear un bucle para añadir 10 filas
1. Añadir el objeto tabla a la primera página del documento de entrada
1. Guardar el archivo.

Los siguientes fragmentos de código muestran cómo añadir texto en un archivo PDF existente.

```php

    // Abrir documento
    $document = new Document($inputFile);        
    // Inicializa una nueva instancia de la Tabla
    $table = new Table();
    $colors= new Color();
    // Establecer el color del borde de la tabla como Gris Claro
    $borderSide = new BorderSide();
    $borderInfo = new BorderInfo($borderSide->All, 0.5, $colors->getLightGray());
    $table->setBorder($borderInfo);
    // establecer el borde para las celdas de la tabla
    $table->setDefaultCellBorder($borderInfo);
    // crear un bucle para añadir 10 filas
    for ($row_count = 1; $row_count < 10; $row_count++) {
        // añadir fila a la tabla
        $row = $table->getRows()->add();
        // añadir celdas a la tabla
        $row->getCells()->add("Columna (" . $row_count . ", 1)");
        $row->getCells()->add("Columna (" . $row_count . ", 2)");
        $row->getCells()->add("Columna (" . $row_count . ", 3)");
    }
    // Añadir el objeto tabla a la primera página del documento de entrada
    $document->getPages()->add()->getParagraphs()->add($table);

    // Guardar el documento PDF resultante.    
    $document->save($outputFile);
    $document->close();
```