---
title: تقسيم ملف PDF إلى صفحات فردية في PHP
linktitle: تقسيم ملف PDF إلى صفحات فردية في PHP
type: docs
weight: 80
url: /java/split-pdf-file-into-individual-pages-in-php/
description: اكتشف كيفية تقسيم مستند PDF إلى صفحات فردية باستخدام PHP وAspose.PDF لاستخراج الصفحات بكفاءة.
lastmod: "2026-06-09"
---
## Aspose.PDF - تقسيم الصفحات

لتقسيم مستند PDF إلى صفحات فردية باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء فئة **SplitAllPages**.

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

** تنزيل كود التشغيل **

قم بتنزيل **تقسيم الصفحات (Aspose.PDF)**В من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/SplitAllPages.php)
