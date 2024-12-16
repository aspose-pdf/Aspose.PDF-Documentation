---
title: بيانات التعريف لملف PDF
type: docs
weight: 20
url: /ar/cpp/pdf-file-metadata/
---

## الحصول على/تعيين معلومات ملف PDF

من أجل الحصول على معلومات محددة لملف PDF، تحتاج أولاً إلى استدعاء **get_Info()** من فئة Document. بمجرد استرجاع كائن DocumentInfo، يمكنك الحصول على قيم الخصائص الفردية. علاوة على ذلك، يمكنك أيضًا تعيين الخصائص باستخدام الطرق المقابلة لفئة DocumentInfo. يوضح مقطع الشفرة التالي كيفية الحصول على/تعيين معلومات ملف PDF باستخدام Aspose.PDF لـ C++:

{{% alert color="primary" %}}

يرجى ملاحظة أنه لا يمكنك تعيين قيم ضد الحقول **Application** و **Producer**، لأن Aspose Ltd. و Aspose.PDF لـ C++ x.x.x ستظهر ضد هذه الحقول.

{{% /alert %}}

```cpp
void WorkingWithPDFMetadata::GetPDFFileInformation()
{
    String _dataDir("C:\\Samples\\");
    // افتح المستند
    auto pdfDocument = MakeObject<Document>(_dataDir + u"GetFileInfo.pdf");
    // احصل على معلومات المستند
    auto docInfo = pdfDocument->get_Info();
    // اعرض معلومات المستند
    Console::WriteLine(u"Author: {0}", docInfo->get_Author());
    Console::WriteLine(u"Creation Date: {0}", docInfo->get_CreationDate());
    Console::WriteLine(u"Keywords: {0}", docInfo->get_Keywords());
    Console::WriteLine(u"Modify Date: {0}", docInfo->get_ModDate());
    Console::WriteLine(u"Subject: {0}", docInfo->get_Subject());
    Console::WriteLine(u"Title: {0}", docInfo->get_Title());
}

void WorkingWithPDFMetadata::SetPDFFileInformation()
{
    String _dataDir("C:\\Samples\\");
    // افتح المستند
    auto pdfDocument = MakeObject<Document>(_dataDir + u"SetFileInfo.pdf");

    // حدد معلومات المستند
    auto docInfo = MakeObject<DocumentInfo>(pdfDocument);

    docInfo->set_Author(u"Aspose");
    docInfo->set_CreationDate(DateTime::get_Now());
    docInfo->set_Keywords (u"Aspose.Pdf, DOM, API");
    docInfo->set_ModDate (DateTime::get_Now());
    docInfo->set_Subject (u"PDF Information");
    docInfo->set_Title (u"Setting PDF Document Information");

    // احفظ المستند الناتج
    pdfDocument->Save(_dataDir + u"SetFileInfo_out.pdf");
}
```
```

## الحصول على/تعيين بيانات XMP التعريفية من ملف PDF

يسمح لك Aspose.PDF for C++ بالوصول إلى البيانات التعريفية XMP لملف PDF وكذلك تعيينها. للحصول على/تعيين البيانات التعريفية لملف PDF:

1. أنشئ كائن Document وافتح ملف PDF المطلوب.
2. احصل على/عين البيانات التعريفية للملف باستخدام الطرق المناسبة.

يوضح لك مقطع الشيفرة التالي كيفية الحصول على/تعيين البيانات التعريفية من ملف PDF.

```cpp
void WorkingWithPDFMetadata::GetXMPMetadata()
{
    String _dataDir("C:\\Samples\\");
    // افتح المستند
    auto pdfDocument = MakeObject<Document>(_dataDir + u"GetXMPMetadata.pdf");

    // احصل على الخصائص
    Console::WriteLine(pdfDocument->get_Metadata()->idx_get(u"xmp:CreateDate"));
    Console::WriteLine(pdfDocument->get_Metadata()->idx_get(u"xmp:Nickname"));
    Console::WriteLine(pdfDocument->get_Metadata()->idx_get(u"xmp:CustomProperty"));
}

void WorkingWithPDFMetadata::SetXMPMetadata()
{
    String _dataDir("C:\\Samples\\");
    // افتح المستند
    auto pdfDocument = MakeObject<Document>(_dataDir + u"SetXMPMetadata.pdf");

    // عين الخصائص
    pdfDocument->get_Metadata()->idx_set(u"xmp:CreateDate", MakeObject<XmpValue>(DateTime::get_Now()));
    pdfDocument->get_Metadata()->idx_set(u"xmp:Nickname", MakeObject<XmpValue>(u"Nickname"));
    pdfDocument->get_Metadata()->idx_set(u"xmp:CustomProperty", MakeObject<XmpValue>(u"Custom Value"));

    // احفظ المستند
    pdfDocument->Save(_dataDir + u"SetXMPMetadata_out.pdf");
}

void WorkingWithPDFMetadata::InsertMetadataWithPrefix()
{
    String _dataDir("C:\\Samples\\");
    // افتح المستند
    auto pdfDocument = MakeObject<Document>(_dataDir + u"SetXMPMetadata.pdf");
    pdfDocument->get_Metadata()->RegisterNamespaceUri(u"xmp", u"http:// Ns.adobe.com/xap/1.0/"); // تم إزالة بادئة xmlns
    pdfDocument->get_Metadata()->idx_set(u"xmp:ModifyDate", MakeObject<XmpValue>(DateTime::get_Now()));

    // احفظ المستند
    pdfDocument->Save(_dataDir + u"SetPrefixMetadata_out.pdf");
}
```