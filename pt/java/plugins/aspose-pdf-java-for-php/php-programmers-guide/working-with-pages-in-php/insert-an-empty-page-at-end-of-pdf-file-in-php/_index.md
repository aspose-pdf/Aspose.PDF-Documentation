---
title: Insira uma página vazia no final do arquivo PDF em PHP
linktitle: Insira uma página vazia no final do arquivo PDF em PHP
type: docs
weight: 60
url: /java/insert-an-empty-page-at-end-of-pdf-file-in-php/
description: Aprenda como inserir uma página vazia no final de um documento PDF em PHP usando Aspose.PDF para expansão do documento.
lastmod: "2026-06-09"
---
## Aspose.PDF - Insira uma página vazia no final do arquivo PDF

Para inserir uma página vazia no final do documento PDF usando **Aspose.PDF Java para PHP**, basta invocar a classe **InsertEmptyPageAtEndOfFile**.

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

## Baixar código em execução

Baixe **Inserir uma página vazia no final do arquivo PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPageAtEndOfFile.php)
