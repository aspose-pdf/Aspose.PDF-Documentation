---
title: تحويل BMP إلى PDF
linktitle: تحويل BMP إلى PDF
type: docs
weight: 220
url: /ar/androidjava/convert-bmp-to-pdf/
lastmod: "2021-06-05"
description: يمكنك بسهولة تحويل ملفات BMP bitmap إلى PDF المستخدمة لتخزين الصور الرقمية bitmap بشكل منفصل عن جهاز العرض باستخدام Aspose.PDF. لنظام Android عبر Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

صور BMP هي ملفات بامتداد .BMP تمثل ملفات صورة Bitmap التي تُستخدم لتخزين الصور الرقمية bitmap. هذه الصور مستقلة عن محول الرسوميات وتُسمى أيضًا تنسيق ملف bitmap المستقل عن الجهاز (DIB).
يمكنك تحويل BMP إلى PDF باستخدام Aspose.PDF لواجهة برمجة تطبيقات Java. لذلك، يمكنك اتباع الخطوات التالية لتحويل صور BMP:

1. تهيئة مستند جديد
1. تحميل ملف صورة BMP نموذجي
1. وأخيرًا، حفظ ملف PDF الناتج

لذلك، يتبع مقتطف الشيفرة التالي هذه الخطوات ويظهر كيفية تحويل BMP إلى PDF باستخدام Java:

```java
public void convertBMPtoPDF () {
        // تهيئة كائن المستند
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

        // تحميل ملف صورة BMP نموذجي
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "BMP-to-PDF.pdf");

        // حفظ المستند الناتج
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```