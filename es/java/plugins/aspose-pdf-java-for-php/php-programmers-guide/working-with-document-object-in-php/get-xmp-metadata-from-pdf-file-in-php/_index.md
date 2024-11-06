---
title: Obtener Metadatos XMP de un Archivo PDF en PHP
type: docs
weight: 50
url: es/java/get-xmp-metadata-from-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obtener Metadatos XMP

Para obtener metadatos XMP de un documento Pdf usando **Aspose.PDF Java para PHP**, simplemente invoque la clase **GetXMPMetadata**.

Código PHP

```php

# Abrir un documento pdf.
$doc = new Document($dataDir . "input1.pdf");

# Obtener propiedades
print "xmp:CreateDate: " + $doc->getMetadata()->get_Item("xmp:CreateDate") . PHP_EOL;
print "xmp:Nickname: " + $doc->getMetadata()->get_Item("xmp:Nickname") . PHP_EOL;
print "xmp:CustomProperty: " + $doc->getMetadata()->get_Item("xmp:CustomProperty") . PHP_EOL;

```

**Descargar Código en Ejecución**

Descargue **Obtener Metadatos XMP (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetXMPMetadata.php)