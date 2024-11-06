---
title: Actualizar Dimensiones de Página en PHP
type: docs
weight: 90
url: es/java/update-page-dimensions-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Actualizar Dimensiones de Página

Para actualizar las dimensiones de la página usando **Aspose.PDF Java para PHP**, simplemente invoque la clase **UpdatePageDimensions**.

Código PHP

```php

# Abre el documento objetivo
$pdf = new Document($dataDir . 'input1.pdf');

# obtener la colección de páginas
$page_collection = $pdf->getPages();

# obtener una página en particular
$pdf_page = $page_collection->get_Item(1);

# establecer el tamaño de la página como A4 (11.7 x 8.3 pulgadas) y en Aspose.PDF, 1 pulgada = 72 puntos
# por lo que las dimensiones en A4 en puntos serán (842.4, 597.6)
$pdf_page->setPageSize(597.6,842.4);

# guardar el archivo PDF recién generado
$pdf->save($dataDir . "output.pdf");

print "¡Dimensiones actualizadas con éxito!" . PHP_EOL;

```

**Descargar Código en Ejecución**

Descargue **Actualizar Dimensiones de Página (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/UpdatePageDimensions.php)