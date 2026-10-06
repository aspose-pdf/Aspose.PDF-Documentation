---
title: Inserir uma página em branco no final do arquivo PDF em PHP
linktitle: Inserir uma página em branco no final do arquivo PDF em PHP
type: docs
weight: 60
url: /pt/java/insert-an-empty-page-at-end-of-pdf-file-in-php/
description: Aprenda como inserir uma página em branco no final de um documento PDF em PHP usando Aspose.PDF para expansão de documentos.
lastmod: "2026-10-06"
---
## Aspose.PDF - inserir uma página em branco no final do arquivo PDF

Para Inserir uma Página em Branco no final do documento PDF usando **Aspose.PDF Java for PHP**, basta invocar a classe **InsertEmptyPageAtEndOfFile**.

Código PHP

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# insert a empty page in a PDF
$pdf->getPages()->add();

# Save the concatenated output file (the target document)
$pdf->save($dataDir . "output.pdf");

print "Empty page added successfully!" . PHP_EOL;

```

## Baixar o exemplo de código

Baixar **Inserir uma Página Vazia ao Final do Arquivo PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPageAtEndOfFile.php)
