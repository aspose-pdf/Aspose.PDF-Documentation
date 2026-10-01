---
title: حذف الصور من ملف PDF باستخدام Java
linktitle: حذف الصور
type: docs
weight: 20
url: /ar/java/delete-images-from-pdf-file/
description: تعلم كيفية حذف الصور المدمجة من ملفات PDF باستخدام Java.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: حذف الصور المدمجة من ملفات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية حذف الصور من مستندات PDF باستخدام Aspose.PDF for Java. يزيل المثال مورد صورة من الصفحة الأولى بناءً على فهرسه في مجموعة صور الصفحة ثم يحفظ المستند المعدل.
---
استخدم مجموعة موارد صور الصفحة عندما تحتاج إلى إزالة الصور المدمجة من صفحة PDF.

## حذف صورة مدمجة حسب الفهرس

1. فتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. الوصول إلى موارد الصور على الهدف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. احذف الصورة المستهدفة من مجموعة موارد الصفحة حسب فهرسها.
1. احفظ ملف PDF المحدث [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void deleteImage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().get_Item(1).getResources().getImages().delete(1);
        document.save(outputFile.toString());
    }
}
```
