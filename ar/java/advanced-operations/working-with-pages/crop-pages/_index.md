---
title: قص صفحات PDF في Java
linktitle: قص صفحات PDF
type: docs
weight: 70
url: /ar/java/crop-pages/
description: تعلم كيفية قص صفحات PDF وضبط صناديق القص، والتقليم، والدم، والوسائط في Java.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قص الصفحات وضبط صناديق الصفحات في ملفات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية قص صفحات PDF باستخدام Aspose.PDF for Java. وهي تغطي تعيين مستطيل قص جديد لصناديق القص، والتقليم، والفن، والدم، وكذلك قص صفحة تلقائيًا استنادًا إلى محتوى الصورة المكتشف.
---
يسمح لك Aspose.PDF for Java بقص الصفحات إما عن طريق إحداثيات الصناديق الصريحة أو استنادًا إلى المحتوى المكتشف.

## اقتصاص صفحة عن طريق ضبط صناديق الصفحة

استخدم هذا المثال عندما تحتاج إلى تطبيق نفس منطقة القص على صناديق الصفحة الرئيسية.

1. افتح PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ الاقتصاص الجديد [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. طبّق المستطيل على صناديق الصفحات المتعلقة بالاقتصاص واحفظ المستند.

```java
public static void cropPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle newBox = new Rectangle(200, 220, 2170, 1520, true);
        document.getPages().get_Item(1).setCropBox(newBox);
        document.getPages().get_Item(1).setTrimBox(newBox);
        document.getPages().get_Item(1).setArtBox(newBox);
        document.getPages().get_Item(1).setBleedBox(newBox);
        document.save(outputFile.toString());
    }
}
```

## قص صفحة بناءً على المحتوى المكتشف

استخدم هذا المثال عندما يجب أن يُستمدّ منطقة القص من أول صورة مكتشفة في الصفحة.

1. افتح PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. استخدم [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) لكشف مواضع الصور.
1. حدّد صندوق القص إلى مستطيل الصورة إذا تم العثور عليه، ثم احفظ المستند.

```java
public static void cropPageByContent(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);
        if (absorber.getImagePlacements().size() > 0) {
            document.getPages().get_Item(1).setCropBox(absorber.getImagePlacements().get_Item(1).getRectangle());
        } else {
            System.out.println("No images found on the first page");
        }
        document.save(outputFile.toString());
    }
}
```
