---
title: حذف النماذج من PDF في Java
linktitle: حذف النماذج
type: docs
weight: 70
url: /ar/java/remove-form/
description: إزالة كائنات النموذج من صفحات PDF باستخدام Aspose.PDF for Java، بما في ذلك التنظيف الكامل والحذف المستهدف.
lastmod: "2026-10-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إزالة موارد النموذج من صفحات PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية إزالة موارد النموذج من مستندات PDF باستخدام Aspose.PDF for Java. وتغطي مسح جميع النماذج من صفحة وحذف موارد نموذج Typewriter المحددة فقط بعد تصفية مجموعة نماذج الصفحة.
---
توضح هذه الأمثلة إزالة موارد النموذج من صفحة بدلاً من مجرد تغيير قيم الحقول.

## إزالة جميع موارد Form من صفحة

استخدم هذا المثال عندما يجب إزالة كل موارد Form على صفحة مختارة في عملية واحدة

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. الوصول إلى [XFormCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/xformcollection/) لصفحة الهدف.
1. امسح المجموعة واحفظ المستند المحدث.

```java
public static void removeAllForms(Path inputFile, int pageNum, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XFormCollection forms = document.getPages().get_Item(pageNum).getResources().getForms();
        forms.clear();
        document.save(outputFile.toString());
    }
}
```

## إزالة موارد النموذج المحددة

استخدم هذا المثال عندما يجب حذف موارد النموذج المحددة فقط، مثل نماذج الكاتب الآلي.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. الوصول إلى [XFormCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/xformcollection/) لصفحة الهدف.
1. تصفية [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) الموارد التي تريد إزالتها وحذفها من المجموعة.
1. احفظ ملف PDF المحدث [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void removeSpecifiedForm(Path inputFile, int pageNum, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XFormCollection forms = document.getPages().get_Item(pageNum).getResources().getForms();
        List<String> formNames = new ArrayList<>();
        for (XForm form : forms) {
            if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
                formNames.add(forms.getFormName(form));
            }
        }
        for (String formName : formNames) {
            forms.delete(formName);
        }
        document.save(outputFile.toString());
    }
}
```
