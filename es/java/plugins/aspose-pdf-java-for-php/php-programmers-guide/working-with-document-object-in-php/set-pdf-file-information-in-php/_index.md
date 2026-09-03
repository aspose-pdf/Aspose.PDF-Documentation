---
title: Establecer información del archivo PDF en PHP
linktitle: Establecer información del archivo PDF en PHP
type: docs
weight: 90
url: /java/set-pdf-file-information-in-php/
description: Aprenda a configurar varias propiedades de archivo, como metadatos, para un documento PDF en PHP usando Aspose.PDF.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Establecer información del archivo PDF



Para actualizar la información del documento PDF usando **Aspose.PDF Java para PHP**, simplemente invoque la clase **SetPdfFileInfo**.

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


**Descargar código de ejecución**



Descargue **Establecer información de archivo PDF (Aspose.PDF)**В desde cualquiera de los sitios de codificación social mencionados a continuación:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetPdfFileInfo.php)
