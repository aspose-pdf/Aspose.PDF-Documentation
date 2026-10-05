---
title: إدارة رؤوس وتذييلات PDF باستخدام Java
linktitle: إدارة رؤوس وتذييلات PDF
type: docs
weight: 70
url: /ar/java/artifacts-header-footer/
description: تعلم كيفية إضافة وإزالة عناصر الرؤوس والتذييلات في مستندات PDF باستخدام Aspose.PDF for Java.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إضافة وتخصيص وإزالة رؤوس وتذييلات PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية إدارة أثار الرأس والتذييل في مستندات PDF باستخدام Aspose.PDF for Java. تغطي إنشاء كائنات `HeaderArtifact` و `FooterArtifact` القابلة لإعادة الاستخدام مع حالة نص مخصصة ومحاذاة، وإضافتها إلى صفحة، وحذف الأثار الحالية للرأس والتذييل.
---
أثار الرأس والتذييل هي عناصر ترقيم الصفحات غير المحتوى تُستخدم عادةً للتسميات المتكررة، ومعرِّفات الصفحات، وإطار التخطيط.

## إنشاء أثر رأس

استخدم هذا المساعد عندما تحتاج إلى أثر رأس قابل لإعادة الاستخدام مع تنسيق نص ثابت ومحاذاة.

1. أنشئ كائنًا من الفئة [HeaderArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerartifact/).
1. عيّن نصه وإعدادات الخط ولون المقدمة.
1. اضبط المحاذاة الأفقية وإرجاع artifact..

```java
public static HeaderArtifact createHeaderArtifact(String text) {
    HeaderArtifact artifact = new HeaderArtifact();
    artifact.setText(text);
    artifact.getTextState().setFontSize(14);
    artifact.getTextState().setFont(FontRepository.findFont("Arial"));
    artifact.getTextState().setForegroundColor(Color.getNavy());
    artifact.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
    return artifact;
}
```

## إنشاء كائن تذييل

هذه الدالة المساعدة تُنشئ كائن تذييل قابل لإعادة الاستخدام بنمط تنسيق مماثل لكائن العنوان.

1. أنشئ كائنًا من الفئة [FooterArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/footerartifact/).
1. عيّن النص، حالة النص، ولون المقدمة.
1. اضبط المحاذاة وإرجاع العنصر.

```java
public static FooterArtifact createFooterArtifact(String text) {
    FooterArtifact artifact = new FooterArtifact();
    artifact.setText(text);
    artifact.getTextState().setFontSize(14);
    artifact.getTextState().setFont(FontRepository.findFont("Arial"));
    artifact.getTextState().setForegroundColor(Color.getNavy());
    artifact.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
    return artifact;
}
```

## إضافة عنصر رأس

استخدم هذا المثال عندما يجب أن تعرض الصفحة عنصر رأس قابل لإعادة الاستخدام.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ عنصر الرأس عبر طريقة المساعد.
1. أضف العنصر إلى الصفحة واحفظ ملف الإخراج.

```java
public static void addHeaderArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HeaderArtifact header = createHeaderArtifact("Sample Header");
        document.getPages().get_Item(1).getArtifacts().add(header);
        document.save(outputFile.toString());
    }
}
```

## إضافة عنصر تذييل

استخدم هذا المثال عندما يجب أن تعرض الصفحة عنصر تذييل مع تنسيق قابل لإعادة الاستخدام.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ عنصر التذييل عبر طريقة المساعد.
1. أضف العنصر إلى الصفحة واحفظ ملف الإخراج.

```java
public static void addFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FooterArtifact footer = createFooterArtifact("Sample Footer");
        document.getPages().get_Item(1).getArtifacts().add(footer);
        document.save(outputFile.toString());
    }
}
```

## حذف عناصر الرأس والتذييل

استخدم هذا النهج عندما يجب إزالة عناصر الرأس والتذييل الموجودة من الصفحة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. مرّ على مجموعة عناصر الصفحة بترتيب عكسي.
1. احذف كائنات الترقيم التي نوعها الفرعي هو الرأس أو التذييل، ثم احفظ المستند.

```java
public static void deleteHeaderFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && (artifact.getSubtype() == Artifact.ArtifactSubtype.Header
                    || artifact.getSubtype() == Artifact.ArtifactSubtype.Footer)) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```
