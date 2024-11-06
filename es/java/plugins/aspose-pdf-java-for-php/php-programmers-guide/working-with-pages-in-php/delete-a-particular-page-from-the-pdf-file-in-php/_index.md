---
title: Eliminar una Página Particular del Archivo PDF en PHP
type: docs
weight: 20
url: es/java/delete-a-particular-page-from-the-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Eliminar Página

Para eliminar una Página Particular del documento PDF usando **Aspose.PDF Java para PHP**, simplemente invoque la clase **DeletePage**.

Código PHP

```php

# Abrir el documento de destino
$pdf = new Document($dataDir . 'input1.pdf');

# eliminar una página particular
$pdf->getPages()->delete(2);

# guardar el archivo PDF recién generado
$pdf->save($dataDir . "output.pdf");

print "¡Página eliminada con éxito!";

```

**Descargar Ejecución**

Descargue **Eliminar Página (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/DeletePage.php)