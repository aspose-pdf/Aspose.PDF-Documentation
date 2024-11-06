---
title: Convert PDF to Excel 
linktitle: Convert PDF to Excel 
type: docs
weight: 90
url: ru/androidjava/convert-pdf-to-excel/
lastmod: "2021-06-05"
description: Aspose.PDF for Android via Java позволяет конвертировать PDF в формат Excel. При этом отдельные страницы PDF файла преобразуются в листы Excel.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for Android via Java API позволяет преобразовывать ваши PDF файлы в форматы Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) и [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/). У нас уже есть другой API, известный как [Aspose.Cells for Java](https://products.aspose.com/cells/java), который предоставляет возможность создавать и изменять существующие рабочие книги Excel. Он также предоставляет возможность преобразовывать рабочие книги Excel в формат PDF.

{{% alert color="primary" %}}

Попробуйте онлайн.
 Вы можете проверить качество конверсии Aspose.PDF и просмотреть результаты онлайн по этой ссылке [products.aspose.app/pdf/conversion/pdf-to-xlsx](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)

## Конвертировать PDF в Excel XLS

Для конвертации файлов PDF в формат XLS, Aspose.PDF имеет класс под названием [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions). Объект класса [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) передается в качестве второго аргумента в конструктор Document.Save(..).

{{% /alert %}}
Конвертация PDF файла в формат XLSX является частью библиотеки Aspose.PDF для версии Java 18.6. Для того чтобы конвертировать PDF файлы в формат XLSX, необходимо установить формат как XLSX, используя метод setFormat() класса [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions).

Следующий фрагмент кода показывает, как конвертировать PDF файл в формат xls и .xlsx:

```java
public void convertPDFtoExcelSimple() {
        // Открыть исходный PDF документ
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Создать объект ExcelSave Option
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Сохранить файл в формате MS документа
            document.save(xlsFileName.toString(), SaveFormat.Excel);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Преобразование PDF в XLS с контролем столбца

При преобразовании PDF в формат XLS пустой столбец добавляется в выходной файл в качестве первого столбца. Параметр InsertBlankColumnAtFirst класса [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) используется для управления этим столбцом. Значение по умолчанию — true.

```java
public void convertPDFtoExcelAdvanced_InsertBlankColumnAtFirst() {
        // Открыть исходный PDF-документ
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Создать объект параметров сохранения Excel
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setInsertBlankColumnAtFirst(false);

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Сохранить файл в формате MS документа
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


## Преобразование PDF в один лист Excel

При экспорте PDF-файла с большим количеством страниц в XLS каждая страница экспортируется на отдельный лист в файле Excel. Это происходит потому, что свойство MinimizeTheNumberOfWorksheets по умолчанию установлено в значение false. Чтобы все страницы были экспортированы на один лист в выходном Excel-файле, установите свойство MinimizeTheNumberOfWorksheets в значение true.

```java
 public void convertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets() {
        // Открыть исходный PDF-документ
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Создание объекта параметров сохранения Excel
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setMinimizeTheNumberOfWorksheets(true);

        // Сохранение результата в формате XLSX
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Сохранить файл в формате MS Excel
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```


## Преобразование в формат XLSX

По умолчанию Aspose.PDF использует XML Spreadsheet 2003 для хранения данных. Чтобы преобразовать PDF файлы в формат XLSX, Aspose.PDF предоставляет класс под названием ExcelSaveOptions с параметром Format. Объект класса [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) передается в качестве второго аргумента методу Document.Save(..).

```java
 public void convertPDFtoExcelAdvanced_SaveCSV() {
        // Загрузить PDF документ
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Создать объект параметров сохранения Excel
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setFormat(ExcelSaveOptions.ExcelFormat.CSV);

        // Сохранить вывод в CSV
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.csv");
        try {
            // Сохранить файл в формате CSV
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```