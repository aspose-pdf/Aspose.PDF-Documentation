---
title: إضافة JavaScript في PHP
linktitle: إضافة JavaScript في PHP
type: docs
weight: 10
url: /ar/java/adding-javascript-in-php/
description: تعلم كيفية إضافة JavaScript إلى ملفات PDF باستخدام PHP و Aspose.PDF لتعزيز تفاعلية المستند.
lastmod: "2026-10-01"
---
## Aspose.PDF - إضافة JavaScript

لإضافة JavaScript في مستند PDF باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء الفئة **AddJavaScript**.

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

**تحميل الكود الجاري**

DownloadВ **إضافة JavaScript (Aspose.PDF)**В منВ أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddJavascript.php)
