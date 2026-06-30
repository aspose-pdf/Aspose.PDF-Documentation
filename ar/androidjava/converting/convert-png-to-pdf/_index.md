---
title: تحويل PNG إلى PDF
linktitle: تحويل PNG إلى PDF
type: docs
weight: 200
url: /ar/androidjava/convert-png-to-pdf/
lastmod: "2026-06-30"
description: توضح هذه المقالة كيفية تحويل PNG إلى PDF باستخدام مكتبة Aspose.PDF في نظام Android عبر تطبيقات Java. يمكنك تحويل صور PNG إلى تنسيق PDF باستخدام خطوات بسيطة.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** تدعم ميزة تحويل صور PNG إلى تنسيق PDF. تحقق من مقتطف الشيفرة التالي لتنفيذ مهمتك.

<abbr title="Portable Network Graphics">PNG</abbr> يشير إلى نوع من تنسيقات ملفات الصور النقطية التي تستخدم ضغطًا بدون فقدان، مما يجعله شائعًا بين مستخدميه.

يمكنك تحويل PNG إلى صورة PDF باستخدام الخطوات التالية:

1. تحميل صورة PNG المدخلة
1. قراءة قيم الارتفاع والعرض
1. إنشاء مستند جديد وإضافة صفحة
1. تعيين أبعاد الصفحة
1. حفظ ملف الإخراج

علاوة على ذلك، يوضح مقطع الشيفرة أدناه كيفية تحويل PNG إلى PDF في تطبيقات Java الخاصة بك:

```java
    public void convertPNGtoPDF () {
        // Initialize document object
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.png");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
```

