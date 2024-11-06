---
title: Agregar cadena HTML usando DOM en PHP
type: docs
weight: 10
url: es/java/add-html-string-using-dom-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Agregar HTML

Para agregar una cadena HTML en un documento PDF usando **Aspose.PDF Java para PHP**, simplemente invoca el módulo **AddHtml**.

Código PHP

```php
# Instanciar objeto Document
$doc = new Document();

# Agregar una página a la colección de páginas del archivo PDF
$page = $doc->getPages()->add();

# Instanciar HtmlFragment con contenidos HTML
$title = new HtmlFragment("<fontsize=10><b><i>Tabla</i></b></fontsize>");

# Establecer MarginInfo para detalles de margen
$margin = new MarginInfo();
$margin->setBottom(10);
$margin->setTop(200);

# Establecer información de margen
$title->setMargin($margin);

# Agregar Fragmento HTML a la colección de párrafos de la página
$page->getParagraphs()->add($title);

# Guardar archivo PDF
$doc->save($dataDir . "html.output.pdf");

print "HTML agregado exitosamente" . PHP_EOL;

```

**Descargar Código en Ejecución**

Descargar **Agregar HTML (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddHtml.php)