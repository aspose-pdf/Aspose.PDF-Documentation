---
title: تحويل ملفات PDF إلى مستندات Microsoft Word في C++
linktitle: تحويل PDF إلى Word
type: docs
weight: 10
url: /cpp/convert-pdf-to-word/
lastmod: "2021-11-19"
description: تتيح لك مكتبة Aspose.PDF لـ C++ تحويل PDF إلى تنسيق Word باستخدام C++ بسهولة وتحكم كامل. تتضمن هذه التنسيقات DOC وDOCX. تعلم المزيد حول كيفية ضبط تحويل مستندات PDF إلى Microsoft Word.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## نظرة عامة

تشرح هذه المقالة كيفية تحويل PDF إلى مستندات Microsoft Word باستخدام C++. تغطي هذه المواضيع.

_التنسيق_: **DOC**
- [C++ تحويل PDF إلى DOC](#cpp-pdf-to-doc)
- [C++ تحويل PDF إلى DOC](#cpp-pdf-to-doc)
- [C++ كيفية تحويل ملف PDF إلى DOC](#cpp-pdf-to-doc)

_التنسيق_: **DOCX**
- [C++ تحويل PDF إلى DOCX](#cpp-pdf-to-docx)
- [C++ تحويل PDF إلى DOCX](#cpp-pdf-to-docx)
- [C++ كيفية تحويل ملف PDF إلى DOCX](#cpp-pdf-to-docx)

_التنسيق_: **تنسيق Microsoft Word DOC**
- [C++ تحويل PDF إلى Word](#cpp-pdf-to-word-doc)
- [C++ تحويل PDF إلى Word](#cpp-pdf-to-word-doc)

- [C++ كيفية تحويل ملف PDF إلى Word](#cpp-pdf-to-word-doc)

_Format_: **تنسيق Microsoft Word DOCX**
- [C++ PDF إلى Word](#cpp-pdf-to-word-docx)
- [C++ تحويل PDF إلى Word](#cpp-pdf-to-word-docx)
- [C++ كيفية تحويل ملف PDF إلى Word](#cpp-pdf-to-word-docx)

المواضيع الأخرى التي يغطيها هذا المقال
- [انظر أيضًا](#see-also)

## تحويلات C++ PDF إلى Word

إحدى الميزات الأكثر شعبية هي تحويل PDF إلى تنسيق Microsoft Word DOC، مما يجعل المحتوى سهل التلاعب. يتيح لك Aspose.PDF for C++ تحويل ملفات PDF إلى DOC.

## تحويل ملف PDF إلى ملف DOC (Word 97-2003)

قم بتحويل ملف PDF إلى تنسيق DOC بسهولة وتحكم كامل. Aspose.PDF for C++ مرن ويدعم مجموعة واسعة من التحويلات. تحويل الصفحات من مستندات PDF إلى صور، على سبيل المثال، هو ميزة شائعة جدًا.

التحويل الذي طلبه العديد من عملائنا هو PDF إلى DOC: تحويل ملف PDF إلى مستند Microsoft Word. 
يرغب العملاء في هذا لأن ملفات PDF لا يمكن تعديلها بسهولة، بينما يمكن تعديل مستندات Word. بعض الشركات ترغب في أن يكون مستخدموها قادرين على معالجة النصوص والجداول والصور في الملفات التي بدأت كملفات PDF.

مع الحفاظ على تقليد جعل الأمور بسيطة ومفهومة، يتيح لك Aspose.PDF لـ C++ تحويل ملف PDF المصدر إلى ملف DOC بسطرين من التعليمات البرمجية. لتحقيق هذه الميزة، قدمنا تعدادًا يسمى SaveFormat وقيمته .Doc تتيح لك حفظ الملف المصدر بتنسيق Microsoft Word.

يوضح مقتطف الشيفرة C++ التالي عملية تحويل ملف PDF إلى تنسيق DOC.

<a name="cpp-pdf-to-doc" id="cpp-pdf-to-doc"><strong>الخطوات: تحويل PDF إلى DOC في C++</strong></a> | <a name="cpp-pdf-to-word-doc" id="cpp-pdf-to-word-doc"><strong>الخطوات: تحويل PDF إلى تنسيق Microsoft Word DOC في C++</strong></a>

1. قم بإنشاء نسخة من كائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) مع مستند PDF المصدر.
2.
``` احفظه بتنسيق **SaveFormat::Doc** عن طريق استدعاء طريقة **Document->Save()**.

```cpp
void ConvertPDFtoWord()
{
    std::clog << __func__ << ": Start" << std::endl;
    // سلسلة لاسم المسار
    String _dataDir("C:\\Samples\\Conversion\\");

    // سلسلة لاسم الملف
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.doc");

    // افتح المستند
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
        // احفظ الملف بتنسيق مستند MS
        document->Save(_dataDir + outfilename, SaveFormat::Doc);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```

يعرض مقتطف الشيفرة التالي عملية تحويل ملف PDF إلى إصدار DOC متقدم:

```cpp
void ConvertPDFtoWordDocAdvanced()
{
    std::clog << __func__ << ": Start" << std::endl;
    // سلسلة لاسم المسار
    String _dataDir("C:\\Samples\\Conversion\\");

    // سلسلة لاسم الملف
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.doc");

    // افتح المستند
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto saveOptions = MakeObject<DocSaveOptions>();
    saveOptions->set_Format(DocSaveOptions::DocFormat::Doc);
    // ضبط وضع التعرف كـ Flow
    saveOptions->set_Mode(DocSaveOptions::RecognitionMode::Flow);
    // ضبط القرب الأفقي كـ 2.5
    saveOptions->set_RelativeHorizontalProximity(2.5f);
    // تمكين القيمة للتعرف على النقاط أثناء عملية التحويل
    saveOptions->set_RecognizeBullets(true);

    try {
        // احفظ الملف بتنسيق مستند MS
        document->Save(_dataDir + outfilename, saveOptions);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```
{{% alert color="success" %}}
**حاول تحويل ملفات PDF إلى DOC عبر الإنترنت**

تقدم لك Aspose.PDF for C++ تطبيقًا مجانيًا عبر الإنترنت ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل PDF إلى DOC](pdf_to_doc.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## تحويل PDF إلى DOCX

تتيح لك Aspose.PDF for C++ API قراءة وتحويل مستندات PDF إلى DOCX باستخدام لغة C++. DOCX هو تنسيق معروف لمستندات Microsoft Word تم تغيير هيكله من ثنائي بسيط إلى مزيج من ملفات XML وثنائية. يمكن فتح ملفات DOCX باستخدام Word 2007 والإصدارات اللاحقة ولكن ليس مع الإصدارات الأقدم من MS Word التي تدعم امتدادات ملفات DOC.

يوضح مقتطف الشفرة C++ التالي عملية تحويل ملف PDF إلى تنسيق DOCX.


<a name="cpp-pdf-to-docx" id="cpp-pdf-to-docx"><strong>الخطوات: تحويل PDF إلى DOCX في C++</strong></a> | <a name="cpp-pdf-to-word-docx" id="cpp-pdf-to-word-docx"><strong>الخطوات: تحويل PDF إلى تنسيق Microsoft Word DOCX في C++</strong></a>

1. قم بإنشاء مثيل لكائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) باستخدام مستند PDF المصدر.
2. احفظه بصيغة **SaveFormat::DocX** عن طريق استدعاء طريقة **Document->Save()**.

```cpp
void ConvertPDFtoWord_DOCX_Format()
{
    std::clog << __func__ << ": Start" << std::endl;
    // سلسلة لاسم المسار
    String _dataDir("C:\\Samples\\Conversion\\");

    // سلسلة لاسم الملف
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.docx");

    // افتح المستند
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
        // احفظ الملف بتنسيق مستند MS
        document->Save(_dataDir + outfilename, SaveFormat::DocX);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```

تحتوي فئة [`DocSaveOptions`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options) على خاصية تسمى Format التي توفر القدرة على تحديد تنسيق المستند الناتج، أي DOC أو DOCX. من أجل تحويل ملف PDF إلى تنسيق DOCX، يرجى تمرير قيمة Docx من التعداد DocSaveOptions.DocFormat.

يرجى إلقاء نظرة على المقطع البرمجي التالي الذي يوفر القدرة على تحويل ملف PDF إلى تنسيق DOCX باستخدام C++.

```cpp
void ConvertPDFtoWord_Advanced_DOCX_Format()
{
    std::clog << __func__ << ": Start" << std::endl;
    // سلسلة لمسار الاسم
    String _dataDir("C:\\Samples\\Conversion\\");

    // سلسلة لاسم الملف
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.docx");

    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto saveOptions = MakeObject<DocSaveOptions>();
    saveOptions->set_Format(DocSaveOptions::DocFormat::DocX);

    // تعيين معلمات DocSaveOptions الأخرى
    // ...

    // حفظ الملف بتنسيق مستند MS

    try {
        // حفظ الملف بتنسيق مستند MS
        document->Save(_dataDir + outfilename, saveOptions);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```
{{% alert color="warning" %}}
**حاول تحويل PDF إلى DOCX عبر الإنترنت**

يوفر لك Aspose.PDF for C++ تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى DOCX"](https://products.aspose.app/pdf/conversion/pdf-to-docx)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF Convertion PDF to Word Free App](pdf_to_docx.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## انظر أيضًا

تغطي هذه المقالة أيضًا هذه المواضيع. الأكواد هي نفسها كما في الأعلى.

_التنسيق_: **تنسيق Microsoft Word DOC**
- [كود C++ PDF إلى Word](#cpp-pdf-to-word-doc)
- [واجهة برمجة تطبيقات C++ PDF إلى Word](#cpp-pdf-to-word-doc)
- [برنامج C++ PDF إلى Word برمجيًا](#cpp-pdf-to-word-doc)
- [مكتبة C++ PDF إلى Word](#cpp-pdf-to-word-doc)
- [حفظ C++ PDF كـ Word](#cpp-pdf-to-word-doc)
- [توليد C++ Word من PDF](#cpp-pdf-to-word-doc)
- [إنشاء C++ Word من PDF](#cpp-pdf-to-word-doc)
- [محول C++ PDF إلى Word](#cpp-pdf-to-word-doc)

_التنسيق_: **تنسيق Microsoft Word DOCX**

- [كود C++ PDF إلى Word](#cpp-pdf-to-word-docx)

- [C++ PDF to Word API](#cpp-pdf-to-word-docx)
- [C++ PDF to Word Programmatically](#cpp-pdf-to-word-docx)
- [C++ PDF to Word Library](#cpp-pdf-to-word-docx)
- [C++ Save PDF as Word](#cpp-pdf-to-word-docx)
- [C++ Generate Word from PDF](#cpp-pdf-to-word-docx)
- [C++ Create Word from PDF](#cpp-pdf-to-word-docx)
- [C++ PDF to Word Converter](#cpp-pdf-to-word-docx)

_تنسيق_: **DOC**
- [C++ PDF to DOC Code](#cpp-pdf-to-doc)
- [C++ PDF to DOC API](#cpp-pdf-to-doc)
- [C++ PDF to DOC Programmatically](#cpp-pdf-to-doc)
- [C++ PDF to DOC Library](#cpp-pdf-to-doc)
- [C++ Save PDF as DOC](#cpp-pdf-to-doc)
- [C++ Generate DOC from PDF](#cpp-pdf-to-doc)
- [C++ Create DOC from PDF](#cpp-pdf-to-doc)
- [C++ PDF to DOC Converter](#cpp-pdf-to-doc)

_تنسيق_: **DOC**
- [C++ PDF to DOCX Code](#cpp-pdf-to-docx)
- [C++ PDF to DOCX API](#cpp-pdf-to-docx)
- [C++ PDF to DOCX Programmatically](#cpp-pdf-to-docx)
- [C++ PDF to DOCX Library](#cpp-pdf-to-docx)
- [C++ Save PDF as DOCX](#cpp-pdf-to-docx)

- [C++ Generate DOCX from PDF](#cpp-pdf-to-docx)
```
- [تحويل DOCX من PDF باستخدام C++](#cpp-pdf-to-docx)
- [محول PDF إلى DOCX باستخدام C++](#cpp-pdf-to-docx)