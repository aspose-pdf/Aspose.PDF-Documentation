---
title: حذف النماذج من PDF في Java
linktitle: حذف النماذج
type: docs
weight: 70
url: /java/remove-form/
description: قم بإزالة كائنات النموذج من صفحات PDF باستخدام Aspose.PDF لـ Java، بما في ذلك التنظيف الكامل والحذف المستهدف.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بإزالة موارد النموذج من صفحات PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية إزالة موارد النموذج من مستندات PDF باستخدام Aspose.PDF لـ Java. ويغطي مسح جميع النماذج من الصفحة وحذف موارد نموذج الآلة الكاتبة المحددة فقط بعد تصفية مجموعة نماذج الصفحة.
---
تقوم هذه الأمثلة بإزالة موارد النموذج من الصفحة بدلاً من مجرد تغيير قيم الحقول.

## إزالة كافة موارد النموذج من الصفحة

استخدم هذا المثال عندما يجب إزالة كل مورد النموذج الموجود على الصفحة المحددة في عملية واحدة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالوصول إلى [XFormCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/xformcollection/) للصفحة المستهدفة.
1. Clear the collection and save the updated document.

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

استخدم هذا المثال عندما يجب حذف موارد النموذج المحددة فقط، مثل نماذج الآلة الكاتبة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالوصول إلى [XFormCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/xformcollection/) للصفحة المستهدفة.
1. قم بتصفية موارد [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) التي تريد إزالتها وحذفها من المجموعة.
1. احفظ ملف PDF المحدث [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
