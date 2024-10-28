---

title: إضافة سلسلة HTML باستخدام DOM في PHP  
type: docs  
weight: 10  
url: /java/add-html-string-using-dom-in-php/  
lastmod: "2021-06-05"  

## Aspose.PDF - إضافة HTML

لإضافة سلسلة HTML في مستند PDF باستخدام **Aspose.PDF Java for PHP**، ببساطة قم باستدعاء وحدة **AddHtml**.

كود PHP

```php
# إنشاء كائن Document
$doc = new Document();

# إضافة صفحة إلى مجموعة الصفحات في ملف PDF
$page = $doc->getPages()->add();

# إنشاء HtmlFragment بمحتويات HTML
$title = new HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>");

# تعيين MarginInfo لتفاصيل الهوامش
$margin = new MarginInfo();
$margin->setBottom(10);
$margin->setTop(200);

# تعيين معلومات الهوامش
$title->setMargin($margin);

# إضافة جزء HTML إلى مجموعة الفقرات في الصفحة
$page->getParagraphs()->add($title);

# حفظ ملف PDF
$doc->save($dataDir . "html.output.pdf");

print "تمت إضافة HTML بنجاح" . PHP_EOL;

```

**تنزيل الكود الجاري**

قم بتنزيل **Add HTML (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddHtml.php)