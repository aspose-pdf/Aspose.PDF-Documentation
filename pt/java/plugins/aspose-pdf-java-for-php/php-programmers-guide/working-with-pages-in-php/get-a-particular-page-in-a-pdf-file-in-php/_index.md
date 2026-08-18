---
title: Obtenha uma página específica em um arquivo PDF em PHP
linktitle: Obtenha uma página específica em um arquivo PDF em PHP
type: docs
weight: 30
url: /java/get-a-particular-page-in-a-pdf-file-in-php/
description: Aprenda como recuperar uma página específica de um arquivo PDF em PHP usando Aspose.PDF para processamento de página direcionado.
lastmod: "2026-06-09"
---
## Aspose.PDF - Obter página

Para obter uma página específica em um documento PDF usando **Aspose.PDF Java para Ruby**, basta invocar a classe **GetPage**.

Código Ruby

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# get the page at particular index of Page Collection
$pdf_page = $pdf->getPages()->get_Item(1);

# create a new Document object
$new_document = new Document();

# add page to pages collection of new document object
$new_document->getPages()->add($pdf_page);

# save the newly generated PDF file
$new_document->save($dataDir . "output.pdf");

print "Process completed successfully!";

```

## Baixar código em execução

Baixe **Get Page (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetPage.php)
