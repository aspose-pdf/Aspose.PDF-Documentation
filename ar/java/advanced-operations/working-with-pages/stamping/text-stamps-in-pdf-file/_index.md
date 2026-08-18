---
title: إضافة طوابع نصية إلى PDF في Java
linktitle: الطوابع النصية في ملف PDF
type: docs
weight: 20
url: /java/text-stamps-in-the-pdf-file/
description: تعرف على كيفية إضافة طوابع نصية إلى مستندات PDF في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أضف طوابع نصية إلى ملفات PDF باستخدام Java
Abstract: يشرح هذا المقال كيفية إضافة طوابع نصية إلى ملفات PDF باستخدام Aspose.PDF لـ Java. ويغطي إنشاء ختم نص الخلفية وتحديد موضعه وتدويره وتخصيص الخط والحجم والنمط واللون.
---
استخدم الطوابع النصية عندما تحتاج إلى إضافة تسميات مرئية أو علامات مائية إلى صفحات PDF.

## أضف ختمًا نصيًا

استخدم هذا المثال عندما يجب أن تعرض الصفحة طابعًا نصيًا مستديرًا بنمط مخصص.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstamp/) وقم بتكوين موضعه ومظهر النص.
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
