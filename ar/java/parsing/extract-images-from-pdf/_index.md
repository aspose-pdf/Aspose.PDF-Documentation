---
title: استخراج الصور من PDF باستخدام جافا
linktitle: استخراج الصور من قوات الدفاع الشعبي
type: docs
weight: 20
url: /java/extract-images-from-the-pdf-file/
description: تعرف على كيفية استخراج الصور المضمنة من ملفات PDF باستخدام Aspose.PDF لـ Java.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية استخراج الصور من PDF عبر جافا
Abstract: تشرح هذه المقالة كيفية استخراج الصور المضمنة من مستند PDF باستخدام Aspose.PDF لـ Java. يوضح كيفية فتح ملف PDF المصدر، والوصول إلى صورة من مجموعة موارد الصفحة، وحفظ XImage المستخرج في ملف خارجي.
---
قم باستخراج الصور من صفحات PDF عندما تحتاج إلى إعادة استخدام الرسومات المضمنة، أو فحص أصول المستند، أو تصدير الصور للمعالجة النهائية.

1. افتح ملف PDF المصدر في مثيل [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وافتح دفق الإخراج لملف الصورة المستخرج.
1. احصل على [الصفحة] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) المستهدفة من المستند وقم بالوصول إلى مجموعتها `Resources.Images`.
1. قم باسترداد كائن [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) المطلوب من مجموعة الصور هذه بواسطة الفهرس.
1. اتصل `image.save(outputImage)` لكتابة بايتات الصورة المستخرجة إلى الدفق الهدف.

```java
public static void extractImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         OutputStream outputImage = Files.newOutputStream(outputFile)) {
        XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(1);
        image.save(outputImage);
    }
}
```
