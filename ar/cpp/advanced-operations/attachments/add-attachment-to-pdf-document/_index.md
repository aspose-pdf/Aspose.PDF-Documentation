---
title: إضافة مرفق إلى مستند PDF
linktitle: إضافة مرفق إلى مستند PDF
type: docs
weight: 10
url: /ar/cpp/add-attachment-to-pdf-document/
description: توضح هذه الصفحة كيفية إضافة مرفق إلى ملف PDF باستخدام مكتبة Aspose.PDF لـ C++
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

يمكن أن تحتوي المرفقات على مجموعة واسعة من المعلومات ويمكن أن تكون من أنواع ملفات متنوعة. يوضح هذا المقال كيفية إضافة مرفق إلى ملف PDF.

1. إنشاء مشروع C++ جديد.
1. إضافة مرجع إلى Aspose.PDF DLL.
1. إنشاء كائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. إنشاء كائن [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification) مع الملف الذي تقوم بإضافته ووصف الملف.
1.
``` أضف الكائن [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification) إلى مجموعة [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) في كائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) باستخدام طريقة Add الخاصة بالمجموعة.

تحتوي مجموعة [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) على جميع المرفقات في ملف PDF. يوضح لك مقطع الشيفرة التالي كيفية إضافة مرفق في مستند PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void WorkingWithAttachments::AddingAttachment()
{

String _dataDir("C:\\Samples\\");


// Open document

auto pdfDocument = MakeObject<Document>(_dataDir + u"AddAttachment.pdf");


// Setup new file to be added as attachment

auto fileSpecification = MakeObject<FileSpecification>(_dataDir + u"test.txt", u"ملف نصي نموذجي");


// Add attachment to document's attachment collection

pdfDocument->get_EmbeddedFiles()->Add(fileSpecification);


// Save new output

pdfDocument->Save(_dataDir + u"AddAttachment_out.pdf");
}
```