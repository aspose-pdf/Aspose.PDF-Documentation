---
title: إضافة نص إلى ملف PDF موجود في PHP
linktitle: إضافة نص إلى ملف PDF موجود في PHP
type: docs
weight: 20
url: /java/add-text-to-an-existing-pdf-file-in-php/
description: تعرف على كيفية إضافة نص جديد إلى مستند PDF موجود في PHP باستخدام Aspose.PDF لتحسين المحتوى.
lastmod: "2026-06-09"
---
## Aspose.PDF - إضافة نص

لإضافة سلسلة نصية في مستند Pdf باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء وحدة **AddText**.

كود PHP

```php

# Instantiate Document object
$doc = new Document($dataDir . 'input1.pdf');

# get particular page
$pdf_page = $doc->getPages()->get_Item(1);

# create text fragment
$text_fragment = new TextFragment("main text");
$text_fragment->setPosition(new Position(100, 600));

$font_repository = new FontRepository();
$color = new Color();

# set text properties
$text_fragment->getTextState()->setFont($font_repository->findFont("Verdana"));
$text_fragment->getTextState()->setFontSize(14);

# create TextBuilder object
$text_builder = new TextBuilder($pdf_page);

# append the text fragment to the PDF page
$text_builder->appendText($text_fragment);

# Save PDF file
$doc->save($dataDir . "Text_Added.pdf");

print "Text added successfully" . PHP_EOL;

```

** تنزيل كود التشغيل **

تنزيلВ **إضافة نص (Aspose.PDF)**В fromВ من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddText.php)
