---
title: تحويل DICOM إلى PDF
linktitle: تحويل DICOM إلى PDF
type: docs
weight: 250
url: /androidjava/convert-dicom-to-pdf/
lastmod: "2021-06-05"
description: تحويل الصور الطبية المحفوظة بتنسيق DICOM إلى ملف PDF باستخدام Aspose.PDF لـ Android عبر Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> هو معيار للتعامل مع المعلومات وتخزينها وطباعتها ونقلها في التصوير الطبي. يشمل تعريف تنسيق الملف وبروتوكول اتصالات الشبكة.

Aspose.PDF for Java يتيح لك تحويل ملفات DICOM إلى تنسيق PDF، تحقق من مقتطف الشيفرة التالي:

1. تحميل الصورة إلى الدفق
1. تهيئة [`كائن الوثيقة`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)
1. تحميل ملف صورة DICOM النموذجي
1. حفظ وثيقة PDF الناتجة

```java
// تحويل DICOM إلى PDF
public void convertDICOMtoPDF () {
    // تهيئة كائن الوثيقة
    document = new Document();

    Page page = document.getPages().add();
    Image image = new Image();

    File imgFileName = new File(fileStorage, "Conversion/bmode.dcm");

    try {
        inputStream = new FileInputStream(imgFileName);
    } catch (FileNotFoundException e) {
        resultMessage.setText(e.getMessage());
        return;
    }

    // تحميل ملف صورة BMP النموذجي
    image.setImageStream(inputStream);
    image.setFileType(ImageFileType.Dicom);
    page.getParagraphs().add(image);

    File pdfFileName = new File(fileStorage, "DICOM-to-PDF.pdf");

    // حفظ الوثيقة الناتجة
    try {
        document.save(pdfFileName.toString());
    } catch (Exception e) {
        resultMessage.setText(e.getMessage());
        return;
    }
    resultMessage.setText(R.string.success_message);
}
```