---
title: Establecer Expiración de PDF en PHP
type: docs
weight: 80
url: es/java/set-pdf-expiration-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Establecer Expiración de PDF

Para establecer la expiración de un documento Pdf usando **Aspose.PDF Java para PHP**, simplemente invoque la clase **SetExpiration**.

Código PHP

```php

# Abrir un documento pdf.
$doc = new Document($dataDir . "input1.pdf");

$javascript = new JavascriptAction(
        "var year=2014;
    var month=4;
    today = new Date();
    today = new Date(today.getFullYear(), today.getMonth());
    expiry = new Date(year, month);
    if (today.getTime() > expiry.getTime())
    app.alert('El archivo ha expirado. Necesitas uno nuevo.');");
$doc->setOpenAction($javascript);

# guardar el documento actualizado con la nueva información
$doc->save($dataDir . "set_expiration.pdf");

print "Actualiza la información del documento, por favor verifica el archivo de salida." . PHP_EOL;

```

**Descargar Código en Ejecución**

Descargar **Establecer Expiración de PDF (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetExpiration.php)