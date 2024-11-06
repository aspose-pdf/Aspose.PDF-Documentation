---
title: Extraer Datos de Tabla de PDF 
linktitle: Extraer Datos de Tabla
type: docs
weight: 40
url: es/php-java/extract-data-from-table-in-pdf/
description: Aprende cómo extraer tablas de PDF usando Aspose.PDF para PHP
lastmod: "2021-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraer Tablas de PDF programáticamente

Extraer tablas de PDF no es una tarea trivial porque la tabla puede ser creada de diversas maneras.

Aspose.PDF para PHP vía Java tiene una herramienta para facilitar la recuperación de tablas. Para extraer datos de tabla, debe realizar los siguientes pasos:

1. Abrir el documento PDF - instanciar un objeto [Document](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/Document);
1. Crear un objeto TableAbsorber [TableAbsorber](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/tableabsorber) para extraer tablas del documento.
1. Iterar a través de cada página del documento.

1. Decida qué páginas se analizarán y aplique [visit](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TableAbsorber#visit-com.aspose.pdf.Page-) a las páginas deseadas. Los datos tabulares serán escaneados y el resultado se guardará en una lista de [AbsorbedTable](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedTable). Podemos obtener esta lista a través del método [getTableList](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TableAbsorber#getTableList--).

2. Para obtener los datos, itere a través de `TableList` y maneje la lista de [filas absorbidas](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedRow) y la lista de celdas absorbidas. Podemos acceder a la primera lista llamando al método [getTableList](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TableAbsorber#getTableList--) y a la segunda llamando al método [getCellList](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedRow#getCellList--).

1. Cada [AbsorbedCell](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedCell) contiene [TextFragmentCollections](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TextFragmentCollection). Puedes procesarlo para tus propios fines.

El siguiente ejemplo muestra la extracción de una tabla de todas las páginas:

```php

$document = new Document($inputFile);
$tableAbsorber = new TableAbsorber();


for ($pageIndex = 1; $pageIndex <= java_values($pages->size()); $pageIndex++) {
    $page = $pages->get_Item($pageIndex);
    $tableAbsorber->visit($page);
    $tableList = $tableAbsorber->getTableList();
    $tableIterator = $tableList->iterator();

    while (java_values($tableIterator->hasNext())) {
        $table = $tableIterator->next();
        $tableRowList = $table->getRowList();
        $tableRowListIterator = $tableRowList->iterator();

        while (java_values($tableRowListIterator->hasNext())) {
            $row = $tableRowListIterator->next();
            $cellList = $row->getCellList();
            $cellListIterator = $cellList->iterator();

            // Iterar a través de cada celda en la fila.
            while (java_values($cellListIterator->hasNext())) {
                $cell = $cellListIterator->next();
                $fragmentList = $cell->getTextFragments();

                // Iterar a través de cada fragmento de texto en la celda.
                for ($fragmentIndex = 1; $fragmentIndex <= java_values($fragmentList->size()); $fragmentIndex++) {
                    $fragment = $fragmentList->get_Item($fragmentIndex);
                    $segments = $fragment->getSegments();

                    // Iterar a través de cada segmento en el fragmento de texto.
                    for ($segmentIndex = 1; $segmentIndex <= java_values($segments->size()); $segmentIndex++) {
                        $segment = $segments->get_Item($segmentIndex);
                        $responseData .= $segment->getText();
                    }
                }
                $responseData .= "|";
            }
            $responseData .= PHP_EOL;
        }
    }
}

// Guardar los datos de la tabla en el archivo de salida.
file_put_contents($outputFile, $responseData);

// Cerrar el documento PDF.
$document->close();
```


## Extraer datos de tabla de PDF y almacenarlos en un archivo CSV

El siguiente ejemplo muestra cómo extraer una tabla y almacenarla como un archivo CSV. Para ver cómo convertir PDF a hoja de cálculo de Excel, por favor consulte el artículo [Convertir PDF a Excel](/pdf/php-java/convert-pdf-to-excel/).

```php

    // Cargar el documento PDF de entrada usando la clase Document.
    $document = new Document($inputFile);

    // Crear una instancia de la clase ExcelSaveOptions para especificar las opciones de guardado.
    $saveOption = new ExcelSaveOptions();

    // Establecer el formato de salida a CSV.
    $saveOption->setFormat(ExcelSaveOptions_ExcelFormat::$CSV);

    // Guardar el documento PDF como un archivo de Excel usando las opciones de guardado especificadas.
    $document->save($outputFile, $saveOption);
```