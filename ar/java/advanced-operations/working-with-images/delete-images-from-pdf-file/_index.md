---
title: حذف الصور من ملف PDF باستخدام Java
linktitle: حذف الصور
type: docs
weight: 20
url: /java/delete-images-from-pdf-file/
description: تعرف على كيفية حذف الصور المضمنة من ملفات PDF في Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: حذف الصور المضمنة من ملفات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية حذف الصور من مستندات PDF باستخدام Aspose.PDF لـ Java. يقوم المثال بإزالة مورد صورة من الصفحة الأولى بواسطة فهرسها في مجموعة صور الصفحة ثم يحفظ المستند المعدل.
---
استخدم مجموعة موارد صور الصفحة عندما تحتاج إلى إزالة الصور المضمنة من صفحة PDF.

## حذف صورة مضمنة حسب الفهرس

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. الوصول إلى موارد الصورة على الهدف [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. احذف الصورة المستهدفة من مجموعة موارد الصفحة بواسطة فهرسها.
1. احفظ ملف PDF المحدث [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void deleteImage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().get_Item(1).getResources().getImages().delete(1);
        document.save(outputFile.toString());
    }
}
```
