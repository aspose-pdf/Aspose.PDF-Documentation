---
title: التعليقات التوضيحية التفاعلية باستخدام جافا
linktitle: التعليقات التوضيحية التفاعلية
type: docs
weight: 60
url: /java/interactive-annotations/
description: تعرف على كيفية إضافة التعليقات التوضيحية للروابط وفحصها وحذفها في مستندات PDF باستخدام Aspose.PDF لـ Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: العمل مع تعليقات PDF التفاعلية في Java.
Abstract: تشرح هذه المقالة كيفية التعامل مع التعليقات التوضيحية للارتباط التفاعلي في ملفات PDF باستخدام Aspose.PDF لـ Java. ويغطي تحديد موقع النص، وإنشاء تعليق توضيحي للرابط فوق منطقة النص المطابق، وقراءة التعليقات التوضيحية للرابط الموجود، وحذفها.
---
تركز التعليقات التوضيحية التفاعلية في هذا القسم على عمليات سير العمل المستندة إلى الارتباط والأزرار والتي تستجيب لإجراءات المستخدم داخل عارض PDF.

## إضافة تعليق توضيحي للارتباط

استخدم هذا المثال عندما تحتاج إلى وضع رابط قابل للنقر فوق النص الموجود في الصفحة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. حدد موقع جزء النص المستهدف وقم بإنشاء [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) فوق المستطيل الخاص به.
1. قم بتعيين [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/) واحفظ المستند المحدث.

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

## الحصول على التعليقات التوضيحية الارتباط

يقوم هذا المثال بمسح مجموعة التعليقات التوضيحية للصفحة والإبلاغ عن موقع كل تعليق توضيحي للرابط.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. كرر من خلال التعليقات التوضيحية على الصفحة المستهدفة.
1. قم بتصفية التعليقات التوضيحية حسب [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Link` واطبع مستطيلاتها.

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

## حذف التعليقات التوضيحية للارتباط

استخدم هذا الأسلوب عندما يجب إزالة التعليقات التوضيحية للرابط الموجود من الصفحة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
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

## إضافة تعليق توضيحي للخط

يقوم هذا المثال بإنشاء تعليق توضيحي لخط تفاعلي مع أنماط الأسهم وإعدادات الحدود وملاحظة منبثقة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [LineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/lineannotation/) بنقاط البداية والنهاية.
1. قم بتكوين مظهره والتعليق التوضيحي المنبثق، ثم احفظ المستند.

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

استخدم هذا المثال عندما يجب أن يتضمن ملف PDF أزرار الصفحة السابقة والصفحة التالية للتنقل التفاعلي.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وتأكد من أن المستند يحتوي على الصفحات المطلوبة.
1. قم بإنشاء عناصر تحكم [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) باستخدام إجراءات التنقل المحددة مسبقًا.
1. أضف الأزرار إلى مجموعة النماذج واحفظ المستند المحدث.

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

## إضافة زر الطباعة

يقوم هذا المثال بإنشاء زر يقوم بتشغيل أمر الطباعة عندما يقوم المستخدم بالنقر فوقه.

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة.
1. قم بإنشاء [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) وقم بتعيين إجراء الطباعة المحدد مسبقًا.
1. قم بتكوين حدود الزر وخلفيته، وأضفهما إلى النموذج، ثم احفظ المستند.

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
