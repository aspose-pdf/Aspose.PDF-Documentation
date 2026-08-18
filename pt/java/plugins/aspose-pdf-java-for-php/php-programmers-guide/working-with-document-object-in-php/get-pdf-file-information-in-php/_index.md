---
title: Obtenha informações do arquivo PDF em PHP
linktitle: Obtenha informações do arquivo PDF em PHP
type: docs
weight: 40
url: /java/get-pdf-file-information-in-php/
description: Descubra como recuperar informações detalhadas sobre um arquivo PDF, incluindo metadados e propriedades, em PHP com Aspose.PDF.
lastmod: "2026-06-09"
---
## Aspose.PDF - Obtenha informações do arquivo PDF

Para obter informações do arquivo do documento PDF usando **Aspose.PDF Java para PHP**, basta invocar a classe **GetPdfFileInfo**.

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

**Baixar código em execução**

Baixe ** Obtenha informações do arquivo PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetPdfFileInfo.php)
