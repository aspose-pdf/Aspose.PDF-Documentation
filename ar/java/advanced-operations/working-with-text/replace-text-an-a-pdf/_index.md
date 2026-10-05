---
title: استبدال النص في PDF باستخدام Java
linktitle: استبدال النص في PDF
type: docs
weight: 40
url: /ar/java/replace-text-in-pdf/
description: تعلم كيفية استبدال وإعادة ترتيب وإزالة النص في مستندات PDF باستخدام Java.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: استبدل، وأزل، واضبط محتوى النص في PDF باستخدام Java
Abstract: تشرح هذه المقالة سير عمل استبدال النص في مستندات PDF باستخدام Aspose.PDF for Java. وتغطي استبدال النص عبر جميع الصفحات، وتحديد الاستبدال إلى منطقة مختارة، وضبط تخطيط الاستبدال، واستخدام المطابقة القائمة على التعابير النمطية (regex)، واستبدال الخطوط، وإزالة جميع النصوص، وحذف النص المخفي.
---
توفر Aspose.PDF for Java كلًا من ميزات الاستبدال البسيط والاستبدال المدرك للتخطيط من خلال `TextFragmentAbsorber` واستبدال الخيارات.

## استبدال النص على جميع الصفحات

استخدم هذا المثال عندما يجب استبدال نفس العبارة في جميع أنحاء المستند.

1. افتح مستند PDF المصدر.
1. ابحث في جميع الصفحات عن العبارة المستهدفة باستخدام `TextFragmentAbsorber`.
1. استبدل النص المتطابق واحفظ ملف PDF المحدث.

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

## استبدال النص في منطقة صفحة محددة

استخدم هذا المثال عندما يجب أن يقتصر الاستبدال على مستطيل محدد في صفحة واحدة.

1. افتح مستند PDF المصدر.
1. اضبط `TextSearchOptions` مع حدود الصفحة ومستطيل الهدف.
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

## استبدال النص وضبط المسافات داخل مستطيل مُزاح

استخدم هذا المثال عندما يجب أن يبقى النص المستبدل على الصفحة مع تعديل التباعد لكن يجب أن يبقى حجم الخط دون تغيير.

1. افتح ملف PDF المصدر وجمع شظايا النص من الصفحة المستهدفة.
1. عدل مستطيل الاستبدال واختر `AdjustSpaceWidth` السلوك.
1. عيّن النص الجديد واحفظ المستند.

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

## استبدال النص داخل مستطيل الفقرة الأكبر

استخدم هذا المثال عندما يجب أن يتوسع النص البديل إلى مساحة صفحة أكبر.

1. افتح ملف PDF المصدر واحصل على أول مقطع نصي من الصفحة المستهدفة.
1. أنشئ مستطيل استبدالي أكبر باستخدام صندوق وسائط الصفحة.
1. طبّق خيارات الاستبدال واحفظ ملف PDF..

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

## استبدل النص وقم بتكبير الخط لملء المستطيل

استخدم هذا المثال عندما يجب أن يتسع النص البديل لملء المنطقة المستهدفة.

1. افتح ملف PDF المصدر وواصل إلى جزء النص الهدف.
1. حدّد مستطيل الاستبدال وقم بتمكينه `ScaleToFill` ضبط الخط.
1. عيّن النص الجديد واحفظ المستند المحدث.

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

## استبدال النص وتقليصه ليتناسب

استخدم هذا المثال عندما يجب أن يبقى نص الاستبدال داخل المستطيل النصي الأصلي.

1. افتح ملف PDF المصدر وحدد الجزء المستهدف.
1. إعادة استخدام مستطيل الجزء الحالي وتمكينه `ShrinkToFit`.
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

## استبدال النص باستخدام التعبير النمطي

استخدم هذا المثال عندما يجب العثور على النص المطابق بواسطة نمط regex وإعادة تنسيقه أثناء الاستبدال.

1. افتح مستند PDF المصدر.
1. ابحث في الصفحة باستخدام regex-enabled `TextFragmentAbsorber`.
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

## استبدل النص النائب ودع الصفحة تعيد ترتيب نفسها

استخدم هذا المثال عندما يجب استبدال عنصر نائب بقيمة حقيقية أطول مع الحفاظ على تخطيط الصفحة.

1. افتح ملف PDF المصدر وابحث عن نص العنصر النائب.
1. عيّن نص الاستبدال وحدّث إعدادات الخط الخاصة به.
1. احفظ المستند بحيث يُعاد حساب التخطيط.

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

## استبدل خطًا بآخر

استخدم هذا المثال عندما يجب استبدال النص الذي يستخدم خطًا مدمجًا محددًا بخط آخر.

1. افتح ملف PDF المصدر وجمع جميع مقاطع النص.
1. تحقّق من اسم الخط في كل جزء واستبدل الخط المستهدف.
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

## استبدال الخطوط وإزالة موارد الخط غير المستخدمة

استخدم هذا المثال عندما يجب تنظيف المستند بعد استبدال الخط.

1. افتح ملف PDF المصدر وقم بالتكوين `TextEditOptions` لإزالة الخطوط غير المستخدمة.
1. امتصّ مقاطع النص وتعيّن الخط البديل.
1. احفظ المستند المُحسّن.

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

## إزالة كل النص من المستند

استخدم هذا المثال عندما يجب حذف جميع محتويات النص من كل صفحة.

1. افتح مستند PDF المصدر.
1. أنشئ `TextFragmentAbsorber` واستدعِ `removeAllText(document)`.
1. احفظ ملف PDF المنظف.

```java
public static void removeAllTextUsingAbsorber1(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.removeAllText(document);
        document.save(outputFile.toString());
    }
}
```

## إزالة جميع النص من صفحة واحدة

استخدم هذا المثال عندما يجب إزالة جميع النصوص فقط من صفحة معينة.

1. افتح مستند PDF المصدر.
1. أنشئ `TextFragmentAbsorber` وأزل النص من الصفحة المستهدفة.
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

## إزالة النص من مستطيل مختار

استخدم هذا المثال عندما يجب حذف النص فقط داخل منطقة صفحة مختارة.

1. افتح مستند PDF المصدر.
1. أنشئ `TextFragmentAbsorber` وحدد المستطيل للتنظيف.
1. أزل النص من تلك المنطقة واحفظ المستند.

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

استخدم هذا المثال عندما يجب إزالة أجزاء النص غير المرئية من ملف PDF.

1. افتح ملف PDF المصدر وامتص جميع مقاطع النص.
1. تحقّق من كل جزء لحالة النص غير المرئي.
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
