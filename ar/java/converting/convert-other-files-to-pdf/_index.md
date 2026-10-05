---
title: تحويل تنسيقات ملفات أخرى إلى PDF في Java
linktitle: تحويل تنسيقات ملفات أخرى إلى PDF
type: docs
weight: 80
url: /ar/java/convert-other-files-to-pdf/
lastmod: "2026-10-05"
description: تعرّف على كيفية تحويل ملفات EPUB و Markdown و PCL و XPS و PostScript و XML و XSL-FO و OFD و TeX إلى PDF في Java باستخدام Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: كيفية تحويل تنسيقات ملفات أخرى إلى PDF في Java
Abstract: تشرح هذه المقالة كيفية تحويل صيغ ملفات مصدر متعددة إلى PDF باستخدام Aspose.PDF for Java. تغطي سير عمل التحويل للـ EPUB و Markdown و OFD و PCL و PostScript و EPS و TeX والنص و XML و XPS و XSL-FO باستخدام خيارات تحميل مخصصة لكل صيغة وخطوات ما قبل المعالجة عند الحاجة.
---
يدعم Aspose.PDF for Java التحويل من صيغ المستند والوسم وتوصيف الصفحات إلى PDF.

## تحويل OFD إلى PDF

استخدم هذا المثال عندما يجب تحويل مستند OFD إلى PDF.

1. افتح مصدر OFD بتمرير مسار الملف و [`OfdLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/ofdloadoptions/) إلى [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) منشئ.
1. دع Aspose.PDF يحلل حزمة OFD إلى نموذج مستند PDF..
1. احفظ ملف PDF الناتج إلى مسار الإخراج الهدف.

```java
public static void convertOfdToPdf(Path inputFile, Path outputFile) {
       try (Document document = new Document(inputFile.toString(), new OfdLoadOptions())) {
           document.save(outputFile.toString());
       }
       System.out.println(inputFile + " converted into " + outputFile);
   }
```

## تحويل TeX إلى PDF

استخدم هذا المثال عندما يجب عرض محتوى TeX مباشرةً كملف PDF.

1. افتح مصدر TeX بتمرير مسار الملف و [`TeXLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/texloadoptions/) إلى [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) منشئ.
1. دع Aspose.PDF يفسّر ترميز TeX ويبني تخطيط PDF أثناء التحميل.
1. احفظ ملف PDF المُولد.

```java
public static void convertTexToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new com.aspose.pdf.TeXLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل PostScript إلى PDF

استخدم هذا المثال عندما يجب تحويل ملف PostScript إلى مستند PDF.

1. افتح مصدر PostScript باستخدام [`PsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/psloadoptions/) في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) منشئ.
1. دع Aspose.PDF يترجم تدفق وصف الصفحة PostScript إلى نموذج مستند PDF..
1. احفظ ملف PDF المحول.

```java
public static void convertPostScripToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new PsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل EPS إلى PDF

استخدم هذا المثال عندما يجب تحويل ملف Encapsulated PostScript إلى PDF.

1. افتح مصدر EPS باستخدام [`PsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/psloadoptions/) لأن EPS يتبع نفس مسار التحميل القائم على PostScript..
1. حمّل الملف إلى [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) لذلك يتم تحويل محتوى وصف الصفحة أثناء الاستيراد.
1. احفظ ملف PDF الناتج.

```java
public static void convertEpsToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new PsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل EPUB إلى PDF

استخدم هذا المثال عندما يجب تحويل كتاب إلكتروني EPUB إلى PDF.

1. افتح مصدر EPUB بتمرير مسار الملف و [`EpubLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubloadoptions/) إلى [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) منشئ.
1. دع Aspose.PDF يحمل بنية الكتاب الإلكتروني ويحولها إلى صفحات PDF..
1. احفظ ملف PDF المحول.

```java
public static void convertEpubToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new EpubLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل Markdown إلى PDF

استخدم هذا المثال عندما يجب عرض محتوى Markdown وحفظه كملف PDF.

1. افتح مصدر Markdown بتمرير مسار الملف و [`MdLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/mdloadoptions/) إلى [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) منشئ.
1. دع Aspose.PDF يفسّر محتوى Markdown ويحوّله إلى محتوى صفحة PDF..
1. احفظ ملف PDF الناتج.

```java
public static void convertMdToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new MdLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل النص إلى PDF باستخدام سير عمل بسيط

استخدم هذا المثال عندما يجب تحويل ملف نصي عادي بسرعة إلى PDF.

1. اقرأ مصدر النص العادي باستخدام فك ترميز UTF-8 بحيث يصبح محتوى النص متاحًا كسلسلة Java.
1. أنشئ كائنًا فارغًا من الفئة [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. غلف النص بـ [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) وأضفه إلى مجموعة فقرات الصفحة.
1. احفظ ملف PDF المُولد.

```java
public static void convertTxtToPdfSimple(Path inputFile, Path outputFile) throws Exception {
    String textContent = Files.readString(inputFile, StandardCharsets.UTF_8);
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment(textContent));
        page.close();
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل النص إلى PDF مع خيارات متقدمة

استخدم هذا المثال عندما يجب تحويل النص العادي مع خيارات تخطيط أو ترميز إضافية.

1. اقرأ جميع أسطر النص من ملف الإدخال بحيث يمكن فحص علامات فواصل الصفحات أثناء التحويل.
1. أنشئ كائنًا فارغًا من الفئة [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وتهيئة كل [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) مع هوامش وحالة النص الافتراضية.
1. استرجع الخط ثابت العرض من خلال [`FontRepository`](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontrepository/) وأضف كل سطر كـ [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. احفظ ملف الإخراج بعد إكمال حلقة بناء الصفحة.

```java
public static void convertTxtToPdf(Path inputFile, Path outputFile) throws Exception {
    List<String> lines = Files.readAllLines(inputFile);
    try (Document document = new Document()) {
        com.aspose.pdf.Page page = document.getPages().add();
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        int pageCount = 1;
        for (String line : lines) {
            if (!line.isEmpty() && line.charAt(0) == '\f') {
                page = document.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
                page.getPageInfo().getDefaultTextState().setFontSize(12);
                pageCount++;
                if (pageCount == 4) {
                    break;
                }
            } else {
                page.getParagraphs().add(new TextFragment(line));
            }
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل PCL إلى PDF

استخدم هذا المثال عندما يجب تحويل تدفق طباعة PCL إلى PDF.

1. أنشئ كائنًا من الفئة [`PclLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pclloadoptions/) وفعّل الأخطاء المكبوتة في التحليل عندما يكون سلوك الاستيراد المتساهل مطلوبًا.
1. افتح مصدر PCL عن طريق تمرير مسار الملف وخيارات التحميل إلى [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) منشئ.
1. احفظ النتيجة كملف PDF..

```java
public static void convertPclToPdf(Path inputFile, Path outputFile) {
    PclLoadOptions loadOptions = new PclLoadOptions();
    loadOptions.setSupressErrors(true);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل XML إلى PDF عبر XSLT و HTML

استخدم هذا المثال عندما يجب تحويل بيانات XML قبل إنشاء PDF النهائي.

1. حوّل مصدر XML باستخدام ملف XSLT إلى ملف HTML مؤقت عن طريق استدعاء طريقة التحويل المخصصة.
1. مرّر ملف HTML الذي تم إنشاؤه إلى وظيفة تحويل HTML إلى PDF الموجودة بحيث يستخدم PDF النهائي المعيار [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) workflow..
1. احذف ملف HTML المؤقت في `finally` حظر بعد اكتمال التحويل.
1. احفظ ملف PDF الذي تم إنشاؤه.

```java
public static void convertXmlToPdf(Path xsltFile, Path xmlFile, Path outputFile) throws Exception {
    Path htmlFile = Files.createTempFile("aspose-pdf-xml-", ".html");
    try {
        transformXmlToHtml(xmlFile, xsltFile, htmlFile);
        HtmlToPdfExamples.convertHtmlToPdf(htmlFile, outputFile);
    } finally {
        Files.deleteIfExists(htmlFile);
    }
    System.out.println(xmlFile + " converted into " + outputFile);
}
```

## تحويل XPS إلى PDF

استخدم هذا المثال عندما يجب تحويل مستند XPS إلى PDF.

1. افتح مصدر XPS بتمرير مسار الملف و [`XpsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xpsloadoptions/) إلى [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) منشئ.
1. دع Aspose.PDF يفسّر وصف صفحة XPS أثناء تحميل المستند.
1. احفظ ملف PDF المحول.

```java
public static void convertXpsToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new XpsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل XSL-FO إلى PDF

استخدم هذا المثال عندما يجب تحويل محتوى XSL-FO إلى PDF.

1. أنشئ كائنًا من الفئة [`XslFoLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions/) مع مسار XSLT بحيث يمكن تحويل مصدر XML أثناء التحميل.
1. اضبط وضع معالجة أخطاء التحليل بحيث يُطرح استثناءً على الفور عندما يتم اكتشاف XSL-FO غير صالح.
1. افتح مصدر XML في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مع خيارات التحميل تلك.
1. احفظ مستند PDF الناتج.

```java
public static void convertXslFoToPdf(Path xsltFile, Path xmlFile, Path outputFile) {
    XslFoLoadOptions loadOptions = new XslFoLoadOptions(xsltFile.toString());
    loadOptions.setParsingErrorsHandlingType(XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately);
    try (Document document = new Document(xmlFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(xmlFile + " converted into " + outputFile);
}
```

## تحويل XML إلى HTML وسيط

استخدم هذه الطريقة عندما يجب تحويل بيانات XML إلى HTML قبل خطوة تحويل PDF النهائية.

1. افتح ملفات XML و XSLT الإدخال كمصادر تحويل.
1. أنشئ `Transformer` من ورقة الأنماط XSLT وتشغيلها على مصدر XML..
1. اكتب ملف HTML المُحوَّل إلى القرص حتى يتمكن دالة تحويل PDF اللاحقة من تحميله.

```java
private static void transformXmlToHtml(Path xmlFile, Path xsltFile, Path htmlFile) throws Exception {
    Transformer transformer = TransformerFactory.newInstance()
            .newTransformer(new StreamSource(xsltFile.toFile()));
    transformer.transform(new StreamSource(xmlFile.toFile()), new StreamResult(htmlFile.toFile()));
}
```
