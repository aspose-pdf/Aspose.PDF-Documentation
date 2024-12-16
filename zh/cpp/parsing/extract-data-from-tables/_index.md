---
title: 从PDF中的表格提取数据
linktitle: 提取表格数据
type: docs
weight: 40
url: /zh/cpp/extract-data-from-table-in-pdf/
description: 学习如何使用Aspose.PDF for C++从PDF中提取表格数据。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 从PDF中以编程方式提取表格

由于PDF是交换文档的最常见格式，让我们考虑一个包含多个数据集的文档，这些数据集需要进行分析。在本文中，我们将描述如何从PDF中提取表格。

**Aspose.PDF for C++** 为开发人员提供了从PDF文档中的表格中提取数据所需的工具。

此示例演示了使用 [TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) 类从PDF文件中的表格中检索表格数据。

以下示例显示了从所有页面提取表格：

```cpp
void ExtractTable() {
    std::clog << __func__ << ": Start" << std::endl;
    // 用于路径名的字符串
    String _dataDir("C:\\Samples\\Parsing\\");

    // 用于文件名的字符串
    String infilename("sample-table.pdf");

    auto document = MakeObject<Document>(_dataDir + infilename);
    auto absorber = MakeObject<TableAbsorber>();

    // 扫描页面
    for (auto page : document->get_Pages()) {
        absorber->Visit(page);
        for (auto table : absorber->get_TableList()) {
        std::cout << "Table" << std::endl;
        // 迭代行列表
        for (auto row : table->get_RowList()) {
            // 迭代单元格列表
            for (auto cell : row->get_CellList()) {
                String sb;
                for (auto fragment : cell->get_TextFragments()) {
                sb += fragment->get_Text();
                }
                std::cout << sb << "|";
            }
            std::cout << std::endl;
        }
        }
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## 提取 PDF 页面特定区域中的表格

每个吸收的表格都有 [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle/) 属性，用于描述页面上表格的位置。

因此，如果需要提取位于特定区域的表格，则必须使用特定坐标。

以下示例显示如何提取用方形注释标记的表格：

```cpp
void ExtractMarkedTable()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名的字符串
    String _dataDir("C:\\Samples\\Parsing\\");

    // 文件名的字符串
    String infilename("sample-table.pdf");


    auto document = MakeObject<Document>(_dataDir + infilename);
    auto absorber = MakeObject<TableAbsorber>();

    auto page = document->get_Pages()->idx_get(1);
    auto sqa = MakeObject<Aspose::Pdf::Annotations::SquareAnnotation>(page, Rectangle::get_Trivial());
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(sqa);


    auto list = annotationSelector->get_Selected();
    if (list->get_Count() == 0) {
        std::cerr << "Marked tables not found.." << std::endl;
        return;
    }

    auto squareAnnotation = System::DynamicCast<Aspose::Pdf::Annotations::SquareAnnotation>(list->idx_get(1));

    absorber->Visit(page);

    for (auto table : absorber->get_TableList())
    {
        auto isInRegion =
        (squareAnnotation->get_Rect()->get_LLX() < table->get_Rectangle()->get_LLX()) &&
        (squareAnnotation->get_Rect()->get_LLY() < table->get_Rectangle()->get_LLY()) &&
        (squareAnnotation->get_Rect()->get_URX() > table->get_Rectangle()->get_URX()) &&
        (squareAnnotation->get_Rect()->get_URY() > table->get_Rectangle()->get_URY());

        if (isInRegion)
        {
        for (auto row : table->get_RowList()) {
            // 遍历单元格列表
            for (auto cell : row->get_CellList()) {
                String sb;
                for (auto fragment : cell->get_TextFragments()) {
                sb += fragment->get_Text();
                }
                std::cout << sb << "|";
            }
            std::cout << std::endl;
        }
        }
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## 从 PDF 提取表格数据并存储到 CSV 文件

以下示例显示了如何提取表格并将其存储为 CSV 文件。要了解如何将 PDF 转换为 Excel 电子表格，请参阅[将 PDF 转换为 Excel](/pdf/zh/cpp/convert-pdf-to-excel/)文章。

```cpp
void ExtractTableSaveCSV()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\Parsing\\");

    // 文件名的字符串
    String infilename("sample-table.pdf");
    String outfilename("PDFToXLS_out.csv");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 实例化 ExcelSave Option 对象
    auto excelSave = MakeObject<ExcelSaveOptions>();
    excelSave->set_Format(ExcelSaveOptions::ExcelFormat::CSV);

    // 以 XLS 格式保存输出
    document->Save(_dataDir + outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```