---
title: Remover metadados de PDF em PHP
linktitle: Remover metadados de PDF em PHP
type: docs
weight: 70
url: /pt/java/remove-metadata-from-pdf-in-php/
description: Explore como remover metadados de um documento PDF em PHP usando Aspose.PDF para melhorar a privacidade e a segurança do documento.
lastmod: "2026-10-06"
---
## Aspose.PDF - remover metadados

Para remover Metadados de um documento Pdf usando **Aspose.PDF Java for PHP**, basta invocar a classe **RemoveMetadata**.

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

**Baixar Código em Execução**

Baixe **Remove Metadata (Aspose.PDF)** de qualquer um dos sites de código social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/RemoveMetadata.php)
