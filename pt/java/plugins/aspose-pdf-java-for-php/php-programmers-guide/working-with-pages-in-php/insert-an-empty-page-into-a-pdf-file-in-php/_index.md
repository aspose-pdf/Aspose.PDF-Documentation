---
title: Inserir uma página vazia em um arquivo PDF em PHP
linktitle: Inserir uma página vazia em um arquivo PDF em PHP
type: docs
weight: 70
url: /pt/java/insert-an-empty-page-into-a-pdf-file-in-php/
description: Aprenda como inserir uma página vazia em qualquer posição dentro de um arquivo PDF em PHP usando Aspose.PDF para estruturação flexível de documentos.
lastmod: "2026-10-06"
---
## Aspose.PDF - inserir uma página vazia

Para inserir uma página vazia em um documento Pdf usando **Aspose.PDF Java for PHP**, basta invocar a classe **InsertEmptyPage**.

Código PHP

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# insert a empty page in a PDF
$pdf->getPages()->insert(1);

# Save the concatenated output file (the target document)
$pdf->save($dataDir . "output.pdf");

print "Empty page added successfully!";

```

**Baixar Código em Execução**

Baixar **Inserir uma Página Vazia (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPage.php)
