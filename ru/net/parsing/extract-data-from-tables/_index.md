---
title: Извлечение данных из таблицы в PDF с использованием C#
linktitle: Извлечение данных из таблицы
type: docs
weight: 40
url: /ru/net/extract-data-from-table-in-pdf/
description: Узнайте, как извлекать табличные данные из PDF с помощью Aspose.PDF для .NET на C#
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Программное извлечение таблиц из PDF

Извлечение таблиц из PDF-файлов не является тривиальной задачей, потому что таблицы могут быть созданы различными способами.

Aspose.PDF для .NET имеет инструмент, который упрощает извлечение таблиц. Для извлечения данных из таблицы необходимо выполнить следующие шаги:

1. Открыть документ - создать объект [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document);
1. Создать объект [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber).
1. `TableList` — это список [AbsorbedTable](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable). Для получения данных итерируйте через `TableList`, обрабатывая [RowList](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable/properties/rowlist) и [CellList](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedrow/properties/celllist).
1. Каждая [AbsorbedCell](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedcell) содержит коллекцию [TextFragments](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedcell/properties/textfragments). Вы можете обработать её для своих целей.

Приведенный ниже фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

Следующий пример показывает извлечение таблиц со всех страниц:

```csharp
public static void Extract_Table()
{
    // Загрузите исходный PDF документ
    var filePath="<... введите путь к файлу pdf здесь ...>";
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(filePath);                       
    foreach (var page in pdfDocument.Pages)
    {
        Aspose.Pdf.Text.TableAbsorber absorber = new Aspose.Pdf.Text.TableAbsorber();
        absorber.Visit(page);
        foreach (AbsorbedTable table in absorber.TableList)
        {
            Console.WriteLine("Table");
            foreach (AbsorbedRow row in table.RowList)
            {
                foreach (AbsorbedCell cell in row.CellList)
                {                                 
                    foreach (TextFragment fragment in cell.TextFragments)
                    {
                        var sb = new StringBuilder();
                        foreach (TextSegment seg in fragment.Segments)
                            sb.Append(seg.Text);
                        Console.Write($"{sb.ToString()}|");
                    }                           
                }
                Console.WriteLine();
            }
        }
    }
}
```
## Извлечение таблицы в определенной области страницы PDF

Каждая извлеченная таблица имеет свойство [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable/properties/rectangle), которое описывает позицию таблицы на странице.

Таким образом, если вам нужно извлечь таблицы, расположенные в определенной области, вам необходимо работать с конкретными координатами.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

Следующий пример показывает, как извлечь таблицу, отмеченную аннотацией Square:

```csharp
public static void Extract_Marked_Table()
{
    // Загрузить исходный PDF документ
    var filePath="<... введите путь к файлу pdf здесь ...>";
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(filePath);  
    var page = pdfDocument.Pages[1];
    var squareAnnotation =
        page.Annotations.FirstOrDefault(ann => ann.AnnotationType == Annotations.AnnotationType.Square)
        as Annotations.SquareAnnotation;


    Aspose.Pdf.Text.TableAbsorber absorber = new Aspose.Pdf.Text.TableAbsorber();
    absorber.Visit(page);

    foreach (AbsorbedTable table in absorber.TableList)
    {
        var isInRegion = (squareAnnotation.Rect.LLX < table.Rectangle.LLX) &&
        (squareAnnotation.Rect.LLY < table.Rectangle.LLY) &&
        (squareAnnotation.Rect.URX > table.Rectangle.URX) &&
        (squareAnnotation.Rect.URY > table.Rectangle.URY);

        if (isInRegion)
        {
            foreach (AbsorbedRow row in table.RowList)
            {
                foreach (AbsorbedCell cell in row.CellList)
                {

                    foreach (TextFragment fragment in cell.TextFragments)
                    {
                        var sb = new StringBuilder();
                        foreach (TextSegment seg in fragment.Segments)
                        {
                            sb.Append(seg.Text);
                        }
                        var text = sb.ToString();
                        Console.Write($"{text}|");
                    }
                }
                Console.WriteLine();
            }
        }
    }
}
```
## Извлечение данных из таблицы PDF и сохранение их в файл CSV

Следующий пример показывает, как извлечь таблицу и сохранить ее в виде файла CSV.
Чтобы узнать, как конвертировать PDF в таблицу Excel, пожалуйста, обратитесь к статье [Конвертация PDF в Excel](/pdf/ru/net/convert-pdf-to-excel/).

Данный фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

```csharp
public static void Extract_Table_Save_CSV()
{
    // Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET

    // Загрузка документа PDF
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // Создание объекта опций сохранения Excel
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.CSV };

    // Сохранение результата в формате XLS
    pdfDocument.Save("PDFToXLS_out.xlsx", excelSave);
}
```
