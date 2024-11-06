---
title: Añadir TOC a PDF Existente en PHP
type: docs
weight: 20
url: es/java/add-toc-to-existing-pdf-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Añadir TOC

Para agregar TOC en un documento Pdf usando **Aspose.PDF Java para PHP**, simplemente invoque la clase **AddToc**.

Código PHP

```php

# Abrir un documento pdf.
$doc = new Document($dataDir . "input1.pdf");

# Obtener acceso a la primera página del archivo PDF
$toc_page = $doc->getPages()->insert(1);

# Crear objeto para representar la información de TOC
$toc_info = new TocInfo();
$title = new TextFragment("Tabla de Contenidos");
$title->getTextState()->setFontSize(20);
#title.getTextState().setFontStyle(Rjb::import('com.aspose.pdf.FontStyles.Bold'))

# Establecer el título para TOC
$toc_info->setTitle($title);
$toc_page->setTocInfo($toc_info);

# Crear objetos de cadena que se usarán como elementos de TOC
$titles = array("Primera página", "Segunda página");

$i = 0;
while ($i < 2){

    # Crear objeto de encabezado
    $heading2 = new Heading(1);

    $segment2 = new TextSegment();
    $heading2->setTocPage($toc_page);
    $heading2->getSegments()->add($segment2);

    # Especificar la página de destino para el objeto de encabezado
    $heading2->setDestinationPage($doc->getPages()->get_Item($i + 2));

    # Página de destino
    $heading2->setTop($doc->getPages()->get_Item($i + 2)->getRect()->getHeight());

    # Coordenada de destino
    $segment2->setText($titles[$i]);

    # Agregar encabezado a la página que contiene TOC
    $toc_page->getParagraphs()->add($heading2);

    $i +=1;

}

# Guardar Documento PDF
$doc->save($dataDir . "TOC.pdf");

print "TOC añadido exitosamente, por favor revise el archivo de salida.";

```


**Descargar Código en Ejecución**

Descargue **Agregar TOC (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddToc.php)