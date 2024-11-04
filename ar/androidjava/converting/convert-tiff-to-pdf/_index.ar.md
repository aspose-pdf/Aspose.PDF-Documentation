---
title: Convert TIFF to PDF 
linktitle: Convert TIFF to PDF
type: docs
weight: 210
url: /androidjava/convert-tiff-to-pdf/
lastmod: "2021-06-05"
description: يسمح Aspose.PDF لنظام Android عبر Java بتحويل الصور متعددة الصفحات أو متعددة الإطارات من نوع TIFF إلى تطبيقات PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF لنظام Android عبر Java** يدعم تنسيق الملف، سواء كان صورة <abbr title="تنسيق ملف صورة موسوم">TIFF</abbr> بإطار واحد أو متعددة الإطارات. هذا يعني أنه يمكنك تحويل صورة TIFF إلى PDF في تطبيقات Java الخاصة بك.

TIFF أو TIF، تنسيق ملف صورة موسوم، يمثل الصور النقطية التي تُستخدم على مجموعة متنوعة من الأجهزة التي تتوافق مع معيار تنسيق هذا الملف.
 يمكن أن تحتوي صورة TIFF على عدة إطارات مع صور مختلفة. يتم دعم تنسيق ملف Aspose.PDF أيضًا، سواء كانت صورة TIFF بإطار واحد أو متعددة الإطارات. لذا يمكنك تحويل صورة TIFF إلى PDF في تطبيقات Java الخاصة بك. لذلك، سننظر في مثال لتحويل صورة TIFF متعددة الصفحات إلى مستند PDF متعدد الصفحات بالخطوات التالية:

1. إنشاء مثيل لفئة Document
1. تحميل صورة TIFF المدخلة
1. الحصول على FrameDimension للإطارات
1. إضافة صفحة جديدة لكل إطار
1. وأخيرًا، حفظ الصور في صفحات PDF

علاوة على ذلك، يوضح مقتطف الشفرة التالي كيفية تحويل صورة TIFF متعددة الصفحات أو متعددة الإطارات إلى PDF:

```java
 public void convertTIFFtoPDF () {
        // تهيئة كائن الوثيقة
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.tiff");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // تحميل ملف صورة TIFF النموذجية
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "TIFF-to-PDF.pdf");

        // حفظ وثيقة الإخراج
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```