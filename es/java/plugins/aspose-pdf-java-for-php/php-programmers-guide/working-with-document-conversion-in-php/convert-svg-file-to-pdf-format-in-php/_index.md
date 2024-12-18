---
title: Convertir archivo SVG a formato PDF en PHP
type: docs
weight: 40
url: /es/java/convert-svg-file-to-pdf-format-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Convertir SVG a PDF

Para convertir un archivo SVG a formato PDF usando **Aspose.PDF Java para PHP**, simplemente invoca el módulo **SvgToPdf**.

Código PHP

```php
# Instanciar objeto LoadOption usando la opción de carga SVG
$options = new SvgLoadOptions();

# Crear objeto de documento
$pdf = new Document($dataDir . 'Example.svg', $options);

# Guardar la salida en formato XLS
$pdf->save($dataDir . "SVG.pdf");

print "El documento ha sido convertido exitosamente";

```

**Descargar Código en Ejecución**

Descargar **Convertir SVG a PDF (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/SvgToPdf.php)