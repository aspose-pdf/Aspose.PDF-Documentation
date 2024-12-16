---
title: Конвертация PDF в PostScript
linktitle: Конвертация PDF в PostScript
type: docs
weight: 30
url: /ru/net/pdf-to-postscript-conversion/
description: У нас есть решение для конвертации PDF в PostScript. Используйте для этой задачи печать и класс PdfViewer.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Конвертация PDF в PostScript",
    "alternativeHeadline": "Конвертация PDF в PostScript",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF документов",
    "keywords": "pdf, c#, pdf to postscript",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
    "publisher": {
        "@type": "Organization",
        "name": "Команда документации Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/pdf-to-postscript-conversion/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-to-postscript-conversion/"
    },
    "dateModified": "2022-02-04",
    "description": "У нас есть решение для конвертации PDF в PostScript. Используйте для этой задачи печать и класс PdfViewer."
}
</script>
Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## **Преобразование PDF в Postscript на C#**

Класс PdfViewer предоставляет возможность печати документов PDF, и с помощью этого класса мы также можем конвертировать файлы PDF в формат PostScript. Для преобразования файла PDF в PostScript сначала установите любой PS принтер и просто напечатайте файл с помощью PdfViewer. Вы можете следовать инструкциям, указанным Университетом Гавайев о том, как установить PS принтер. Следующий фрагмент кода показывает, как печатать и конвертировать PDF в формат PostScript.

```csharp
public static void PrintToPostscriptFile()
{
    // Путь к директории документов.
    // string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    Aspose.Pdf.Facades.PdfViewer viewer = new Aspose.Pdf.Facades.PdfViewer();
    viewer.BindPdf(_dataDir + "input.pdf");
    // Установка настроек принтера и настроек страницы
    System.Drawing.Printing.PrinterSettings printerSettings = new System.Drawing.Printing.PrinterSettings();
    printerSettings.Copies = 1;
    // Установка PS принтера, этот драйвер можно найти в списке предустановленных драйверов принтера в Windows
    printerSettings.PrinterName = "HP LaserJet 2300 Series PS";
    // Установка имени выходного файла и атрибута PrintToFile
    printerSettings.PrintFileName = _dataDir + "PdfToPostScript_out.ps";
    printerSettings.PrintToFile = true;
    // Отключение диалога печати страницы
    viewer.PrintPageDialog = false;
    // Передача объекта настроек принтера в метод
    viewer.PrintDocumentWithSettings(printerSettings);
    viewer.Close();
}
```
## Проверка статуса задания печати

PDF-файл может быть напечатан на физическом принтере, а также на Microsoft XPS Document Writer, без отображения диалога печати, с использованием класса PdfViewer. При печати больших PDF-файлов процесс может занять много времени, поэтому пользователь может не быть уверен, завершился ли процесс печати или возникла проблема. Для определения статуса задания печати используйте свойство PrintStatus. Следующий фрагмент кода показывает, как напечатать PDF-файл в XPS-файл и получить статус печати.

```csharp
public static void CheckingPrintJobStatus()
{
    // Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
    // Путь к директории с документами.
    // string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Создание объекта PdfViewer
    PdfViewer viewer = new PdfViewer();

    // Привязка исходного PDF файла
    viewer.BindPdf(_dataDir + "input.pdf");
    viewer.AutoResize = true;

    // Скрытие диалога печати
    viewer.PrintPageDialog = false;

    // Создание объекта настроек принтера
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

    // Указание имени принтера
    ps.PrinterName = "Microsoft XPS Document Writer";

    // Имя результирующего файла печати
    ps.PrintFileName = "ResultantPrintout.xps";

    // Печать вывода в файл
    ps.PrintToFile = true;
    ps.FromPage = 1;
    ps.ToPage = 2;
    ps.PrintRange = System.Drawing.Printing.PrintRange.SomePages;

    // Указание размера страницы печати
    pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);
    ps.DefaultPageSettings.PaperSize = pgs.PaperSize;
    pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

    // Печать документа с указанными выше настройками
    viewer.PrintDocumentWithSettings(pgs, ps);

    // Проверка статуса печати
    if (viewer.PrintStatus != null)
    {
        // Было выброшено исключение
        if (viewer.PrintStatus is Exception ex)
        {
            // Получение сообщения исключения
            Console.WriteLine(ex.Message);
        }
    }
    else
    {
        // Ошибок не найдено. Задание печати успешно завершено
        Console.WriteLine("printing completed without any issue..");
    }
}
```
## Получение/установка имени владельца задания печати

Недавно мы получили требование получить/установить имя владельца задания печати (фактического пользователя, который нажал кнопку печати на веб-странице). Эта информация требуется при печати файла PDF. Для выполнения этого требования вы можете использовать свойство с именем PrinterJobName:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();
PdfViewer viewer = new PdfViewer();
// Привязка исходного PDF файла
viewer.BindPdf(dataDir + "input.pdf");
// Указание имени задания печати
viewer.PrinterJobName = GetCurrentUserCredentials();
```

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static string GetCurrentUserCredentials()
{
    // Реализация зависит от типа выполняемого приложения (ASP.NET, Windows forms и т.д.)
    string userCredentials = string.Empty;
    return userCredentials;
}
```
## Использование Имперсонации

Другой подход к получению имени владельца задания печати заключается в использовании имперсонации (выполнение процедур печати от имени другого пользователя) или пользователь может напрямую изменить имя владельца, используя процедуру SetJob.

Обратите внимание, что нет возможности установить значение владельца с помощью API печати Aspose.PDF по соображениям безопасности. Свойство PrinterJobName может использоваться для установки значения столбца имени документа в приложении печати спулера. Приведенный выше фрагмент кода показывает, как пользователь может включить имя пользователя в столбец имени документа (например, используя синтаксис UserName\documentName). Но установка столбцов владельца может быть реализована следующими способами напрямую пользователем:

1) Имперсонация. Поскольку значение столбца владельца содержит значение пользователя, который запускает код печати, есть способ вызвать API печати Aspose.PDF в контексте другого пользователя. Например, посмотрите на решение, описанное здесь. Используя этот класс, пользователь может достичь цели:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();
PdfViewer viewer = new PdfViewer();
viewer.BindPdf(dataDir + "input.pdf");
viewer.PrintPageDialog = false;
// Не выводить диалоговое окно номера страницы при печати
using (new Impersonator("OwnerUserName", "SomeDomain", "OwnerUserNamePassword"))
{
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    ps.PrinterName = "Microsoft XPS Document Writer";
    viewer.PrintDocumentWithSettings(ps); // OwnerUserName является значением столбца Owner в приложении спулера
    viewer.Close();
}
```
2) Использование API спулера и функции SetJob

Следующий фрагмент кода показывает, как напечатать некоторые страницы PDF-файла в режиме Simplex и некоторые страницы в режиме Duplex.

```csharp
struct PrintingJobSettings
{
    public int ToPage { get; set; }
    public int FromPage { get; set; }
    public string OutputFile { get; set; }
    public System.Drawing.Printing.Duplex Mode { get; set; }
}
```

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

int printingJobIndex = 0;
string inPdf = dataDir + "input.pdf";
string output = dataDir;
IList<PrintingJobSettings> printingJobs = new List<PrintingJobSettings>();

PrintingJobSettings printingJob1 = new PrintingJobSettings();
printingJob1.FromPage = 1;
printingJob1.ToPage = 3;
printingJob1.OutputFile = output + "35925_1_3.xps";
printingJob1.Mode = Duplex.Default;

printingJobs.Add(printingJob1);

PrintingJobSettings printingJob2 = new PrintingJobSettings();
printingJob2.FromPage = 4;
printingJob2.ToPage = 6;
printingJob2.OutputFile = output + "35925_4_6.xps";
printingJob2.Mode = Duplex.Simplex;

printingJobs.Add(printingJob2);

PrintingJobSettings printingJob3 = new PrintingJobSettings();
printingJob3.FromPage = 7;
printingJob3.ToPage = 7;
printingJob3.OutputFile = output + "35925_7.xps";
printingJob3.Mode = Duplex.Default;

printingJobs.Add(printingJob3);

PdfViewer viewer = new PdfViewer();

viewer.BindPdf(inPdf);
viewer.AutoResize = true;
viewer.AutoRotate = true;
viewer.PrintPageDialog = false;

PrinterSettings ps = new PrinterSettings();
PageSettings pgs = new PageSettings();

ps.PrinterName = "Microsoft XPS Document Writer";
ps.PrintFileName = Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
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
        ps.PrintFileName = Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
        ps.FromPage = printingJobs[printingJobIndex].FromPage;
        ps.ToPage = printingJobs[printingJobIndex].ToPage;
        ps.Duplex = printingJobs[printingJobIndex].Mode;
        viewer.PrintDocumentWithSettings(pgs, ps);
    }
};

viewer.PrintDocumentWithSettings(pgs, ps);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Библиотека Aspose.PDF для .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "продажи",
                "areaServed": "US",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "GB",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "AU",
                "availableLanguage": "английский"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Библиотека для манипуляции PDF для .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

