---
title: Definir informações do arquivo PDF em PHP
linktitle: Definir informações do arquivo PDF em PHP
type: docs
weight: 90
url: /java/set-pdf-file-information-in-php/
description: Aprenda como definir várias propriedades de arquivo, como metadados, para um documento PDF em PHP usando Aspose.PDF.
lastmod: "2026-06-09"
---
## Aspose.PDF - Definir informações do arquivo PDF

Para atualizar as informações do documento PDF usando **Aspose.PDF Java para PHP**, basta invocar a classe **SetPdfFileInfo**.

Código PHP

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get document information
$doc_info = $doc->getInfo();

$doc_info->setAuthor("Aspose.PDF for java");
$doc_info->setCreationDate(new Date());
$doc_info->setKeywords("Aspose.PDF, DOM, API");
$doc_info->setModDate(new Date());
$doc_info->setSubject("PDF Information");
$doc_info->setTitle("Setting PDF Document Information");

# save update document with new information
$doc->save($dataDir . "Updated_Information.pdf");

print "Update document information, please check output file.";

```

**Baixar código em execução**

Baixe **Definir informações do arquivo PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetPdfFileInfo.php)
