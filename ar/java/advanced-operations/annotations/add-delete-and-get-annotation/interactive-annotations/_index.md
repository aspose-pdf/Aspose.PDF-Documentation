---
title: التعليقات التفاعلية باستخدام جافا
linktitle: التعليقات التفاعلية
type: docs
weight: 60
url: /ar/java/interactive-annotations/
description: تعرّف على كيفية إضافة وفحص وحذف تعليقات الروابط في مستندات PDF باستخدام Aspose.PDF for Java.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: اعمل مع تعليقات PDF التفاعلية في Java.
Abstract: تُوضح هذه المقالة كيفية العمل مع تعليقات الارتباط التفاعلية في ملفات PDF باستخدام Aspose.PDF for Java. وتغطي تحديد النص، وإنشاء تعليق ارتباط فوق منطقة النص المتطابقة، وقراءة تعليقات الارتباط الموجودة، وحذفها.
---
تُركز التعليقات التوضيحية التفاعلية في هذا القسم على سير العمل القائم على الروابط والأزرار الذي يستجيب لإجراءات المستخدم داخل عارض PDF.

## إضافة تعليق ارتباط

استخدم هذا المثال عندما تحتاج إلى وضع رابط قابل للنقر فوق النص الموجود في الصفحة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. حدد مقطع النص المستهدف وأنشئ [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) فوق مستطيله.
1. تعيين [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/) وحفظ المستند المحدث.

```java
public static void linkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("file");
        document.getPages().get_Item(1).accept(textFragmentAbsorber);

        var phoneNumberFragment = textFragmentAbsorber.getTextFragments().get_Item(1);
        LinkAnnotation linkAnnotation = new LinkAnnotation(
                document.getPages().get_Item(1),
                phoneNumberFragment.getRectangle());
        linkAnnotation.setAction(new GoToURIAction("https://www.aspose.com"));

        document.getPages().get_Item(1).getAnnotations().add(linkAnnotation);
        document.save(outputFile.toString());
    }
}
```

## احصل على تعليقات الروابط

يتم في هذا المثال مسح مجموعة تعليقات الصفحة وإبلاغ موقع كل تعليق ارتباط.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. تكرار عبر التعليقات التوضيحية على الصفحة المستهدفة.
1. تصفية التعليقات التوضيحية حسب [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Link` وطبع مستطيلاتهم.

```java
public static void linkGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

## حذف تعليقات الارتباط

استخدم هذا النهج عندما يجب إزالة تعليقات الروابط الموجودة من الصفحة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. جمع التعليقات التوضيحية التي يكون نوعها [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Link`.
1. احذف التعليقات التوضيحية المجمعة واحفظ ملف الإخراج.

```java
public static void linkDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## إضافة تعليق خط

هذا المثال ينشئ تعليقا خطيًا تفاعليًا مع أنماط الأسهم وإعدادات الحدود وملاحظة منبثقة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إنشاء [LineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/lineannotation/) مع نقاط البدء والنهاية.
1. قم بتكوين مظهره وتعليق النافذة المنبثقة، ثم احفظ المستند.

```java
public static void lineAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        LineAnnotation lineAnnotation = new LineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(550, 93, 562, 439, true),
                new Point(556, 99),
                new Point(556, 443));

        lineAnnotation.setTitle("John Smith");
        lineAnnotation.setColor(Color.getRed());
        lineAnnotation.setStartingStyle(LineEnding.OpenArrow);
        lineAnnotation.setEndingStyle(LineEnding.OpenArrow);

        Border border = new Border(lineAnnotation);
        border.setWidth(3);
        lineAnnotation.setBorder(border);

        PopupAnnotation popup = new PopupAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(842, 124, 1021, 266, true));
        lineAnnotation.setPopup(popup);

        document.getPages().get_Item(1).getAnnotations().add(lineAnnotation);
        document.save(outputFile.toString());
    }
}
```

## إضافة أزرار التنقل

استخدم هذا المثال عندما يجب أن يحتوي ملف PDF على أزرار الصفحة السابقة والصفحة التالية للتنقل التفاعلي.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وتأكد من أن المستند يحتوي على الصفحات المطلوبة.
1. إنشاء [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) عناصر التحكم مع إجراءات التنقل المعرفة مسبقًا.
1. أضف الأزرار إلى مجموعة Form واحفظ المستند المحدث.

```java
public static void navigationButtonsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().add();

        record ButtonConfig(String name, double xPos, PredefinedAction action) {}
        List<ButtonConfig> buttonConfigs = List.of(
                new ButtonConfig("Previous Page", 120.0, PredefinedAction.PrevPage),
                new ButtonConfig("Next Page", 230.0, PredefinedAction.NextPage));

        for (Page page : document.getPages()) {
            for (ButtonConfig config : buttonConfigs) {
                Rectangle rect = new Rectangle(config.xPos(), 10.0, config.xPos() + 100, 40.0, true);
                ButtonField button = new ButtonField(page, rect);
                button.setPartialName(config.name());
                button.setValue(config.name());
                button.getCharacteristics().setBorder(Color.getRed());
                button.getCharacteristics().setBackground(Color.getOrange().toRgb());
                button.getAnnotationActions().setOnReleaseMouseBtn(new NamedAction(config.action()));
                document.getForm().add(button);
            }
        }
        document.save(outputFile.toString());
    }
}
```

## إضافة زر طباعة

هذا المثال ينشئ زرًا يفعِّل أمر الطباعة عندما ينقر المستخدم عليه.

1. إنشاء PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحةً.
1. إنشاء [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) وتعيين الإجراء المسبق للطباعة.
1. قم بتكوين حدود الزر والخلفية، أضفه إلى النموذج، واحفظ المستند.

```java
public static void printButtonAdd(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Rectangle rect = new Rectangle(72, 748, 164, 768, true);
        ButtonField printButton = new ButtonField(page, rect);
        printButton.setAlternateName("Print current document");
        printButton.setColor(Color.getBlack());
        printButton.setPartialName("printBtn1");
        printButton.setValue("Print Document");
        printButton.getAnnotationActions().setOnReleaseMouseBtn(
                new NamedAction(PredefinedAction.File_Print));

        Border border = new Border(printButton);
        border.setStyle(BorderStyle.Solid);
        border.setWidth(2);
        printButton.setBorder(border);

        printButton.getCharacteristics().setBorder(Color.getBlue());
        printButton.getCharacteristics().setBackground(Color.getLightBlue().toRgb());

        document.getForm().add(printButton);
        document.save(outputFile.toString());
    }
}
```
