---
title: تحويل ملف PDF إلى تنسيق HTML
linktitle: تحويل ملف PDF إلى تنسيق HTML
type: docs
weight: 50
url: ar/cpp/convert-pdf-to-html/
lastmod: "2021-11-19"
description: يوضح هذا الموضوع كيفية استخدام Aspose.PDF لتحويل ملف PDF إلى تنسيق HTML باستخدام مكتبة C++.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

يوفر **Aspose.PDF for C++** العديد من الميزات لتحويل تنسيقات الملفات المختلفة إلى مستندات PDF وتحويل ملفات PDF إلى تنسيقات إخراج مختلفة. تناقش هذه المقالة كيفية تحويل ملف PDF إلى <abbr title="لغة ترميز النص التشعبي">HTML</abbr>. يوفر Aspose.PDF for C++ القدرة على تحويل ملفات HTML إلى تنسيق PDF باستخدام نهج InLineHtml. لقد تلقينا العديد من الطلبات للحصول على وظيفة تحويل ملف PDF إلى تنسيق HTML وقد وفرنا هذه الميزة. يرجى ملاحظة أن هذه الميزة تدعم أيضًا XHTML 1.0.

يدعم **Aspose.PDF for C++** الميزات لتحويل ملف PDF إلى HTML. The main tasks you can accomplish with the Aspose.PDF library are listed:

- تحويل PDF إلى HTML;
- تقسيم المخرجات إلى HTML متعدد الصفحات;
- تحديد مجلد لتخزين ملفات SVG;
- ضغط صور SVG أثناء التحويل;
- تحديد مجلد الصور;
- إنشاء ملفات لاحقة بمحتويات الجسم فقط;
- عرض النص الشفاف;
- عرض طبقات مستند PDF.

Aspose.PDF for C++ يوفر كود من خطين لتحويل ملف PDF المصدر إلى HTML. يحتوي `SaveFormat enumeration` على القيمة Html التي تتيح لك حفظ الملف المصدر إلى HTML. يوضح مقتطف الشفرة التالي عملية تحويل ملف PDF إلى HTML.

```cpp
void ConvertPDFtoHTML()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for file name
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
    // Save the output in HTML format
    document->Save(outfilename, SaveFormat::Html);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى HTML عبر الإنترنت**

يقدم Aspose.PDF لـ C++ تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html)، حيث يمكنك محاولة التحقيق في الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى HTML باستخدام التطبيق المجاني](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

## تقسيم المخرجات إلى HTML متعدد الصفحات

عند تحويل ملف PDF كبير يحتوي على عدة صفحات إلى تنسيق HTML، تظهر النتيجة كصفحة HTML واحدة. يمكن أن تصبح طويلة جدًا. للتحكم في حجم الصفحة، من الممكن تقسيم المخرجات إلى عدة صفحات أثناء تحويل PDF إلى HTML. يرجى محاولة استخدام مقتطف الشيفرة التالي.

```cpp
void ConvertPDFtoHTML_SplittingOutputToMultiPageHTML()
{
    std::clog << __func__ << ": Start" << std::endl;
    // سلسلة لمسار الاسم
    String _dataDir("C:\\Samples\\Conversion\\");

    // سلسلة لاسم الملف
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + infilename);

    // إنشاء كائن خيار حفظ HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();
    // تحديد تقسيم المخرجات إلى صفحات متعددة
    htmlOptions->set_SplitIntoPages(true);

    try {
    // حفظ المخرجات بتنسيق HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```
```

## تحديد المجلد لتخزين ملفات SVG

أثناء تحويل PDF إلى HTML، من الممكن تحديد المجلد الذي يجب حفظ صور SVG فيه. استخدم [`HtmlSaveOption class`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options) [`SpecialFolderForSvgImages property`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options#ac1bb3905c599118fb3db67fd67a5a06f) لتحديد دليل صور SVG خاص. تقوم هذه الخاصية بالحصول على أو تعيين المسار إلى الدليل الذي يجب حفظ صور SVG فيه عند مواجهتها أثناء التحويل. إذا كانت المعلمة فارغة أو null، فسيتم حفظ أي ملفات SVG مع ملفات الصور الأخرى.

```cpp
void ConvertPDFtoHTML_SpecifyFolderForStoringSVGfiles()
{
    std::clog << __func__ << ": Start" << std::endl;
    // سلسلة لاسم المسار
    String _dataDir("C:\\Samples\\Conversion\\");

    // سلسلة لاسم الملف
    String infilename("sample.pdf");
    String outfilename("SaveSVGFiles_out.html");

    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + infilename);

    // إنشاء كائن خيار حفظ HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // تحديد المجلد حيث يتم حفظ صور SVG أثناء تحويل PDF إلى HTML
    htmlOptions->SpecialFolderForSvgImages = (_dataDir + String("\\svg\\"));

    // حفظ الإخراج بتنسيق HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## ضغط صور SVG أثناء التحويل

لضغط صور SVG أثناء تحويل PDF إلى HTML، يرجى محاولة استخدام الكود التالي:

```cpp
void ConvertPDFtoHTML_CompressingSVGimages()
{
    std::clog << __func__ << ": Start" << std::endl;
    // سلسلة لاسم المسار
    String _dataDir("C:\\Samples\\Conversion\\");

    // سلسلة لاسم الملف
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + infilename);

    // إنشاء كائن خيار حفظ HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // تحديد المجلد الذي تُحفظ فيه صور SVG أثناء تحويل PDF إلى HTML
    htmlOptions->SpecialFolderForSvgImages = (_dataDir + String("\\svg\\"));

    // حفظ النتيجة بتنسيق HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## تحديد مجلد الصور

يمكننا أيضًا تحديد المجلد الذي سيتم حفظ الصور فيه أثناء تحويل PDF إلى HTML:

```cpp
void ConvertPDFtoHTML_SpecifyFolderForStoringAllImages()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for file name
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instantiate HTML Save Option object
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // Specify the folder where All images are saved during PDF to HTML conversion
    htmlOptions->SpecialFolderForAllImages = (_dataDir + String("\\images\\"));

    // Save the output in HTML format
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## إنشاء ملفات لاحقة بمحتويات الجسم فقط

مؤخراً، طلب منا تقديم ميزة حيث يتم تحويل ملفات PDF إلى HTML ويمكن للمستخدم الحصول على محتويات وسم `<body>` فقط لكل صفحة. هذا سينتج ملفًا واحدًا يحتوي على CSS، تفاصيل `<html>` و `<head>` وجميع الصفحات في ملفات أخرى فقط بمحتويات `<body>`.

لتلبية هذا المتطلب، تم تقديم خاصية جديدة، HtmlMarkupGenerationMode، إلى فئة [HtmlSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options).

باستخدام جزء الكود البسيط التالي، يمكنك تقسيم HTML الناتج إلى صفحات. في الصفحات الناتجة، يجب أن تذهب جميع كائنات HTML تمامًا حيث تذهب الآن (معالجة وإخراج الخطوط، إنشاء وإخراج CSS، إنشاء وإخراج الصور)، باستثناء أن HTML الناتج سيحتوي على محتويات موجودة حاليًا داخل العلامات (الآن سيتم حذف العلامات “body”). ومع ذلك، عند استخدام هذا النهج، تكون مسؤولية ربط CSS على عاتق الكود الخاص بك، لأن الأشياء مثل سيتم حذفها. لهذا الغرض، يمكنك قراءة CSS عبر File.ReadAllText() وإرساله عبر AJAX إلى صفحة ويب حيث سيتم تطبيقه بواسطة jQuery.

```cpp
void ConvertPDFtoHTML_CreateSubsequentFilesWithBodyContentsOnly()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for file name
    String infilename("sample.pdf");
    String outfilename("CreateSubsequentFiles_out.html");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instantiate HTML Save Option object
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    htmlOptions->HtmlMarkupGenerationMode = HtmlSaveOptions::HtmlMarkupGenerationModes::WriteOnlyBodyContent;
    htmlOptions->set_SplitIntoPages(true);

    // Save the output in HTML format
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## عرض النص الشفاف

في حالة احتواء ملف PDF المصدر/الإدخال على نصوص شفافة مغطاة بصور في المقدمة، فقد تحدث مشكلات في عرض النص. لذا، من أجل معالجة مثل هذه السيناريوهات، يمكن استخدام خصائص [SaveShadowedTextsAsTransparentTexts](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options#a6269cf414eb8c252f0ba64a0baf2f9ef) و SaveTransparentTexts.

```cpp
void ConvertPDFtoHTML_TransparentTextRendering()
{
    std::clog << __func__ << ": Start" << std::endl;
    // سلسلة لاسم المسار
    String _dataDir("C:\\Samples\\Conversion\\");

    // سلسلة لاسم الملف
    String infilename("sample.pdf");
    String outfilename("TransparentTextRendering_out.html");

    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + infilename);

    // إنشاء كائن خيار حفظ HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    htmlOptions->HtmlMarkupGenerationMode = HtmlSaveOptions::HtmlMarkupGenerationModes::WriteOnlyBodyContent;
    htmlOptions->SaveShadowedTextsAsTransparentTexts = true;
    htmlOptions->SaveTransparentTexts = true;

    // حفظ النتيجة بتنسيق HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## عرض طبقات مستند PDF

يمكننا عرض طبقات مستند PDF في عنصر نوع طبقة منفصلة أثناء تحويل PDF إلى HTML:

```cpp
void ConvertPDFtoHTML_DocumentLayersRendering()
{
    std::clog << __func__ << ": Start" << std::endl;
    // سلسلة لاسم المسار
    String _dataDir("C:\\Samples\\Conversion\\");

    // سلسلة لاسم الملف
    String infilename("sample.pdf");
    String outfilename("LayersRendering_out.html");

    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + infilename);

    // إنشاء كائن خيار حفظ HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // تحديد عرض طبقات مستند PDF بشكل منفصل في HTML الناتج
    htmlOptions->set_ConvertMarkedContentToLayers(true);

    // حفظ الناتج بتنسيق HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```