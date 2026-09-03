---
title: Obtener metadatos XMP de un archivo PDF en PHP
linktitle: Obtener metadatos XMP de un archivo PDF en PHP
type: docs
weight: 50
url: /es/java/get-xmp-metadata-from-pdf-file-in-php/
description: Aprenda cómo extraer los metadatos XMP de documentos PDF en PHP usando Aspose.PDF para análisis avanzado de contenido.
lastmod: "2026-09-03"
---
## Aspose.PDF - Obtener metadatos XMP

Para obtener los metadatos XMP de un documento Pdf usando **Aspose.PDF Java for PHP**, simplemente invoque la clase **GetXMPMetadata**.

Código PHP

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get properties
print "xmp:CreateDate: " + $doc->getMetadata()->get_Item("xmp:CreateDate") . PHP_EOL;
print "xmp:Nickname: " + $doc->getMetadata()->get_Item("xmp:Nickname") . PHP_EOL;
print "xmp:CustomProperty: " + $doc->getMetadata()->get_Item("xmp:CustomProperty") . PHP_EOL;

```

**Descargar Código en Ejecución**

DescargarВ **Get XMP Metadata (Aspose.PDF)**В deВ cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetXMPMetadata.php)
