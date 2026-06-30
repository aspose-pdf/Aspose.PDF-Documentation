---
title: تحويل TIFF إلى PDF
linktitle: تحويل TIFF إلى PDF
type: docs
weight: 210
url: /ar/androidjava/convert-tiff-to-pdf/
lastmod: "2026-06-30"
description: تتيح Aspose.PDF for Android عبر Java تحويل صور TIFF متعددة الصفحات أو متعددة الإطارات إلى تطبيقات PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** تنسيق ملف مدعوم، سواءً كان إطارًا واحدًا أو متعدد الإطارات <abbr title="Tag Image File Format">TIFF</abbr> صورة. هذا يعني أنك يمكنك تحويل صورة TIFF إلى PDF في تطبيقات Java الخاصة بك.

TIFF أو TIF، Tagged Image File Format، تمثل صورًا نقطية مخصصة للاستخدام على مجموعة متنوعة من الأجهزة التي تتوافق مع معيار هذا التنسيق. يمكن لصورة TIFF أن تحتوي على عدة إطارات بصور مختلفة. كما يتم دعم تنسيق Aspose.PDF، سواء كان إطارًا واحدًا أو صورة TIFF متعددة الإطارات. لذلك يمكنك تحويل صورة TIFF إلى PDF في تطبيقات Java الخاصة بك. وبالتالي، سنلقي نظرة على مثال لتحويل صورة TIFF متعددة الصفحات إلى مستند PDF متعدد الصفحات بالخطوات التالية:

1. إنشاء مثيل من الفئة Document
1. تحميل صورة TIFF المدخلة
1. احصل على FrameDimension للإطارات
1. أضف صفحة جديدة لكل إطار
1. أخيرًا، احفظ الصور إلى صفحات PDF

علاوة على ذلك، يوضح المقتطف البرمجي التالي كيف تقوم بتحويل صورة TIFF متعددة الصفحات أو متعددة الإطارات إلى PDF:

```java
 public void convertTIFFtoPDF () {
        // Initialize document object
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

        // Load sample TIFF image file
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "TIFF-to-PDF.pdf");

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

