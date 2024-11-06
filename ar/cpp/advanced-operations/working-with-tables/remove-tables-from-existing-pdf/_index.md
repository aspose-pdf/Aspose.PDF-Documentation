---
title: إزالة الجداول من ملف PDF موجود
linktitle: إزالة الجداول
type: docs
weight: 50
url: ar/cpp/remove-tables-from-existing-pdf/
description: يصف هذا القسم كيفية إزالة الجدول من مستند PDF.
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF لـ C++ يسمح لك بإدراج وإنشاء جدول داخل مستند PDF أثناء إنشائه من الصفر أو يمكنك أيضًا إضافة كائن الجدول في أي مستند PDF موجود. ولكن قد يكون لديك متطلب لـ [معالجة الجداول في PDF موجود](https://docs.aspose.com/pdf/cpp/manipulate-tables-in-existing-pdf/) حيث يمكنك تحديث المحتويات في خلايا الجدول الموجودة. أيضًا، قد تصادف متطلبًا لإزالة كائنات الجدول من مستندات PDF الموجودة.

من أجل إزالة الجداول، نحتاج إلى استخدام فئة [TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.absorbed_table) للحصول على الجداول في PDF الموجود ثم استدعاء طريقة 'Remove'.

## إزالة الجدول من مستند PDF

لقد أضفنا وظيفة جديدة وهي. [Remove](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber#ace39006d8f44c9cb776ee26281a1cbb3) إلى الفصل الحالي TableAbsorber من أجل إزالة الجدول من مستند PDF. بمجرد أن يجد الماص الجداول على الصفحة بنجاح، يصبح قادرًا على إزالتها. يرجى التحقق من مقتطف الكود التالي الذي يوضح كيفية إزالة جدول من مستند PDF:

>العناوين:

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/TableAbsorber.h>
```

>أمثلة:

```cpp
using namespace System;
using namespace Aspose::Pdf;

void RemoveTable() {

    String _dataDir("C:\\Samples\\");

    // تحميل مستند PDF المصدر
    auto document = MakeObject<Document>(_dataDir + u"Table_input.pdf");

    // إنشاء كائن TableAbsorber للعثور على الجداول
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // زيارة الصفحة الأولى باستخدام الماص
    absorber->Visit(document->get_Pages()->idx_get(1));

    // الحصول على الجدول الأول في الصفحة
    auto table = absorber->get_TableList()->idx_get(0);

    // إزالة الجدول
    absorber->Remove(table);

    // حفظ PDF
    document->Save(_dataDir + u"Table_out.pdf");
}
```
## إزالة جداول متعددة من مستند PDF

ستكون بعض المهام مرتبطة بالعمل مع عدة جداول في مستند pdf واحد. وستحتاج إلى حذف عدة جداول منه. لإزالة جداول متعددة من مستند PDF، استخدم مقتطف الشيفرة التالي:

```cpp
void RemoveMultipleTables() {

    String _dataDir("C:\\Samples\\");

    // تحميل مستند PDF موجود
    auto document = MakeObject<Document>(_dataDir + u"Table_input2.pdf");

    // إنشاء كائن TableAbsorber للعثور على الجداول
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // زيارة الصفحة الأولى مع الماص
    absorber->Visit(document->get_Pages()->idx_get(1));

    // الحصول على نسخة من مجموعة الجداول
    auto tables = absorber->get_TableList();


    // التكرار عبر نسخة المجموعة وإزالة الجداول
    for(auto table : tables)
    absorber->Remove(table);

    // حفظ المستند
    document->Save(_dataDir + u"Table2_out.pdf");
}
```

{{% alert color="primary" %}}

يرجى أخذ بعين الاعتبار أن إزالة أو استبدال الجدول يغير مجموعة TableList. {{% /alert %}}

لذلك، في حالة إزالة/استبدال الجداول في حلقة، فإن نسخ مجموعة TableList أمر ضروري.