---
title: Definir expiração de PDF em PHP
linktitle: Definir expiração de PDF em PHP
type: docs
weight: 80
url: /java/set-pdf-expiration-in-php/
description: Descubra como definir uma data de validade para um arquivo PDF em PHP, controlando o acesso com Aspose.PDF.
lastmod: "2026-06-09"
---
## Aspose.PDF - Definir expiração do PDF

Para definir a expiração do documento PDF usando **Aspose.PDF Java para PHP**, basta invocar a classe **SetExpiration**.

Código PHP

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

$javascript = new JavascriptAction(
        "var year=2014;
    var month=4;
    today = new Date();
    today = new Date(today.getFullYear(), today.getMonth());
    expiry = new Date(year, month);
    if (today.getTime() > expiry.getTime())
    app.alert('The file is expired. You need a new one.');");
$doc->setOpenAction($javascript);

# save update document with new information
$doc->save($dataDir . "set_expiration.pdf");

print "Update document information, please check output file." . PHP_EOL;

```

**Baixar código em execução**

Baixe **Definir expiração de PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetExpiration.php)
