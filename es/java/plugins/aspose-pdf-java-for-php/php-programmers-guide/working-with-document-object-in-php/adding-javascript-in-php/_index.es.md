---
title: Añadiendo JavaScript en PHP
type: docs
weight: 10
url: /java/adding-javascript-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Añadiendo JavaScript

Para añadir JavaScript en un documento Pdf usando **Aspose.PDF Java para PHP**, simplemente invoca la clase **AddJavaScript**.

Código PHP

```php
# Abrir un documento pdf.
$doc = new Document($dataDir . "input1.pdf");

# Añadiendo JavaScript a nivel de documento
# Instanciar JavascriptAction con la declaración de JavaScript deseada
$javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

# Asignar el objeto JavascriptAction a la acción deseada del Documento
$doc->setOpenAction($javaScript);

# Añadiendo JavaScript a nivel de página
$doc->getPages()->get_Item(2)->getActions()->setOnOpen(new JavascriptAction("app.alert('page 2 is opened')"));
$doc->getPages()->get_Item(2)->getActions()->setOnClose(new JavascriptAction("app.alert('page 2 is closed')"));

# Guardar el Documento PDF
$doc->save($dataDir . "JavaScript-Added.pdf");

print "JavaScript añadido exitosamente, por favor revisa el archivo de salida.";
```


**Descargar Código en Ejecución**

Descargue **Agregar JavaScript (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddJavascript.php)