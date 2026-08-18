---
title: إضافة جافا سكريبت في PHP
linktitle: إضافة جافا سكريبت في PHP
type: docs
weight: 10
url: /java/adding-javascript-in-php/
description: تعرف على كيفية إضافة JavaScript إلى ملفات PDF باستخدام PHP وAspose.PDF لتحسين تفاعل المستند.
lastmod: "2026-06-09"
---
## Aspose.PDF - إضافة جافا سكريبت

لإضافة JavaScript في مستند Pdf باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء فئة **AddJavaScript**.

كود PHP

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

** تنزيل كود التشغيل **

تنزيلВ **إضافة JavaScript (Aspose.PDF)**В fromВ من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddJavascript.php)
