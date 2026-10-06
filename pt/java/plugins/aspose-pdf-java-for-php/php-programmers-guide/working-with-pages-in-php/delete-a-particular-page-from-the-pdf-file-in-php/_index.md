---
title: Excluir uma página específica do arquivo PDF em PHP
linktitle: Excluir uma página específica do arquivo PDF em PHP
type: docs
weight: 20
url: /pt/java/delete-a-particular-page-from-the-pdf-file-in-php/
description: Explore como excluir uma página específica de um documento PDF em PHP com Aspose.PDF, simplificando a edição de documentos.
lastmod: "2026-10-06"
---
## Aspose.PDF - Excluir página

Para excluir uma página específica do documento PDF usando **Aspose.PDF Java for PHP**, basta invocar a classe **DeletePage**.

Código PHP

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# delete a particular page
$pdf->getPages()->delete(2);

# save the newly generated PDF file
$pdf->save($dataDir . "output.pdf");

print "Page deleted successfully!";

```

**Download em execução**

Baixar **Delete Page (Aspose.PDF)**В deВ qualquer dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/DeletePage.php)
