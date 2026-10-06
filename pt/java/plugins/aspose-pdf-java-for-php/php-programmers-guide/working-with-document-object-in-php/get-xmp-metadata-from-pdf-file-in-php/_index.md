---
title: Obter metadados XMP de arquivo PDF em PHP
linktitle: Obter metadados XMP de arquivo PDF em PHP
type: docs
weight: 50
url: /pt/java/get-xmp-metadata-from-pdf-file-in-php/
description: Aprenda a extrair metadados XMP de documentos PDF em PHP usando Aspose.PDF para análise avançada de conteúdo.
lastmod: "2026-10-06"
---
## Aspose.PDF - obter metadados XMP

Para obter Metadados XMP de um documento Pdf usando **Aspose.PDF Java for PHP**, basta invocar a classe **GetXMPMetadata**.

Código PHP

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get properties
print "xmp:CreateDate: " + $doc->getMetadata()->get_Item("xmp:CreateDate") . PHP_EOL;
print "xmp:Nickname: " + $doc->getMetadata()->get_Item("xmp:Nickname") . PHP_EOL;
print "xmp:CustomProperty: " + $doc->getMetadata()->get_Item("xmp:CustomProperty") . PHP_EOL;

```

**Baixar Código em Execução**

Baixar **Get XMP Metadata (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetXMPMetadata.php)
