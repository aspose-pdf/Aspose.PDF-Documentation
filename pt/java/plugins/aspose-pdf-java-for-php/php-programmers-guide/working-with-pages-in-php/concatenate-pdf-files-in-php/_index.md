---
title: Concatenar arquivos PDF em PHP
linktitle: Concatenar arquivos PDF em PHP
type: docs
weight: 10
url: /pt/java/concatenate-pdf-files-in-php/
description: Aprenda a concatenar vários arquivos PDF em um único documento em PHP usando Aspose.PDF para facilitar o gerenciamento de documentos.
lastmod: "2026-10-06"
---
## Aspose.PDF - concatenar arquivos PDF

Para concatenar arquivos PDF usando **Aspose.PDF Java for PHP**, basta invocar a classe **ConcatenatePdfFiles**.

Código PHP

```php

# Open the target document
$pdf1 = new Document($dataDir . 'input1.pdf');

# Open the source document
$pdf2 = new Document($dataDir . 'input2.pdf');

# Add the pages of the source document to the target document
$pdf1->getPages()->add($pdf2->getPages());

# Save the concatenated output file (the target document)
$pdf1->save($dataDir . "Concatenate_output.pdf");

print "New document has been saved, please check the output file" . PHP_EOL;

```

**Baixar Código em Execução**

Baixe **Concatenate PDF Files (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/ConcatenatePdfFiles.php)
