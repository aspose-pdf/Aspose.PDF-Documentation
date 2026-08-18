---
title: تحويل تنسيقات الملفات الأخرى إلى PDF في Java
linktitle: تحويل تنسيقات الملفات الأخرى إلى PDF
type: docs
weight: 80
url: /java/convert-other-files-to-pdf/
lastmod: "2026-06-16"
description: تعرف على كيفية تحويل ملفات EPUB، وMarkdown، وPCL، وXPS، وPostScript، وXML، وXSL-FO، وOFD، وTeX إلى PDF في Java باستخدام Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: كيفية تحويل تنسيقات الملفات الأخرى إلى PDF في جافا
Abstract: تشرح هذه المقالة كيفية تحويل تنسيقات ملفات مصدر متعددة إلى PDF باستخدام Aspose.PDF لـ Java. وهو يغطي سير عمل تحويل EPUB، وMarkdown، وOFD، وPCL، وPostScript، وEPS، وTeX، والنص، وXML، وXPS، وXSL-FO باستخدام خيارات التحميل الخاصة بالتنسيق وخطوات المعالجة المسبقة عند الحاجة.
---
يدعم Aspose.PDF for Java التحويل من تنسيقات المستندات والعلامات ووصف الصفحة إلى PDF.

## تحويل OFD إلى PDF

استخدم هذا المثال عندما يجب تحويل مستند OFD إلى PDF.

1. افتح مصدر OFD عن طريق تمرير مسار الملف و[`OfdLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/ofdloadoptions/) إلى المُنشئ [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اسمح لـ Aspose.PDF بتحليل حزمة OFD في نموذج مستند PDF.
1. احفظ ملف PDF الناتج في مسار الإخراج المستهدف.

```java
public static void convertOfdToPdf(Path inputFile, Path outputFile) {
       try (Document document = new Document(inputFile.toString(), new OfdLoadOptions())) {
           document.save(outputFile.toString());
       }
       System.out.println(inputFile + " converted into " + outputFile);
   }
```

## تحويل تكس إلى PDF

استخدم هذا المثال عندما يجب عرض محتوى TeX مباشرة بصيغة PDF.

1. افتح مصدر TeX عن طريق تمرير مسار الملف و[`TeXLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/texloadoptions/) إلى المُنشئ [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اسمح لـ Aspose.PDF بتفسير علامة TeX وإنشاء تخطيط PDF أثناء التحميل.
1. احفظ ملف PDF الذي تم إنشاؤه.

```java
public static void convertTexToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new com.aspose.pdf.TeXLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل بوستسكريبت إلى PDF

استخدم هذا المثال عندما يجب تحويل ملف PostScript إلى مستند PDF.

1. افتح مصدر PostScript باستخدام [`PsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/psloadoptions/) في المُنشئ [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اسمح لـ Aspose.PDF بترجمة تدفق وصف صفحة PostScript إلى نموذج مستند PDF.
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

1. افتح مصدر EPS باستخدام [`PsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/psloadoptions/) لأن EPS يتبع نفس مسار التحميل المستند إلى PostScript.
1. قم بتحميل الملف في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) بحيث يتم تحويل محتوى وصف الصفحة أثناء الاستيراد.
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

1. افتح مصدر EPUB عن طريق تمرير مسار الملف و[`EpubLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubloadoptions/) إلى المُنشئ [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اسمح لـ Aspose.PDF بتحميل بنية الكتاب الإلكتروني وتحويله إلى صفحات PDF.
1. احفظ ملف PDF المحول.

```java
public static void convertEpubToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new EpubLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل تخفيض السعر إلى PDF

استخدم هذا المثال عندما يجب عرض محتوى Markdown وحفظه بتنسيق PDF.

1. افتح مصدر Markdown عن طريق تمرير مسار الملف و[`MdLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/mdloadoptions/) إلى المُنشئ [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اسمح لـ Aspose.PDF بتفسير محتوى Markdown وتحويله إلى محتوى صفحة PDF.
1. احفظ ملف PDF الناتج.

```java
public static void convertMdToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new MdLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل النص إلى PDF بسير عمل بسيط

استخدم هذا المثال عندما يجب تحويل ملف نصي عادي بسرعة إلى PDF.

1. اقرأ مصدر النص العادي باستخدام فك تشفير UTF-8 بحيث يكون محتوى النص متاحًا كسلسلة Java.
1. أنشئ [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) فارغًا وأضف [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. لف النص في [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) وأضفه إلى مجموعة فقرات الصفحة.
1. احفظ ملف PDF الذي تم إنشاؤه.

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

## تحويل النص إلى PDF مع الخيارات المتقدمة

استخدم هذا المثال عندما يجب تحويل النص العادي باستخدام خيارات تخطيط أو ترميز إضافية.

1. اقرأ كافة الأسطر النصية من ملف الإدخال حتى يمكن فحص علامات فاصل الصفحات أثناء التحويل.
1. قم بإنشاء [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) فارغة وقم بتكوين كل [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) بالهوامش وحالة النص الافتراضية.
1. قم بحل الخط أحادي المسافة من خلال [`FontRepository`](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontrepository/) وأضف كل سطر كـ [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. احفظ ملف الإخراج بعد اكتمال حلقة بناء الصفحة.

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

1. قم بإنشاء [`PclLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pclloadoptions/) وقم بتمكين أخطاء التحليل المحظورة عندما يكون سلوك الاستيراد المتساهل مطلوبًا.
1. افتح مصدر PCL عن طريق تمرير مسار الملف وخيارات التحميل إلى المُنشئ [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. احفظ النتيجة بصيغة PDF.

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

## تحويل XML إلى PDF من خلال XSLT وHTML

استخدم هذا المثال عندما يجب تحويل بيانات XML قبل إنشاء PDF النهائي.

1. قم بتحويل مصدر XML باستخدام ملف XSLT إلى ملف HTML مؤقت عن طريق استدعاء طريقة التحويل المخصصة.
1. قم بتمرير ملف HTML الذي تم إنشاؤه إلى وظيفة تحويل HTML إلى PDF الموجودة بحيث يستخدم ملف PDF النهائي سير العمل القياسي [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/).
1. احذف ملف HTML المؤقت الموجود في كتلة `finally` بعد اكتمال التحويل.
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

1. افتح مصدر XPS عن طريق تمرير مسار الملف و[`XpsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xpsloadoptions/) إلى المُنشئ [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اسمح لـ Aspose.PDF بتفسير وصف صفحة XPS أثناء تحميل المستند.
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

استخدم هذا المثال عندما يجب عرض محتوى XSL-FO بصيغة PDF.

1. قم بإنشاء [`XslFoLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions/) باستخدام مسار XSLT بحيث يمكن تحويل مصدر XML أثناء التحميل.
1. قم بتكوين وضع معالجة أخطاء التحليل للرمي فورًا عند مواجهة XSL-FO غير صالح.
1. افتح مصدر XML في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) باستخدام خيارات التحميل هذه.
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

## تحويل XML إلى HTML المتوسط

استخدم هذه الطريقة عندما يتعين تحويل بيانات XML إلى HTML قبل خطوة تحويل PDF النهائية.

1. افتح ملفات إدخال XML وXSLT كمصادر تحويل.
1. قم بإنشاء `Transformer` من ورقة أنماط XSLT وقم بتشغيلها على مصدر XML.
1. قم بكتابة ملف HTML المحول على القرص حتى تتمكن وظيفة تحويل PDF من تحميله.

```java
private static void transformXmlToHtml(Path xmlFile, Path xsltFile, Path htmlFile) throws Exception {
    Transformer transformer = TransformerFactory.newInstance()
            .newTransformer(new StreamSource(xsltFile.toFile()));
    transformer.transform(new StreamSource(xmlFile.toFile()), new StreamResult(htmlFile.toFile()));
}
```
