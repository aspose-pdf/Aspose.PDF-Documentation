---
title: Разделить PDF-файл на отдельные страницы в PHP
linktitle: Разделить PDF-файл на отдельные страницы в PHP
type: docs
weight: 80
url: /java/split-pdf-file-into-individual-pages-in-php/
description: Узнайте, как разделить PDF-документ на отдельные страницы с помощью PHP и Aspose.PDF для эффективного извлечения страниц.
lastmod: "2026-06-09"
---
## Aspose.PDF — Разделение страниц

Чтобы разделить PDF-документ на отдельные страницы с помощью **Aspose.PDF Java для PHP**, просто вызовите класс **SplitAllPages**.

PHP-код

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

**Загрузить рабочий код**

Загрузите **Split Pages (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/SplitAllPages.php)
