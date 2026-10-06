---
title: Atualizar dimensões da página em PHP
linktitle: Atualizar dimensões da página em PHP
type: docs
weight: 90
url: /pt/java/update-page-dimensions-in-php/
description: Aprenda como modificar as dimensões da página em um documento PDF em PHP usando Aspose.PDF para melhor controle de layout.
lastmod: "2026-10-06"
---
## Aspose.PDF - Atualizar dimensões da página

Para atualizar as dimensões da página usando **Aspose.PDF Java for PHP**, basta invocar a classe **UpdatePageDimensions**.

Código PHP

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# get page collection
$page_collection = $pdf->getPages();

# get particular page
$pdf_page = $page_collection->get_Item(1);

# set the page size as A4 (11.7 x 8.3 in) and in Aspose.PDF, 1 inch = 72 points
# so A4 dimensions in points will be (842.4, 597.6)
$pdf_page->setPageSize(597.6,842.4);

# save the newly generated PDF file
$pdf->save($dataDir . "output.pdf");

print "Dimensions updated successfully!" . PHP_EOL;

```

**Baixar Código em Execução**

Baixar\u0412\u00A0**Atualizar Dimensões da Página (Aspose.PDF)**\u0412\u00A0de\u0412\u00A0qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/UpdatePageDimensions.php)
