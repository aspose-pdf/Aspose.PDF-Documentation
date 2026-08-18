---
title: إضافة تلميحات الأدوات إلى نص PDF في Java
linktitle: تلميح أداة PDF
type: docs
weight: 20
url: /java/pdf-tooltip/
description: تعرف على كيفية إضافة تلميحات الأدوات إلى أجزاء النص في مستندات PDF في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أضف تلميحات أدوات تفاعلية إلى أجزاء نص PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية إضافة تعليمات تفاعلية إلى نص PDF باستخدام Aspose.PDF لـ Java. وهو يغطي إرفاق نص تلميح الأداة بحقول الأزرار غير المرئية الموضوعة فوق أجزاء النص المطابقة وإنشاء حقل نص مخفي يظهر عندما يدخل المؤشر إلى منطقة المشغل.
---
يتيح لك Aspose.PDF for Java إضافة مساعدة تفاعلية عن طريق وضع حقول النموذج فوق أجزاء النص.

## أضف تلميحات الأدوات إلى النص المطابق

استخدم هذا المثال عندما يُظهر النص الموجود في ملف PDF تلميح أداة عند التمرير.

1. قم بإنشاء نموذج PDF وأعد فتحه للتحرير.
1. ابحث في أجزاء النص المستهدف باستخدام `TextFragmentAbsorber`.
1. ضع `ButtonField` تراكبات على النص المطابق وقم بتعيين نص تلميح الأداة.
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

## إظهار كتلة نصية عائمة عند التمرير

استخدم هذا المثال عندما يؤدي التمرير فوق منطقة النص إلى الكشف عن حقل نص مخفي.

1. قم بإنشاء نموذج PDF وأعد فتحه للتحرير.
1. ابحث عن جزء نص التشغيل باستخدام `TextFragmentAbsorber`.
1. أنشئ `TextBoxField` مخفيًا و`ButtonField` باستخدام إجراءات الدخول والخروج.
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
