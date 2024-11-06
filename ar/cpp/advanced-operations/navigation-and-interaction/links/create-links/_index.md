---
title: إنشاء روابط في ملف PDF باستخدام C++
linktitle: إنشاء روابط
type: docs
weight: 10
url: ar/cpp/create-links/
description: يوضح هذا القسم كيفية إنشاء روابط في مستند PDF الخاص بك باستخدام C++.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## إنشاء روابط

من خلال إضافة رابط إلى تطبيق داخل مستند، يمكن الربط بالتطبيقات من المستند. هذا مفيد عندما تريد أن يتخذ القراء إجراءً معينًا في نقطة محددة في البرنامج التعليمي، على سبيل المثال، أو لإنشاء مستند غني بالميزات. لإنشاء رابط تطبيق:

1. [إنشاء مستند](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) كائن.
1. الحصول على [صفحة](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) التي تريد إضافة الرابط إليها.
1. إنشاء كائن [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) باستخدام صفحة وكائن [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle).
1. قم بتعيين سمات الرابط باستخدام كائن [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/).
1. أيضًا، قم بتعيين الخاصية Action لكائن [LaunchAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.launch_action/).
1. عند إنشاء كائن [LaunchAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.launch_action/)، حدد التطبيق الذي تريد تشغيله.
1. أضف الرابط إلى خاصية [Annotations](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.annotations) لكائن الصفحة.
1. أخيرًا، احفظ ملف PDF المحدث باستخدام طريقة Save الخاصة بكائن Document.

يعرض المقطع البرمجي التالي كيفية إنشاء رابط لتطبيق في ملف PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;

void CreateLink() 
{
    String _dataDir("C:\\Samples\\");
    // Create Document instance
    auto document = MakeObject<Document>(_dataDir + u"CreateApplicationLink.pdf");

    // Add page to pages collection of PDF file
    auto page = document->get_Pages()->idx_get(1);

    auto link = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, MakeObject<Rectangle>(100, 200, 300, 300));
    link->set_Color(Aspose::Pdf::Color::get_Green());
    link->set_Action(MakeObject<Aspose::Pdf::Annotations::LaunchAction>(document, _dataDir + u"sample.pdf"));
    page->get_Annotations()->Add(link);

    // Save updated document
    document->Save(_dataDir + u"CreateApplicationLink.pdf");
}
```
### إنشاء رابط مستند PDF في ملف PDF

تتيح لك Aspose.PDF for C++ إضافة رابط إلى ملف PDF خارجي بحيث يمكنك ربط عدة مستندات معًا. لإنشاء رابط مستند PDF:

1. أولاً، قم بإنشاء كائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. ثم، احصل على [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) المحددة التي تريد إضافة الرابط إليها.
1. قم بإنشاء كائن [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) باستخدام كائنات Page و[Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle).
1. قم بتعيين خصائص الرابط باستخدام كائن [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/).
1. قم بتعيين خاصية Action إلى الكائن [GoToRemoteAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_remote_action/).
1. أثناء إنشاء كائن GoToRemoteAction، حدد ملف PDF الذي يجب تشغيله، بالإضافة إلى رقم الصفحة التي يجب فتحها عليه.
1. أضف الرابط إلى مجموعة التعليقات التوضيحية لكائن الصفحة.
1. احفظ ملف الـ PDF المحدث باستخدام طريقة Save لكائن المستند.

يوضح مقطع الكود التالي كيفية إنشاء رابط مستند PDF في ملف PDF.

 ```cpp
void CreatePDFDocumentLink() 
{

    String _dataDir("C:\\Samples\\");
    // Create Document instance
    auto document = MakeObject<Document>(_dataDir + u"CreateDocumentLink.pdf");

    // Add page to pages collection of PDF file
    auto page = document->get_Pages()->idx_get(1);


    auto link = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, MakeObject<Rectangle>(100, 200, 300, 300));
    link->set_Color(Aspose::Pdf::Color::get_Green());

    link->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToRemoteAction>(_dataDir + u"sample.pdf", 1));
    page->get_Annotations()->Add(link);

    // Save updated document
    document->Save(_dataDir + u"CreateDocumentLink_out.pdf");
}
```