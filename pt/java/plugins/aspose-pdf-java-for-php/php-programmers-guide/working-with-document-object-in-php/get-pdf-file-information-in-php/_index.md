---
title: Obter informações do arquivo PDF em PHP
linktitle: Obter informações do arquivo PDF em PHP
type: docs
weight: 40
url: /pt/java/get-pdf-file-information-in-php/
description: Descubra como recuperar informações detalhadas sobre um arquivo PDF, incluindo metadados e propriedades, em PHP com Aspose.PDF.
lastmod: "2026-10-06"
---
## Aspose.PDF - Obter informações do PDF

Para obter informações do arquivo de documento PDF usando **Aspose.PDF Java for PHP**, basta invocar a classe **GetPdfFileInfo**.

Código PHP

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get document information
$doc_info = $doc->getInfo();

# Show document information
print "Author:-" . $doc_info->getAuthor();
print "Creation Date:-" . $doc_info->getCreationDate();
print "Keywords:-" . $doc_info->getKeywords();
print "Modify Date:-" . $doc_info->getModDate();
print "Subject:-" . $doc_info->getSubject();
print "Title:-" . $doc_info->getTitle();

```

**Baixar Código em Execução**

DownloadВ **Obter informações do arquivo PDF (Aspose.PDF)**В deВ qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetPdfFileInfo.php)
