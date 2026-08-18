---
title: إدارة رؤوس وتذييلات PDF باستخدام Java
linktitle: إدارة رؤوس وتذييلات PDF
type: docs
weight: 70
url: /java/artifacts-header-footer/
description: تعرف على كيفية إضافة عناصر الرؤوس والتذييلات وإزالتها في مستندات PDF باستخدام Aspose.PDF لـ Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إضافة رؤوس وتذييلات PDF وتخصيصها وإزالتها باستخدام Java
Abstract: يشرح هذا المقال كيفية إدارة عناصر الرأس والتذييل في مستندات PDF باستخدام Aspose.PDF لـ Java. ويغطي إنشاء كائنات `HeaderArtifact` و@KEEP_1@@ قابلة لإعادة الاستخدام بحالة نصية ومحاذاة مخصصة، وإضافتها إلى الصفحة، وحذف عناصر الرأس والتذييل الموجودة.
---
عناصر الرأس والتذييل هي عناصر ترقيم صفحات غير متعلقة بالمحتوى تُستخدم بشكل شائع للتسميات المتكررة ومعرفات الصفحة وتأطير التخطيط.

## إنشاء قطعة أثرية رأس

استخدم هذا المساعد عندما تحتاج إلى قطعة رأس قابلة لإعادة الاستخدام مع تصميم ومحاذاة نص متسقين.

1. قم بإنشاء [HeaderArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerartifact/).
1. اضبط النص وإعدادات الخط ولون المقدمة.
1. قم بتكوين المحاذاة الأفقية وإرجاع القطعة الأثرية.

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

## إنشاء قطعة أثرية تذييل

يقوم هذا المساعد بإنشاء عنصر تذييل قابل لإعادة الاستخدام بنفس نمط التصميم مثل عنصر الرأس.

1. قم بإنشاء [FooterArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/footerartifact/).
1. قم بتعيين النص وحالة النص ولون المقدمة.
1. قم بتكوين المحاذاة وإرجاع القطعة الأثرية.

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

## أضف قطعة أثرية للرأس

استخدم هذا المثال عندما يجب أن تعرض الصفحة قطعة رأس قابلة لإعادة الاستخدام.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء قطعة أثرية للرأس من خلال الطريقة المساعدة.
1. أضف القطعة الأثرية إلى الصفحة واحفظ ملف الإخراج.

```java
public static void addHeaderArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HeaderArtifact header = createHeaderArtifact("Sample Header");
        document.getPages().get_Item(1).getArtifacts().add(header);
        document.save(outputFile.toString());
    }
}
```

## إضافة قطعة أثرية تذييل

استخدم هذا المثال عندما يجب أن تعرض الصفحة عنصر تذييل بتنسيق قابل لإعادة الاستخدام.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء قطعة أثرية للتذييل من خلال الطريقة المساعدة.
1. أضف القطعة الأثرية إلى الصفحة واحفظ ملف الإخراج.

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

استخدم هذا الأسلوب عندما يجب إزالة عناصر الرأس والتذييل الموجودة من الصفحة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالتكرار عبر مجموعة عناصر الصفحة بترتيب عكسي.
1. احذف عناصر ترقيم الصفحات التي يكون نوعها الفرعي هو الرأس أو التذييل، ثم احفظ المستند.

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
