---
title: استخراج البيانات من AcroForm
linktitle: استخراج البيانات من AcroForm
type: docs
weight: 50
url: /ar/cpp/extract-data-from-acroform/
description: تجعل Aspose.PDF من السهل استخراج بيانات حقول النماذج من ملفات PDF. تعلم كيفية استخراج البيانات من AcroForms وحفظها بتنسيق XML أو FDF.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## استخراج حقول النموذج من مستند PDF

يسمح لك Aspose.PDF لـ C++ ليس فقط بإنشاء حقول النموذج وملء حقول النموذج بل يجعل من السهل أيضًا استخراج بيانات حقول النموذج أو معلومات حقول النموذج من ملفات PDF.

في مثال الكود أدناه، نوضح كيفية التكرار عبر كل صفحة في PDF لاستخراج معلومات حول جميع AcroForms في PDF وكذلك قيم حقول النموذج. يفترض هذا المثال البرمجي أنك لا تعرف أسماء حقول النموذج مسبقًا.

```cpp
void ExtractFormFields() {
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Parsing\\");

    // String for file name
    String infilename("StudentInfoFormElectronic.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Get values from all fields
    for (auto formField : document->get_Form()->get_Fields()) {
        std::cout << "Field Name :" << formField->get_PartialName() << std::endl;
        std::cout << "Value : " << formField->get_Value() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## استخراج البيانات إلى XML من ملف PDF

تسمح لك فئة [Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.form) بتصدير البيانات إلى ملف XML من ملف PDF باستخدام طريقة ExportXml. من أجل تصدير البيانات إلى XML، تحتاج إلى إنشاء كائن من فئة Form ثم استدعاء طريقة ExportXml باستخدام كائن FileStream. بعد ذلك يجب عليك إغلاق كائن FileStream والتخلص من كائن Form.

يوضح لك مقطع الشيفرة التالي كيفية تصدير البيانات إلى ملف XML.

```cpp
void ExtractFormFieldsToXML() {
    std::clog << __func__ << ": Start" << std::endl;
    // سلسلة لمسار الاسم
    String _dataDir("C:\\Samples\\Parsing\\");

    // سلسلة لاسم الملف
    String infilename(_dataDir + u"StudentInfoFormElectronic.pdf");
    String xmlFileName(_dataDir + u"StudentInfoFormElectronic.xml");

    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + infilename);
    auto fdfOutputStream = System::IO::File::OpenWrite(xmlFileName);

    // تصدير البيانات
    form->ExportXml(fdfOutputStream);

    // إغلاق تدفق الملف
    fdfOutputStream->Close();
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## تصدير البيانات إلى FDF من ملف PDF

[Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.form) تسمح لك بتصدير البيانات إلى ملف FDF من ملف PDF باستخدام طريقة ExportFdf. من أجل تصدير البيانات إلى FDF، تحتاج إلى إنشاء كائن من فئة Form ثم استدعاء طريقة ExportFdf باستخدام كائن FileStream. بعد ذلك يمكنك حفظ ملف PDF باستخدام طريقة Save من فئة Form.

يوضح لك مقطع الشيفرة التالي كيفية تصدير البيانات إلى ملف FDF.

```cpp
void ExtractFormExportFDF() {
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Parsing\\");

    // String for file name
    String infilename(_dataDir + u"StudentInfoFormElectronic.pdf");
    String fdfFileName(_dataDir+ u"StudentInfoFormElectronic.fdf");

    //String fdfFileName = Paths.get(_dataDir, "student.xfdf").toString();
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + infilename);

    auto fdfOutputStream = System::IO::File::OpenWrite(fdfFileName);

    // Export data
    form->ExportFdf(fdfOutputStream);

    // Close file stream
    fdfOutputStream->Close();
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## تصدير البيانات إلى XFDF من ملف PDF

Aspose PDF لـ C++ مع فئة [Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.form) تُمكّنك من تصدير البيانات إلى ملف XFDF من ملف PDF باستخدام طريقة ExportXfdf. من أجل تصدير البيانات إلى XFDF، تحتاج إلى إنشاء كائن من فئة Form ثم استدعاء طريقة ExportXfdf باستخدام كائن FileStream.

في النهاية، يمكنك حفظ ملف PDF باستخدام طريقة Save لفئة Form.

يوضح لك مقتطف الكود التالي كيفية تصدير البيانات إلى ملف XFDF.

```cpp
void ExtractFormExportXFDF() {
    std::clog << __func__ << ": Start" << std::endl;
    // سلسلة لأسم المسار
    String _dataDir("C:\\Samples\\Parsing\\");

    // سلسلة لأسم الملف
    String infilename("StudentInfoFormElectronic.pdf");
    String fdfFileName("StudentInfoFormElectronic.xfdf");

    //String fdfFileName = Paths.get(_dataDir, "student.xfdf").toString();
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + infilename);

    auto fdfOutputStream = System::IO::File::OpenWrite(fdfFileName);

    // تصدير البيانات
    form->ExportXfdf(fdfOutputStream);

    // إغلاق تدفق الملف
    fdfOutputStream->Close();
    std::clog << __func__ << ": Finish" << std::endl;
}
```