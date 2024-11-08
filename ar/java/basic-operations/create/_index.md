---
title: إنشاء مستند PDF
linktitle: إنشاء
type: docs
weight: 10
url: /ar/java/create-document/
description: تعلم كيفية إنشاء ملف PDF في Aspose.PDF لـ Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Java** API يسمح لمطوري تطبيقات جافا بدمج وظيفة معالجة مستندات PDF في تطبيقاتهم. يمكن استخدامه لإنشاء وقراءة ملفات PDF دون الحاجة إلى تثبيت أي برامج أخرى على الآلة الأساسية. يمكن استخدام Aspose.PDF لـ Java في أنواع مختلفة من تطبيقات Java مثل تطبيقات سطح المكتب، JSP، وJSF.

## كيفية إنشاء ملف PDF باستخدام Java

لإنشاء ملف PDF باستخدام Java، يمكن اتباع الخطوات التالية.

1. إنشاء كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. إضافة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) إلى كائن المستند
1. إنشاء كائن [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment)

1. أضف [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment) إلى مجموعة [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) في الصفحة
1. احفظ مستند PDF الناتج

```java
// تهيئة كائن المستند
Document document = new Document();

//إضافة صفحة
Page page = document.getPages().add();

// إضافة نص إلى الصفحة الجديدة
page.getParagraphs().add(new TextFragment("Hello World!"));

// حفظ ملف PDF المحدث
document.save("HelloWorld_out.pdf");
```