---
title: Establecer Información del Archivo PDF en PHP
type: docs
weight: 90
url: /java/set-pdf-file-information-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Establecer Información del Archivo PDF

Para actualizar la información del documento Pdf usando **Aspose.PDF Java para PHP**, simplemente invoque la clase **SetPdfFileInfo**.

Código PHP

```php

# Abrir un documento pdf.
$doc = new Document($dataDir . "input1.pdf");

# Obtener información del documento
$doc_info = $doc->getInfo();

$doc_info->setAuthor("Aspose.PDF para java");
$doc_info->setCreationDate(new Date());
$doc_info->setKeywords("Aspose.PDF, DOM, API");
$doc_info->setModDate(new Date());
$doc_info->setSubject("Información del PDF");
$doc_info->setTitle("Estableciendo Información del Documento PDF");

# guardar documento actualizado con nueva información
$doc->save($dataDir . "Updated_Information.pdf");

print "Actualizar información del documento, por favor revise el archivo de salida.";

```

**Descargar Código en Ejecución**

Descargar **Establecer Información del Archivo PDF (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetPdfFileInfo.php)