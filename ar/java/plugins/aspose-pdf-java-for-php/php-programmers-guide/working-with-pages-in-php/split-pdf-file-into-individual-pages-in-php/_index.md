---
title: قسّم ملف PDF إلى صفحات فردية في PHP
linktitle: قسّم ملف PDF إلى صفحات فردية في PHP
type: docs
weight: 80
url: /ar/java/split-pdf-file-into-individual-pages-in-php/
description: اكتشف كيف يمكنك قسمة مستند PDF إلى صفحات فردية باستخدام PHP و Aspose.PDF لاستخراج الصفحات بكفاءة.
lastmod: "2026-10-01"
---
## Aspose.PDF - قسمة الصفحات

لقسمة مستند PDF إلى صفحات فردية باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء الفئة **SplitAllPages**.

كود PHP

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# loop through all the pages
$pdf_page = 1;
$total_size = $pdf->getPages()->size();
#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)
while ($pdf_page <= $total_size)

{

    # create a new Document object
    $new_document = new Document();

    # get the page at particular index of Page Collection
    $new_document->getPages()->add($pdf->getPages()->get_Item($pdf_page));

    # save the newly generated PDF file
    $new_document->save($dataDir . "page_#{$pdf_page}.pdf");

    $pdf_page++;

}

print "Split process completed successfully!";

```

**تحميل الكود الجاري**

تنزيل **Split Pages (Aspose.PDF)**В منВ أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/SplitAllPages.php)
