---
title: Insira uma página vazia em um arquivo PDF em PHP
linktitle: Insira uma página vazia em um arquivo PDF em PHP
type: docs
weight: 70
url: /java/insert-an-empty-page-into-a-pdf-file-in-php/
description: Aprenda como inserir uma página vazia em qualquer posição dentro de um arquivo PDF em PHP usando Aspose.PDF para estruturação flexível de documentos.
lastmod: "2026-06-09"
---
## Aspose.PDF - Insira uma página vazia

Para inserir uma página vazia em um documento PDF usando **Aspose.PDF Java para PHP**, basta invocar a classe **InsertEmptyPage**.

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

**Baixar código em execução**

Baixe **Insira uma página vazia (Aspose.PDF)**Â de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPage.php)
