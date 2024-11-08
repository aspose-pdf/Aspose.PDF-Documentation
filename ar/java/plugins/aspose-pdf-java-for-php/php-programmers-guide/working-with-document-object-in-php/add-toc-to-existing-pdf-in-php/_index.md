---
title: إضافة جدول محتويات إلى PDF موجود في PHP
type: docs
weight: 20
url: /ar/java/add-toc-to-existing-pdf-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - إضافة جدول محتويات

لإضافة جدول محتويات في مستند Pdf باستخدام **Aspose.PDF Java for PHP**، ببساطة استدعي فئة **AddToc**.

كود PHP

```php

# فتح مستند pdf.
$doc = new Document($dataDir . "input1.pdf");

# الوصول إلى الصفحة الأولى من ملف PDF
$toc_page = $doc->getPages()->insert(1);

# إنشاء كائن لتمثيل معلومات جدول المحتويات
$toc_info = new TocInfo();
$title = new TextFragment("جدول المحتويات");
$title->getTextState()->setFontSize(20);
#title.getTextState().setFontStyle(Rjb::import('com.aspose.pdf.FontStyles.Bold'))

# تعيين العنوان لجدول المحتويات
$toc_info->setTitle($title);
$toc_page->setTocInfo($toc_info);

# إنشاء كائنات سلسلة والتي ستُستخدم كعناصر جدول المحتويات
$titles = array("الصفحة الأولى", "الصفحة الثانية");

$i = 0;
while ($i < 2){

    # إنشاء كائن العنوان
    $heading2 = new Heading(1);

    $segment2 = new TextSegment();
    $heading2->setTocPage($toc_page);
    $heading2->getSegments()->add($segment2);

    # تحديد صفحة الوجهة لكائن العنوان
    $heading2->setDestinationPage($doc->getPages()->get_Item($i + 2));

    # صفحة الوجهة
    $heading2->setTop($doc->getPages()->get_Item($i + 2)->getRect()->getHeight());

    # الإحداثيات الوجهة
    $segment2->setText($titles[$i]);

    # إضافة العنوان إلى الصفحة التي تحتوي على جدول المحتويات
    $toc_page->getParagraphs()->add($heading2);

    $i +=1;

}

# حفظ مستند PDF
$doc->save($dataDir . "TOC.pdf");

print "تمت إضافة جدول المحتويات بنجاح، يرجى التحقق من ملف الإخراج.";

```


**تنزيل الكود الجاري**

قم بتنزيل **إضافة جدول المحتويات (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddToc.php)