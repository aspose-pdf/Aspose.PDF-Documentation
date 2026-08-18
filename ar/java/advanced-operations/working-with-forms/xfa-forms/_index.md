---
title: العمل مع نماذج XFA
linktitle: نماذج XFA
type: docs
weight: 20
url: /java/xfa-forms/
description: تعرف على كيفية تحويل نماذج XFA إلى AcroForms القياسية في مستندات PDF باستخدام Aspose.PDF لـ Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بتحويل نماذج PDF المستندة إلى XFA إلى AcroForms القياسية باستخدام Java
Abstract: تشرح هذه المقالة كيفية العمل مع النماذج المستندة إلى XFA باستخدام Aspose.PDF لـ Java. وهو يغطي تحويل نموذج XFA الديناميكي إلى AcroForm قياسي ومعالجة مستندات XFA التي تتطلب خيار عرض تجاهل الاحتياجات قبل التحويل.
---
يمكن تحويل نماذج XFA إلى AcroForms القياسية حتى يمكن معالجتها باستخدام واجهات برمجة تطبيقات نماذج PDF العادية.

## تحويل نموذج XFA ديناميكي إلى AcroForm

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالوصول إلى المستند [النموذج](https://reference.aspose.com/pdf/java/com.aspose.pdf/form/) وقم بتعيين خصائص [FormType](https://reference.aspose.com/pdf/java/com.aspose.pdf/formtype/) المطلوبة.
1. احفظ ملف PDF المحدث [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void convertDynamicXfaToAcroform(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getForm().setType(FormType.Standard);
        document.save(outputFile.toString());
    }
}
```

## تحويل نموذج XFA باستخدام `ignoreNeedsRendering`

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالوصول إلى المستند [النموذج](https://reference.aspose.com/pdf/java/com.aspose.pdf/form/) وقم بتعيين خصائص `ignoreNeedsRendering` و[FormType](https://reference.aspose.com/pdf/java/com.aspose.pdf/formtype/) المطلوبة.
1. احفظ ملف PDF المحدث [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void convertXfaFormWithIgnoreNeedsRendering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (!document.getForm().getNeedsRendering() && document.getForm().hasXfa()) {
            document.getForm().setIgnoreNeedsRendering(true);
        }
        document.getForm().setType(FormType.Standard);
        document.save(outputFile.toString());
    }
}
```
