---
title: Eliminar una página particular del archivo PDF en PHP
linktitle: Eliminar una página particular del archivo PDF en PHP
type: docs
weight: 20
url: /es/java/delete-a-particular-page-from-the-pdf-file-in-php/
description: Descubra cómo eliminar una página específica de un documento PDF en PHP con Aspose.PDF, simplificando la edición de documentos.
lastmod: "2026-09-29"
---
## Aspose.PDF - eliminar página

Para eliminar una página particular del documento PDF usando **Aspose.PDF Java for PHP**, simplemente invoque la clase **DeletePage**.

Código PHP

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# delete a particular page
$pdf->getPages()->delete(2);

# save the newly generated PDF file
$pdf->save($dataDir . "output.pdf");

print "Page deleted successfully!";

```

**Descarga en curso**

Descargar **Delete Page (Aspose.PDF)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/DeletePage.php)
