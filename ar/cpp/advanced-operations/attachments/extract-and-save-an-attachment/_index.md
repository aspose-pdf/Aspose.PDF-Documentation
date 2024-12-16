---
title: استخراج وحفظ مرفق 
linktitle: استخراج وحفظ مرفق
type: docs
weight: 20
url: /ar/cpp/extract-and-save-an-attachment/
description: Aspose.PDF ل C++ يسمح لك بالحصول على جميع المرفقات من مستند PDF. أيضًا، يمكنك الحصول على مرفق فردي من المستند الخاص بك.
lastmod: "2022-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## الحصول على جميع المرفقات

مع Aspose.PDF، من الممكن الحصول على جميع المرفقات من مستند PDF. هذا مفيد إما عندما تريد حفظ المستندات بشكل منفصل عن PDF، أو إذا كنت بحاجة إلى تجريد PDF من المرفقات.

للحصول على جميع المرفقات من ملف PDF:

1. Loop خلال مجموعة [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection). تحتوي مجموعة [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) على جميع المرفقات. يمثل كل عنصر من هذه المجموعة كائن [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification). تعيد كل تكرار في حلقة foreach عبر مجموعة [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) كائن [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification).
1. بمجرد توفر الكائن، قم باسترجاع إما جميع خصائص الملف المرفق أو الملف نفسه.

توضح الشفرات البرمجية التالية كيفية الحصول على جميع المرفقات من مستند PDF.

```cpp
void WorkingWithAttachments::GetAllAttachments()
{
 String _dataDir("C:\\Samples\\");

 // افتح المستند
 auto pdfDocument = new Document(_dataDir + u"GetAlltheAttachments.pdf");

 // احصل على مجموعة الملفات المدمجة
 auto embeddedFiles = pdfDocument->get_EmbeddedFiles();

 // احصل على عدد الملفات المدمجة
 Console::WriteLine(u"Total files : {0}", embeddedFiles->get_Count());

 int count = 1;

 // حلق من خلال المجموعة للحصول على جميع المرفقات
 for (auto fileSpecification : embeddedFiles)
 {
  Console::WriteLine(u"Name: {0}", fileSpecification->get_Name());
  Console::WriteLine(u"Description: {0}", fileSpecification->get_Description());
  Console::WriteLine(u"Mime Type: {0}", fileSpecification->get_MIMEType());

  // تحقق مما إذا كان كائن المعلمة يحتوي على المعلمات
  if (fileSpecification->get_Params() != nullptr)
  {
   Console::WriteLine(u"CheckSum: {0}",
    fileSpecification->get_Params()->get_CheckSum());
   Console::WriteLine(u"Creation Date: {0}",
    fileSpecification->get_Params()->get_CreationDate());
   Console::WriteLine(u"Modification Date: {0}",
    fileSpecification->get_Params()->get_ModDate());
   Console::WriteLine(u"Size: {0}", fileSpecification->get_Params()->get_Size());
  }

  // احصل على المرفق واكتب إلى الملف أو المجرى
  auto fileContent = MakeArray<uint8_t>(fileSpecification->get_Contents()->get_Length());
  fileSpecification->get_Contents()->Read(fileContent, 0, fileContent->get_Length());
  auto fileStream = System::IO::File::OpenWrite(_dataDir + u"test" + count + u"_out.txt");
  fileStream->Write(fileContent, 0, fileContent->get_Length());
  fileStream->Close();
  count += 1;
 }
}
```
## احصل على مرفق فردي

من أجل الحصول على مرفق فردي، يمكننا تحديد مؤشر المرفق في كائن `EmbeddedFiles` من مثيل المستند. يرجى محاولة استخدام جزء الشيفرة التالي.

```cpp
void WorkingWithAttachments::GetIndividualAttachment() {
    String _dataDir("C:\\Samples\\");

    // افتح المستند
    auto pdfDocument = MakeObject<Document>(_dataDir + u"GetIndividualAttachment.pdf");

    // احصل على ملف مضمّن معين
    auto fileSpecification = pdfDocument->get_EmbeddedFiles()->idx_get(1);

    // احصل على خصائص الملف
    Console::WriteLine(u"الاسم: {0}", fileSpecification->get_Name());
    Console::WriteLine(u"الوصف: {0}", fileSpecification->get_Description());
    Console::WriteLine(u"نوع Mime: {0}", fileSpecification->get_MIMEType());

    // تحقق مما إذا كان كائن المعلمة يحتوي على المعلمات
    if (fileSpecification->get_Params() != nullptr)
    {
        Console::WriteLine(u"التحقق: {0}",
        fileSpecification->get_Params()->get_CheckSum());
        Console::WriteLine(u"تاريخ الإنشاء: {0}",
        fileSpecification->get_Params()->get_CreationDate());
        Console::WriteLine(u"تاريخ التعديل: {0}",
        fileSpecification->get_Params()->get_ModDate());
        Console::WriteLine(u"الحجم: {0}",
        fileSpecification->get_Params()->get_Size());
    }


    // احصل على المرفق واكتب إلى ملف أو دفق
    auto fileContent = MakeArray<uint8_t>(fileSpecification->get_Contents()->get_Length());
    fileSpecification->get_Contents()->Read(fileContent, 0, fileContent->get_Length());

    auto fileStream = System::IO::File::OpenWrite(_dataDir + u"test_out.txt");
    fileStream->Write(fileContent, 0, fileContent->get_Length());
    fileStream->Close();

}
```