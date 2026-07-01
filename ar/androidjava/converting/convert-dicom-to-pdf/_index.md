---
title: تحويل DICOM إلى PDF
linktitle: تحويل DICOM إلى PDF
type: docs
weight: 250
url: /ar/androidjava/convert-dicom-to-pdf/
lastmod: "2026-06-30"
description: تحويل الصور الطبية المحفوظة بتنسيق DICOM إلى ملف PDF باستخدام Aspose.PDF for Android عبر Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> هو معيار لمعالجة وتخزين وطباعة ونقل المعلومات في التصوير الطبي. يتضمن تعريف تنسيق ملف وبروتوكول اتصالات الشبكة.

Aspsoe.PDF for Java يتيح لك تحويل ملفات DICOM إلى تنسيق PDF، تحقق من مقتطف الشيفرة التالي:

1. تحميل الصورة إلى تدفق
1. تهيئة [`Document object`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)
1. تحميل ملف صورة DICOM النموذجية
1. حفظ مستند PDF الناتج

```java
//    Convert DICOM to PDF
    public void convertDICOMtoPDF () {
        // Initialize document object
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/bmode.dcm");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Load sample BMP image file
        image.setImageStream(inputStream);
        image.setFileType(ImageFileType.Dicom);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "DICOM-to-PDF.pdf");

        // Save output document
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

