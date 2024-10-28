---
title: Obter Metadados XMP de Arquivo PDF em PHP
type: docs
weight: 50
url: /java/get-xmp-metadata-from-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obter Metadados XMP

Para obter metadados XMP de um documento PDF usando **Aspose.PDF Java for PHP**, basta invocar a classe **GetXMPMetadata**.

Código PHP

```php

# Abra um documento PDF.
$doc = new Document($dataDir . "input1.pdf");

# Obter propriedades
print "xmp:CreateDate: " + $doc->getMetadata()->get_Item("xmp:CreateDate") . PHP_EOL;
print "xmp:Nickname: " + $doc->getMetadata()->get_Item("xmp:Nickname") . PHP_EOL;
print "xmp:CustomProperty: " + $doc->getMetadata()->get_Item("xmp:CustomProperty") . PHP_EOL;

```

**Baixar Código em Execução**

Baixar **Obter Metadados XMP (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetXMPMetadata.php)