---
title: تقسيم ملف PDF إلى صفحات فردية في PHP
type: docs
weight: 80
url: /java/split-pdf-file-into-individual-pages-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - تقسيم الصفحات

لتقسيم مستند PDF إلى صفحات فردية باستخدام **Aspose.PDF Java for PHP**، قم فقط باستدعاء فئة **SplitAllPages**.

كود PHP

```php

# افتح المستند الهدف
$pdf = new Document($dataDir . 'input1.pdf');

# حلقة عبر جميع الصفحات
$pdf_page = 1;
$total_size = $pdf->getPages()->size();
#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)
while ($pdf_page <= $total_size)

{

    # إنشاء كائن مستند جديد
    $new_document = new Document();

    # الحصول على الصفحة عند فهرس محدد من مجموعة الصفحات
    $new_document->getPages()->add($pdf->getPages()->get_Item($pdf_page));

    # حفظ ملف PDF الذي تم إنشاؤه حديثًا
    $new_document->save($dataDir . "page_#{$pdf_page}.pdf");

    $pdf_page++;

}

print "اكتمل عملية التقسيم بنجاح!";

```

**تحميل الكود التشغيلي**

قم بتنزيل **تقسيم الصفحات (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/SplitAllPages.php)

key: description

changefreq: "monthly"

type: docs