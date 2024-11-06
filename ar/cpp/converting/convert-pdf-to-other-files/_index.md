---
title: تحويل ملف PDF إلى تنسيقات أخرى
linktitle: تحويل PDF إلى تنسيقات أخرى
type: docs
weight: 90
url: ar/cpp/convert-pdf-to-other-files/
lastmod: "2021-11-19"
description: يوضح هذا الموضوع كيف يسمح Aspose.PDF بتحويل ملف PDF إلى تنسيقات ملفات أخرى.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## تحويل PDF إلى EPUB

{{% alert color="success" %}}
**حاول تحويل PDF إلى EPUB عبر الإنترنت**

يقدم لك Aspose.PDF for C++ تطبيقًا مجانيًا عبر الإنترنت ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى EPUB مع تطبيق مجاني](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

<abbr title="Electronic Publication">EPUB</abbr> (اختصار لـ Electronic Publication) هو معيار كتاب إلكتروني مجاني ومفتوح من منتدى النشر الرقمي الدولي (IDPF). تكون الملفات بامتداد .epub. تم تصميم EPUB لمحتوى قابل لإعادة التدفق، مما يعني أن قارئ EPUB يمكنه تحسين النص لجهاز عرض معين. EPUB يدعم أيضًا المحتوى الثابت التنسيق. يُقصد من التنسيق أن يكون تنسيقًا موحدًا يمكن للناشرين وبيوت التحويل استخدامه داخليًا، وكذلك للتوزيع والبيع. إنه يحل محل معيار الكتاب الإلكتروني المفتوح.

Aspose.PDF for C++ يدعم أيضًا ميزة تحويل مستندات PDF إلى تنسيق EPUB. يحتوي Aspose.PDF for C++ على فئة تسمى EpubSaveOptions والتي يمكن استخدامها كمعامل ثاني لطريقة [`Document.Save(..)`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa)، لإنشاء ملف EPUB. يرجى محاولة استخدام مقتطف الشيفرة التالي لتحقيق هذا المتطلب باستخدام C++.

```cpp
void ConvertPDFtoEPUB()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for input file name
    String infilename("sample.pdf");
    // String for output file name
    String outfilename("PDFToEPUB_out.epub");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Save PDF file into EPUB format
    document->Save(_dataDir + outfilename, SaveFormat::Epub);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## تحويل PDF إلى LaTeX/TeX

يدعم **Aspose.PDF for C++** تحويل PDF إلى LaTeX/TeX. 
تنسيق ملف LaTeX هو تنسيق ملف نصي مع ترميز خاص ويستخدم في نظام إعداد المستندات القائم على TeX لتنسيق عالي الجودة.

لتحويل ملفات PDF إلى TeX، يحتوي Aspose.PDF على الفئة [LaTeXSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.la_te_x_save_options) التي توفر الخاصية OutDirectoryPath لحفظ الصور المؤقتة أثناء عملية التحويل.

يظهر مقتطف الشفرة التالي عملية تحويل ملفات PDF إلى تنسيق TEX باستخدام C++.

```cpp
void ConvertPDFtoLaTeX()
{
    std::clog << __func__ << ": Start" << std::endl;
    // سلسلة لاسم المسار
    String _dataDir("C:\\Samples\\Conversion\\");

    // سلسلة لاسم الملف المدخل
    String infilename("sample.pdf");
    // سلسلة لاسم الملف المخرج
    String outfilename("PDFToTeX_out.tex");

    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + infilename);

    // إنشاء خيار حفظ LaTeX
    auto saveOptions = MakeObject<LaTeXSaveOptions>();

    // تعيين مسار دليل الخرج لكائن خيار الحفظ
    saveOptions->set_OutDirectoryPath(_dataDir);

    // حفظ ملف PDF بتنسيق LaTeX
    document->Save(_dataDir + outfilename, saveOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى LaTeX/TeX عبر الإنترنت**

تقدم Aspose.PDF for C++ لك تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي تعمل بها.

[![Aspose.PDF تحويل PDF إلى LaTeX/TeX باستخدام التطبيق المجاني](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## تحويل PDF إلى نص

يدعم **Aspose.PDF for C++** تحويل وثيقة PDF كاملة وصفحة واحدة إلى ملف نصي.

### تحويل وثيقة PDF كاملة إلى ملف نصي

يمكنك تحويل وثيقة PDF إلى ملف TXT باستخدام فئة [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_absorber/).

يوضح مقتطف الكود التالي كيفية استخراج النصوص من جميع الصفحات.

```cpp
void ConvertPDFDocToTXT()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for input file name
    String infilename("sample.pdf");
    // String for output file name
    String outfilename("input_Text_Extracted_out.txt");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto ta = MakeObject<TextAbsorber>();
    ta->Visit(document);
    // Save the extracted text in text file
    System::IO::File::WriteAllText(_dataDir + outfilename, ta->get_Text());
    std::clog << __func__ << ": Finish" << std::endl;
}
```

### تحويل صفحة PDF إلى ملف نصي

يمكنك تحويل مستند PDF إلى ملف TXT باستخدام Aspose.PDF لـ C++. يجب عليك استخدام [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_absorber/) لحل هذه المهمة.

يشرح مقطع الشيفرة التالي كيفية استخراج النصوص من الصفحات المحددة.

```cpp
void ConvertPDFPagestoTXT()
{
    std::clog << __func__ << ": Start" << std::endl;
    // سلسلة لمسار الاسم
    String _dataDir("C:\\Samples\\Conversion\\");

    // سلسلة لاسم الملف المدخل
    String infilename("sample-4pages.pdf");
    // سلسلة لاسم الملف الناتج
    String outfilename("sample-4pages_out.txt");

    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto ta = MakeObject<TextAbsorber>();

    auto pages = { 1, 3, 4 };
    try {
    for (auto page : pages)
    {
    ta->Visit(document->get_Pages()->idx_get(page));
    }
    // حفظ النص المستخرج في ملف نصي
    auto text = ta->get_Text();
    System::IO::File::WriteAllText(_dataDir + outfilename, text);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى نص عبر الإنترنت**

يقدم Aspose.PDF for C++ تطبيقًا مجانيًا عبر الإنترنت ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى نص باستخدام تطبيق مجاني](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## تحويل PDF إلى XPS

يوفر **Aspose.PDF for C++** إمكانية تحويل ملفات PDF إلى تنسيق <abbr title="XML Paper Specification">XPS</abbr>. دعونا نحاول استخدام كود المثال المقدم لتحويل ملفات PDF إلى تنسيق XPS باستخدام C++.

يرتبط نوع ملف XPS بشكل أساسي بمواصفات XML Paper Specification من قبل شركة Microsoft Corporation. مواصفات XML Paper Specification (XPS)، والتي كانت تُعرف سابقًا باسم Metro وتحتوي على مفهوم التسويق Next Generation Print Path (NGPP)، هي مبادرة من Microsoft لدمج إنشاء المستندات وعرضها في نظام التشغيل Windows.

لتحويل ملفات PDF إلى XPS، يحتوي Aspose.PDF على الفئة [XpsSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.xps_save_options) والتي تُستخدم كحجة ثانية لطريقة [Document.Save(..)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) لتوليد ملف XPS.

الشفرة البرمجية التالية توضح عملية تحويل ملف PDF إلى تنسيق XPS.

```cpp
void ConvertPDFtoXPS()
{
    std::clog << __func__ << ": Start" << std::endl;
    // سلسلة نصية لاسم المسار
    String _dataDir("C:\\Samples\\Conversion\\");

    // سلسلة نصية لاسم الملف المدخل
    String infilename("sample.pdf");
    // سلسلة نصية لاسم ملف الإخراج
    String outfilename("PDFToXPS_out.xps");

    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + infilename);

    // إنشاء خيار حفظ LaTex
    auto saveOptions = MakeObject<XpsSaveOptions>();

    // حفظ ملف PDF بتنسيق XPS
    document->Save(_dataDir + outfilename, saveOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى SVG عبر الإنترنت**

يقدم لك Aspose.PDF for C++ تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

{{% /alert %}}
