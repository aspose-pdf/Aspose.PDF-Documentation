---
title: Ajouter du JavaScript en PHP
linktitle: Ajouter du JavaScript en PHP
type: docs
weight: 10
url: /java/adding-javascript-in-php/
description: Découvrez comment ajouter du JavaScript aux fichiers PDF à l'aide de PHP et Aspose.PDF pour améliorer l'interactivité des documents.
lastmod: "2026-09-21"
---
## Aspose.PDF - Ajouter du JavaScript

Pour ajouter du JavaScript dans un document PDF à l'aide de **Aspose.PDF Java pour PHP**, utilisez la classe **AddJavaScript**.

Code PHP

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

**Télécharger l’exemple de code**

Téléchargez **Ajouter du JavaScript (Aspose.PDF)** à partir de l'un des plateformes d’hébergement de code mentionnées ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddJavascript.php)
