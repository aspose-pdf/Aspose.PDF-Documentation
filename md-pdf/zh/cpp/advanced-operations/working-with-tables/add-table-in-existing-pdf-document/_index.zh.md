---
title: 在 PDF 中创建或添加表格
linktitle: 创建或添加表格
type: docs
weight: 10
url: /cpp/add-table-in-existing-pdf-document/
description: Aspose.PDF for C++ 是一个用于创建、读取和编辑 PDF 表格的库。使用该库，您可以使用 C++ 在 PDF 页面上分页显示表格。
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 使用 C++ 创建表格

在处理 PDF 文档时，表格是非常重要的。它们为系统化地显示信息提供了极好的功能。

PDF 文档中的表格以系统化的方式在行和列中组织数据。Aspose.PDF for C++ API 允许您向 PDF 文档中添加表格，并在您的 C++ 应用程序中为其添加行和列。[Table](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table/) 类用于向文档中添加表格。可以按照以下步骤使用 C++ 向 PDF 文档中添加表格。

### 在现有 PDF 文档中添加表格

要使用 Aspose.PDF for C++ 向现有 PDF 文件添加表格，请执行以下步骤：

1. 加载源文件。
1. 初始化一个表并设置其列和行。
1. 设置表格设置（我们已经设置了边框）。
1. 填充表格。
1. 将表格添加到页面。
1. 保存文件。

以下代码片段显示了如何在现有 PDF 文件中添加文本。

>Headers

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
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/PageInfo.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Generator/GraphInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderCornerStyle.h>
#include <Aspose.PDF.Cpp/Generator/ColumnAdjustment.h>
#include <Aspose.PDF.Cpp/Generator/ImageFileType.h>
#include <Aspose.PDF.Cpp/Generator/Image.h>
#include <Aspose.PDF.Cpp/Generator/HtmlFragment.h>

#include <Aspose.PDF.Cpp/Text/TextFragment.h>

#include <Aspose.PDF.Cpp/Color.h>

#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
```

>示例

```cpp
using namespace System;
using namespace Aspose::Pdf;

void AddingTableInExistingPDFDocument() {
    
    String _dataDir("C:\\Samples\\");
    
    // 加载源PDF文档
    auto document = MakeObject<Document>(_dataDir + u"AddTable.pdf");
    
    // 初始化一个新的Table实例
    auto table = MakeObject<Table>();
    
    // 设置表格边框颜色为LightGray
    table->set_Border(MakeObject<Aspose::Pdf::BorderInfo>(
        Aspose::Pdf::BorderSide::All, .5f, 
        Aspose::Pdf::Color::get_LightGray()));
    // 设置表格单元格的边框
    table->set_DefaultCellBorder (MakeObject<Aspose::Pdf::BorderInfo>(
        Aspose::Pdf::BorderSide::All, .5f, 
        Aspose::Pdf::Color::get_LightGray()));

    // 创建一个循环以添加10行
    for (int row_count = 1; row_count < 10; row_count++)
    {
        // 向表中添加行
        auto row = table->get_Rows()->Add();
        // 添加表格单元格
        row->get_Cells()->Add(String::Format(u"Column ({0}, 1)", row_count));
        row->get_Cells()->Add(String::Format(u"Column ({0}, 2)", row_count));
        row->get_Cells()->Add(String::Format(u"Column ({0}, 3)", row_count));
    }

    // 将表对象添加到输入文档的第一页
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(table);
    
    // 保存更新后的包含表对象的文档
    document->Save(_dataDir + u"document_with_table_out.pdf");
}
```

### ColSpan 和 RowSpan 在表格中

Aspose.PDF for C++ 提供了一个 [ColSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#ae79c581d2245258699c98617e78c01d1) 属性用于合并表格中的列，以及一个 [RowSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#a4eb7337d118314e6c2180670fb32721a) 属性用于合并表格中的行。

我们在创建表格单元格的 [Cell](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell) 对象上使用 [ColSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#ae79c581d2245258699c98617e78c01d1) 或 [RowSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#a4eb7337d118314e6c2180670fb32721a) 属性。应用所需属性后，创建的单元格可以被添加到表格中。

```cpp
void AddTable_RowColSpan()
{
    String _dataDir("C:\\Samples\\");

    // 加载源 PDF 文档
    auto document = MakeObject<Document>();
    document->get_Pages()->Add();

    // 初始化 Table 的新实例
    auto table = MakeObject<Table>();
    // 将表格边框颜色设置为浅灰色
    table->set_Border(MakeObject<Aspose::Pdf::BorderInfo>(
        Aspose::Pdf::BorderSide::All, .5f, 
        Color::get_Black()));
        // 设置表格单元格的边框
    table->set_DefaultCellBorder(
        MakeObject<Aspose::Pdf::BorderInfo>(
            Aspose::Pdf::BorderSide::All, .5f, 
            Color::get_Black()));
    

    // 向表格添加第一行
    auto row1 = table->get_Rows()->Add();
    for (int cellCount = 1; cellCount < 5; cellCount++)
    {
        // 添加表格单元格
        row1->get_Cells()->Add(String::Format(u"Test 1 {0}", cellCount));
    }

    // 向表格添加第二行
    auto row2 = table->get_Rows()->Add();
    row2->get_Cells()->Add(u"Test 2 1");
    auto cell = row2->get_Cells()->Add(u"Test 2 2");
    cell->set_ColSpan(2);
    row2->get_Cells()->Add(u"Test 2 4");

    // 向表格添加第三行
    auto row3 = table->get_Rows()->Add();
    row3->get_Cells()->Add(u"Test 3 1");
    row3->get_Cells()->Add(u"Test 3 2");
    row3->get_Cells()->Add(u"Test 3 3");
    row3->get_Cells()->Add(u"Test 3 4");

    // 向表格添加第四行
    auto row4 = table->get_Rows()->Add();
    row4->get_Cells()->Add(u"Test 4 1");
    cell = row4->get_Cells()->Add(u"Test 4 2");
    cell->set_RowSpan (2);
    row4->get_Cells()->Add(u"Test 4 3");
    row4->get_Cells()->Add(u"Test 4 4");


    // 向表格添加第五行
    auto row5 = table->get_Rows()->Add();
    row5->get_Cells()->Add(u"Test 5 1");
    row5->get_Cells()->Add(u"Test 5 3");
    row5->get_Cells()->Add(u"Test 5 4");

    // 将表格对象添加到输入文档的第一页
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(table);

    // 保存包含表格对象的更新文档
    document->Save(_dataDir + u"document_with_table_out.pdf");
}
```

代码执行结果如下图所示的表格：

![ColSpan 和 RowSpan 演示](colspan_rowspan.png)

## 使用边框、边距和填充

请注意，它还支持为表格设置边框、边距和单元格填充的功能，首先让我们理解边框、边距和填充的概念，如下图所示：

![边框、边距和填充](set-border-style-margins-and-padding-of-table_1.png)

详细检查图示。它显示了表格、行和单元格的边框是如何重叠的。使用 Aspose.PDF for C++ 可以为表格设置边距，并可以缩进单元格。要设置单元格边距，我们必须设置单元格填充。

## 边框

要设置 Table、[Row](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.row) 和 [Cell](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell) 对象的边框，请使用 Table.Border、Row.Border 和 Cell.Border 属性。 单元格边框也可以使用 [Table](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table) 或 Row 类的 DefaultCellBorder 属性进行设置。上面讨论的所有边框相关属性都被分配给 Row 类的一个实例，该实例是通过调用其构造函数创建的。Row 类有许多重载，几乎可以接受所有参数来定制边框。

## 边距或填充

单元格填充可以使用 Table 类的 [DefaultCellPadding](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table#ac64196de6dfed7550c3278892ed9dbe0) 属性进行管理。所有填充相关属性都被分配给 [MarginInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.margin_info/) 类的一个实例，该实例获取有关 `Left`、`Right`、`Top` 和 `Bottom` 参数的信息，以创建自定义边距。

![PDF 表格中的边距和边框](margin-border.png)

```cpp
void AddTable_MergingPadding() {

    String _dataDir("C:\\Samples\\");

    // 通过调用其空构造函数实例化 Document 对象
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    // 实例化一个表对象
    auto tab1 = MakeObject<Table>();
    // 在所需部分的段落集合中添加表格
    page->get_Paragraphs()->Add(tab1);
    // 设置表格的列宽
    tab1->set_ColumnWidths (u"50 50 50");
    // 使用 BorderInfo 对象设置默认单元格边框
    tab1->set_DefaultCellBorder (
        MakeObject<Aspose::Pdf::BorderInfo>(
            Aspose::Pdf::BorderSide::All, 0.1F));
    // 使用另一个自定义的 BorderInfo 对象设置表格边框
    tab1->set_Border (
        MakeObject<Aspose::Pdf::BorderInfo>(
            Aspose::Pdf::BorderSide::All, 1.0F));

    // 创建 MarginInfo 对象并设置其左、下、右和上边距
    auto margin = MakeObject<MarginInfo>();
    margin->set_Top (5.0f);
    margin->set_Left (5.0f);
    margin->set_Right (5.0f);
    margin->set_Bottom (5.0f);

    // 将默认单元格填充设置为 MarginInfo 对象
    tab1->set_DefaultCellPadding (margin);
    // 在表格中创建行，然后在行中创建单元格
    auto row1 = tab1->get_Rows()->Add();
    row1->get_Cells()->Add(u"col1");
    row1->get_Cells()->Add(u"col2");
    row1->get_Cells()->Add();

    auto mytext = MakeObject<Aspose::Pdf::Text::TextFragment>(u"col3 with large text string");
        
    row1->get_Cells()->idx_get(2)->get_Paragraphs()->Add(mytext);
    row1->get_Cells()->idx_get(2)->set_IsWordWrapped(false);
    

    auto row2 = tab1->get_Rows()->Add();
    row2->get_Cells()->Add(u"item1");
    row2->get_Cells()->Add(u"item2");
    row2->get_Cells()->Add(u"item3");
    
    // 保存 Pdf
    document->Save(_dataDir + u"MarginsOrPadding_out.pdf");
}
```
要创建带圆角的表格，可使用 [BorderInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.border_info) 类的 [RoundedBorderRadius](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.border_info#a6a2bed69dd034fba9ce439dcbe1fd3de) 值，并将表格角样式设置为圆角。

```cpp
void AddTable_RoundedBorderRadius()
{
    // 文档目录的路径。
    String _dataDir("C:\\Samples\\");

    auto tab1 = MakeObject<Aspose::Pdf::Table>();

    auto graph = MakeObject<GraphInfo>();
    graph->set_Color(Color::get_Red());
    // 创建一个空的 BorderInfo 对象
    auto bInfo = MakeObject<BorderInfo>(BorderSide::All, graph);

    // 设置边框为圆角，圆角半径为 15
    bInfo->set_RoundedBorderRadius(15);
    // 将表格角样式设置为圆角。
    tab1->set_CornerStyle (Aspose::Pdf::BorderCornerStyle::Round);
    // 设置表格边框信息
    tab1->set_Border(bInfo);
}
```

### ColumnAdjustmentType 枚举中的 AutoFitToWindow 属性

```cpp
void AddTable_AutoFitToWindow() {
    
    // 文档目录的路径。
    String _dataDir("C:\\Samples\\");

    // 通过调用其空构造函数实例化Pdf对象
    auto document = MakeObject<Document>();

    // 在Pdf对象中创建部分
    auto sec1 = document->get_Pages()->Add();

    // 实例化一个表对象
    auto tab1 = MakeObject<Aspose::Pdf::Table>();
    // 在所需部分的段落集合中添加表格
    sec1->get_Paragraphs()->Add(tab1);

    // 设置表格的列宽
    tab1->set_ColumnWidths (u"50 50 50");
    tab1->set_ColumnAdjustment (ColumnAdjustment::AutoFitToWindow);

    // 使用BorderInfo对象设置默认单元格边框
    tab1->set_DefaultCellBorder(MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::All, 0.1F));

    // 使用另一个自定义的BorderInfo对象设置表格边框
    tab1->set_Border (MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::All, 1.0F));

    // 创建MarginInfo对象并设置其左、下、右和上边距
    auto margin = MakeObject<MarginInfo>();
    margin->set_Top(5.0f);
    margin->set_Left(5.0f);
    margin->set_Right(5.0f);
    margin->set_Bottom(5.0f);

    // 将默认单元格填充设置为MarginInfo对象
    tab1->set_DefaultCellPadding(margin);

    // 在表格中创建行，然后在行中创建单元格
    auto row1 = tab1->get_Rows()->Add();
    row1->get_Cells()->Add(u"col1");
    row1->get_Cells()->Add(u"col2");
    row1->get_Cells()->Add(u"col3");

    auto row2 = tab1->get_Rows()->Add();
    row2->get_Cells()->Add(u"item1");
    row2->get_Cells()->Add(u"item2");
    row2->get_Cells()->Add(u"item3");
    
    // 保存包含表对象的更新文档
    document->Save(_dataDir + u"AutoFitToWindow_out.pdf");
}
```

### 获取表格宽度

在某些任务中，您需要动态获取表格的宽度。
[Aspose.PDF.Table](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table) 类为此目的提供了一个 [GetWidth] 方法 (https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table#a3361cc8d4af87eec2e3da616c474ac1c)。例如，您没有明确设置表格列的宽度，并且没有将 [ColumnAdjustment] (https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#afc01382935026dd569c96d77d09dc3a4) 设置为 AutoFitToContent。在这种情况下，您可以获取下一个表格宽度。

```cpp
void GetTableWidth() {
    // 创建一个新文档
    auto document = MakeObject<Document>();
    
    // 在文档中添加页面
    auto page = document->get_Pages()->Add();

    // 初始化新表格
    auto table = MakeObject<Table>();
    table->set_ColumnAdjustment(ColumnAdjustment::AutoFitToContent);
    
    // 在表格中添加行
    auto row = table->get_Rows()->Add();

    // 在表格中添加单元格
    auto cell = row->get_Cells()->Add(u"单元格 1 文本");
    cell = row->get_Cells()->Add(u"单元格 2 文本");
    // 获取表格宽度
    Console::WriteLine(table->GetWidth());
}
```

## 将 SVG 图像添加到表格单元格

Aspose.PDF for C++ 允许您向 PDF 文件添加表格单元格。当您创建表格时，可以向单元格中添加文本或图像。此外，API 还提供了将 SVG 文件转换为 PDF 的功能。通过结合这些功能，可以加载 SVG 图像并将其添加到表格单元格中。

以下代码片段展示了实例化表格并将 SVG 图像添加到表格单元格的步骤。

```cpp
void InsertSVGObject() 
{
    String _dataDir("C:\\Samples\\");

    // 实例化 Document 对象
    auto document = MakeObject<Document>();
    // 创建图像实例
    auto img = MakeObject<Aspose::Pdf::Image>();

    // 将图像类型设置为 SVG
    img->set_FileType(Aspose::Pdf::ImageFileType::Svg);
    // 源文件的路径
    img->set_File (_dataDir + u"SVGToPDF.svg");
    // 设置图像实例的宽度
    img->set_FixWidth (50);
    // 设置图像实例的高度
    img->set_FixHeight(50);
    // 创建表格实例
    auto table = MakeObject<Aspose::Pdf::Table>();
    // 设置表格单元格的宽度
    table->set_ColumnWidths (u"100 100");
    // 创建行对象并将其添加到表格实例中
    auto row = table->get_Rows()->Add();
    // 创建单元格对象并将其添加到行实例中
    auto cell = row->get_Cells()->Add();
    // 向单元格对象的段落集合中添加文本片段
    cell->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"First cell"));
    // 向行对象中添加另一个单元格
    cell = row->get_Cells()->Add();
    // 向最近添加的单元格实例的段落集合中添加 SVG 图像
    cell->get_Paragraphs()->Add(img);
    // 创建页面对象并将其添加到文档实例的页面集合中
    auto page = document->get_Pages()->Add();
    // 将表格添加到页面对象的段落集合中
    page->get_Paragraphs()->Add(table);    
    // 保存 PDF 文件
    document->Save(_dataDir + u"AddSVGObject_out.pdf");
}
```

## 在表格中使用 HTML 标签

对于某些任务，您需要导入带有一些 HTML 标签的数据库内容，然后将内容导入到表格对象中。导入内容时，HTML 标签必须显示在 PDF 文档中。

在下面的代码片段中，您可以设置表格边框颜色，为表格单元格设置边框。之后，您将创建一个循环来添加 10 行。将表格对象添加到输入文档的第一页并保存更新的文档。

```cpp
void AddHTMLFragmentToTableCell() {
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"input.pdf");    
    // 初始化表格的新实例
    auto table = MakeObject<Table>();
    // 将表格边框颜色设置为 LightGray
    table->set_Border(new BorderInfo(BorderSide::All, .5f, Color::get_LightGray()));
    // 设置表格单元格的边框
    table->set_DefaultCellBorder(new BorderInfo(BorderSide::All, .5f, Color::get_LightGray()));
    // 创建一个循环以添加 10 行       
    for (int row_count = 1; row_count < 10; row_count++) {
        SmartPtr<Cell> cell;
        // 将行添加到表格
        auto row = table->get_Rows()->Add();
        // 添加表格单元格
        cell = row->get_Cells()->Add();
        cell->get_Paragraphs()->Add(new HtmlFragment(String::Format(u"Column <strong>({0}, 1)</strong>", row_count)));

        cell = row->get_Cells()->Add();
        cell->get_Paragraphs()->Add(new HtmlFragment(String::Format(u"Column <span style='color:red'>({0}, 2)</span>",row_count)));

        cell = row->get_Cells()->Add();
        cell->get_Paragraphs()->Add(new HtmlFragment(String::Format(u"Column <span style='text-decoration: underline'>([0}, 3)</span>", row_count)));
    }
    // 将表格对象添加到输入文档的第一页
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(table);
    // 保存包含表格对象的更新文档
    document->Save(_dataDir + u"AddHTMLObject_out.pdf");
}
```

## 在表格的行之间插入分页符

通常，当在 PDF 中创建表格时，当表格到达底部边距时，表格会流向后续页面。但我们可能需要在向表格添加一定数量的行时强制插入分页符。以下代码片段显示了在向表格添加 10 行时插入分页符的步骤。

以下代码片段显示了在向表格添加 10 行时插入分页符的步骤。

```cpp
void InsertPageBreak() {
    String _dataDir("C:\\Samples\\");

    // 实例化 Document 实例
    auto document = MakeObject<Document>();
    
    // 将页面添加到 PDF 文件的页面集合中
    auto page = document->get_Pages()->Add();

    // 创建表格实例
    auto tab = MakeObject<Table>();

    // 设置表格的边框样式
    tab->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));
    // 设置表格的默认边框样式，边框颜色为红色
    tab->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));
    // 指定表格列宽
    tab->set_ColumnWidths(u"100 100");

    // 创建一个循环为表格添加 200 行
    for (int counter = 0; counter <= 200; counter++) {
        auto row = MakeObject<Row>();
        tab->get_Rows()->Add(row);
        auto cell1 = MakeObject<Cell>();
        cell1->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(String::Format(u"Cell {0}, 0", counter)));
        row->get_Cells()->Add(cell1);

        auto cell2 = new Cell();
        cell2->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(String::Format(u"Cell {0}, 1", counter)));
        row->get_Cells()->Add(cell2);
        // 当添加了 10 行时，在新页面中呈现新行
        if (counter % 10 == 0 && counter != 0)
            row->set_IsInNewPage(true);
    }
    // 将表格添加到 PDF 文件的段落集合中
    page->get_Paragraphs()->Add(tab);

    // 保存 PDF 文档
    document->Save(_dataDir + u"InsertPageBreak_out.pdf");
}
```

## 在新页面上渲染表格

默认情况下，段落被添加到页面对象的段落集合中。然而，可以在新页面上渲染表格，而不是直接在页面上先前添加的段落级对象之后。

### 示例：如何使用 C++ 在新页面上渲染表格

要在新页面上渲染表格，请在 [BaseParagraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.base_paragraph) 类中使用 [IsInNewPage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.base_paragraph#a614946048d22afb9dce4cd42346c7561) 属性。
以下代码片段展示了如何实现。

```cpp
void RenderTableOnNewPage()
{
    auto document = MakeObject<Document>();
    auto pageInfo = document->get_PageInfo();
    auto marginInfo = pageInfo->get_Margin();

    marginInfo->set_Left (37);
    marginInfo->set_Right (37);
    marginInfo->set_Top (37);
    marginInfo->set_Bottom (37);

    pageInfo->set_IsLandscape(true);

    auto table = MakeObject<Aspose::Pdf::Table>();
    table->set_ColumnWidths(u"50 100");
    // 添加页面。
    auto curPage = document->get_Pages()->Add();
    for (int i = 1; i <= 120; i++)
    {
        auto row = table->get_Rows()->Add();
        row->set_FixedRowHeight(15);
        auto cell1 = row->get_Cells()->Add();
        cell1->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Content 1"));
        auto cell2 = row->get_Cells()->Add();
        cell2->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"HHHHH"));
    }
    auto paragraphs = curPage->get_Paragraphs();
    paragraphs->Add(table);

    //-------------------------------------

    auto document = MakeObject<Document>();
    auto table1 = MakeObject<Aspose::Pdf::Table>();
    table1->set_ColumnWidths(u"100 100");

    String _dataDir("C:\\Samples\\");

    for (int i = 1; i <= 10; i++)
    {
        auto row = table1->get_Rows()->Add();
        auto cell1 = row->get_Cells()->Add();
        cell1->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"LAAAAAAA"));
        auto cell2 = row->get_Cells()->Add();
        cell2->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"LAAGGGGGG"));
    }
    
    table1->set_IsInNewPage (true);
    // 我希望将表格 1 保留在下一页...
    paragraphs->Add(table1);
    
    document->Save(_dataDir + u"IsNewPageProperty_Test_out.pdf");
}
```