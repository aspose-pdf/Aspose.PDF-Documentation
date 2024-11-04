---
title: تحويل PNG إلى PDF 
linktitle: تحويل PNG إلى PDF
type: docs
weight: 200
url: /androidjava/convert-png-to-pdf/
lastmod: "2021-06-05"
description: توضح هذه المقالة كيفية تحويل PNG إلى PDF باستخدام مكتبة Aspose.PDF في تطبيقات Android عبر Java. يمكنك تحويل صور PNG إلى تنسيق PDF باستخدام خطوات بسيطة.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** تدعم ميزة تحويل صور PNG إلى تنسيق PDF. تحقق من مقتطف الكود التالي لتحقيق مهمتك.

يشير <abbr title="Graphics الشبكة المحمولة">PNG</abbr> إلى نوع من تنسيقات ملفات الصور النقطية التي تستخدم الضغط بدون فقدان، مما يجعلها شائعة بين مستخدميها.

يمكنك تحويل صورة PNG إلى PDF باستخدام الخطوات التالية:

1. تحميل صورة PNG المدخلة
2. قراءة قيم الطول والعرض
3. إنشاء مستند جديد وإضافة صفحة
4. ضبط أبعاد الصفحة
5. حفظ الملف الناتج

علاوة على ذلك، يوضح مقتطف الكود أدناه كيفية تحويل PNG إلى PDF في تطبيقات Java الخاصة بك:

```java
    public void convertPNGtoPDF () {
        // تهيئة كائن المستند
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