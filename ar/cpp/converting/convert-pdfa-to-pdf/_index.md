---
title: تحويل PDF/A إلى تنسيق PDF
linktitle: تحويل PDF/A إلى تنسيق PDF
type: docs
weight: 110
url: ar/cpp/convert-pdfa-to-pdf/
lastmod: "2021-11-19"
description: يوضح لك هذا الموضوع كيفية استخدام Aspose.PDF لتحويل ملف PDF/A إلى مستند PDF باستخدام مكتبة C++.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## تحويل مستند PDF/A إلى PDF

تحويل مستند PDF/A إلى PDF يعني إزالة قيود <abbr title="أرشيف تنسيق المستند المحمول">PDF/A</abbr> من المستند الأصلي. تحتوي فئة [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) على طريقة 'RemovePdfaCompliance' لإزالة معلومات التوافق مع PDF من الملف المصدر/المدخل.
بعد [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) الملف المدخل.

```cpp
void ConvertPDFAtoPDF()
{
    std::clog << "PDF/A to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample-pdfa.pdf");
    String outfilename("PDFAToPDF_out.pdf");

    auto document = MakeObject<Document>(_dataDir + infilename);

    // إزالة معلومات التوافق مع PDF/A
    document->RemovePdfaCompliance();

    // حفظ المستند المحدث
    document->Save(_dataDir + outfilename);
    std::clog << "PDF/A to PDF convert: End" << std::endl;
}
```

هذه المعلومات تُزال أيضًا إذا قمت بإجراء أي تغييرات في المستند (مثل إضافة صفحات). في المثال التالي، يفقد المستند الناتج التوافق مع PDF/A بعد إضافة الصفحة.

```cpp
void ConvertPDFAtoPDFAdvanced()
{
    std::clog << "PDF/A to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample-pdfa.pdf");
    String outfilename("PDFAToPDF_out.pdf");

    auto document = MakeObject<Document>(_dataDir + infilename);
    // إضافة صفحة جديدة (فارغة) يزيل معلومات التوافق مع PDF/A.

    document->get_Pages()->Add();
    // حفظ المستند المحدث
    document->Save(_dataDir + outfilename);
    std::clog << "PDF/A to PDF convert: End" << std::endl;
}
```