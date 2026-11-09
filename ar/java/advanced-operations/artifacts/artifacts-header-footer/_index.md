---
title: إضافة رؤوس الصفحات وتذييلاتها إلى PDF باستخدام Java
linktitle: إضافة الرؤوس والتذييلات
type: docs
weight: 70
url: /ar/java/artifacts-header-footer/
description: إنشاء عناصر رؤوس الصفحات وتذييلاتها وتنسيقها وإضافتها إلى صفحات PDF باستخدام Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة رؤوس الصفحات وتذييلاتها إلى PDF في Java
Abstract: إنشاء عناصر رؤوس الصفحات وتذييلاتها وتنسيقها وإضافتها إلى صفحات PDF.
---

تُستخدم عناصر رؤوس الصفحات وتذييلاتها لعرض تسميات متكررة ومعرّفات الصفحات وتنظيم تخطيطها.

## إنشاء عنصر رأس الصفحة

تنشئ الطريقة المساعدة عنصر رأس قابلًا لإعادة الاستخدام بتنسيق ومحاذاة موحّدين.

1. أنشئ كائنًا من الفئة [HeaderArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerartifact/).
1. اضبط نص العنصر وإعدادات الخط ولون النص.
1. اضبط المحاذاة الأفقية وأرجع العنصر.

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

## إنشاء عنصر تذييل الصفحة

تنشئ الطريقة المساعدة عنصر تذييل بتنسيق مماثل لتنسيق الرأس.

1. أنشئ كائنًا من الفئة [FooterArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/footerartifact/).
1. اضبط نص العنصر وحالة النص ولونه.
1. اضبط المحاذاة وأرجع العنصر.

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

## إضافة عنصر رأس الصفحة

يستخدم المثال الطريقة المساعدة لإضافة رأس منسّق إلى الصفحة الأولى.

1. افتح ملف PDF المصدر باستخدام الفئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ عنصر الرأس باستخدام الطريقة المساعدة.
1. أضف العنصر إلى الصفحة واحفظ ملف PDF الناتج.

```java
public static void addHeaderArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HeaderArtifact header = createHeaderArtifact("Sample Header");
        document.getPages().get_Item(1).getArtifacts().add(header);
        document.save(outputFile.toString());
    }
}
```

## إضافة عنصر تذييل الصفحة

يستخدم المثال الطريقة المساعدة لإضافة تذييل منسّق إلى الصفحة الأولى.

1. افتح ملف PDF المصدر باستخدام الفئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ عنصر التذييل باستخدام الطريقة المساعدة.
1. أضف العنصر إلى الصفحة واحفظ ملف PDF الناتج.

```java
public static void addFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FooterArtifact footer = createFooterArtifact("Sample Footer");
        document.getPages().get_Item(1).getArtifacts().add(footer);
        document.save(outputFile.toString());
    }
}
```

## مواضيع ذات صلة

- [إزالة الرؤوس والتذييلات](/pdf/ar/java/remove-headers-footers/)
- [العمل مع عناصر PDF](/pdf/ar/java/artifacts/)
