---
title: Dividir archivo PDF en páginas individuales con PHP
linktitle: Dividir archivo PDF en páginas individuales con PHP
type: docs
weight: 80
url: /es/java/split-pdf-file-into-individual-pages-in-php/
description: Descubra cómo dividir un documento PDF en páginas individuales usando PHP y Aspose.PDF para una extracción eficiente de páginas.
lastmod: "2026-09-03"
---
## Aspose.PDF - Dividir páginas

Para dividir un documento PDF en páginas individuales usando **Aspose.PDF Java for PHP**, simplemente invoque la clase **SplitAllPages**.

Código PHP

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# loop through all the pages
$pdf_page = 1;
$total_size = $pdf->getPages()->size();
#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)
while ($pdf_page <= $total_size)

{

    # create a new Document object
    $new_document = new Document();

    # get the page at particular index of Page Collection
    $new_document->getPages()->add($pdf->getPages()->get_Item($pdf_page));

    # save the newly generated PDF file
    $new_document->save($dataDir . "page_#{$pdf_page}.pdf");

    $pdf_page++;

}

print "Split process completed successfully!";

```

**Descargar Código en Ejecución**

Descargar **Split Pages (Aspose.PDF)** de cualquier de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/SplitAllPages.php)
