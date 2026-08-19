---
title: Добавление JavaScript в PHP
linktitle: Добавление JavaScript в PHP
type: docs
weight: 10
url: /ru/java/adding-javascript-in-php/
description: Узнайте, как добавить JavaScript в PDF‑файлы с помощью PHP и Aspose.PDF, чтобы улучшить интерактивность документа.
lastmod: "2026-08-19"
---
## Aspose.PDF — Добавление JavaScript

Чтобы добавить JavaScript в документ PDF, используя **Aspose.PDF Java for PHP**, просто вызовите класс **AddJavaScript**.

Код PHP

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

**Скачать исполняемый код**

СкачатьВ **Adding JavaScript (Aspose.PDF)**В изВ любого из перечисленных ниже сайтов совместного кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddJavascript.php)

