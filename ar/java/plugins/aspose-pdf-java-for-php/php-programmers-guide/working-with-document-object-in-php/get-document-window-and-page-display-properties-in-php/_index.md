---
title: احصل على خصائص نافذة المستند وخصائص عرض الصفحة في PHP
type: docs
weight: 30
url: /ar/java/get-document-window-and-page-display-properties-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - احصل على خصائص نافذة المستند وخصائص عرض الصفحة

للحصول على خصائص نافذة المستند وخصائص عرض الصفحة في مستند PDF باستخدام **Aspose.PDF Java for PHP**، يمكنك ببساطة استدعاء فئة **GetDocumentWindow**.

كود PHP

```php

# فتح مستند pdf.
$doc = new Document($dataDir . "input1.pdf");

# الحصول على خصائص المستند المختلفة
# موضع نافذة المستند - الافتراضي: false
print "CenterWindow :- " . $doc->getCenterWindow() . PHP_EOL;

# ترتيب القراءة السائد؛ تحديد موضع الصفحة
# عند العرض جنبًا إلى جنب - الافتراضي: L2R
print "Direction :- " . $doc->getDirection() . PHP_EOL;

# ما إذا كان شريط عنوان النافذة يجب أن يعرض عنوان المستند.
# إذا كان false، يعرض شريط العنوان اسم ملف PDF - الافتراضي: false
print "DisplayDocTitle :- " . $doc->getDisplayDocTitle() . PHP_EOL;

#ما إذا كان يجب تغيير حجم نافذة المستند لتناسب حجم
#الصفحة الأولى المعروضة - الافتراضي: false
print "FitWindow :- " . $doc->getFitWindow() . PHP_EOL;

# ما إذا كان يجب إخفاء شريط القوائم لتطبيق العارض - الافتراضي: false
print "HideMenuBar :-" . $doc->getHideMenubar() . PHP_EOL;

# ما إذا كان يجب إخفاء شريط الأدوات لتطبيق العارض - الافتراضي: false
print "HideToolBar :-" . $doc->getHideToolBar() . PHP_EOL;

# ما إذا كان يجب إخفاء عناصر واجهة المستخدم مثل أشرطة التمرير
# وترك محتويات الصفحة فقط معروضة - الافتراضي: false
print "HideWindowUI :-" . $doc->getHideWindowUI() . PHP_EOL;

# وضع صفحة المستند. كيفية عرض المستند عند الخروج من وضع الشاشة الكاملة.
print "NonFullScreenPageMode :-" . $doc->getNonFullScreenPageMode() . PHP_EOL;

# تخطيط الصفحة أي صفحة واحدة، عمود واحد
print "PageLayout :-" . $doc->getPageLayout() . PHP_EOL;

#كيف يجب عرض المستند عند فتحه.
print "pageMode :-" . $doc->getPageMode() . PHP_EOL;
```


**تنزيل الكود قيد التشغيل**

قم بتنزيل **احصل على خصائص نافذة المستند وعرض الصفحة (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetDocumentWindow.php)