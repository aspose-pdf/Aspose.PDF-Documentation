---
title: حفظ مستند PDF باستخدام C++
linktitle: حفظ
type: docs
weight: 30
url: /ar/cpp/save-pdf-document/
description: تعلم كيفية حفظ ملف PDF باستخدام مكتبة Aspose.PDF لـ C++.
lastmod: "2021-11-01"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## حفظ مستند PDF في نظام الملفات

يمكنك حفظ مستند PDF الذي تم إنشاؤه أو تعديله في نظام الملفات باستخدام طريقة Save لفئة [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

```cpp
void SaveDocument()
{
    // سلسلة لاسم المسار
    String _dataDir("C:\\Samples\\");

    String originalFileName("SimpleResume.pdf");
    String modifiedFileName("SimpleResumeModified.pdf");

    auto document = MakeObject<Document>(_dataDir + originalFileName);
    // قم ببعض التعديلات، مثل إضافة صفحة فارغة جديدة
    document->get_Pages()->Add();
    document->Save(_dataDir + modifiedFileName);
}
```

## حفظ مستند PDF في الدفق

يمكنك أيضًا حفظ مستند PDF الذي تم إنشاؤه أو تعديله في الدفق باستخدام التحميلات الزائدة لطرق Save.

```cpp
void SaveDocumentStream()
{
    // سلسلة لاسم المسار
    String _dataDir("C:\\Samples\\");

    String originalFileName("SimpleResume.pdf");
    String modifiedFileName("SimpleResumeModified.pdf");

    auto document = MakeObject<Document>(_dataDir + originalFileName);

    // قم ببعض التعديلات، مثل إضافة صفحة فارغة جديدة
    document->get_Pages()->Add();

    auto fileStream = System::IO::File::OpenWrite(_dataDir + modifiedFileName);
    document->Save(fileStream);
}
```

## حفظ بصيغة PDF/A أو PDF/X

PDF/A هو إصدار من معيار ISO لصيغة المستندات المحمولة (PDF) للاستخدام في الأرشفة والحفظ الطويل الأمد للمستندات الإلكترونية. يختلف PDF/A عن PDF في أنه يحظر الميزات غير المناسبة للأرشفة الطويلة الأمد، مثل ربط الخطوط (على عكس تضمين الخطوط) والتشفير. تشمل متطلبات ISO لعارضي PDF/A إرشادات إدارة الألوان، ودعم تضمين الخطوط، وواجهة المستخدم لقراءة التعليقات التوضيحية المضمنة.

PDF/X هو مجموعة فرعية من معيار ISO لـ PDF. الغرض من PDF/X هو تسهيل تبادل الرسومات، ولذلك فإنه يحتوي على سلسلة من المتطلبات المتعلقة بالطباعة والتي لا تنطبق على ملفات PDF القياسية.

في كلتا الحالتين، تُستخدم طريقة الحفظ لتخزين المستندات، بينما يجب إعداد المستندات باستخدام [PdfFormatConversionOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pdf_format_conversion_options).

```cpp
void SaveDocumentAsPDFx()
{
    // سلسلة لمسار الاسم
    String _dataDir("C:\\Samples\\");

    // سلسلة لاسم الملف
    String infilename("SimpleResume.pdf");
    String outfilename("SimpleResume_A3U.pdf");

    auto document = MakeObject<Document>(_dataDir + infilename);
    auto options = new PdfFormatConversionOptions(Aspose::Pdf::PdfFormat::PDF_A_3U);
    try
    {
        document->Convert(options);
    }
    catch (const std::exception& e)
    {
        std::cerr << e.what();
    }

    document->Save(_dataDir + outfilename);
}
```