---
title: بحث واستخراج نص PDF في جافا
linktitle: البحث والحصول على النص
type: docs
weight: 60
url: /java/search-and-get-text-from-pdf/
description: تعرف على كيفية البحث عن النص وفحصه واستخراجه من مستندات PDF في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: ابحث عن نص PDF وافحص الأجزاء المستخرجة في Java
Abstract: تشرح هذه المقالة كيفية البحث عن النص واستخراجه من مستندات PDF باستخدام Aspose.PDF لـ Java. وهو يغطي TextAbsorter وTextFragmentAbsorter، بما في ذلك الاستخراج على أساس المنطقة، وعمليات البحث الخاصة بالصفحة، والتعبير العادي ومطابقة العبارة، وإدراج الارتباط التشعبي، وفحص النص المصمم، وتمييز الأجزاء.
---
يدعم Aspose.PDF for Java استخراج النص الخام والبحث على مستوى الأجزاء باستخدام الإحداثيات والأنماط ومطابقة التعبير العادي.

## استخراج النص من جميع الصفحات باستخدام TextAbsorter

استخدم هذا المثال عندما تحتاج إلى نص عادي مستخرج من منطقة مستند محددة عبر جميع الصفحات.

1. افتح مستند PDF المصدر.
1. قم بإنشاء `TextExtractionOptions` وعلى أساس المنطقة `TextSearchOptions`.
1. قم بتشغيل `TextAbsorber` على كافة الصفحات وأخرج النص المستخرج.

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

## استخراج النص من صفحة واحدة باستخدام TextAbsorter

استخدم هذا المثال عندما يقتصر استخراج النص العادي على صفحة واحدة.

1. افتح مستند PDF المصدر.
1. تكوين خيارات استخراج النص والبحث مع المنطقة المستهدفة.
1. قم بتشغيل `TextAbsorber` على الصفحة المحددة وأخرج النتيجة.

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

## فحص كافة أجزاء النص في المستند

استخدم هذا المثال عندما تحتاج إلى محتوى نصي مع البيانات التعريفية للخط والموضع واللون.

1. افتح مستند PDF المصدر.
1. قم بتشغيل `TextFragmentAbsorber` عبر كافة الصفحات.
1. قم بالتكرار عبر الأجزاء وإخراج بيانات التعريف الخاصة بها.

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

استخدم هذا المثال عندما يجب العثور على كلمة مستهدفة في صفحة محددة فقط.

1. افتح مستند PDF المصدر.
1. قم بإنشاء `TextFragmentAbsorber` باستخدام العبارة المستهدفة.
1. قم بزيارة الصفحة المختارة وإخراج مواضع الأجزاء المطابقة.

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

## متابعة البحث المتسلسل عبر الصفحات

استخدم هذا المثال عندما تريد إعادة استخدام أحد العناصر الممتصة أثناء الانتقال من صفحة بحث إلى أخرى.

1. افتح مستند PDF المصدر وقم بإنشاء أداة امتصاص قابلة لإعادة الاستخدام.
1. ابحث في الصفحة الأولى وافحص النتائج.
1. استمر في البحث في الصفحات الإضافية وراجع التطابقات المحدثة.

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

## ابحث عن عبارة داخل المستطيل المحدد

استخدم هذا المثال عندما تكون مطابقة العبارة مقتصرة على منطقة في صفحة واحدة.

1. افتح مستند PDF المصدر.
1. قم بإنشاء `TextFragmentAbsorber` باستخدام العبارة المستهدفة والمستندة إلى المستطيل `TextSearchOptions`.
1. قم بزيارة الصفحة وإخراج مواضع الأجزاء المتطابقة.

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

## البحث عن النص عن طريق التعبير العادي

استخدم هذا المثال عندما يجب العثور على المطابقات من خلال نمط regex بدلاً من عبارة ثابتة.

1. افتح مستند PDF المصدر.
1. قم بإنشاء `TextFragmentAbsorber` مع تمكين التعبير العادي.
1. قم بزيارة الصفحة المستهدفة وأخرج الأجزاء المطابقة.

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

## ابحث في قائمة العبارات حسب أنماط التعبير العادي

استخدم هذا المثال عندما يجب العثور على عدة عبارات مستهدفة في مسار واحد.

1. افتح مستند PDF المصدر.
1. أنشئ مصفوفة من أنماط التعبير العادي وقم بتمريرها إلى `TextFragmentAbsorber`.
1. قم بزيارة المستند وافحص نتائج التعبير العادي المجمعة.

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

## ابحث عن النص وقم بتحويله إلى ارتباطات تشعبية

استخدم هذا المثال عندما يجب تمييز الكلمات المطابقة وتحويلها إلى روابط قابلة للنقر.

1. افتح مستند PDF المصدر.
1. ابحث في الكلمات المستهدفة مع تمكين بحث regex.
1. قم بتحديث نمط النص وإرفاق الارتباطات التشعبية وحفظ ملف PDF المعدل.

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

## البحث عن النص حسب خصائص النمط

استخدم هذا المثال عندما تحتاج إلى فحص الأجزاء بناءً على التنسيق مثل النص الغامق أو غير المرئي.

1. افتح مستند PDF المصدر.
1. قم بتشغيل `TextFragmentAbsorber` على الصفحة المستهدفة.
1. تحقق من كل نمط جزء وأخرج الإدخالات المطابقة.

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

## قم بتمييز نتائج البحث في معاينات الصفحة المعروضة

استخدم هذا المثال عندما يجب ربط مطابقات النص بصور الصفحة المعروضة للفحص البصري.

1. قم بإنشاء جهاز PNG بالدقة المطلوبة.
1. ابحث في كل صفحة باستخدام `TextFragmentAbsorber` وقم بعرض الصفحة على دفق الصور.
1. اكتب صور معاينة الصفحة وإحداثيات جزء الإخراج للفحص.

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
