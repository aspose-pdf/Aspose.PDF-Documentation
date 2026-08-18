---
title: تحويل HTML إلى PDF في جافا
linktitle: تحويل ملف HTML إلى PDF
type: docs
weight: 40
url: /java/convert-html-to-pdf/
lastmod: "2026-06-16"
description: تعرف على كيفية تحويل HTML وMHTML وصفحات الويب إلى PDF في Java باستخدام Aspose.PDF، بما في ذلك إعدادات الوسائط وقواعد صفحة CSS وتضمين الخط ومحتوى SVG ومخرجات الصفحة الواحدة.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: كيفية تحويل HTML إلى PDF في Java باستخدام Aspose.PDF
Abstract: يشرح هذا المقال كيفية تحويل ملفات HTML وMHTML إلى PDF باستخدام Aspose.PDF لـ Java. وهو يغطي سير عمل HTML إلى PDF الأساسي ويوضح كيفية التحكم في العرض باستخدام أنواع الوسائط وأولوية قاعدة صفحة CSS والخطوط المضمنة ومحتوى SVG ومخرجات الصفحة الواحدة والتحويل المباشر من صفحة ويب مباشرة.
---
يمكن لـ Aspose.PDF for Java تحويل ملفات HTML المحلية ومحتوى MHTML المؤرشف وصفحات الويب المباشرة إلى مستندات PDF. يمكنك التحكم في مسار التحويل باستخدام `HtmlLoadOptions` و`MhtLoadOptions` للتأثير على قياس التخطيط، ومعالجة وسائط CSS، وأولوية قاعدة الصفحة، وتضمين الخط، ودقة الموارد، وسلوك عرض الصفحة الواحدة.

## تحويل HTML إلى PDF

استخدم هذا المثال عندما يجب تحويل ملف HTML محلي مباشرة إلى مستند PDF.

1. قم بإنشاء مثيل [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) لتكوين كيفية تفسير مصدر HTML أثناء الاستيراد.
1. قم بتعيين [`HtmlPageLayoutOption`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlpagelayoutoption/) على `ScaleToPageWidth` بحيث يتم تغيير حجم محتوى HTML الواسع إلى عرض صفحة PDF المستهدفة بدلاً من قصه.
1. افتح ملف HTML المصدر عن طريق تمرير مساره وخيارات التحميل التي تم تكوينها إلى المُنشئ [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. احفظ الملف [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) الذي تم إنشاؤه كملف PDF في مسار الإخراج المستهدف.

```java
public static void convertHtmlToPdf(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setPageLayoutOption(HtmlPageLayoutOption.ScaleToPageWidth);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل HTML إلى PDF مع خيارات نوع الوسائط

استخدم هذا المثال عندما يجب التحكم في معالجة نوع وسائط CSS أثناء تحويل HTML.

1. قم بإنشاء مثيل [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) لإعدادات التحويل.
1. اضبط [`HtmlMediaType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlmediatype/) على `Screen` عندما يجب عرض HTML باستخدام قواعد CSS المخصصة للعرض على الشاشة بدلاً من وسائط الطباعة.
1. افتح ملف HTML باستخدام خيارات التحميل التي تم تكوينها بحيث يتم تطبيق الأنماط المعتمدة على استعلام الوسائط أثناء التحويل.
1. احفظ الناتج [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) كملف PDF.

```java
public static void convertHtmlToPdfMediaType(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setHtmlMediaType(HtmlMediaType.Screen);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل HTML إلى PDF مع أولوية قاعدة صفحة CSS

استخدم هذا المثال عندما تؤثر قواعد CSS `@page` على التخطيط النهائي لصفحة PDF.

1. قم بإنشاء مثيل [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) قبل فتح ملف HTML.
1. قم بتكوين `setPriorityCssPageRule(false)` عندما تكون إعدادات التخطيط الأخرى لها الأولوية على إعلانات CSS `@page` في ترميز المصدر.
1. قم بتحميل محتوى HTML في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) باستخدام الخيارات التي تم تكوينها حتى يتم حل تخطيط الصفحة أثناء الاستيراد.
1. احفظ ملف PDF الذي تم إنشاؤه.

```java
public static void convertHtmlToPdfPriorityCssPageRule(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setPriorityCssPageRule(false);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل HTML إلى PDF مع الخطوط المضمنة

استخدم هذا المثال عندما يجب أن يحافظ ملف PDF الناتج على خطوط HTML عن طريق دمجها.

1. قم بإنشاء مثيل [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) لتكوين استيراد HTML.
1. قم بتمكين `setEmbedFonts(true)` بحيث يتم تخزين الخطوط التي تم حلها أثناء عرض HTML في ملف PDF الناتج.
1. افتح مصدر HTML باستخدام خيارات التحميل هذه للحفاظ على الطباعة الأصلية متاحة في المستند النهائي.
1. احفظ [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) كملف PDF مع تضمين موارد الخطوط المضمنة.

```java
public static void convertHtmlToPdfEmbedFonts(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setEmbedFonts(true);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## عرض محتوى HTML على صفحة PDF واحدة

استخدم هذا المثال عندما يجب الاحتفاظ بمحتوى HTML الطويل على صفحة PDF واحدة بدلاً من التدفق عبر صفحات متعددة.

1. قم بإنشاء مثيل [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) لإعدادات التحويل.
1. قم بتمكين `setRenderToSinglePage(true)` بحيث يتم وضع HTML المستورد على صفحة PDF واحدة بدلاً من تقسيمه عبر عدة صفحات.
1. افتح HTML المصدر باستخدام خيارات التحميل التي تم تكوينها ودع Aspose.PDF ينشئ تخطيط الصفحة في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. احفظ ملف PDF الناتج.

```java
public static void convertHtmlToPdfRenderContentToSamePage(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setRenderToSinglePage(true);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل HTML يحتوي على SVG مضمنة

استخدم هذا المثال عندما يتضمن مصدر HTML بيانات SVG مضمنة يجب عرضها في ملف PDF.

1. قم بإنشاء مثيل [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) باستخدام الدليل الأصلي لملف HTML كمسار أساسي بحيث يمكن حل الموارد ذات الصلة بشكل متسق أثناء التحويل.
1. افتح ملف HTML الذي يحتوي على علامة SVG المضمنة عن طريق تمرير المسار المصدر وخيارات التحميل إلى المُنشئ [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اسمح لـ Aspose.PDF بعرض HTML DOM مع عناصر SVG المضمنة في محتوى صفحة PDF.
1. احفظ مستند PDF الذي تم إنشاؤه.

```java
public static void convertHtmlToPdfWithSvgData(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions(inputFile.getParent().toString());
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل صفحة ويب إلى PDF

استخدم هذا المثال عندما يجب عرض عنوان URL المباشر للويب وحفظه كمستند PDF.

1. قم بإنشاء مثيل [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) باستخدام عنوان URL المستهدف بحيث يمكن تحليل الموارد النسبية مثل أوراق الأنماط والصور مقابل هذا العنوان.
1. قم بتحويل سلسلة URL إلى كائن `URL` وافتح تدفق الإدخال الخاص بها لجلب محتوى HTML المباشر.
1. قم بإنشاء [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) من تدفق الاستجابة وخيارات التحميل التي تم تكوينها بحيث تتم معالجة الصفحة التي تم تنزيلها باستخدام عنوان URL الأساسي الصحيح.
1. احفظ صفحة الويب المعروضة كملف PDF وأغلق موارد الدفق تلقائيًا من خلال تجربة الموارد.

```java
public static void convertWebPageToPdf(String urlString, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions(urlString);
    try {
        URL url = URI.create(urlString).toURL();

        try (InputStream inputStream = url.openStream()) {
            try (Document document = new Document(inputStream, loadOptions)) {
                document.save(outputFile.toString());
            }
        }
        System.out.println(url + " converted into " + outputFile);
    } catch (Exception e) {
        e.printStackTrace();
    }
}
```

## تحويل MHTML إلى PDF

استخدم هذا المثال عندما يجب تحويل ملف MHTML المؤرشف إلى مستند PDF.

1. قم بإنشاء مثيل [`MhtLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/mhtloadoptions/) لإخبار Aspose.PDF بتحميل المصدر كمحتوى MIME HTML.
1. افتح الملف `.mht` أو `.mhtml` عن طريق تمرير مساره وخيارات تحميل MHTML إلى المُنشئ [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اسمح لـ Aspose.PDF بتحليل محتوى HTML المؤرشف وموارده المضمنة في نموذج مستند PDF.
1. احفظ ملف PDF الذي تم إنشاؤه.

```java
public static void convertMhtmlToPdf(Path inputFile, Path outputFile) {
    MhtLoadOptions loadOptions = new MhtLoadOptions();
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
