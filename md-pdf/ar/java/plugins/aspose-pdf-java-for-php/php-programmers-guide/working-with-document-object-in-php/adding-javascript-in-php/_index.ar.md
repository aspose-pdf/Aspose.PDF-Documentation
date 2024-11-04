---
title: إضافة JavaScript في PHP
type: docs
weight: 10
url: /java/adding-javascript-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - إضافة JavaScript

لإضافة JavaScript في مستند Pdf باستخدام **Aspose.PDF Java for PHP**، قم ببساطة باستدعاء فئة **AddJavaScript**.

كود PHP

```php
# فتح مستند pdf.
$doc = new Document($dataDir . "input1.pdf");

# إضافة JavaScript على مستوى المستند
# إنشاء JavascriptAction مع التعليمة البرمجية المطلوبة لـ JavaScript
$javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

# تعيين كائن JavascriptAction للإجراء المطلوب للمستند
$doc->setOpenAction($javaScript);

# إضافة JavaScript على مستوى الصفحة
$doc->getPages()->get_Item(2)->getActions()->setOnOpen(new JavascriptAction("app.alert('page 2 is opened')"));
$doc->getPages()->get_Item(2)->getActions()->setOnClose(new JavascriptAction("app.alert('page 2 is closed')"));

# حفظ مستند PDF
$doc->save($dataDir . "JavaScript-Added.pdf");

print "تمت إضافة JavaScript بنجاح، يرجى التحقق من ملف الإخراج.";
```


**تنزيل الكود الجاري**

قم بتنزيل **إضافة JavaScript (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddJavascript.php)