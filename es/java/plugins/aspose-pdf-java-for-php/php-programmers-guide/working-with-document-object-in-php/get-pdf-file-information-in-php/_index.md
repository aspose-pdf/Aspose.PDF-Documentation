---
title: Obtener información del archivo PDF en PHP
linktitle: Obtener información del archivo PDF en PHP
type: docs
weight: 40
url: /es/java/get-pdf-file-information-in-php/
description: Descubra cómo recuperar información detallada sobre un archivo PDF, incluidos los metadatos y propiedades, en PHP con Aspose.PDF.
lastmod: "2026-09-03"
---
## Aspose.PDF - Obtener información del archivo PDF

Para obtener la información del archivo de un documento Pdf usando **Aspose.PDF Java for PHP**, simplemente invoque la clase **GetPdfFileInfo**.

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

**Descargar código en ejecución**

DescargarВ **Get PDF File Information (Aspose.PDF)**В deВ cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetPdfFileInfo.php)
