---
title: Eliminar metadatos de PDF en PHP
linktitle: Eliminar metadatos de PDF en PHP
type: docs
weight: 70
url: /es/java/remove-metadata-from-pdf-in-php/
description: Explora cómo eliminar metadatos de un documento PDF en PHP usando Aspose.PDF para mejorar la privacidad y la seguridad del documento.
lastmod: "2026-09-29"
---
## Aspose.PDF - eliminar metadatos

Para eliminar metadatos de un documento Pdf usando **Aspose.PDF Java for PHP**, simplemente invoca la clase **RemoveMetadata**.

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

**Descargar código en ejecución**

Download **Remove Metadata (Aspose.PDF)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/RemoveMetadata.php)
