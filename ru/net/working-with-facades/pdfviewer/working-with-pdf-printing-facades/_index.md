---
title: Работа с печатью PDF - Фасады
type: docs
weight: 10
url: /ru/net/working-with-pdf-printing-facades/
description: В этом разделе объясняется, как печатать PDF файлы с помощью Aspose.PDF Facades, используя класс PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

## Печать PDF файла на принтер по умолчанию с использованием настроек принтера и страницы

Сначала документ преобразуется в изображение, а затем печатается на принтере. Мы создаем экземпляр класса [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer), который позволяет печатать PDF файл на принтер по умолчанию, используя метод BindPdf для документа, и делаем определенные настройки. В нашем примере мы используем формат A4, портретную ориентацию. В printerSettings, в первую очередь, указываем имя принтера, на который мы печатаем. В противном случае он будет печатать на принтер по умолчанию. Далее указываем количество копий, которые нам нужны.

```csharp
 public static void PrintingPDFFile()
        {
            // Создать объект PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Открыть входной PDF файл
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Установить атрибуты для печати
            viewer.AutoResize = true;         // Печатать файл с подогнанным размером
            viewer.AutoRotate = true;         // Печатать файл с подогнанным поворотом
            viewer.PrintPageDialog = false;   // Не выводить диалог с номером страницы при печати

            // Создать объекты для настроек принтера и страницы и PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();
            System.Drawing.Printing.PrintDocument prtdoc = new System.Drawing.Printing.PrintDocument();

            // Установить имя принтера
            ps.PrinterName = prtdoc.PrinterSettings.PrinterName;

            // Установить размер страницы (если необходимо)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Установить поля страницы (если необходимо)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Печатать документ, используя настройки принтера и страницы
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Закрыть PDF файл после печати
            viewer.Close();
        }
```

Для отображения диалогового окна печати попробуйте использовать следующий фрагмент кода:

```csharp
        public static void PrintingPDFDisplayPrintDialog()
        {
            // Создать объект PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Открыть входной PDF файл
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Установить атрибуты для печати
            viewer.AutoResize = true;         // Печать файла с измененным размером
            viewer.AutoRotate = true;         // Печать файла с измененным поворотом

            // Создать объекты для настроек принтера, страницы и документа для печати

            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings
            {

                // Установить размер страницы (если требуется)
                PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169),

                // Установить поля страницы (если требуется)
                Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0)
            };

            System.Windows.Forms.PrintDialog printDialog = new System.Windows.Forms.PrintDialog();
            if (printDialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
            {
                // Код для печати документа здесь
                // Печать документа с использованием настроек принтера и страницы
                System.Drawing.Printing.PrinterSettings ps = printDialog.PrinterSettings;
                viewer.PrintDocumentWithSettings(pgs, ps);
            }

            // Закрыть PDF файл после печати
            viewer.Close();
        }
```

## Печать PDF на виртуальный принтер

Существуют принтеры, которые печатают в файл. Мы задаем имя виртуального принтера и, по аналогии с предыдущим примером, выполняем настройки.

```csharp
public static void PrintingPDFToSoftPrinter()
        {
            // Создаем объект PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Открываем входной PDF файл
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Устанавливаем параметры для печати
            viewer.AutoResize = true;         // Печать файла с подогнанным размером
            viewer.AutoRotate = true;         // Печать файла с подогнанным поворотом
            viewer.PrintPageDialog = false;   // Не выводить диалог номера страницы при печати

            viewer.PrintAsImage = false;

            // Создаем объекты для настроек принтера и страницы и PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Устанавливаем имя принтера
            ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
            // Или устанавливаем PDF принтер
            //ps.PrinterName = "Adobe PDF";

            // Устанавливаем размер страницы (если требуется)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Устанавливаем поля страницы (если требуется)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Печатаем документ с использованием настроек принтера и страницы
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Закрываем PDF файл после печати
            viewer.Close();
        }
```

## Скрытие диалогового окна печати

Aspose.PDF для .NET позволяет скрыть диалоговое окно печати. Для этого используйте метод [PrintPageDialog](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/properties/printpagedialog).

Следующий фрагмент кода показывает, как скрыть диалоговое окно печати.

```csharp
public static void PrintingPDFHidePrintDialog()
        {
            // Создать объект PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Открыть входной PDF файл
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Установить атрибуты для печати
            viewer.AutoResize = true;         // Печатать файл с подогнанным размером
            viewer.AutoRotate = true;         // Печатать файл с подогнанным вращением

            viewer.PrintPageDialog = false;   // Не показывать диалоговое окно с номером страницы при печати

            // Создать объекты для настроек принтера и страницы и PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Установить имя принтера XPS/PDF
            ps.PrinterName = "OneNote for Windows 10";

            // Установить размер страницы (если требуется)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Установить поля страницы (если требуется)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Печатать документ, используя настройки принтера и страницы
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Закрыть PDF файл после печати
            viewer.Close();
        }
```

## Печать цветного PDF в файл XPS в оттенках серого

Цветной PDF-документ можно напечатать на XPS-принтере в оттенках серого, используя [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer). Для этого нужно использовать свойство PdfViewer.PrintAsGrayscale и установить его в *true*. Следующий фрагмент кода демонстрирует реализацию свойства PdfViewer.PrintAsGrayscale.

```csharp
public static void PrintingPDFasGrayscale()
        {
            // Создать объект PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Открыть входной PDF файл
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Установить атрибуты для печати
            viewer.AutoResize = true;         // Печать файла с подогнанным размером
            viewer.AutoRotate = true;         // Печать файла с подогнанным поворотом

            viewer.PrintPageDialog = false;   // Не выводить диалоговое окно с номером страницы при печати
            viewer.PrintAsGrayscale = false;

            // Создать объекты для настроек принтера и страницы и PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Установить имя XPS/PDF принтера
            ps.PrinterName = "OneNote for Windows 10";

            // Установить размер страницы (если требуется)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Установить поля страницы (если требуется)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Напечатать документ, используя настройки принтера и страницы
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Закрыть PDF файл после печати
            viewer.Close();
        }
```

## PDF to PostScript conversion

Класс [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) предоставляет возможность печати PDF документов, и с помощью этого класса мы также можем конвертировать PDF файлы в формат PostScript. Чтобы преобразовать PDF файл в PostScript, сначала установите любой PS принтер и просто распечатайте файл с помощью PdfViewer.

Следующий фрагмент кода показывает, как распечатать и конвертировать PDF в формат PostScript.

```csharp
public static void PrintingPDFToPostScript()
        {
            // Создать объект PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Открыть входной PDF файл
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Установить атрибуты для печати
            viewer.AutoResize = true;         // Печать файла с измененным размером
            viewer.AutoRotate = true;         // Печать файла с измененным поворотом
            viewer.PrintPageDialog = false;   // Не отображать диалог номера страницы при печати

            viewer.PrintAsImage = false;

            // Создать объекты для настроек принтера и страницы и PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Установить имя XPS/PDF принтера
            ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
            // Установить имя выходного файла и атрибут PrintToFile
            ps.PrintFileName = _dataDir + "PdfToPostScript_out.ps";
            ps.PrintToFile = true;

            // Установить размер страницы (если необходимо)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Установить поля страницы (если необходимо)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Печать документа с использованием настроек принтера и страницы
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Закрыть PDF файл после печати
            viewer.Close();
        }
```

## Проверка статуса задания на печать

PDF-файл может быть распечатан на физическом принтере, а также с помощью Microsoft XPS Document Writer, без отображения диалога печати, с использованием класса [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer). При печати больших PDF-файлов процесс может занять много времени, поэтому пользователь может не быть уверен в том, завершился ли процесс печати или возникла проблема. Чтобы определить статус задания на печать, используйте свойство PrintStatus. Следующий фрагмент кода показывает, как распечатать PDF-файл в XPS-файл и получить статус печати.

```csharp
public static void CheckingPrintJobStatus()
        {
            // Создать объект PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Открыть входной PDF-файл
            viewer.BindPdf(_dataDir + "sample1.pdf");

            // Установить атрибуты для печати
            viewer.AutoResize = true;         // Печать файла с настроенным размером
            viewer.AutoRotate = true;         // Печать файла с настроенной ориентацией
            viewer.PrintPageDialog = false;   // Не отображать диалог номера страницы при печати

            viewer.PrintAsImage = false;

            // Создать объекты для настроек принтера и страницы и PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Установить имя принтера XPS/PDF
            ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
            // Установить имя выходного файла и атрибут PrintToFile
            ps.PrintFileName = _dataDir + "PdfToPostScript_out.ps";
            ps.PrintToFile = true;

            // Установить размер страницы (если необходимо)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Установить поля страницы (если необходимо)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Печать документа с использованием настроек принтера и страницы
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Проверить статус печати
            if (viewer.PrintStatus != null && viewer.PrintStatus is Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            else
            {
                // Ошибок не найдено. Задание на печать выполнено успешно
                Console.WriteLine("Печать завершена без проблем..");
            }

            // Закрыть PDF-файл после печати
            viewer.Close();
        }

        struct PrintingJobSettings
        {
            public int ToPage { get; set; }
            public int FromPage { get; set; }
            public string OutputFile { get; set; }
            public System.Drawing.Printing.Duplex Mode { get; set; }
        }
```

## Печать страниц в режимах Simplex и Duplex

В конкретной задаче печати страницы PDF документа могут быть напечатаны либо в режиме Duplex, либо в режиме Simplex, но вы не можете печатать одни страницы как simplex, а другие как duplex в рамках одной печатной задачи. Тем не менее, для выполнения этого требования можно использовать разные диапазоны страниц и объект PrintingJobSettings. Следующий фрагмент кода показывает, как напечатать некоторые страницы PDF файла в режиме Simplex, а некоторые страницы в режиме Duplex.

```csharp
 public static void PrintingPagesInSimplexAndDuplexMode()
        {
            int printingJobIndex = 0;
            string inPdf = _dataDir + "sample-8page.pdf";
            string output = _dataDir;
            IList<PrintingJobSettings> printingJobs = new List<PrintingJobSettings>();

            PrintingJobSettings printingJob1 = new PrintingJobSettings
            {
                FromPage = 1,
                ToPage = 3,
                OutputFile = output + "sample_1_3.xps",
                Mode = Duplex.Default
            };

            printingJobs.Add(printingJob1);

            PrintingJobSettings printingJob2 = new PrintingJobSettings
            {
                FromPage = 4,
                ToPage = 6,
                OutputFile = output + "sample_4_6.xps",
                Mode = Duplex.Simplex
            };

            printingJobs.Add(printingJob2);

            PrintingJobSettings printingJob3 = new PrintingJobSettings
            {
                FromPage = 7,
                ToPage = 7,
                OutputFile = output + "sample_7.xps",
                Mode = Duplex.Default
            };

            printingJobs.Add(printingJob3);

            PdfViewer viewer = new PdfViewer();

            viewer.BindPdf(inPdf);
            viewer.AutoResize = true;
            viewer.AutoRotate = true;
            viewer.PrintPageDialog = false;

            PrinterSettings ps = new PrinterSettings();
            PageSettings pgs = new PageSettings();

            ps.PrinterName = "Microsoft XPS Document Writer";
            ps.PrintFileName = System.IO.Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
            ps.PrintToFile = true;
            ps.FromPage = printingJobs[printingJobIndex].FromPage;
            ps.ToPage = printingJobs[printingJobIndex].ToPage;
            ps.Duplex = printingJobs[printingJobIndex].Mode;
            ps.PrintRange = PrintRange.SomePages;

            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);
            ps.DefaultPageSettings.PaperSize = pgs.PaperSize;
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            viewer.EndPrint += (sender, args) =>
            {
                if (++printingJobIndex < printingJobs.Count)
                {
                    ps.PrintFileName = System.IO.Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
                    ps.FromPage = printingJobs[printingJobIndex].FromPage;
                    ps.ToPage = printingJobs[printingJobIndex].ToPage;
                    ps.Duplex = printingJobs[printingJobIndex].Mode;
                    viewer.PrintDocumentWithSettings(pgs, ps);
                }
            };

            viewer.PrintDocumentWithSettings(pgs, ps);
        }
```