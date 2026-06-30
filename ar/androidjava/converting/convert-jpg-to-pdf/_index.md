---
title: تحويل JPG إلى PDF
linktitle: تحويل JPG إلى PDF
type: docs
weight: 190
url: /ar/androidjava/convert-jpg-to-pdf/
lastmod: "2026-06-30"
description: تعلم كيفية تحويل صورة JPG بسهولة إلى ملف PDF. يمكنك أيضًا تحويل صورة إلى PDF بنفس ارتفاع وعرض الصفحة.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

ليس هناك حاجة للتساؤل عن كيفية تحويل JPG إلى PDF، لأن مكتبة Apose.PDF لنظام Android عبر Java هي الخيار الأفضل.

يمكنك بسهولة كبيرة تحويل صور JPG إلى PDF باستخدام Aspose.PDF لنظام Android عبر Java باتباع الخطوات التالية:

1. تهيئة كائن من [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) فئة
1. تحميل صورة JPG وإضافتها إلى الفقرة
1. حفظ ملف PDF الناتج

المقتطف البرمجي أدناه يوضح كيفية تحويل صورة JPG إلى PDF:

```java
public void convertJPEGtoPDF () {
        // Initialize document object
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.jpg");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Load sample JPEG image file
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "JPEG-to-PDF.pdf");

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
