---
title: Remover metadados de PDF em PHP
linktitle: Remover metadados de PDF em PHP
type: docs
weight: 70
url: /java/remove-metadata-from-pdf-in-php/
description: Explore como remover metadados de um documento PDF em PHP usando Aspose.PDF para melhorar a privacidade e segurança do documento.
lastmod: "2026-06-09"
---
## Aspose.PDF - Remover metadados

Para remover metadados de um documento PDF usando **Aspose.PDF Java para PHP**, basta invocar a classe **RemoveMetadata**.

Código PHP

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

if (preg_match('/pdfaid:part/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("pdfaid:part");

}

if (preg_match('/dc:format/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("dc:format");

}

# save update document with new information
$doc->save($dataDir . "Remove_Metadata.pdf");

print "Removed metadata successfully, please check output file." . PHP_EOL;

```

**Baixar código em execução**

Baixe **Remover metadados (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/RemoveMetadata.php)
