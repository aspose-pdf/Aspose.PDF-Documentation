---
title: تحويل HTML إلى PDF في Java
linktitle: تحويل HTML إلى ملف PDF
type: docs
weight: 40
url: /ar/java/convert-html-to-pdf/
lastmod: "2026-10-05"
description: تعرّف على كيفية تحويل HTML و MHTML وصفحات الويب إلى PDF في Java باستخدام Aspose.PDF، بما في ذلك إعدادات الوسائط، قواعد صفحات CSS، تضمين الخط، محتوى SVG، والإخراج بصفحة واحدة.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: كيفية تحويل HTML إلى PDF في Java باستخدام Aspose.PDF
Abstract: تشرح هذه المقالة كيفية تحويل ملفات HTML و MHTML إلى PDF باستخدام Aspose.PDF for Java. تغطي سير عمل التحويل الأساسي من HTML إلى PDF وتظهر كيفية التحكم في العرض باستخدام أنواع الوسائط، أولوية قواعد صفحة CSS، الخطوط المدمجة، محتوى SVG، الإخراج بصفحة واحدة، والتحويل المباشر من صفحة ويب حية.
---
يمكن لـ Aspose.PDF for Java تحويل ملفات HTML المحلية، ومحتوى MHTML المؤرشف، وصفحات الويب الحية إلى مستندات PDF. يمكنك التحكم في خط أنابيب التحويل باستخدام `HtmlLoadOptions` و `MhtLoadOptions` للتأثير على تحجيم التخطيط، معالجة وسائط CSS، أولوية قواعد الصفحة، تضمين الخطوط، حل الموارد، وسلوك عرض الصفحة الواحدة.

## تحويل HTML إلى PDF

استخدم هذا المثال عندما يجب تحويل ملف HTML محلي مباشرةً إلى مستند PDF.

1. أنشئ كائنًا من الفئة [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) لتكوين كيفية تفسير مصدر HTML أثناء الاستيراد.
1. عيّن [`HtmlPageLayoutOption`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlpagelayoutoption/) إلى `ScaleToPageWidth` لذلك يتم تعديل محتوى HTML الواسع ليتناسب مع عرض صفحة PDF المستهدفة بدلاً من قطعه.
1. افتح ملف HTML المصدر عن طريق تمرير مساره وخيارات التحميل المُكوَّنة إلى [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) منشئ.
1. احفظ ما تم إنشاؤه [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) كملف PDF في مسار الإخراج المستهدف.

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

1. أنشئ مثيلًا [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) لإعدادات التحويل.
1. عيّن [`HtmlMediaType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlmediatype/) إلى `Screen` عند الحاجة إلى عرض HTML باستخدام قواعد CSS المخصصة للعرض على الشاشة بدلاً من وسائط الطباعة.
1. افتح ملف HTML باستخدام خيارات التحميل المكوَّنة بحيث يتم تطبيق الأنماط المعتمدة على استعلامات الوسائط أثناء التحويل.
1. احفظ الناتج [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) كملف PDF..

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

استخدم هذا المثال عند CSS `@page` يجب أن تؤثر القواعد على تخطيط صفحة PDF النهائي.

1. أنشئ المثيل [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) قبل فتح ملف HTML..
1. اضبط `setPriorityCssPageRule(false)` عندما يجب أن تتجاوز إعدادات التخطيط الأخرى CSS `@page` الإعلانات في ترميز المصدر.
1. حمّل محتوى HTML إلى [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مع الخيارات المُكوَّنة بحيث يتم حل تخطيط الصفحة أثناء الاستيراد.
1. احفظ ملف PDF المُنتج.

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

## تحويل HTML إلى PDF مع خطوط مضمنة

استخدم هذا المثال عندما يجب على ملف PDF الناتج الحفاظ على خطوط HTML عن طريق تضمينها.

1. أنشئ مثيلًا [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) لتكوين استيراد HTML..
1. فعّل `setEmbedFonts(true)` لذا يتم تخزين الخطوط التي تم حلّها أثناء عرض HTML في ملف PDF الناتج.
1. افتح مصدر HTML باستخدام خيارات التحميل هذه للحفاظ على الطباعة الأصلية المتاحة في المستند النهائي.
1. احفظ [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) كملف PDF مع تضمين موارد الخط المدمجة.

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

1. أنشئ مثيلًا [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) لإعدادات التحويل.
1. فعّل `setRenderToSinglePage(true)` لذا فإن HTML المستورد يُعرض على صفحة PDF واحدة بدلاً من أن يتم تقسيمه على عدة صفحات.
1. افتح ملف HTML المصدر باستخدام خيارات التحميل المكوَّنة ودع Aspose.PDF يبني تخطيط الصفحة في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
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

## تحويل HTML يحتوي على SVG مضمّن

استخدم هذا المثال عندما يتضمن مصدر HTML بيانات SVG مدمجة يجب عرضها في ملف PDF.

1. أنشئ كائنًا من الفئة [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) مثال يضع الدليل الأب لملف HTML كمسار أساسي بحيث يمكن حل الموارد ذات الصلة بشكل ثابت أثناء التحويل.
1. افتح ملف HTML الذي يحتوي على ترميز SVG مضمن بتمرير مسار المصدر وخيارات التحميل إلى [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) منشئ.
1. دع Aspose.PDF يعيد رسم DOM HTML مع العناصر المدمجة SVG إلى محتوى صفحة PDF..
1. احفظ مستند PDF المُولَّد.

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

استخدم هذا المثال عندما يجب عرض عنوان URL ويب مباشر وحفظه كمستند PDF.

1. أنشئ كائنًا من الفئة [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) مثال مع عنوان URL الهدف بحيث يمكن حل الموارد النسبية مثل أوراق الأنماط والصور بالنسبة لهذا العنوان.
1. حوّل سلسلة URL إلى الكائن `URL` وفتح تدفق الإدخال الخاص به لجلب محتوى HTML الحي.
1. أنشئ كائنًا من الفئة [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) من تدفق الاستجابة وخيارات التحميل المكوَّنة بحيث تتم معالجة الصفحة التي تم تنزيلها باستخدام عنوان URL الأساسي الصحيح.
1. احفظ صفحة الويب المعروضة كملف PDF وأغلق موارد التدفق تلقائيًا باستخدام try-with-resources..

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

استخدم هذا المثال عندما يجب تحويل ملف MHTML مؤرشف إلى مستند PDF.

1. أنشئ المثيل [`MhtLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/mhtloadoptions/) لإخبار Aspose.PDF بتحميل المصدر كـ MIME HTML content..
1. افتح `.mht` أو `.mhtml` ملف عن طريق تمرير مساره وخيارات تحميل MHTML إلى [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) منشئ.
1. دع Aspose.PDF يقوم بتحليل محتوى HTML المؤرشف والموارد المدمجة فيه إلى نموذج مستند PDF..
1. احفظ ملف PDF المُنتج.

```java
public static void convertMhtmlToPdf(Path inputFile, Path outputFile) {
    MhtLoadOptions loadOptions = new MhtLoadOptions();
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
