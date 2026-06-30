---
title: تحويل BMP إلى PDF
linktitle: تحويل BMP إلى PDF
type: docs
weight: 220
url: /ar/androidjava/convert-bmp-to-pdf/
lastmod: "2026-06-30"
description: يمكنك بسهولة تحويل ملفات BMP النقطية إلى PDF التي تُستخدم لتخزين الصور الرقمية النقطية بشكل منفصل عن جهاز العرض باستخدام Aspose.PDF for Android عبر Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

تُعد صور BMP ملفات ذات امتداد .BMP تمثل ملفات صورة نقطية تُستخدم لتخزين الصور الرقمية النقطية. هذه الصور مستقلة عن محول الرسومات وتُعرف أيضًا باسم تنسيق ملف نقطية مستقل عن الجهاز (DIB).
يمكنك تحويل BMP إلى PDF باستخدام Aspose.PDF for Java API. لذلك، يمكنك اتباع الخطوات التالية لتحويل صور BMP:

1. إنشاء مستند جديد
1. تحميل ملف صورة BMP تجريبي
1. أخيرًا، احفظ ملف PDF الناتج

إليك مقتطف الشيفرة التالي الذي يتبع هذه الخطوات ويظهر كيفية تحويل BMP إلى PDF باستخدام Java:

```java
public void convertBMPtoPDF () {
        // Initialize document object
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.bmp");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Load sample BMP image file
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "BMP-to-PDF.pdf");

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

