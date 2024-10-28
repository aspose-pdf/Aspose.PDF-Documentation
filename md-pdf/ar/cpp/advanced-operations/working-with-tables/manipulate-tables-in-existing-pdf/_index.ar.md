---
title: معالجة الجداول في PDF الحالي
linktitle: معالجة الجداول
type: docs
weight: 40
url: /cpp/manipulate-tables-in-existing-pdf/
description: يغطي هذا القسم طرق مختلفة لتعديل الجداول باستخدام Aspose.PDF لـ C++
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## معالجة الجداول في PDF الحالي

يسمح لك Aspose.PDF لـ C++ بالعمل بسرعة وكفاءة مع الجداول، أي إنشائها من الصفر أو إضافتها إلى مستندات PDF الحالية.

كما تحصل على القدرة على دمج الجدول مع قاعدة البيانات (DOM) لإنشاء جداول ديناميكية بناءً على محتويات قاعدة البيانات.

تسمح لك فئة [Aspose.PDF.Text.TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.absorbed_table) بالبحث وتحليل الجداول البسيطة التي توجد بالفعل على صفحة مستند PDF. يوضح المقتطف التالي من الشيفرة الخطوات لتحديث المحتوى في خلية معينة في جدول.

> العناوين:

```cpp
#include <system/date_time.h>
#include <system/io/file.h>
#include <system/console.h>
#include <data/data_table.h>
#include <data/data_column_collection.h>
#include <system/type_info.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>

#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>

#include <Aspose.PDF.Cpp/Color.h>

#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/TableAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedTable.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedRow.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedCell.h>
```

>عينات:

```cpp
using namespace System;
using namespace Aspose::Pdf;

#include "Table-Manipulate.h"

void ManipulateTables() {

    String _dataDir("C:\\Samples\\");

    // تحميل ملف PDF الموجود
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    // إنشاء كائن TableAbsorber للعثور على الجداول
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // زيارة الصفحة الأولى مع الماص
    absorber->Visit(document->get_Pages()->idx_get(1));

    // الحصول على الوصول إلى الجدول الأول على الصفحة، خليتهم الأولى وقطع النص فيها
    auto fragment = absorber->get_TableList()->idx_get(0)->get_RowList()->idx_get(0)->get_CellList()->idx_get(0)->get_TextFragments()->idx_get(1);

    // تغيير نص القطعة النصية الأولى في الخلية
    fragment->set_Text(u"hi world");
    document->Save(_dataDir + u"ManipulateTable_out.pdf");
}
```

## استبدال الجدول القديم بآخر جديد في مستند PDF

في حال كنت بحاجة إلى العثور على جدول معين واستبداله بالجدول المطلوب، يمكنك استخدام Replace() الطريقة الخاصة بـ [TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.absorbed_table) Class للقيام بذلك.

النموذج التالي يوضح الوظيفة لاستبدال الجدول داخل مستند PDF:

```cpp
void ReplaceOldTable() {
    String _dataDir("C:\\Samples\\");

    // تحميل ملف PDF موجود
    auto document = MakeObject<Document>(_dataDir + u"Table_input2.pdf");

    // إنشاء كائن TableAbsorber للعثور على الجداول
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // زيارة الصفحة الأولى باستخدام الماص
    absorber->Visit(document->get_Pages()->idx_get(1));

    // الحصول على الجدول الأول في الصفحة
    auto table = absorber->get_TableList()->idx_get(0);

    // إنشاء جدول جديد
    auto newTable = MakeObject<Table>();
    newTable->set_ColumnWidths(u"100 100 100");
    newTable->set_DefaultCellBorder (MakeObject<BorderInfo>(BorderSide::All, 1.0F));

    auto row = newTable->get_Rows()->Add();
    row->get_Cells()->Add(u"Col 1");
    row->get_Cells()->Add(u"Col 2");
    row->get_Cells()->Add(u"Col 3");

    // استبدال الجدول بالجديد
    absorber->Replace(document->get_Pages()->idx_get(1), table, newTable);

    // حفظ المستند
    document->Save(_dataDir + u"TableReplaced_out.pdf");
}
```