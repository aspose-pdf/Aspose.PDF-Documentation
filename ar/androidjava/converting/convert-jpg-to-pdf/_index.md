---
title: تحويل JPG إلى PDF 
linktitle: تحويل JPG إلى PDF 
type: docs
weight: 190
url: /ar/androidjava/convert-jpg-to-pdf/
lastmod: "2021-06-05"
description: تعلم كيفية تحويل صورة JPG بسهولة إلى ملف PDF. كما يمكنك تحويل صورة إلى PDF مع الاحتفاظ بنفس ارتفاع وعرض الصفحة.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

لا داعي للتساؤل عن كيفية تحويل JPG إلى PDF، لأن مكتبة Apose.PDF لأندرويد عبر Java توفر أفضل حل.

يمكنك بسهولة تحويل صور JPG إلى PDF باستخدام Aspose.PDF لأندرويد عبر Java باتباع الخطوات التالية:

1. تهيئة كائن من فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. تحميل صورة JPG وإضافتها إلى الفقرة
1. حفظ ملف PDF الناتج

يوضح مقتطف الكود أدناه كيفية تحويل صورة JPG إلى PDF:

```java
public void convertJPEGtoPDF () {
        // تهيئة كائن الوثيقة
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

        // تحميل ملف صورة JPEG التجريبي
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "JPEG-to-PDF.pdf");

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