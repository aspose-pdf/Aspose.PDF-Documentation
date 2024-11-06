---
title: Извлечение данных из таблицы в PDF
linktitle: Извлечение данных из таблицы
type: docs
weight: 40
url: ru/cpp/extract-data-from-table-in-pdf/
description: Узнайте, как извлечь таблицы из PDF с использованием Aspose.PDF для C++.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Программное извлечение таблиц из PDF

Поскольку PDF является наиболее распространенным форматом для обмена документами, давайте рассмотрим документ с несколькими наборами данных, которые нуждаются в анализе. В этой статье мы опишем извлечение таблиц из PDF.

**Aspose.PDF для C++** предоставляет разработчикам инструменты, необходимые для извлечения данных из таблиц в документах PDF.

Этот пример демонстрирует использование класса [TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) для получения табличных данных из таблиц в файле PDF.

Следующий пример показывает извлечение таблицы со всех страниц:

```cpp
void ExtractTable() {
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Parsing\\");

    // Строка для имени файла
    String infilename("sample-table.pdf");


    auto document = MakeObject<Document>(_dataDir + infilename);
    auto absorber = MakeObject<TableAbsorber>();

    // Сканирование страниц
    for (auto page : document->get_Pages()) {
        absorber->Visit(page);
        for (auto table : absorber->get_TableList()) {
        std::cout << "Table" << std::endl;
        // Итерация по списку строк
        for (auto row : table->get_RowList()) {
            // Итерация по списку ячеек
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

## Извлечение таблицы в определенной области страницы PDF

Каждая поглощенная таблица имеет свойство [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle/), которое описывает положение таблицы на странице.

Таким образом, если вам нужно извлечь таблицы, расположенные в конкретной области, вам необходимо работать с конкретными координатами.

Следующий пример показывает, как извлечь таблицу, обозначенную квадратной аннотацией:

```cpp
void ExtractMarkedTable()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Parsing\\");

    // Строка для имени файла
    String infilename("sample-table.pdf");


    auto document = MakeObject<Document>(_dataDir + infilename);
    auto absorber = MakeObject<TableAbsorber>();

    auto page = document->get_Pages()->idx_get(1);
    auto sqa = MakeObject<Aspose::Pdf::Annotations::SquareAnnotation>(page, Rectangle::get_Trivial());
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(sqa);


    auto list = annotationSelector->get_Selected();
    if (list->get_Count() == 0) {
        std::cerr << "Обозначенные таблицы не найдены.." << std::endl;
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
            // Перебор списка ячеек
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

## Извлечение данных таблицы из PDF и сохранение их в файл CSV

Следующий пример показывает, как извлечь таблицу и сохранить её как файл CSV. Чтобы узнать, как конвертировать PDF в электронную таблицу Excel, пожалуйста, ознакомьтесь со статьей [Конвертировать PDF в Excel](/pdf/cpp/convert-pdf-to-excel/).

```cpp
void ExtractTableSaveCSV()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для пути
    String _dataDir("C:\\Samples\\Parsing\\");

    // Строка для имени файла
    String infilename("sample-table.pdf");
    String outfilename("PDFToXLS_out.csv");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Создать объект параметров сохранения в Excel
    auto excelSave = MakeObject<ExcelSaveOptions>();
    excelSave->set_Format(ExcelSaveOptions::ExcelFormat::CSV);

    // Сохранить вывод в формате XLS
    document->Save(_dataDir + outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```