---
title: تحويل PDF إلى Microsoft PowerPoint في C++
linktitle: تحويل PDF إلى PowerPoint
type: docs
weight: 30
url: /ar/cpp/convert-pdf-to-powerpoint/
description: يسمح Aspose.PDF لك بتحويل PDF إلى صيغة PowerPoint باستخدام C++. هناك إمكانية لتحويل PDF إلى PPTX مع الشرائح كصور.
lastmod: "2021-11-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## نظرة عامة

تشرح هذه المقالة كيفية **تحويل PDF إلى صيغ PowerPoint باستخدام C++**. وتغطي المواضيع التالية.

_الصيغة_: **PPTX**
- [C++ PDF إلى PPTX](#cpp-pdf-to-pptx)
- [C++ تحويل PDF إلى PPTX](#cpp-pdf-to-pptx)
- [C++ كيفية تحويل ملف PDF إلى PPTX](#cpp-pdf-to-pptx)

_الصيغة_: **صيغة Microsoft PowerPoint PPTX**
- [C++ PDF إلى PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ تحويل PDF إلى PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ كيفية تحويل ملف PDF إلى PowerPoint](#cpp-pdf-to-powerpoint-pptx)

مواضيع أخرى مغطاة في هذه المقالة.
- [انظر أيضًا](#see-also)

## تحويلات PDF إلى PowerPoint باستخدام C++

يسمح لك **Aspose.PDF for C++** بتتبع تقدم تحويل PDF إلى PPTX.

أثناء تحويل PDF إلى <abbr title="عرض تقديمي بتنسيق XML لـ Microsoft PowerPoint 2007">PPTX</abbr>، يتم عرض النص كنص يمكنك تحديده/تحديثه. يرجى ملاحظة أنه من أجل تحويل ملفات PDF إلى تنسيق PPTX، يوفر Aspose.PDF فئة تسمى [`PptxSaveOptions`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options). يتم تمرير كائن من فئة PptxSaveOptions كمعامل ثانٍ إلى طريقة [`Document.Save(..) method`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa). يُظهر جزء الكود التالي عملية تحويل ملفات PDF إلى تنسيق PPTX.

## تحويل بسيط من PDF إلى PPTX باستخدام Aspose.PDF لـ C++

من أجل تحويل PDF إلى PPTX، ينصح Aspose.PDF لـ C++ باستخدام خطوات الكود التالية.

<a name="cpp-pdf-to-pptx" id="cpp-pdf-to-pptx"><strong>الخطوات: تحويل PDF إلى PPTX في C++</strong></a> | <a name="cpp-pdf-to-powerpoint-pptx" id="cpp-pdf-to-powerpoint-pptx"><strong>الخطوات: تحويل PDF إلى تنسيق PowerPoint PPTX في C++</strong></a>

1. قم بإنشاء مثيل لفئة [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
2. قم بإنشاء مثيل لفئة [PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options).
3. استخدم طريقة **Save** لكائن **Document** لـ _حفظ ملف PDF كـ PPTX_.

```cpp
void ConvertPDFtoPPTX()
{
    std::clog << __func__ << ": Start" << std::endl;
    // سلسلة لاسم المسار
    String _dataDir("C:\\Samples\\Conversion\\");

    // سلسلة لاسم الملف
    String infilename("JSON Fundamenals.pdf");
    String outfilename("JSON Fundamenals.pptx");

    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + infilename);

    // حفظ المخرجات بتنسيق PPTX
    document->Save(_dataDir + outfilename, SaveFormat::Pptx);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## تحويل PDF إلى PPTX مع الشرائح كصور

في حالة إذا كنت بحاجة لتحويل PDF قابل للبحث إلى PPTX كصور بدلاً من نص قابل للتحديد، يوفر Aspose.PDF مثل هذه الميزة عبر فئة [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options). لتحقيق ذلك، قم بتعيين خاصية [SlidesAsImages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options#aeca0659ae24ea7cdeb171d941440dcb2) من فئة [PptxSaveOptios](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) إلى 'true' كما هو موضح في نموذج الكود التالي.

```cpp
void ConvertPDFtoPPTX_SlidesAsImages()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for file name
    String infilename("JSON Fundamenals.pdf");
    String outfilename("JSON Fundamenals.pptx");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto pptxOptions = MakeObject<PptxSaveOptions>();
    pptxOptions->set_SlidesAsImages(true);

    // Save the output in PPTX format
    document->Save(_dataDir + outfilename, pptxOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## تفاصيل تقدم تحويل PPTX

Aspose.PDF for C++ يتيح لك تتبع تقدم تحويل PDF إلى PPTX. The [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) توفر فئة [CustomProgressHandler](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options#ac9ad606c4b4d7249c5f299fd8d766474) خاصية يمكن تحديدها لطريقة مخصصة لتتبع تقدم التحويل كما هو موضح في عينة الكود التالية.

```cpp
void ConvertPDFtoPPTX_ProgressDetailConversion()
{
    std::clog << __func__ << ": Start" << std::endl;
    // سلسلة لاسم المسار
    String _dataDir("C:\\Samples\\Conversion\\");

    // سلسلة لاسم الملف
    String infilename("JSON Fundamenals.pdf");
    String outfilename("JSON Fundamenals.pptx");

    // افتح المستند
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto pptxOptions = MakeObject<PptxSaveOptions>();
    //pptxOptions->set_SlidesAsImages(true);
    //حدد معالج تقدم مخصص
    pptxOptions->set_CustomProgressHandler(ShowProgressOnConsole);

    // احفظ النتيجة بتنسيق PPTX
    document->Save(_dataDir + outfilename, pptxOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
فيما يلي الطريقة المخصصة لعرض تحويل التقدم.

```cpp
void ShowProgressOnConsole(SharedPtr<UnifiedSaveOptions::ProgressEventHandlerInfo> eventInfo)
{
    switch (eventInfo->EventType)
    {
    case ProgressEventType::TotalProgress:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - تقدم التحويل : " << eventInfo->Value << std::endl;
    break;
    case ProgressEventType::ResultPageCreated:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - تم إنشاء تخطيط الصفحة الناتجة " << eventInfo->Value << " من " << eventInfo->MaxValue << "." << std::endl;
    break;
    case ProgressEventType::ResultPageSaved:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - تم تصدير الصفحة الناتجة " << eventInfo->Value << " من " << eventInfo->MaxValue << "." << std::endl;
    break;
    case ProgressEventType::SourcePageAnalysed:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - تم تحليل الصفحة المصدر " << eventInfo->Value << " من " << eventInfo->MaxValue << "." << std::endl;
    break;
    default:
    break;
    }
}
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى PowerPoint عبر الإنترنت**

Aspose.PDF for C++ يقدم لك تطبيق مجاني عبر الإنترنت ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF Convertion PDF to PPTX with Free App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## انظر أيضًا

تغطي هذه المقالة أيضًا هذه المواضيع. الأكواد هي نفسها كما هو موضح أعلاه.

_التنسيق_: **PowerPoint**
- [كود C++ لتحويل PDF إلى PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [API C++ لتحويل PDF إلى PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [برمجة C++ لتحويل PDF إلى PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [مكتبة C++ لتحويل PDF إلى PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [حفظ C++ لملف PDF كـ PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [توليد C++ لملف PowerPoint من PDF](#cpp-pdf-to-powerpoint-pptx)
- [إنشاء C++ لملف PowerPoint من PDF](#cpp-pdf-to-powerpoint-pptx)

- [محول C++ لتحويل PDF إلى PowerPoint](#cpp-pdf-to-powerpoint-pptx)


_التنسيق_: **Microsoft PowerPoint PPTX format**
- [C++ PDF إلى PowerPoint PPTX كود](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF إلى PowerPoint PPTX API](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF إلى PowerPoint PPTX برمجيًا](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF إلى PowerPoint PPTX مكتبة](#cpp-pdf-to-powerpoint-pptx)
- [C++ حفظ PDF كـ PowerPoint PPTX](#cpp-pdf-to-powerpoint-pptx)
- [C++ توليد PowerPoint PPTX من PDF](#cpp-pdf-to-powerpoint-pptx)
- [C++ إنشاء PowerPoint PPTX من PDF](#cpp-pdf-to-powerpoint-pptx)
- [C++ محول PDF إلى PowerPoint PPTX](#cpp-pdf-to-powerpoint-pptx)

_التنسيق_: **PPTX**
- [C++ PDF إلى PPTX كود](#cpp-pdf-to-pptx)
- [C++ PDF إلى PPTX API](#cpp-pdf-to-pptx)
- [C++ PDF إلى PPTX برمجيًا](#cpp-pdf-to-pptx)
- [C++ PDF إلى PPTX مكتبة](#cpp-pdf-to-pptx)
- [C++ حفظ PDF كـ PPTX](#cpp-pdf-to-pptx)
- [C++ توليد PPTX من PDF](#cpp-pdf-to-pptx)
- [C++ إنشاء PPTX من PDF](#cpp-pdf-to-pptx)
- [C++ محول PDF إلى PPTX](#cpp-pdf-to-pptx)
```