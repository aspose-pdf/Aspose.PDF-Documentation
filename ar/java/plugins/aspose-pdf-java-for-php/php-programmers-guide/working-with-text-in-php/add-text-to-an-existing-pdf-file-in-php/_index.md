---
title: إضافة نص إلى ملف PDF موجود في PHP
type: docs
weight: 20
url: ar/java/add-text-to-an-existing-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - إضافة نص

لإضافة سلسلة نصية في مستند Pdf باستخدام **Aspose.PDF Java for PHP**، ببساطة قم باستدعاء وحدة **AddText**.

كود PHP

```php

# إنشاء كائن المستند
$doc = new Document($dataDir . 'input1.pdf');

# الحصول على الصفحة المحددة
$pdf_page = $doc->getPages()->get_Item(1);

# إنشاء جزء نصي
$text_fragment = new TextFragment("النص الرئيسي");
$text_fragment->setPosition(new Position(100, 600));

$font_repository = new FontRepository();
$color = new Color();

# ضبط خصائص النص
$text_fragment->getTextState()->setFont($font_repository->findFont("Verdana"));
$text_fragment->getTextState()->setFontSize(14);

# إنشاء كائن TextBuilder
$text_builder = new TextBuilder($pdf_page);

# إضافة الجزء النصي إلى صفحة PDF
$text_builder->appendText($text_fragment);

# حفظ ملف PDF
$doc->save($dataDir . "Text_Added.pdf");

print "تمت إضافة النص بنجاح" . PHP_EOL;

```


**تنزيل الكود قيد التشغيل**

قم بتنزيل **إضافة نص (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddText.php)