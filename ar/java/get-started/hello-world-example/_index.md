---
title: مثال مرحبا بالعالم بلغة جافا
linktitle: مثال مرحبا بالعالم
type: docs
weight: 40
url: ar/java/hello-world-example/
description: توضح هذه الصفحة كيفية استخدام البرمجة البسيطة لإنشاء مستند PDF يحتوي على نص - مرحبا بالعالم باستخدام Aspose.PDF for Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## مثال مرحبا بالعالم

يتم استخدام مثال "مرحبا بالعالم" تقليديًا لتقديم ميزات لغة البرمجة أو البرنامج بحالة استخدام بسيطة.

تمكن Aspose.PDF for Java API مطوري تطبيقات جافا من إنشاء وقراءة وتحرير ومعالجة ملفات PDF في تطبيقاتهم. يتيح لك قراءة وتحويل عدة أنواع مختلفة من الملفات إلى ومن صيغة ملف PDF. تُظهر هذه المقالة حول مرحبا بالعالم كيفية إنشاء ملف PDF في جافا باستخدام Aspose.PDF for Java API. بعد [تثبيت Aspose.PDF for Java](/pdf/java/installation/) في بيئتك، يمكنك تنفيذ مثال الكود أدناه لمعرفة كيفية عمل Aspose.PDF API.

يتبع جزء الكود أدناه هذه الخطوات:

1. قم بإنشاء كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document)
1. أضف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page) إلى كائن المستند
1. أنشئ كائن [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment)
1. أضف TextFragment إلى مجموعة [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) الخاصة بالصفحة
1. احفظ مستند PDF الناتج

يُظهر المقتطف البرمجي التالي برنامج Hello World لعرض عمل Aspose.PDF لـ Java API.

```java
// تهيئة كائن المستند
Document document = new Document();
 
// إضافة صفحة
Page page = document.getPages().add();
 
// إضافة نص إلى الصفحة الجديدة
page.getParagraphs().add(new TextFragment("Hello World!"));
 
// حفظ ملف PDF المحدث
document.save("HelloWorld_out.pdf");
```