---
title: إضافة تلميحات إلى نص PDF في جافا
linktitle: تلميح PDF
type: docs
weight: 20
url: /ar/java/pdf-tooltip/
description: تعلم كيفية إضافة تلميحات إلى مقتطفات النص في مستندات PDF باستخدام جافا.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة تلميحات تفاعلية إلى مقتطفات نص PDF باستخدام جافا
Abstract: توضح هذه المقالة كيفية إضافة مساعدة تفاعلية إلى نص PDF باستخدام Aspose.PDF for Java. وتغطي إرفاق نص التلميح إلى حقول أزرار غير مرئية موضوعة فوق مقتطفات النص المتطابقة وإنشاء حقل نص مخفي يظهر عندما يدخل المؤشر منطقة المشغل.
---
يتيح لك Aspose.PDF for Java إضافة مساعدة تفاعلية عن طريق وضع حقول النماذج فوق مقتطفات النص.

## إضافة تلميحات إلى النص المتطابق

استخدم هذا المثال عندما يجب أن يظهر النص في PDF تلميحًا عند التحويم.

1. إنشاء ملف PDF عينة وإعادة فتحه للتحرير.
1. ابحث عن شظايا النص المستهدف باستخدام `TextFragmentAbsorber`.
1. مكان `ButtonField` يضع تغطيـات على النص المتطابق ويعيّن نص التلميح.
1. احفظ المستند المحدث.

```java
public static void addToolTipToSearchedText(Path outputFile) {
        Document document = new Document();
        document.getPages().add().getParagraphs()
                .add(new TextFragment("Move the mouse cursor here to display a tooltip"));
        document.getPages().get_Item(1).getParagraphs()
                .add(new TextFragment("Move the mouse cursor here to display a very long tooltip"));
        document.save(outputFile.toString());
        document.close();

        document = new Document(outputFile.toString());
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(
                "Move the mouse cursor here to display a tooltip");
        document.getPages().accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
            field.setAlternateName("Tooltip for text.");
            document.getForm().add(field);
        }

        absorber = new TextFragmentAbsorber("Move the mouse cursor here to display a very long tooltip");
        document.getPages().accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
            field.setAlternateName("Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
                    + " sed do eiusmod tempor incididunt ut labore et dolore magna"
                    + " aliqua. Ut enim ad minim veniam, quis nostrud exercitation"
                    + " ullamco laboris nisi ut aliquip ex ea commodo consequat."
                    + " Duis aute irure dolor in reprehenderit in voluptate velit"
                    + " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint"
                    + " occaecat cupidatat non proident, sunt in culpa qui officia"
                    + " deserunt mollit anim id est laborum.");
            document.getForm().add(field);
        }

        document.save(outputFile.toString());
        document.close();
    }
```

## إظهار كتلة نص عائمة عند التحويم

استخدم هذا المثال عندما يؤدي التحويم فوق منطقة النص إلى إظهار حقل نص مخفي.

1. إنشاء ملف PDF عينة وإعادة فتحه للتحرير.
1. ابحث عن جزء النص المشغّل باستخدام `TextFragmentAbsorber`.
1. إنشاء مخفي `TextBoxField` و `ButtonField` مع إجراءات الدخول والخروج.
1. احفظ ملف PDF النهائي.

```java
public static void createHiddenTextBlock(Path outputFile) {
    Document document = new Document();
    document.getPages().add().getParagraphs()
            .add(new TextFragment("Move the mouse cursor here to display floating text"));
    document.save(outputFile.toString());
    document.close();

    document = new Document(outputFile.toString());
    TextFragmentAbsorber absorber = new TextFragmentAbsorber(
            "Move the mouse cursor here to display floating text");
    document.getPages().accept(absorber);
    TextFragment fragment = absorber.getTextFragments().get_Item(1);

    TextBoxField floatingField = new TextBoxField(
            fragment.getPage(), new Rectangle(100.0, 700.0, 220.0, 740.0, false));
    floatingField.setValue("This is the \"floating text field\".");
    floatingField.setReadOnly(true);
    floatingField.setFlags(floatingField.getFlags() | AnnotationFlags.Hidden);
    floatingField.setPartialName("FloatingField_1");
    floatingField.setDefaultAppearance(new DefaultAppearance("Helv", 10, java.awt.Color.BLUE));
    floatingField.getCharacteristics().setBackground(java.awt.Color.CYAN);
    floatingField.getCharacteristics().setBorder(java.awt.Color.BLUE);
    floatingField.setBorder(new Border(floatingField));
    floatingField.getBorder().setWidth(1);
    floatingField.setMultiline(true);

    document.getForm().add(floatingField);

    ButtonField buttonField = new ButtonField(fragment.getPage(), fragment.getRectangle());
    buttonField.getAnnotationActions().setOnEnter(new HideAction(floatingField, false));
    buttonField.getAnnotationActions().setOnExit(new HideAction(floatingField));

    document.getForm().add(buttonField);
    document.save(outputFile.toString());
    document.close();
}
```
