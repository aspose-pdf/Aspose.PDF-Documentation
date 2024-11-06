---
title: استخراج البيانات من الجدول في PDF 
linktitle: استخراج البيانات من الجدول
type: docs
weight: 40
url: ar/cpp/extract-data-from-table-in-pdf/
description: تعلم كيفية استخراج الجداول من PDF باستخدام Aspose.PDF لـ C++.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## استخراج الجداول من PDF برمجيًا

نظرًا لأن PDF هو التنسيق الأكثر شيوعًا لتبادل المستندات، لننظر في مستند يحتوي على عدة مجموعات بيانات تحتاج إلى تحليل. في هذه المقالة، سنصف استخراج الجداول من PDF.

يوفر **Aspose.PDF لـ C++** للمطورين الأدوات التي يحتاجونها لاستخراج البيانات من الجداول في مستندات PDF.

يظهر هذا المثال استخدام الفئة [TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) لاسترجاع البيانات الجدولية من الجداول في ملف PDF.

يوضح المثال التالي استخراج الجداول من جميع الصفحات:

```cpp
void ExtractTable() {
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Parsing\\");

    // String for file name
    String infilename("sample-table.pdf");


    auto document = MakeObject<Document>(_dataDir + infilename);
    auto absorber = MakeObject<TableAbsorber>();

    // Scan pages
    for (auto page : document->get_Pages()) {
        absorber->Visit(page);
        for (auto table : absorber->get_TableList()) {
        std::cout << "Table" << std::endl;
        // Iterate throught list of rows
        for (auto row : table->get_RowList()) {
            // Iterate throught list of cell
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

## استخراج جدول في منطقة محددة من صفحة PDF

كل جدول مستوعب لديه خاصية [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle/) التي تصف موضع الجدول على الصفحة.

لذلك، إذا كنت بحاجة إلى استخراج الجداول الموجودة في منطقة معينة، يجب عليك العمل مع إحداثيات محددة.

المثال التالي يوضح كيفية استخراج الجدول الذي تم تمييزه بتعليق مربع:

```cpp
void ExtractMarkedTable()
{
    std::clog << __func__ << ": Start" << std::endl;
    // سلسلة لاسم المسار
    String _dataDir("C:\\Samples\\Parsing\\");

    // سلسلة لاسم الملف
    String infilename("sample-table.pdf");


    auto document = MakeObject<Document>(_dataDir + infilename);
    auto absorber = MakeObject<TableAbsorber>();

    auto page = document->get_Pages()->idx_get(1);
    auto sqa = MakeObject<Aspose::Pdf::Annotations::SquareAnnotation>(page, Rectangle::get_Trivial());
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(sqa);


    auto list = annotationSelector->get_Selected();
    if (list->get_Count() == 0) {
        std::cerr << "لم يتم العثور على الجداول المميزة.." << std::endl;
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
            // Iterarate throught list of cell
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

## استخراج بيانات الجدول من PDF وتخزينها في ملف CSV

يوضح المثال التالي كيفية استخراج الجدول وتخزينه كملف CSV.
لرؤية كيفية تحويل PDF إلى جدول بيانات Excel يرجى الرجوع إلى مقال [تحويل PDF إلى Excel](/pdf/cpp/convert-pdf-to-excel/).

```cpp
void ExtractTableSaveCSV()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Parsing\\");

    // String for file name
    String infilename("sample-table.pdf");
    String outfilename("PDFToXLS_out.csv");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instantiate ExcelSave Option object
    auto excelSave = MakeObject<ExcelSaveOptions>();
    excelSave->set_Format(ExcelSaveOptions::ExcelFormat::CSV);

    // Save the output in XLS format
    document->Save(_dataDir + outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```