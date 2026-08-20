---
title: Eliminar metadatos de PDF en PHP
linktitle: Eliminar metadatos de PDF en PHP
type: docs
weight: 70
url: /java/remove-metadata-from-pdf-in-php/
description: Explore cómo eliminar metadatos de un documento PDF en PHP usando Aspose.PDF para mejorar la privacidad y la seguridad de los documentos.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Eliminar metadatos



Para eliminar metadatos de un documento PDF usando **Aspose.PDF Java para PHP**, simplemente invoque la clase **RemoveMetadata**.

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


**Descargar código de ejecución**



DescargarВ **Eliminar metadatos (Aspose.PDF)**В de cualquiera de los sitios de codificación social mencionados a continuación:


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/RemoveMetadata.php)
