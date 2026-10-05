---
title: استخراج الصور من PDF باستخدام Java
linktitle: استخراج الصور من PDF
type: docs
weight: 20
url: /ar/java/extract-images-from-the-pdf-file/
description: تعرّف على كيفية استخراج الصور المدمجة من ملفات PDF باستخدام Aspose.PDF for Java.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية استخراج الصور من PDF عبر Java
Abstract: تشرح هذه المقالة كيفية استخراج الصور المدمجة من مستند PDF باستخدام Aspose.PDF for Java. توضح كيفية فتح ملف PDF المصدر، والوصول إلى صورة من مجموعة موارد الصفحة، وحفظ XImage المستخرج إلى ملف خارجي.
---
استخراج الصور من صفحات PDF عندما تحتاج إلى إعادة استخدام الرسومات المدمجة، أو فحص أصول المستند، أو تصدير الصور للمعالجة اللاحقة.

1. افتح ملف PDF المصدر في كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وافتح تدفق إخراج لملف الصورة المستخرجة.
1. احصل على الهدف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) من المستند والوصول إلىه مجموعة `Resources.Images`.
1. استرجع الكائن المطلوب [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) من مجموعة الصور تلك بواسطة الفهرس.
1. استدعِ `image.save(outputImage)` لكتابة بايتات الصورة المستخرجة إلى التدفق الهدف.

```java
public static void extractImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         OutputStream outputImage = Files.newOutputStream(outputFile)) {
        XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(1);
        image.save(outputImage);
    }
}
```
