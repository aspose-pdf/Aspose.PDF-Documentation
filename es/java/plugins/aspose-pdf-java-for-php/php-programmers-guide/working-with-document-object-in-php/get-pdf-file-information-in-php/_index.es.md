---
title: Obtener Información de Archivo PDF en PHP
type: docs
weight: 40
url: /java/get-pdf-file-information-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obtener Información de Archivo PDF

Para obtener la información de archivo de un documento Pdf usando **Aspose.PDF Java para PHP**, simplemente invoca la clase **GetPdfFileInfo**.

Código PHP

```php

# Abrir un documento pdf.
$doc = new Document($dataDir . "input1.pdf");

# Obtener información del documento
$doc_info = $doc->getInfo();

# Mostrar información del documento
print "Autor:-" . $doc_info->getAuthor();
print "Fecha de Creación:-" . $doc_info->getCreationDate();
print "Palabras Clave:-" . $doc_info->getKeywords();
print "Fecha de Modificación:-" . $doc_info->getModDate();
print "Asunto:-" . $doc_info->getSubject();
print "Título:-" . $doc_info->getTitle();

```

**Descargar Código en Ejecución**

Descargar **Obtener Información de Archivo PDF (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetPdfFileInfo.php)