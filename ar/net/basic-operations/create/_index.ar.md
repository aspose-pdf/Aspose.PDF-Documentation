---
title: إنشاء مستند PDF برمجيًا
linktitle: إنشاء PDF
type: docs
weight: 10
url: /net/create-document/
description: تصف هذه الصفحة كيفية إنشاء مستند PDF من البداية باستخدام مكتبة Aspose.PDF.
---

Aspose.PDF لـ .NET API يتيح لك إنشاء وقراءة ملفات PDF باستخدام C# و VB.NET. يمكن استخدام الواجهة البرمجية في مجموعة متنوعة من تطبيقات .NET بما في ذلك WinForms، ASP.NET، والعديد من التطبيقات الأخرى. في هذه المقالة، سنوضح كيفية استخدام Aspose.PDF لـ .NET API لتوليد وقراءة ملفات PDF بسهولة في تطبيقات .NET.

## كيفية إنشاء ملف PDF باستخدام C#

لإنشاء ملف PDF باستخدام C#، يمكن استخدام الخطوات التالية.

1. إنشاء كائن من فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1. إضافة كائن [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) إلى مجموعة [Pages](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/pages) من كائن Document
1.
1. احفظ مستند PDF الناتج

الشفرة التالية تعمل أيضًا مع واجهة رسومية جديدة [Aspose.Drawing](/pdf/net/drawing/).

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

// تهيئة كائن المستند
Document document = new Document();
// إضافة صفحة
Page page = document.Pages.Add();
// إضافة نص إلى الصفحة الجديدة
page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
// حفظ PDF المُحدث
document.Save(dataDir + "HelloWorld_out.pdf")
```

في هذه الحالة، نقوم بإنشاء مستند PDF مكون من صفحة واحدة بحجم صفحة A4 وتوجيه عمودي. ستحتوي صفحتنا على عبارة "Hello, World" في الجزء العلوي الأيسر من الصفحة.
