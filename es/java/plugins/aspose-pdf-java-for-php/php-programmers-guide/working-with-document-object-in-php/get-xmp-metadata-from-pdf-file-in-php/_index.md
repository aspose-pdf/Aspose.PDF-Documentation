---
title: Obtenga metadatos XMP de un archivo PDF en PHP
linktitle: Obtenga metadatos XMP de un archivo PDF en PHP
type: docs
weight: 50
url: /java/get-xmp-metadata-from-pdf-file-in-php/
description: Aprenda a extraer metadatos XMP de documentos PDF en PHP utilizando Aspose.PDF para un análisis de contenido avanzado.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Obtener metadatos XMP



Para obtener metadatos XMP de un documento PDF utilizando **Aspose.PDF Java para PHP**, simplemente invoque la clase **GetXMPMetadata**.

Código PHP


```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get properties
print "xmp:CreateDate: " + $doc->getMetadata()->get_Item("xmp:CreateDate") . PHP_EOL;
print "xmp:Nickname: " + $doc->getMetadata()->get_Item("xmp:Nickname") . PHP_EOL;
print "xmp:CustomProperty: " + $doc->getMetadata()->get_Item("xmp:CustomProperty") . PHP_EOL;

```


**Descargar código de ejecución**



DescargarВ **Obtener metadatos XMP (Aspose.PDF)**В de cualquiera de los sitios de codificación social mencionados a continuación:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetXMPMetadata.php)
