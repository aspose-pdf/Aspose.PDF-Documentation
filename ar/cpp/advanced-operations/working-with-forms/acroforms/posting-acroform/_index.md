---
title: Posting AcroForm Data
linktitle: Posting AcroForm
type: docs
weight: 50
url: /ar/cpp/posting-acroform-data/
description: يمكنك استيراد وتصدير بيانات النموذج إلى ملف XML باستخدام مساحة الأسماء Aspose.Pdf.Facades في Aspose.PDF for C++.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

AcroForm هو نوع هام من مستندات PDF. يمكنك ليس فقط إنشاء وتحرير AcroForm باستخدام [فضاء الأسماء Aspose.Pdf.Facades](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.facades)، ولكن أيضًا استيراد وتصدير بيانات النموذج إلى ملف XML. يسمح لك فضاء الأسماء Aspose.Pdf.Facades في Aspose.PDF لـ C++ بتنفيذ ميزة أخرى من AcroForm، والتي تساعدك على إرسال بيانات AcroForm إلى صفحة ويب خارجية. ثم تقرأ هذه الصفحة المتغيرات المرسلة وتستخدم هذه البيانات لمزيد من المعالجة. تكون هذه الميزة مفيدة في الحالات التي لا تريد فقط الاحتفاظ بالبيانات في ملف PDF، بل ترغب في إرسالها إلى الخادم الخاص بك ثم حفظها في قاعدة بيانات وما إلى ذلك.

{{% /alert %}}

## تفاصيل التنفيذ

في هذه المقالة، حاولنا إنشاء AcroForm باستخدام [فضاء الأسماء Aspose.Pdf.Facades](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.facades) وفئة [FormEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.form_editor/). كما أضفنا زر إرسال وقمنا بتعيين عنوان URL المستهدف له.

توضح لك المقاطع البرمجية التالية كيفية إنشاء النموذج ثم تلقي البيانات المرسلة على صفحة الويب.
```cpp
using namespace System;
using namespace Aspose::Pdf;

void PostingExample() {

    // String _dataDir("C:\\Samples\\");
    // إنشاء مثيل لفئة FormEditor وربط ملفات pdf المدخلة والإخراج
    auto editor = MakeObject<Aspose::Pdf::Facades::FormEditor>("input.pdf", "output.pdf");

    // إنشاء حقول AcroForm - لقد أنشأت حقلين فقط للتبسيط
    editor->AddField(Aspose::Pdf::Facades::FieldType::Text, u"firstname", 1, 100, 600, 200, 625);
    editor->AddField(Aspose::Pdf::Facades::FieldType::Text, u"lastname", 1, 100, 550, 200, 575);

    // إضافة زر إرسال وتعيين عنوان URL الهدف
    editor->AddSubmitBtn(u"submitbutton", 1, u"Submit", u"http://localhost/csharptesting/show.aspx", 100, 450, 150, 475);

    // حفظ ملف pdf الناتج
    editor->Save();
}
```