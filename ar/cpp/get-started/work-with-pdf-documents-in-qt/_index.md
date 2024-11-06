---
title: العمل مع مستندات PDF في Qt
type: docs
weight: 130
url: ar/cpp/work-with-pdf-documents-in-qt/
lastmod: "2021-11-01"
---

Qt هو إطار عمل لتطوير التطبيقات عبر الأنظمة الأساسية يتيح إنشاء مجموعة متنوعة من التطبيقات لسطح المكتب والهواتف المحمولة والويب ونظام التطبيقات المدمج. سنرى في هذه المقالة كيف يمكنك دمج مكتبة PDF الخاصة بنا في C++ للعمل مع مستندات PDF في تطبيقات Qt الخاصة بك.

## استخدام Aspose.PDF لـ C++ داخل Qt

لاستخدام Aspose.PDF لـ C++ في تطبيق Qt الخاص بك على نظام التشغيل Windows، قم بتنزيل أحدث إصدار من واجهة برمجة التطبيقات من قسم [التنزيلات](https://downloads.aspose.com/pdf/cpp). بمجرد تنزيل واجهة برمجة التطبيقات، يمكنك استخدام أي من الخيارات التالية لاستخدامها مع Qt.

- استخدام Qt Creator
- استخدام Visual Studio

هنا، سنوضح كيفية دمج واستخدام Aspose.PDF لـ C++ داخل تطبيق وحدة التحكم في Qt باستخدام Qt Creator.

### إنشاء تطبيق وحدة تحكم Qt

{{% alert color="primary" %}}

تفترض هذه المقالة أنك قد قمت بتثبيت بيئة تطوير Qt وQt Creator بشكل صحيح.
```

{{% /alert %}}

- افتح Qt Creator وأنشئ تطبيق *Qt Console Application* جديد.

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Qt-Console-Application.jpg)

- اختر خيار QMake من القائمة المنسدلة *Build System*.

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Qt-Console-Application-QMake.jpg)

- اختر الحزمة المناسبة وأنهِ المعالج.

في هذه المرحلة، يجب أن يكون لديك تطبيق Qt Console Application قابل للتنفيذ ويجب أن يُجمَّع بدون مشكلات.

### دمج Aspose.PDF لواجهة برمجة تطبيقات C++ مع Qt

- استخراج أرشيف Aspose.PDF لـ C++ الذي قمت بتنزيله سابقًا
- انسخ المجلدات *Aspose.Pdf.Cpp* و *CodePorting.Native.Cs2Cpp_vc14_20.4* من الحزمة المستخرجة لـ Aspose.PDF لـ C++ إلى جذر المشروع. يجب أن يكون مشروعك كما هو موضح في الصورة التالية.

![todo:image_alt_text](work-with-pdf-documents-in-qt_1.png)

- من أجل إضافة مسارات إلى مجلدات lib و include، انقر بزر الماوس الأيمن على المشروع في لوحة LHS واختر *Add Library*.

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Add-Word-Library.jpg)

- اختر خيار المكتبة الخارجية وقم بتصفح المسارات لتضمين المجلدات lib و include واحدًا تلو الآخر.

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Add-Word-Library-2.jpg)

- بمجرد الانتهاء، سيحتوي ملف المشروع .pro الخاص بك على الإدخالات التالية:

![todo:image_alt_text](work-with-pdf-documents-in-qt_2.png)

- قم ببناء التطبيق وانتهيت من عملية الدمج.

### إنشاء مستند PDF في Qt

الآن بعد أن تم دمج Aspose.PDF for C++ مع Qt، نحن جاهزون لإنشاء مستند PDF يحتوي على بعض النصوص وحفظه على القرص. للقيام بذلك:

- قم بتضمين الرؤوس التالية في main.cpp

```cpp

    #include "Aspose.PDF.Cpp/Document.h"
    #include "Aspose.PDF.Cpp/Page_.h"
    #include "Aspose.PDF.Cpp/PageCollection.h"
    #include "Aspose.PDF.Cpp/Generator/Paragraphs.h"
    #include "Aspose.PDF.Cpp/Text/TextFragment.h"
```

- أدخل الشيفرة التالية في الدالة الرئيسية لإنشاء مستند PDF وحفظه على القرص

```cpp

    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Text;
    
    QString text = "مرحبا بالعالم";
    auto doc = MakeObject<Document>();

    auto pages = doc->get_Pages();

    pages->Add();

    auto page = pages->idx_get(1);

    auto paragraps = page->get_Paragraphs();

    paragraps->Add(MakeObject<TextFragment>(text.toStdU16String().c_str()));

    doc->Save(file_name.toStdU16String().c_str());
```