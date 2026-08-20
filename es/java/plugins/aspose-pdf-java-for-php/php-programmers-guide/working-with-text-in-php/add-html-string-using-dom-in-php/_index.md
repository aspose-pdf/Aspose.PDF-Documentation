---
title: Agregar cadena HTML usando DOM en PHP
linktitle: Agregar cadena HTML usando DOM en PHP
type: docs
weight: 10
url: /java/add-html-string-using-dom-in-php/
description: Explore cómo agregar contenido HTML a un documento PDF usando DOM en PHP con Aspose.PDF para la creación de documentos enriquecidos.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Agregar HTML



Para agregar una cadena HTML en un documento PDF usando **Aspose.PDF Java para PHP**, simplemente invoque el módulo **AddHtml**.

Código PHP


```php
# Instantiate Document object
$doc = new Document();

# Add a page to pages collection of PDF file
$page = $doc->getPages()->add();

# Instantiate HtmlFragment with HTML contents
$title = new HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>");

# set MarginInfo for margin details
$margin = new MarginInfo();
$margin->setBottom(10);
$margin->setTop(200);

# Set margin information
$title->setMargin($margin);

# Add HTML Fragment to paragraphs collection of page
$page->getParagraphs()->add($title);

# Save PDF file
$doc->save($dataDir . "html.output.pdf");

print "HTML added successfully" . PHP_EOL;

```


**Descargar código de ejecución**



Descargue **Agregue HTML (Aspose.PDF)**В desde cualquiera de los sitios de codificación social mencionados a continuación:


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddHtml.php)
