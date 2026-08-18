---
title: Obtenha metadados XMP de arquivo PDF em PHP
linktitle: Obtenha metadados XMP de arquivo PDF em PHP
type: docs
weight: 50
url: /java/get-xmp-metadata-from-pdf-file-in-php/
description: Aprenda como extrair metadados XMP de documentos PDF em PHP usando Aspose.PDF para análise avançada de conteúdo.
lastmod: "2026-06-09"
---
## Aspose.PDF - Obtenha metadados XMP

Para obter metadados XMP de um documento PDF usando **Aspose.PDF Java para PHP**, basta invocar a classe **GetXMPMetadata**.

Código PHP

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get properties
print "xmp:CreateDate: " + $doc->getMetadata()->get_Item("xmp:CreateDate") . PHP_EOL;
print "xmp:Nickname: " + $doc->getMetadata()->get_Item("xmp:Nickname") . PHP_EOL;
print "xmp:CustomProperty: " + $doc->getMetadata()->get_Item("xmp:CustomProperty") . PHP_EOL;

```

**Baixar código em execução**

Baixe **Obtenha metadados XMP (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetXMPMetadata.php)
