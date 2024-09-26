---
title: PDF에서 PostScript로 변환
linktitle: PDF에서 PostScript로 변환
type: docs
weight: 30
url: /net/pdf-to-postscript-conversion/
keywords: "pdf to postscript c#"
description: PDF에서 PostScript로 변환하는 솔루션을 제공합니다. 이 작업을 위해 인쇄 및 PdfViewer 클래스를 사용하세요.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF에서 PostScript로 변환",
    "alternativeHeadline": "PDF를 PostScript로 변환",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "pdf, c#, pdf to postscript",
    "wordcount": "302",
    "proficiencyLevel":"초보자",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "description": "PDF에서 PostScript로 변환하는 솔루션을 제공합니다. 이 작업을 위해 인쇄 및 PdfViewer 클래스를 사용하세요."
}
</script>
다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

## **C#에서 PDF를 Postscript로 변환**

PdfViewer 클래스는 PDF 문서를 인쇄하는 기능을 제공하며 이 클래스를 사용하여 PDF 파일을 PostScript 형식으로 변환할 수 있습니다. PDF 파일을 PostScript로 변환하려면 먼저 PS 프린터를 설치하고 PdfViewer를 사용하여 파일로 인쇄하십시오. 하와이 대학의 지침에 따라 PS 프린터를 설치하는 방법을 따를 수 있습니다. 다음 코드 조각은 PDF를 PostScript 형식으로 인쇄하고 변환하는 방법을 보여줍니다.

```csharp
public static void PrintToPostscriptFile()
{
    // 문서 디렉토리의 경로입니다.
    // string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    Aspose.Pdf.Facades.PdfViewer viewer = new Aspose.Pdf.Facades.PdfViewer();
    viewer.BindPdf(_dataDir + "input.pdf");
    // PrinterSettings 및 PageSettings 설정
    System.Drawing.Printing.PrinterSettings printerSettings = new System.Drawing.Printing.PrinterSettings();
    printerSettings.Copies = 1;
    // PS 프린터 설정, Windows에 사전 설치된 프린터 드라이버 목록에서 이 드라이버를 찾을 수 있습니다
    printerSettings.PrinterName = "HP LaserJet 2300 Series PS";
    // 출력 파일 이름 및 PrintToFile 속성 설정
    printerSettings.PrintFileName = _dataDir + "PdfToPostScript_out.ps";
    printerSettings.PrintToFile = true;
    // 인쇄 페이지 대화 상자 비활성화
    viewer.PrintPageDialog = false;
    // 메소드에 프린터 설정 객체 전달
    viewer.PrintDocumentWithSettings(printerSettings);
    viewer.Close();
}
```
## 인쇄 작업 상태 확인

PDF 파일은 물리적 프린터뿐만 아니라 Microsoft XPS Document Writer에도 인쇄 대화 상자를 표시하지 않고 PdfViewer 클래스를 사용하여 인쇄할 수 있습니다. 큰 PDF 파일을 인쇄할 때 프로세스가 오래 걸릴 수 있으므로 사용자는 인쇄 프로세스가 완료되었는지 또는 문제가 발생했는지 확실하지 않을 수 있습니다. 인쇄 작업의 상태를 확인하려면 PrintStatus 속성을 사용하십시오. 다음 코드 조각은 PDF 파일을 XPS 파일로 인쇄하고 인쇄 상태를 얻는 방법을 보여줍니다.

```csharp
public static void CheckingPrintJobStatus()
{
    // 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.Pdf-for-.NET에서 확인하세요.
    // 문서 디렉토리 경로입니다.
    // string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // PdfViewer 객체 인스턴스화
    PdfViewer viewer = new PdfViewer();

    // 소스 PDF 파일 바인딩
    viewer.BindPdf(_dataDir + "input.pdf");
    viewer.AutoResize = true;

    // 인쇄 대화 상자 숨기기
    viewer.PrintPageDialog = false;

    // 프린터 설정 객체 생성
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

    // 프린터 이름 지정
    ps.PrinterName = "Microsoft XPS Document Writer";

    // 결과 출력물 이름
    ps.PrintFileName = "ResultantPrintout.xps";

    // 파일로 출력 인쇄
    ps.PrintToFile = true;
    ps.FromPage = 1;
    ps.ToPage = 2;
    ps.PrintRange = System.Drawing.Printing.PrintRange.SomePages;

    // 인쇄물의 페이지 크기 지정
    pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);
    ps.DefaultPageSettings.PaperSize = pgs.PaperSize;
    pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

    // 위에서 지정한 설정으로 문서 인쇄
    viewer.PrintDocumentWithSettings(pgs, ps);

    // 인쇄 상태 확인
    if (viewer.PrintStatus != null)
    {
        // 예외가 발생했습니다
        if (viewer.PrintStatus is Exception ex)
        {
            // 예외 메시지 가져오기
            Console.WriteLine(ex.Message);
        }
    }
    else
    {
        // 오류가 없습니다. 인쇄 작업이 성공적으로 완료되었습니다
        Console.WriteLine("printing completed without any issue..");
    }
}
```
## 인쇄 작업 소유자 이름 가져오기/설정하기

최근에 웹 페이지에서 인쇄 버튼을 누른 실제 사용자인 인쇄 작업 소유자 이름을 가져오고 설정해야 하는 요구사항을 받았습니다. 이 정보는 PDF 파일을 인쇄할 때 필요합니다. 이 요구사항을 충족하기 위해 PrinterJobName이라는 속성을 사용할 수 있습니다:

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.Pdf-for-.NET 에서 확인할 수 있습니다.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();
PdfViewer viewer = new PdfViewer();
// 소스 PDF 파일 바인딩
viewer.BindPdf(dataDir + "input.pdf");
// 인쇄 작업의 이름 지정
viewer.PrinterJobName = GetCurrentUserCredentials();
```

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.Pdf-for-.NET 에서 확인할 수 있습니다.
private static string GetCurrentUserCredentials()
{
    // 구현은 실행 중인 애플리케이션 유형(ASP.NET, Windows Forms 등)에 따라 다릅니다.
    string userCredentials = string.Empty;
    return userCredentials;
}
```
## 위장 사용하기

프린트 작업 소유자 이름을 가져오는 또 다른 방법은 위장(다른 사용자 컨텍스트에서 인쇄 루틴 실행)을 사용하거나 사용자가 SetJob 루틴을 사용하여 소유자 이름을 직접 변경하는 것입니다.

Aspose.PDF 인쇄 API를 사용하여 보안 고려 사항으로 소유자 값을 설정할 수 없다는 점에 유의하십시오. PrinterJobName 속성은 스풀러 인쇄 응용 프로그램의 문서 이름 열 값 설정에 사용될 수 있습니다. 위에 공유된 코드 스니펫은 사용자가 문서 이름 열에 사용자 이름을 어떻게 포함시킬 수 있는지를 보여줍니다(예를 들어 UserName\documentName 구문 사용). 그러나 소유자 열의 설정은 사용자에 의해 다음 방법으로 직접 구현될 수 있습니다:

1) 위장. 소유자 열 값은 인쇄 코드를 실행하는 사용자의 값을 포함하므로 다른 사용자 컨텍스트 내에서 Aspose.PDF 인쇄 API를 호출할 방법이 있습니다. 예를 들어 여기에 설명된 솔루션을 살펴보십시오. 이 클래스를 사용하여 사용자는 목표를 달성할 수 있습니다:

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.Pdf-for-.NET 에서 확인하십시오.
// 문서 디렉토리로의 경로.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();
PdfViewer viewer = new PdfViewer();
viewer.BindPdf( dataDir + "input.pdf");
viewer.PrintPageDialog = false;
// 인쇄 시 페이지 번호 대화 상자를 생성하지 않습니다
using (new Impersonator("OwnerUserName", "SomeDomain", "OwnerUserNamePassword"))
{
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    ps.PrinterName = "Microsoft XPS Document Writer";
    viewer.PrintDocumentWithSettings(ps); // OwnerUserName은 스풀러 앱의 소유자 열의 값입니다
    viewer.Close();
}
```
2) Spooler API 및 SetJob 루틴 사용하기

다음 코드 스니펫은 PDF 파일의 일부 페이지를 Simplex 모드와 Duplex 모드로 인쇄하는 방법을 보여줍니다.

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
// 전체 예제와 데이터 파일은 다음에서 확인하십시오: https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// 문서 디렉토리 경로
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
    "name": "Aspose.PDF for .NET Library",
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
                "contactType": "영업",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "영업",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "영업",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": ".NET용 PDF 조작 라이브러리",
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

