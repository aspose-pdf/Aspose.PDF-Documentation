---
title: 从PDF提取表格
linktitle: 提取表格
type: docs
weight: 20
url: /zh/cpp/extract-table-from-existing-pdf-document/
description: Aspose.PDF for C++使您能够对PDF文档中包含的表格进行各种操作。您可以在现有PDF文档中添加和提取表格，在新页面上渲染表格等。
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 从PDF提取表格

从PDF文档中提取任何数据似乎相当困难。然而，**Aspose.PDF for C++**库允许您处理此任务。使用C++从您的pdf文件中提取表格：

>Header:

```cpp
#include <system/console.h>
#include <system/collections/stack.h>
#include <system/io/memory_stream.h>

#include <drawing/imaging/image_format.h>
#include <drawing/bitmap.h>
#include <drawing/graphics.h>
#include <drawing/solid_brush.h>
#include <drawing/drawing2d/matrix.h>
#include <drawing/drawing2d/graphics_path.h>
#include <drawing/drawing2d/smoothing_mode.h>
#include <system/console.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/PageInfo.h>

#include <Aspose.PDF.Cpp/Operator.h>
#include <Aspose.PDF.Cpp/OperatorCollection.h>

#include <Aspose.PDF.Cpp/DOM/Matrix.h>

#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TextSegment.h>
#include <Aspose.PDF.Cpp/Text/TextSegmentCollection.h>

#include <Aspose.PDF.Cpp/Text/TableAbsorber/TableAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedTable.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedRow.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedCell.h>
```

```cpp
使用命名空间 System;
使用命名空间 System::Collections::Generic;

使用命名空间 Aspose::Pdf;
使用命名空间 Aspose::Pdf::Text;

void 提取_表格()
{
    String _dataDir("C:\\Samples\\");
    // 加载源 PDF 文档    
    auto document = MakeObject<Document>(_dataDir + u"the_worlds_cities_in_2018_data_booklet 7.pdf");
    for (auto page : document->get_Pages())
    {
        auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();
        absorber->Visit(page);
        for (auto table : absorber->get_TableList())
        {
            for (auto row : table->get_RowList())
            {
                for (auto cell : row->get_CellList())
                {
                    auto textfragment = MakeObject<TextFragment>();
                    auto textFragmentCollection = cell->get_TextFragments();
                    for (auto fragment : textFragmentCollection)
                    {
                        String txt;
                        for (auto seg : fragment->get_Segments())
                        {
                            txt += seg->get_Text();
                        }
                        Console::WriteLine(txt);
                    }
                }
            }
        }
    }
}
```

## 提取表格边框为图像

以下代码片段展示了从 PDF 文档中提取表格边框为图像的步骤：