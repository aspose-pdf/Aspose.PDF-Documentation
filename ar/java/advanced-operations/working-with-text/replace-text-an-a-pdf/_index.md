---
title: استبدال النص في PDF بـ Java
linktitle: استبدال النص في PDF
type: docs
weight: 40
url: /java/replace-text-in-pdf/
description: تعرف على كيفية استبدال النص وإعادة ترتيبه وإزالته في مستندات PDF باستخدام Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: استبدال محتوى النص وإزالته وضبطه في PDF باستخدام Java
Abstract: تشرح هذه المقالة سير عمل استبدال النص في مستندات PDF باستخدام Aspose.PDF لـ Java. ويغطي استبدال النص في جميع الصفحات، وقصر الاستبدال على منطقة محددة، وضبط تخطيط الاستبدال، واستخدام المطابقة المستندة إلى regex، واستبدال الخطوط، وإزالة النص بالكامل، وحذف النص المخفي.
---
يوفر Aspose.PDF لـ Java كلاً من ميزات الاستبدال البسيطة والاستبدال المدركة للتخطيط من خلال `TextFragmentAbsorber` وخيارات الاستبدال.

## استبدال النص في كافة الصفحات

استخدم هذا المثال عندما يجب استبدال نفس العبارة في المستند بأكمله.

1. افتح مستند PDF المصدر.
1. ابحث في جميع الصفحات عن العبارة المستهدفة باستخدام `TextFragmentAbsorber`.
1. استبدل النص المطابق واحفظ ملف PDF المحدث.

```java
public static void replaceTextOnAllPages(Path inputFile, Path outputFile) {
        String searchPhrase = "PDF";
        String replacePhrase = "pdf";

        try (Document document = new Document(inputFile.toString())) {
            TextFragmentAbsorber absorber = new TextFragmentAbsorber(searchPhrase);
            document.getPages().accept(absorber);

            for (TextFragment fragment : absorber.getTextFragments()) {
                fragment.setText(replacePhrase);
            }

            document.save(outputFile.toString());
        }
    }
```

## استبدال النص في منطقة صفحة معينة

استخدم هذا المثال عندما يقتصر الاستبدال على مستطيل محدد في صفحة واحدة.

1. افتح مستند PDF المصدر.
1. قم بتكوين `TextSearchOptions` بحدود الصفحة والمستطيل المستهدف.
1. استبدل النص المطابق داخل تلك المنطقة واحفظ المستند.

```java
public static void replaceTextInParticularPageRegion(Path inputFile, Path outputFile) {
    String searchPhrase = "doc";
    String replacePhrase = "DOC";

    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(searchPhrase);
        absorber.getTextSearchOptions().setLimitToPageBounds(true);
        absorber.getTextSearchOptions().setRectangle(new Rectangle(300, 442, 500, 742, true));
        document.getPages().get_Item(1).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            fragment.setText(replacePhrase);
        }

        document.save(outputFile.toString());
    }
}
```

## استبدل النص واضبط التباعد داخل مستطيل مُزاح

استخدم هذا المثال عندما يجب أن يظل النص البديل على الصفحة مع تباعد مضبوط ولكن حجم الخط يجب أن يظل بدون تغيير.

1. افتح ملف PDF المصدر واجمع أجزاء النص من الصفحة المستهدفة.
1. قم بتعديل المستطيل البديل واختر السلوك `AdjustSpaceWidth`.
1. قم بتعيين النص الجديد وحفظ المستند.

```java
public static void replaceTextAndResizeAndShiftWithoutChangingFontSize(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        TextFragment fragment = absorber.getTextFragments().get_Item(1);
        String text = fragment.getText();
        Rectangle rectangle = fragment.getRectangle();
        rectangle.setLLX(rectangle.getLLX() + 50);
        rectangle.setURX(rectangle.getURX() - 50);
        fragment.getReplaceOptions().setRectangle(rectangle);
        fragment.getReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.AdjustSpaceWidth);
        fragment.setText(text + " " + text);

        document.save(outputFile.toString());
    }
}
```

## استبدل النص داخل مستطيل فقرة أكبر

استخدم هذا المثال عندما يجب توسيع النص البديل إلى مساحة صفحة أكبر.

1. افتح ملف PDF المصدر واحصل على جزء النص الأول من الصفحة المستهدفة.
1. قم ببناء مستطيل بديل أكبر من مربع وسائط الصفحة.
1. قم بتطبيق خيارات الاستبدال وحفظ ملف PDF.

```java
public static void replaceTextAndResizeAndShiftParagraph(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        TextFragment fragment = absorber.getTextFragments().get_Item(1);
        String text = fragment.getText();
        Rectangle rectangle = document.getPages().get_Item(1).getMediaBox();
        rectangle.setLLX(rectangle.getLLX() + 20);
        rectangle.setURX(rectangle.getURX() - 20);
        rectangle.setURY(rectangle.getURY() - 20);
        fragment.getReplaceOptions().setRectangle(rectangle);
        fragment.getReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.AdjustSpaceWidth);
        fragment.setText(text + " " + text);

        document.save(outputFile.toString());
    }
}
```

## استبدل النص وقم بقياس الخط لملء المستطيل

استخدم هذا المثال عندما يجب تكبير النص البديل لملء المنطقة المستهدفة.

1. افتح ملف PDF المصدر وقم بالوصول إلى جزء النص المستهدف.
1. حدد مستطيلًا بديلاً وقم بتمكين تعديل الخط `ScaleToFill`.
1. قم بتعيين النص الجديد واحفظ المستند المحدث.

```java
public static void replaceTextAndResizeAndExpandFont(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        TextFragment fragment = absorber.getTextFragments().get_Item(1);
        String text = fragment.getText();
        fragment.getReplaceOptions().setRectangle(new Rectangle(100, 300, 512, 692, true));
        fragment.getReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.AdjustSpaceWidth);
        fragment.getReplaceOptions().setFontSizeAdjustmentAction(TextReplaceOptions.FontSizeAdjustment.ScaleToFill);
        fragment.setText(text + " " + text);

        document.save(outputFile.toString());
    }
}
```

## استبدل النص وقم بتقليصه ليناسب النص

استخدم هذا المثال عندما يجب أن يبقى النص البديل داخل مستطيل النص الأصلي.

1. افتح ملف PDF المصدر وحدد الجزء المستهدف.
1. أعد استخدام مستطيل الجزء الحالي وقم بتمكين `ShrinkToFit`.
1. استبدل النص واحفظ المستند.

```java
public static void replaceTextAndFitTextIntoRectangle(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        TextFragment fragment = absorber.getTextFragments().get_Item(1);
        String text = fragment.getText();
        fragment.getReplaceOptions().setRectangle(fragment.getRectangle());
        fragment.getReplaceOptions().setFontSizeAdjustmentAction(TextReplaceOptions.FontSizeAdjustment.ShrinkToFit);
        fragment.getReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.AdjustSpaceWidth);
        fragment.setText(text + " " + text);

        document.save(outputFile.toString());
    }
}
```

## استبدال النص بالتعبير العادي

استخدم هذا المثال عندما يجب العثور على النص المطابق من خلال نمط regex وإعادة تصميمه أثناء الاستبدال.

1. افتح مستند PDF المصدر.
1. ابحث في الصفحة باستخدام `TextFragmentAbsorber` الذي يدعم التعبير العادي.
1. استبدل كل تطابق، وحدّث نمط النص الخاص به، واحفظ النتيجة.

```java
public static void replaceTextBasedOnRegex(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(Pattern.compile("\\d{4}-\\d{4}"));
        absorber.setTextSearchOptions(new TextSearchOptions(true));
        document.getPages().get_Item(1).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            fragment.setText("ABC1-2XZY");
            fragment.getTextState().setFont(FontRepository.findFont("Verdana"));
            fragment.getTextState().setFontSize(12);
            fragment.getTextState().setForegroundColor(Color.getBlue());
            fragment.getTextState().setBackgroundColor(Color.getLightGreen());
        }

        document.save(outputFile.toString());
    }
}
```

## استبدل نص العنصر النائب واترك الصفحة تعيد ترتيبها

استخدم هذا المثال عندما يجب استبدال العنصر النائب بقيمة حقيقية أطول مع الحفاظ على تخطيط الصفحة.

1. افتح ملف PDF المصدر وابحث عن نص العنصر النائب.
1. قم بتعيين النص البديل وتحديث إعدادات الخط الخاصة به.
1. احفظ المستند حتى تتم إعادة حساب التخطيط.

```java
public static void automaticallyRearrangePageContents(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("[Long_placeholder_Long_placeholder]");
        document.getPages().accept(absorber);

        for (TextFragment textFragment : absorber.getTextFragments()) {
            textFragment.setText("John Smith, South Development Studio");
            textFragment.getTextState().setFont(FontRepository.findFont("Calibri"));
            textFragment.getTextState().setFontSize(12);
            textFragment.getTextState().setForegroundColor(Color.getNavy());
        }

        document.save(outputFile.toString());
    }
}
```

## استبدال خط بآخر

استخدم هذا المثال عندما يجب تبديل النص الذي يستخدم خطًا مضمنًا محددًا إلى خط آخر.

1. افتح ملف PDF المصدر واجمع كل أجزاء النص.
1. تحقق من اسم الخط لكل جزء واستبدل الخط المستهدف.
1. احفظ ملف PDF المحدث.

```java
public static void replaceFonts(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        document.getPages().accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            if ("Arial-BoldMT".equals(fragment.getTextState().getFont().getFontName())) {
                fragment.getTextState().setFont(FontRepository.findFont("Verdana"));
            }
        }

        document.save(outputFile.toString());
    }
}
```

## استبدال الخطوط وإزالة موارد الخطوط غير المستخدمة

استخدم هذا المثال عندما يجب تنظيف المستند بعد استبدال الخط.

1. افتح ملف PDF المصدر وقم بتكوين `TextEditOptions` لإزالة الخطوط غير المستخدمة.
1. استيعاب أجزاء النص وتعيين الخط البديل.
1. احفظ المستند الأمثل.

```java
public static void removeUnusedFonts(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextEditOptions options = new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts);
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(options);
        document.getPages().accept(absorber);

        for (TextFragment textFragment : absorber.getTextFragments()) {
            textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        }

        document.save(outputFile.toString());
    }
}
```

## قم بإزالة كل النص من المستند

استخدم هذا المثال عندما يجب حذف محتوى النص بالكامل من كل صفحة.

1. افتح مستند PDF المصدر.
1. أنشئ `TextFragmentAbsorber` واتصل بـ`removeAllText(document)`.
1. احفظ ملف PDF الذي تم تنظيفه.

```java
public static void removeAllTextUsingAbsorber1(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.removeAllText(document);
        document.save(outputFile.toString());
    }
}
```

## إزالة كل النص من صفحة واحدة

استخدم هذا المثال عندما يجب إزالة النص بالكامل من صفحة معينة فقط.

1. افتح مستند PDF المصدر.
1. قم بإنشاء `TextFragmentAbsorber` وقم بإزالة النص من الصفحة المستهدفة.
1. احفظ المستند المحدث.

```java
public static void removeAllTextUsingAbsorber2(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.removeAllText(document.getPages().get_Item(1));
        document.save(outputFile.toString());
    }
}
```

## إزالة النص من المستطيل المحدد

استخدم هذا المثال عندما يجب حذف النص فقط داخل منطقة الصفحة المختارة.

1. افتح مستند PDF المصدر.
1. قم بإنشاء `TextFragmentAbsorber` وحدد المستطيل المراد تنظيفه.
1. قم بإزالة النص من تلك المنطقة واحفظ المستند.

```java
public static void removeAllTextUsingAbsorber3(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.removeAllText(document.getPages().get_Item(1), new Rectangle(10, 200, 120, 600, true));
        document.save(outputFile.toString());
    }
}
```

## إزالة النص المخفي

استخدم هذا المثال عندما يجب تجريد أجزاء النص غير المرئية من ملف PDF.

1. افتح ملف PDF المصدر واستوعب جميع أجزاء النص.
1. تحقق من كل جزء لمعرفة حالة النص غير المرئي.
1. امسح النص المخفي واحفظ المستند.

```java
public static void removeHiddenText(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textAbsorber = new TextFragmentAbsorber();
        textAbsorber.setTextReplaceOptions(new TextReplaceOptions(TextReplaceOptions.ReplaceAdjustment.None));
        document.getPages().accept(textAbsorber);

        for (TextFragment fragment : textAbsorber.getTextFragments()) {
            if (fragment.getTextState().isInvisible()) {
                fragment.setText("");
            }
        }

        document.save(outputFile.toString());
    }
}
```
