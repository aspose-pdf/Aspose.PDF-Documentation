---
title: Eliminar Metadatos de PDF en PHP
type: docs
weight: 70
url: es/java/remove-metadata-from-pdf-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Eliminar Metadatos

Para eliminar metadatos de un documento Pdf usando **Aspose.PDF Java para PHP**, simplemente invoque la clase **RemoveMetadata**.

Código PHP

```php

# Abrir un documento pdf.
$doc = new Document($dataDir . "input1.pdf");

if (preg_match('/pdfaid:part/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("pdfaid:part");

}

if (preg_match('/dc:format/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("dc:format");

}

# guardar documento actualizado con nueva información
$doc->save($dataDir . "Remove_Metadata.pdf");

print "Metadatos eliminados con éxito, por favor revise el archivo de salida." . PHP_EOL;

```

**Descargar Código en Ejecución**

Descargue **Eliminar Metadatos (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/RemoveMetadata.php)