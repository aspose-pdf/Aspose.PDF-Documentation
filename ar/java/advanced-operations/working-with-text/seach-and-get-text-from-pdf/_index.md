---
title: البحث واستخراج نص PDF في Java
linktitle: البحث والحصول على النص
type: docs
weight: 60
url: /ar/java/search-and-get-text-from-pdf/
description: تعلم كيفية البحث وتفحص واستخراج النص من مستندات PDF بلغة Java.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: ابحث عن نص PDF وتفحص المقاطع المستخرجة في Java
Abstract: تشرح هذه المقالة كيفية البحث واستخراج النص من مستندات PDF باستخدام Aspose.PDF for Java. تغطي المقالة كلًا من TextAbsorber و TextFragmentAbsorber، بما في ذلك الاستخراج القائم على المنطقة، والبحث في صفحات محددة، وتطابق regex والعبارات، وإدراج الروابط التشعبية، وفحص النص المنسق، وتسليط الضوء على القطع.
---
Aspose.PDF for Java يدعم استخراج النص الخام والبحث على مستوى القطع مع الإحداثيات والأنماط ومطابقة regex.

## استخراج النص من جميع الصفحات باستخدام TextAbsorber

استخدم هذا المثال عندما تحتاج إلى نص مستخرج بسيط من منطقة مختارة في المستند عبر جميع الصفحات.

1. افتح مستند PDF المصدر.
1. إنشاء `TextExtractionOptions` والمعتمد على المنطقة `TextSearchOptions`.
1. تشغيل `TextAbsorber` على جميع الصفحات وإخراج النص المستخرج.

```java
public static void textAbsorberSearch(Path inputFile) {
        try (Document document = new Document(inputFile.toString())) {
            TextExtractionOptions textExtractionOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
            TextSearchOptions textSearchOptions = new TextSearchOptions(new Rectangle(0, 0, 842, 250, true));
            TextAbsorber absorber = new TextAbsorber(textExtractionOptions, textSearchOptions);

            document.getPages().accept(absorber);
            System.out.println("Text fragments found: " + absorber.getText());
        }
    }
```

## استخراج النص من صفحة واحدة باستخدام TextAbsorber

استخدم هذا المثال عندما يجب أن يقتصر استخراج النص العادي على صفحة واحدة.

1. افتح مستند PDF المصدر.
1. قم بتكوين استخراج النص وخيارات البحث مع المنطقة المستهدفة.
1. تشغيل `TextAbsorber` على الصفحة المحددة وإخراج النتيجة.

```java
public static void textAbsorberSearchPage(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextExtractionOptions textExtractionOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
        TextSearchOptions textSearchOptions = new TextSearchOptions(new Rectangle(0, 0, 842, 250, true));
        TextAbsorber absorber = new TextAbsorber(textExtractionOptions, textSearchOptions);

        document.getPages().get_Item(2).accept(absorber);
        System.out.println("Text fragments found: " + absorber.getText());
    }
}
```

## افحص جميع شظايا النص في المستند

استخدم هذا المثال عندما تحتاج إلى محتوى نصي مع بيانات الخط والموضع واللون.

1. افتح مستند PDF المصدر.
1. تشغيل `TextFragmentAbsorber` عبر جميع الصفحات.
1. تكرار عبر القطع وإخراج البيانات الوصفية الخاصة بها.

```java
public static void textFragmentAbsorberSearch(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        document.getPages().accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
            System.out.println("XIndent: " + fragment.getPosition().getXIndent());
            System.out.println("YIndent: " + fragment.getPosition().getYIndent());
            System.out.println("Font - Name: " + fragment.getTextState().getFont().getFontName());
            System.out.println("Font - IsAccessible: " + fragment.getTextState().getFont().isAccessible());
            System.out.println("Font - IsEmbedded: " + fragment.getTextState().getFont().isEmbedded());
            System.out.println("Font - IsSubset: " + fragment.getTextState().getFont().isSubset());
            System.out.println("Font Size: " + fragment.getTextState().getFontSize());
            System.out.println("Foreground Color: " + fragment.getTextState().getForegroundColor());
        }
    }
}
```

## ابحث عن عبارة واحدة في صفحة محددة

استخدم هذا المثال عندما يجب العثور على كلمة الهدف في صفحة مختارة فقط.

1. افتح مستند PDF المصدر.
1. إنشاء `TextFragmentAbsorber` مع العبارة المستهدفة.
1. قم بزيارة الصفحة المختارة وأخرج مواضع الأجزاء المتطابقة.

```java
public static void textFragmentAbsorberSearchPage(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("whale");
        document.getPages().get_Item(2).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
        }
    }
}
```

## متابعة بحث متسلسل عبر الصفحات

استخدم هذا المثال عندما تريد إعادة استخدام ممتص واحد أثناء الانتقال من بحث صفحة إلى الأخرى.

1. افتح مستند PDF المصدر وأنشئ ماصًا قابلاً لإعادة الاستخدام.
1. ابحث في الصفحة الأولى وتفقد النتائج.
1. استمر في البحث عن صفحات إضافية ومراجعة التطابقات المحدّثة.

```java
public static void textFragmentAbsorberSequentialSearch(Path inputFile) {
    Document document = new Document(inputFile.toString());
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    absorber.setPhrase("whale");

    document.getPages().get_Item(1).accept(absorber);
    for (TextFragment fragment : absorber.getTextFragments()) {
        System.out.println("Text: " + fragment.getText());
        System.out.println("Page: " + fragment.getPage().getNumber());
        System.out.println("Position: " + fragment.getPosition());
    }

    System.out.println("--");

    document.getPages().get_Item(2).accept(absorber);
    absorber.visit(document);

    for (TextFragment fragment : absorber.getTextFragments()) {
        System.out.println("Text: " + fragment.getText());
        System.out.println("Page: " + fragment.getPage().getNumber());
        System.out.println("Position: " + fragment.getPosition());
    }
}
```

## ابحث عن عبارة داخل مستطيل محدد

استخدم هذا المثال عندما يجب أن يقتصر مطابقة العبارات على منطقة في صفحة واحدة.

1. افتح مستند PDF المصدر.
1. إنشاء `TextFragmentAbsorber` مع العبارة المستهدفة والمعتمد على المستطيل `TextSearchOptions`.
1. قم بزيارة الصفحة وأخرج مواضع القطع المتطابقة.

```java
public static void textFragmentAbsorberSearchPhrase(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(
                "elephant", new TextSearchOptions(new Rectangle(0, 0, 842, 250, true)));

        document.getPages().get_Item(2).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
        }
    }
}
```

## ابحث عن النص باستخدام تعبير عادي

استخدم هذا المثال عندما يجب العثور على التطابقات بنمط regex بدلاً من العبارة الثابتة

1. افتح مستند PDF المصدر.
1. إنشاء regex-enabled `TextFragmentAbsorber`.
1. قم بزيارة الصفحة المستهدفة وأخرج المقاطع المطابقة.

```java
public static void textFragmentAbsorberSearchRegex(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(
                Pattern.compile("\\d+\\.\\d+"), new TextSearchOptions(true));

        document.getPages().get_Item(2).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
        }
    }
}
```

## ابحث في قائمة من العبارات باستخدام أنماط regex

استخدم هذا المثال عندما يجب العثور على عدة عبارات مستهدفة في تمريرة واحدة.

1. افتح مستند PDF المصدر.
1. إنشاء مصفوفة من أنماط regex وتمريرها إلى `TextFragmentAbsorber`.
1. قم بزيارة المستند وتفقد النتائج المجمعة للتعبير النمطي.

```java
public static void textFragmentAbsorberSearchListOfPhrases(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Pattern[] patterns = new Pattern[] {
                Pattern.compile("whale"),
                Pattern.compile("elephant")
        };
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(patterns, new TextSearchOptions(true));
        document.getPages().accept(absorber);

        for (TextFragmentCollection fragments : absorber.getRegexResults().values()) {
            for (TextFragment fragment : fragments) {
                System.out.println("Text: " + fragment.getText());
                System.out.println("Position: " + fragment.getPosition());
            }
        }
    }
}
```

## ابحث عن النص وحوله إلى روابط تشعبية

استخدم هذا المثال عندما يجب تمييز الكلمات المتطابقة وتحويلها إلى روابط قابلة للنقر.

1. افتح مستند PDF المصدر.
1. ابحث عن الكلمات المستهدفة مع تمكين البحث باستخدام regex.
1. قم بتحديث نمط النص، أرفق الروابط التشعبية، واحفظ ملف PDF المعدل.

```java
public static void textFragmentAbsorberSearchAndAddHyperlink(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("whale|elephant");
        absorber.setTextSearchOptions(new TextSearchOptions(true));
        absorber.visit(document.getPages().get_Item(1));

        for (TextFragment fragment : absorber.getTextFragments()) {
            fragment.getTextState().setForegroundColor(Color.getBlue());
            fragment.getTextState().setUnderline(true);
            fragment.setHyperlink(new WebHyperlink("https://en.wikipedia.org/wiki/" + fragment.getText()));
        }

        document.save(inputFile.toString().replace("in.pdf", "out.pdf"));
    }
}
```

## بحث النص حسب خصائص النمط

استخدم هذا المثال عندما تحتاج إلى فحص المقاطع بناءً على التنسيق مثل النص الغامق أو النص غير المرئي.

1. افتح مستند PDF المصدر.
1. تشغيل `TextFragmentAbsorber` على الصفحة المستهدفة.
1. تحقق من كل نمط للجزء وأخرج الإدخالات المطابقة.

```java
public static void textFragmentAbsorberSearchStyledText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.setTextSearchOptions(new TextSearchOptions(true));
        absorber.visit(document.getPages().get_Item(1));

        for (TextFragment fragment : absorber.getTextFragments()) {
            if (fragment.getTextState().getFontStyle() == FontStyles.Bold) {
                System.out.println("Bold: " + fragment.getText());
            }
            if (fragment.getTextState().isInvisible()) {
                System.out.println("Invisible: " + fragment.getText());
            }
        }
    }
}
```

## تمييز نتائج البحث في معاينات الصفحات المعروضة

استخدم هذا المثال عندما يجب ربط تطابق النصوص مع صور الصفحات المعروضة للتفتيش البصري.

1. إنشاء جهاز PNG بالدقة المطلوبة.
1. ابحث في كل صفحة باستخدام `TextFragmentAbsorber` وعرض الصفحة إلى تدفق صورة.
1. اكتب صور معاينة الصفحة وإحداثيات قطع الإخراج للفحص.

```java
public static void textFragmentAbsorberSearchAndHighlight(Path inputFile) throws Exception {
    int resolution = 150;
    PngDevice pngDevice = new PngDevice(new Resolution(resolution, resolution));

    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(Pattern.compile("[\\S]+"));
        absorber.setTextSearchOptions(new TextSearchOptions(true));

        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            Page page = document.getPages().get_Item(pageNumber);
            page.accept(absorber);

            try (ByteArrayOutputStream stream = new ByteArrayOutputStream()) {
                pngDevice.process(page, stream);
                Path output = Path.of(inputFile.toString().replace("_in.pdf", page.getNumber() + "_out.png"));
                Files.write(output, stream.toByteArray());
            }

            for (TextFragment textFragment : absorber.getTextFragments()) {
                Rectangle pageRect = page.getPageRect(true);
                System.out.println("TextFragment = " + textFragment.getText()
                        + " Page URY = " + pageRect.getURY()
                        + " TextFragment URY = " + textFragment.getRectangle().getURY());
            }
        }
    }
}
```
