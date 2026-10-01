---
title: العمل مع نماذج XFA
linktitle: نماذج XFA
type: docs
weight: 20
url: /ar/java/xfa-forms/
description: تعلم كيفية تحويل نماذج XFA إلى AcroForms قياسية في مستندات PDF باستخدام Aspose.PDF for Java.
lastmod: "2026-10-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تحويل نماذج PDF المستندة إلى XFA إلى AcroForms قياسية باستخدام Java
Abstract: تشرح هذه المقالة كيفية العمل مع النماذج المستندة إلى XFA باستخدام Aspose.PDF for Java. وتغطي تحويل نموذج XFA الديناميكي إلى AcroForm قياسي ومعالجة مستندات XFA التي تتطلب خيار ignore-needs-rendering قبل التحويل.
---
يمكن تحويل نماذج XFA إلى AcroForms قياسية حتى يمكن معالجتها باستخدام واجهات برمجة تطبيقات نماذج PDF العادية.

## تحويل نموذج XFA الديناميكي إلى AcroForm

1. فتح PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. الوصول إلى Document [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/form/) و تعيين المطلوب [FormType](https://reference.aspose.com/pdf/java/com.aspose.pdf/formtype/) الخصائص.
1. احفظ ملف PDF المحدث [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void convertDynamicXfaToAcroform(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getForm().setType(FormType.Standard);
        document.save(outputFile.toString());
    }
}
```

## تحويل نموذج XFA باستخدام `ignoreNeedsRendering`

1. فتح PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. الوصول إلى Document [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/form/) و تعيين المطلوب `ignoreNeedsRendering` و [FormType](https://reference.aspose.com/pdf/java/com.aspose.pdf/formtype/) الخصائص.
1. احفظ ملف PDF المحدث [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
