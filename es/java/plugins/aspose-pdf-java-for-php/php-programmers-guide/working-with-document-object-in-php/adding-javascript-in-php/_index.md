---
title: Agregar JavaScript en PHP
linktitle: Agregar JavaScript en PHP
type: docs
weight: 10
url: /es/java/adding-javascript-in-php/
description: Aprenda cómo agregar JavaScript a archivos PDF usando PHP y Aspose.PDF para mejorar la interactividad del documento.
lastmod: "2026-09-03"
---
## Aspose.PDF - Agregar JavaScript

Para agregar JavaScript en un documento Pdf usando **Aspose.PDF Java for PHP**, simplemente invoque la clase **AddJavaScript**.

Código PHP

```php
# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Adding JavaScript at Document Level
# Instantiate JavascriptAction with desried JavaScript statement
$javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

# Assign JavascriptAction object to desired action of Document
$doc->setOpenAction($javaScript);

# Adding JavaScript at Page Level
$doc->getPages()->get_Item(2)->getActions()->setOnOpen(new JavascriptAction("app.alert('page 2 is opened')"));
$doc->getPages()->get_Item(2)->getActions()->setOnClose(new JavascriptAction("app.alert('page 2 is closed')"));

# Save PDF Document
$doc->save($dataDir . "JavaScript-Added.pdf");

print "Added JavaScript Successfully, please check the output file.";
```

**Descargar código en ejecución**

DescargarВ **Adding JavaScript (Aspose.PDF)**В deВ cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddJavascript.php)
