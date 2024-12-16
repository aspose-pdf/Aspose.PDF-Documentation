---
title: تحويل ملف PDF إلى تنسيق HTML
linktitle: تحويل ملف PDF إلى تنسيق HTML
type: docs
weight: 50
url: /ar/java/convert-pdf-to-html/
lastmod: "2021-11-19"
description: يوضح هذا الموضوع كيف يسمح Aspose.PDF بتحويل ملف PDF إلى تنسيق HTML باستخدام مكتبة Java.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

يوفر Aspose.PDF for Java العديد من الميزات لتحويل صيغ الملفات المختلفة إلى مستندات PDF وتحويل ملفات PDF إلى صيغ إخراج مختلفة. يناقش هذا المقال كيفية تحويل ملف PDF إلى تنسيق HTML وحفظ الصور من ملف PDF في مجلد معين.

{{% alert color="success" %}}
**حاول تحويل PDF إلى HTML عبر الإنترنت**

يقدم لك Aspose.PDF for Java تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى HTML مع تطبيق مجاني](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)

{{% /alert %}}

عند تحويل ملف PDF كبير يحتوي على عدة صفحات إلى تنسيق HTML، يظهر الناتج كصفحة HTML واحدة. قد يصبح طويلًا جدًا. للتحكم في حجم الصفحة، من الممكن تقسيم الناتج إلى عدة صفحات أثناء تحويل PDF إلى HTML.

## تحويل صفحات PDF إلى HTML

يوفر Aspose.PDF for Java العديد من الميزات لتحويل تنسيقات الملفات المختلفة إلى مستندات PDF وتحويل ملفات PDF إلى تنسيقات إخراج متنوعة. تناقش هذه المقالة كيفية تحويل ملف PDF إلى تنسيق HTML وحفظ الصور من ملف PDF في مجلد معين.

يوضح لك مقطع الشيفرة التالي جميع الخيارات الممكنة التي يمكنك استخدامها عند تحويل PDF إلى HTML.

```java
// افتح مستند PDF المصدر
Document pdfDocument = new Document(_dataDir + "PDFToHTML.pdf");

// احفظ الملف بتنسيق مستند MS
pdfDocument.save(_dataDir + "output_out.html", SaveFormat.Html);
```

## تحويل PDF إلى HTML - تقسيم الناتج إلى HTML متعدد الصفحات

يدعم Aspose.PDF for Java ميزة تحويل مستندات PDF إلى تنسيقات إخراج متنوعة بما في ذلك HTML.
 ومع ذلك، عند تحويل ملفات PDF كبيرة (تتألف من صفحات متعددة)، قد يكون لديك حاجة لحفظ صفحة PDF فردية إلى ملف HTML منفصل.

عند تحويل ملف PDF كبير مع عدة صفحات إلى تنسيق HTML، يظهر الناتج كصفحة HTML واحدة. قد ينتهي الأمر بأن يكون طويلًا جدًا. للتحكم في حجم الصفحة، من الممكن تقسيم الناتج إلى عدة صفحات أثناء تحويل PDF إلى HTML. يرجى محاولة استخدام مقتطف الشيفرة التالي.

```java
// افتح مستند PDF المصدر
Document document = new Document(_dataDir + "PDFToHTML.pdf");

// إنشاء كائن خيارات حفظ HTML
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();

// تحديد تقسيم الناتج إلى صفحات متعددة
htmlOptions.setSplitIntoPages(true);

// احفظ المستند
document.save(_dataDir + "MultiPageHTML_out.html", htmlOptions);    
```

## تحويل PDF إلى HTML - تجنب حفظ الصور بتنسيق SVG

التنسيق الافتراضي لحفظ الصور عند التحويل من PDF إلى HTML هو SVG. أثناء التحويل، تتحول بعض الصور من PDF إلى صور متجهة SVG. قد يكون هذا بطيئًا. بدلاً من ذلك، يمكن تحويل الصور إلى PNG. للسماح بذلك، توفر Aspose.PDF خيار استخدام SVG للمتجهات أو إنشاء PNGs.

لإزالة عرض الصور بشكل كامل كصيغة SVG عند تحويل ملفات PDF إلى صيغة HTML، يرجى محاولة استخدام كود الشفرة التالي.

```java
 // تحميل ملف PDF
Document document = new Document(DATA_DIR + "PDFToHTML.pdf")

// إنشاء كائن خيارات الحفظ لـ HTML
HtmlSaveOptions saveOptions = new HtmlSaveOptions();

// تحديد المجلد الذي تُحفظ فيه صور SVG أثناء تحويل PDF إلى HTML
saveOptions.setSpecialFolderForSvgImages(DATA_DIR.toString());

// حفظ الملف الناتج
document.save(DATA_DIR + "SaveSVGFiles_out.html", saveOptions);
```

## ضغط صور SVG أثناء التحويل

لضغط صور SVG أثناء تحويل PDF إلى HTML، يرجى محاولة استخدام الكود التالي:

```java
// تحميل ملف PDF
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");

// إنشاء خيار حفظ HTML مع الميزة المختبرة
HtmlSaveOptions saveOptions = new HtmlSaveOptions();

// ضغط صور SVG إذا كانت موجودة
saveOptions.setCompressSvgGraphicsIfAny(true);
document.save(DATA_DIR + "SaveSVGFiles_out.html", saveOptions);
document.close();
```

## تحويل PDF إلى HTML - تحديد مجلد الصور

بشكل افتراضي، عند تحويل ملف PDF إلى HTML، يتم حفظ الصور في ملف PDF في مجلد منفصل يتم إنشاؤه في نفس الدليل الذي يتم إنشاء ملف HTML الناتج فيه. ولكن في بعض الأحيان، يكون من الضروري تحديد مجلد مختلف لحفظ الصور عند إنشاء ملفات HTML. لتحقيق ذلك، قمنا بتقديم [SaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SaveOptions).
يستخدم [طريقة SpecialFolderForAllImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/#setSpecialFolderForAllImages-java.lang.String-) لتحديد المجلد المستهدف لتخزين الصور.

```java
// تحميل ملف PDF
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");
HtmlSaveOptions saveOptions = new HtmlSaveOptions();

// تحديد المجلد المنفصل لحفظ الصور
saveOptions.setSpecialFolderForAllImages(DATA_DIR.toString());
document.save(DATA_DIR + "SaveSVGFiles_out.html", saveOptions);
document.close();
```

## إنشاء ملفات لاحقة بمحتويات الجسم فقط

مع مقتطف الشيفرة البسيط التالي، يمكنك تقسيم مخرجات HTML إلى صفحات. في صفحات المخرجات، يجب أن تذهب جميع كائنات HTML إلى أماكنها الحالية بالضبط (معالجة الخطوط والمخرجات، إنشاء CSS والمخرجات، إنشاء الصور والمخرجات)، باستثناء أن مخرجات HTML ستحتوي على المحتويات الموضوعة حاليًا داخل العلامات (الآن سيتم إغفال علامات "body").

```java
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");

HtmlSaveOptions saveOptions = new HtmlSaveOptions();

saveOptions.setHtmlMarkupGenerationMode(HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent);
saveOptions.setSplitIntoPages(true);

document.save(DATA_DIR + "CreateSubsequentFiles_out.html", saveOptions);
document.close();
```

## عرض النص الشفاف

في حالة احتواء ملف PDF المصدر/المدخل على نصوص شفافة مغطاة بصور في المقدمة، فقد تكون هناك مشكلات في عرض النصوص. لذا لمعالجة مثل هذه السيناريوهات، يمكن استخدام طريقتي `setSaveShadowedTextsAsTransparentTexts` و `setSaveTransparentTexts`.

```java
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");

// إنشاء كائن خيارات حفظ HTML
HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();
htmlsaveOptions.setSaveShadowedTextsAsTransparentTexts(true);
htmlsaveOptions.setSaveTransparentTexts(true);

// حفظ المستند
document.save(DATA_DIR + "TransparentTextRendering_out.html", htmlsaveOptions);
document.close();
```


## عرض طبقات مستند PDF

يمكننا عرض طبقات مستند PDF في عنصر نوع طبقة منفصل أثناء تحويل PDF إلى HTML:

```java
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");
// إنشاء كائن HTML SaveOptions

HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();

// تحديد عرض طبقات مستند PDF بشكل منفصل في HTML الناتج
htmlsaveOptions.setConvertMarkedContentToLayers(true);

// حفظ المستند
document.save(DATA_DIR + "LayersRendering_out.html", htmlsaveOptions);
document.close();
```

يعد تحويل PDF إلى HTML أحد أكثر الميزات شيوعًا في Aspose.PDF لأنه يجعل من الممكن عرض محتوى ملفات PDF على منصات مختلفة دون استخدام عارض مستندات PDF. يتوافق HTML الناتج مع معايير WWW ويمكن عرضه بسهولة في جميع متصفحات الويب. باستخدام هذه الميزة، يمكن عرض ملفات PDF على الأجهزة المحمولة لأنك لا تحتاج إلى تثبيت أي تطبيق لعرض PDF ولكن يمكنك استخدام متصفح ويب بسيط.


## PDF إلى HTML - استثناء موارد الخطوط

إذا كنت تنوي استبعاد جميع أو بعض موارد الخطوط أثناء تحويل PDF إلى HTML، يتيح لك Aspose.PDF for Java API تحقيق ذلك بمساعدة فئة HtmlSaveOptions. توفر API خيارين لهذا الغرض.

- `htmlOptions.FontSavingMode = HTmlSaveOptions.FontSavingModes.DontSave` - لمنع تصدير جميع الخطوط
- `htmlOptions.ExcludeFontNameList = (new String[] { "ArialMT", "SymbolMT" });` - هو لمنع تصدير خطوط معينة (يجب تحديد أسماء الخطوط بدون علامات)

من أجل تحويل PDF إلى HTML مع استبعاد موارد الخطوط، استخدم الخطوات التالية:

1. تعريف كائن جديد من فئة HtmlSaveOptions
2. تعريف وتعيين أسماء الخطوط التي يجب منع تصديرها في HtmlSaveOptions.ExcludeFontNameList
3. تحويل PDF إلى HTML باستخدام طريقة الحفظ

```java
HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();
htmlsaveOptions.setExplicitListOfSavedPages(
        new int[]{
                1
        }
);
htmlsaveOptions.setFixedLayout(true);
htmlsaveOptions.setCompressSvgGraphicsIfAny(false);
htmlsaveOptions.setSaveTransparentTexts(true);
htmlsaveOptions.setSaveShadowedTextsAsTransparentTexts(true);
htmlsaveOptions.setExcludeFontNameList(new String[]{"ArialMT", "SymbolMT"});
htmlsaveOptions.setFontSavingMode(HtmlSaveOptions.FontSavingModes.DontSave);
htmlsaveOptions.setDefaultFontName("Comic Sans MS");
htmlsaveOptions.setUseZOrder(true);
htmlsaveOptions
        .setLettersPositioningMethod(LettersPositioningMethods.UseEmUnitsAndCompensationOfRoundingErrorsInCss);
htmlsaveOptions
        .setPartsEmbeddingMode(HtmlSaveOptions.PartsEmbeddingModes.NoEmbedding);
htmlsaveOptions
        .setRasterImagesSavingMode(HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
htmlsaveOptions.setSplitIntoPages(false);

Document document = new Document(DATA_DIR + "sample.pdf");
document.save(DATA_DIR + "output_out.html", htmlsaveOptions);
document.close();
```