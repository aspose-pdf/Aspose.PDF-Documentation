---
title: Преобразовать PDF в Excel
linktitle: Преобразовать PDF в Excel
type: docs
weight: 90
url: /ru/androidjava/convert-pdf-to-excel/
lastmod: "2026-07-01"
description: Aspose.PDF for Android via Java позволяет преобразовать PDF в формат Excel. При этом отдельные страницы PDF‑файла преобразуются в листы Excel.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for Android via Java API позволяет рендерить ваши PDF‑файлы в Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) и [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/) форматы файлов. У нас уже есть другой API, известный как [Aspose.Cells for Java](https://products.aspose.com/cells/java), который предоставляет возможность создавать и изменять существующие рабочие книги Excel. Он также предоставляет возможность преобразовывать рабочие книги Excel в формат PDF.

{{% alert color="primary" %}}

Попробуйте онлайн. Вы можете проверить качество конвертации Aspose.PDF и просмотреть результаты онлайн по этой ссылке [products.aspose.app/pdf/conversion/pdf-to-xlsx](https://products.aspose.app/pdf/conversion/pdf-to-xlsx) 

{{% /alert %}}

## Преобразовать PDF в Excel XLS

Чтобы преобразовать файлы PDF в формат XLS, Aspose.PDF имеет класс под названием [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions). Объект [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) класс передаётся в качестве второго аргумента конструктору Document.Save(..). 

Преобразование PDF‑файла в формат XLSX является частью библиотеки Aspose.PDF for Java версии 18.6. Чтобы преобразовать PDF‑файлы в формат XLSX, необходимо установить формат XLSX с помощью метода setFormat(). [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) Класс.

Следующий фрагмент кода показывает, как преобразовать файл PDF в форматы xls и .xlsx:

```java
public void convertPDFtoExcelSimple() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Save the file into MS document format
            document.save(xlsFileName.toString(), SaveFormat.Excel);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Конвертировать PDF в XLS с контрольным столбцом

При конвертации PDF в формат XLS в выходной файл добавляется пустой столбец в качестве первого столбца. В [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) Опция class InsertBlankColumnAtFirst используется для управления этим столбцом. Ее значение по умолчанию — true.

```java
public void convertPDFtoExcelAdvanced_InsertBlankColumnAtFirst() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setInsertBlankColumnAtFirst(false);

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Save the file into MS document format
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Преобразовать PDF в один лист Excel 

При экспорте PDF‑файла с большим количеством страниц в XLS каждая страница экспортируется на отдельный лист в файле Excel. Это происходит потому, что свойство MinimizeTheNumberOfWorksheets по умолчанию установлено в false. Чтобы обеспечить экспорт всех страниц на один единственный лист в результирующем файле Excel, установите свойство MinimizeTheNumberOfWorksheets в true.

```java
 public void convertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setMinimizeTheNumberOfWorksheets(true);

        // Save the output in XLSX
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Save the file into MS Excel format
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```

## Преобразовать в формат XLSX 

По умолчанию Aspose.PDF использует XML Spreadsheet 2003 для хранения данных. Чтобы преобразовать PDF‑файлы в формат XLSX, Aspose.PDF имеет класс под названием ExcelSaveOptions с параметром Format. Объект [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) класс передается в качестве второго аргумента методу Document.Save(..).

```java
 public void convertPDFtoExcelAdvanced_SaveCSV() {
        // Load PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setFormat(ExcelSaveOptions.ExcelFormat.CSV);

        // Save the output in CSV
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.csv");
        try {
            // Save the file into CSV format
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```
