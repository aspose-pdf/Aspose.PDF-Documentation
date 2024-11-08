---
title: Работа с печатью PDF
type: docs
weight: 10
url: /ru/java/print-pdf-file/
description: Этот раздел объясняет, как печатать PDF-файл с использованием Aspose.PDF Facades и класса PdfViewer.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Печать PDF-файла на принтер по умолчанию с использованием настроек принтера и страницы

Класс [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) позволяет печатать PDF-файл на принтер по умолчанию. Для этого необходимо создать объект [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) и открыть PDF с помощью метода openPdfFile(..).

Вызовите метод printDocument(..) для печати PDF на принтер по умолчанию.

Следующий код демонстрирует, как печатать PDF на принтер по умолчанию с настройками принтера и страницы.

```java
 public static void PrintingPDFFile() {
        // Создать объект PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Открыть входной PDF-файл
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Установить атрибуты для печати
        viewer.setAutoResize(true); // Печать файла с подогнанным размером
        viewer.setAutoRotate(true); // Печать файла с подогнанным поворотом
        viewer.setPrintPageDialog(false); // Не выводить диалоговое окно с номером страницы при печати

        // Создать объекты для настроек принтера и страницы и PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Установить имя принтера
        printerSettings.setPrinterName("Microsoft Print to PDF");
        

        // Установить размер страницы (если необходимо)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Установить поля страницы (если необходимо)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Печать документа с использованием настроек принтера и страницы
        viewer.printDocumentWithSettings(pageSettings, printerSettings);
        
        // Закрыть PDF-файл после печати
        viewer.close();
    }
```


Для отображения диалогового окна печати попробуйте использовать следующий фрагмент кода:

```java
public static void PrintingPDFDisplayPrintDialog() {
        // Создать объект PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Открыть входной PDF файл
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Установить атрибуты для печати
        viewer.setAutoResize(true); // Печатать файл с подогнанным размером
        viewer.setAutoRotate(true); // Печатать файл с подогнанным поворотом
        viewer.setPrintPageDialog(true);

        // Создать объекты для настроек принтера и страницы и PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Установить размер страницы (если требуется)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Установить поля страницы (если требуется)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        java.awt.print.PrinterJob pj = java.awt.print.PrinterJob.getPrinterJob();

        if (pj.printDialog()) {
            printerSettings.setPrinterName(pj.getPrintService().getName());
            printerSettings.setCopies((short) pj.getCopies());
            // Печать документа с использованием настроек принтера и страницы
            viewer.printDocumentWithSettings(pageSettings, printerSettings);
        }
        // Закрыть PDF файл после печати
        viewer.close();
    }
```


## Печать PDF на виртуальный принтер

Существуют принтеры, которые печатают в файл. Мы устанавливаем имя виртуального принтера и, по аналогии с предыдущим примером, производим настройки.

```java
public static void PrintingPDFToSoftPrinter() {
        // Создать объект PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Открыть входной PDF файл
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Установить атрибуты для печати
        viewer.setAutoResize(true); // Печать файла с настройкой размера
        viewer.setAutoRotate(true); // Печать файла с настройкой поворота
        viewer.setPrintPageDialog(false); // Не отображать диалог выбора страницы при печати

        // Создать объекты для настроек принтера и страницы и PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Установить принтер Microsoft Soft Printer
        printerSettings.setPrinterName("Microsoft Print to PDF");
        // или Adobe
        // printerSettings.setPrinterName("Adobe PDF");

        // Установить размер страницы (если требуется)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Установить поля страницы (если требуется)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Распечатать документ, используя настройки страницы и принтера
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // Закрыть PDF файл после печати
        viewer.close();
    }
```


## Скрытие диалога печати

Aspose.PDF для Java позволяет скрыть диалог печати. Для этого используйте метод [getPrintPageDialog](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer#getPrintPageDialog--).

Следующий фрагмент кода показывает, как скрыть диалог печати.

```java
public static void PrintingPDFHidePrintDialog() {
        // Создать объект PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Открыть входной PDF файл
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Установить атрибуты для печати
        viewer.setAutoResize(true); // Печать файла с подогнанным размером
        viewer.setAutoRotate(true); // Печать файла с подогнанным поворотом

        viewer.setPrintPageDialog(false); // Не отображать диалог с номером страницы при печати

        // Создать объекты для настроек принтера и страницы и PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Установить принтер Microsoft Soft Printer
        printerSettings.setPrinterName("Microsoft Print to PDF");

        // Установить размер страницы (если требуется)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Установить поля страницы (если требуется)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Печать документа с использованием настроек принтера и страницы
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // Закрыть PDF файл после печати
        viewer.close();
    }
```


## Печать цветного PDF в файл XPS в градациях серого

Цветной PDF-документ может быть напечатан на XPS-принтер в градациях серого с использованием [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer). Для этого необходимо использовать свойство PdfViewer.PrintAsGrayscale и установить его в *true*. 

Следующий фрагмент кода демонстрирует реализацию свойства PdfViewer.PrintAsGrayscale.

```java
 public static void PrintingPDFasGrayscale() {
        // Создать объект PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Открыть входной PDF файл
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Установить атрибуты для печати
        viewer.setAutoResize(true); // Печать файла с подогнанным размером
        viewer.setAutoRotate(true); // Печать файла с подогнанным поворотом

        viewer.setPrintAsGrayscale(true);

        // Создать объекты для настроек принтера и страницы и PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Установить принтер Microsoft Soft Printer
        printerSettings.setPrinterName("Microsoft Print to PDF");

        // Установить размер страницы (если необходимо)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Установить поля страницы (если необходимо)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Печать документа с использованием настроек принтера и страницы
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // Закрыть PDF файл после печати
        viewer.close();
    }
```


## Преобразование PDF в PostScript

Класс [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) предоставляет возможность печати PDF документов, и с помощью этого класса мы также можем конвертировать PDF файлы в формат PostScript. Чтобы преобразовать PDF файл в PostScript, сначала установите любой PS-принтер и просто распечатайте файл с помощью PdfViewer.

Следующий фрагмент кода показывает, как распечатать и конвертировать PDF в формат PostScript.

```java
public static void PrintingPDFToPostScript() {
        // Создать объект PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Открыть входной PDF файл
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Установить атрибуты для печати
        viewer.setAutoResize(true); // Печать файла с подогнанным размером
        viewer.setAutoRotate(true); // Печать файла с подогнанным поворотом

        viewer.setPrintAsGrayscale(true);
        

        // Создать объекты для настроек принтера, страницы и PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Установить PostScript принтер
        printerSettings.setPrinterName("HP Universal Printing PS (v7.0.0)");
        printerSettings.setPrintToFile(true);
        printerSettings.setPrintFileName(_dataDir+"result.ps");

        // Установить размер страницы (если необходимо)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Установить поля страницы (если необходимо)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Печать документа с использованием настроек принтера и страницы
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // Закрыть PDF файл после печати
        viewer.close();
    }
```


## Проверка статуса задания на печать

PDF файл может быть напечатан как на физическом принтере, так и с использованием Microsoft XPS Document Writer, без отображения диалога печати, с использованием класса [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer). При печати больших PDF файлов процесс может занять много времени, поэтому пользователь может не быть уверенным, завершился ли процесс печати или возникла проблема. Чтобы определить статус задания на печать, используйте свойство PrintStatus. Следующий фрагмент кода показывает, как напечатать PDF файл в файл XPS и получить статус печати.

```java
public static void CheckingPrintJobStatus() {
        // Создать объект PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Открыть входной PDF файл
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Установить атрибуты для печати
        viewer.setAutoResize(true); // Печатать файл с измененным размером
        viewer.setAutoRotate(true); // Печатать файл с измененным поворотом

        viewer.setPrintAsGrayscale(true);

        // Создать объекты для настроек принтера и страницы, а также PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Установить принтер Microsoft Soft Printer
        printerSettings.setPrinterName("HP Universal Printing PS (v7.0.0)");

        // Установить размер страницы (если требуется)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Установить поля страницы (если требуется)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Печатать документ с использованием настроек принтера и страницы
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // // Проверить статус печати
        if (viewer.getPrintStatus() != null) {
            Exception ex = (Exception) viewer.getPrintStatus();
            System.out.println(ex.getMessage());
        } else {
            // Ошибки не найдены. Задание на печать успешно завершено
            System.out.println("Все в порядке!");
        }
        // Закрыть PDF файл после печати
        viewer.close();
    }
```