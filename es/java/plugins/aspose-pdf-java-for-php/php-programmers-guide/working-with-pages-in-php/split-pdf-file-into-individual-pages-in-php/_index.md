---
title: Dividir archivo PDF en páginas individuales en PHP
type: docs
weight: 80
url: es/java/split-pdf-file-into-individual-pages-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Dividir Páginas

Para dividir un documento PDF en páginas individuales usando **Aspose.PDF Java para PHP**, simplemente invoca la clase **SplitAllPages**.

Código PHP

```php

# Abrir el documento de destino
$pdf = new Document($dataDir . 'input1.pdf');

# recorrer todas las páginas
$pdf_page = 1;
$total_size = $pdf->getPages()->size();
#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)
while ($pdf_page <= $total_size)

{

    # crear un nuevo objeto Document
    $new_document = new Document();

    # obtener la página en un índice particular de la Colección de Páginas
    $new_document->getPages()->add($pdf->getPages()->get_Item($pdf_page));

    # guardar el archivo PDF recién generado
    $new_document->save($dataDir . "page_#{$pdf_page}.pdf");

    $pdf_page++;

}

print "¡El proceso de división se completó con éxito!";

```

**Descargar Código en Ejecución**

Descargar **Dividir Páginas (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/SplitAllPages.php)