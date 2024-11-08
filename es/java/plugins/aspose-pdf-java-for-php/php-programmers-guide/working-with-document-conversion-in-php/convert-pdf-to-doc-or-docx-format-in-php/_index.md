---
title: Convertir PDF a formato DOC o DOCX en PHP
type: docs
weight: 10
url: /es/java/convert-pdf-to-doc-or-docx-format-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Convertir PDF a DOC o DOCX

Para convertir un documento PDF a formato DOC o DOCX usando **Aspose.PDF Java para PHP**, simplemente invoque el módulo **PdfToDoc**.

Código PHP

```php

# Abrir el documento de destino
$pdf = new Document($dataDir . 'input1.pdf');

# Guardar el archivo de salida concatenado (el documento de destino)
$pdf->save($dataDir . "output.doc");

print "El documento ha sido convertido exitosamente";

```

**Descargar Código en Ejecución**

Descargue **Convertir PDF a DOC o DOCX (Aspose.PDF)** desde cualquiera de los siguientes sitios de codificación social:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToDoc.php)