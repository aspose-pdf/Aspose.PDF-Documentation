---
title: Diviser un fichier PDF en pages individuelles en PHP
linktitle: Diviser un fichier PDF en pages individuelles en PHP
type: docs
weight: 80
url: /java/split-pdf-file-into-individual-pages-in-php/
description: Découvrez comment diviser un document PDF en pages individuelles à l'aide de PHP et Aspose.PDF pour une extraction de page efficace.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Pages divisées



Pour diviser un document PDF en pages individuelles à l'aide de **Aspose.PDF Java pour PHP**, invoquez simplement la classe **SplitAllPages**.

Code PHP


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


**Télécharger le code d'exécution**



Téléchargez **Split Pages (Aspose.PDF)**В à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/SplitAllPages.php)
