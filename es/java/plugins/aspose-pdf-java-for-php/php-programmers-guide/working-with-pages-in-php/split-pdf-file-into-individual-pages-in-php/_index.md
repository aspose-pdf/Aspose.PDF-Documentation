---
title: Dividir un archivo PDF en páginas individuales en PHP
linktitle: Dividir un archivo PDF en páginas individuales en PHP
type: docs
weight: 80
url: /java/split-pdf-file-into-individual-pages-in-php/
description: Descubra cómo dividir un documento PDF en páginas individuales usando PHP y Aspose.PDF para una extracción de páginas eficiente.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Dividir páginas



Para dividir un documento PDF en páginas individuales usando **Aspose.PDF Java para PHP**, simplemente invoque la clase **SplitAllPages**.

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


**Descargar código de ejecución**



Descargue **Split Pages (Aspose.PDF)** de cualquiera de los sitios de codificación social mencionados a continuación:


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/SplitAllPages.php)
