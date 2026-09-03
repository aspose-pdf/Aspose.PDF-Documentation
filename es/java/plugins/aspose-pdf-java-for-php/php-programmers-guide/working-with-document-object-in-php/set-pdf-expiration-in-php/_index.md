---
title: Establecer expiración de PDF en PHP
linktitle: Establecer expiración de PDF en PHP
type: docs
weight: 80
url: /es/java/set-pdf-expiration-in-php/
description: Descubra cómo establecer una fecha de expiración para un archivo PDF en PHP, controlando el acceso con Aspose.PDF.
lastmod: "2026-09-03"
---
## Aspose.PDF - Establecer expiración de PDF

Para establecer la expiración deВ  Pdf documento usando **Aspose.PDF Java for PHP**, simplemente invoque la clase **SetExpiration**.

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

**Descargar Código en Ejecución**

DescargueВ **Set PDF Expiration (Aspose.PDF)**В deВ cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetExpiration.php)
