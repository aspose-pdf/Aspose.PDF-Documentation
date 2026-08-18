---
title: Divida o arquivo PDF em páginas individuais em PHP
linktitle: Divida o arquivo PDF em páginas individuais em PHP
type: docs
weight: 80
url: /java/split-pdf-file-into-individual-pages-in-php/
description: Descubra como dividir um documento PDF em páginas individuais usando PHP e Aspose.PDF para extração eficiente de páginas.
lastmod: "2026-06-09"
---
## Aspose.PDF - Dividir páginas

Para dividir um documento PDF em páginas individuais usando **Aspose.PDF Java para PHP**, basta invocar a classe **SplitAllPages**.

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

**Baixar código em execução**

Baixe **Split Pages (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/SplitAllPages.php)
