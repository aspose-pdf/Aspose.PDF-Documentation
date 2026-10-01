---
title: إضافة طوابع نصية إلى PDF باستخدام Java
linktitle: طوابع نصية في ملف PDF
type: docs
weight: 20
url: /ar/java/text-stamps-in-the-pdf-file/
description: تعلم كيفية إضافة طوابع نصية إلى مستندات PDF باستخدام Java.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة طوابع نصية إلى ملفات PDF باستخدام Java
Abstract: يشرح هذا المقال كيفية إضافة طوابع نصية إلى ملفات PDF باستخدام Aspose.PDF for Java. يغطي إنشاء طابع نصي كخلفية، وتحديد موقعه، وتدويره، وتخصيص الخط والحجم والنمط واللون.
---
استخدم الطوابع النصية عندما تحتاج إلى إضافة تسميات مرئية أو علامات مائية إلى صفحات PDF.

## إضافة ختم نصي

استخدم هذا المثال عندما يجب أن تُظهر صفحة ختم نصي مُدوَّر مع تنسيق مخصص.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إنشاء [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstamp/) وتكوين موضعه ومظهر النص.
1. أضف الختم إلى الصفحة المستهدفة واحفظ المستند.

```java
public static void addTextStamp(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextStamp textStamp = new TextStamp("Sample Stamp");
        textStamp.setBackground(true);
        textStamp.setXIndent(100);
        textStamp.setYIndent(100);
        textStamp.setRotate(Rotation.on90);
        textStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        textStamp.getTextState().setFontSize(14.0f);
        textStamp.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        textStamp.getTextState().setForegroundColor(Color.getDarkGreen());
        document.getPages().get_Item(1).addStamp(textStamp);
        document.save(outputFile.toString());
    }
}
```
