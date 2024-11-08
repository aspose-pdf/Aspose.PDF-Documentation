---
title: .NET Core에서 PDF 파일 출력 방법
linktitle: .NET Core에서 PDF 출력
type: docs
weight: 40
url: /ko/net/print-dotnetcore/
keywords: "print pdf .net core"
description: 이 페이지에서는 .NET Core에서 PDF 문서를 XPS로 변환하고 로컬 프린터의 대기열에 작업으로 추가하는 방법에 대해 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": ".NET Core에서 PDF 파일 출력 방법",
    "alternativeHeadline": ".NET Core에서 PDF 파일 출력",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, .NET Core에서 pdf",
    "wordcount": "302",
    "proficiencyLevel":"초보자",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF 문서 팀",
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
    "url": "/net/print-dotnetcore/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/print-dotnetcore/"
    },
    "dateModified": "2022-02-04",
    "description": ".NET Core에서 PDF 문서를 XPS로 변환하고 로컬 프린터의 대기열에 작업으로 추가하는 방법을 설명하는 페이지입니다."
}
</script>
다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## **.NET Core에서 Pdf 문서 인쇄**

Aspose.PDF 라이브러리를 사용하면 PDF 파일을 XPS로 변환할 수 있습니다. 이 기능은 문서 인쇄를 조직하는 데 유용할 수 있습니다. 기본 프린터를 사용하는 예를 살펴보겠습니다:

```csharp
class Program
{
    static void Main()
    {
        // 생성자의 ThreadStart 대리자 매개변수에 인쇄 메서드를 전달하여 보조 스레드를 생성합니다.
        Thread printingThread = new Thread(() => PrintPDF(@"C:\tmp\doc-pdf.pdf"));

        // PrintQueue.AddJob을 사용하는 스레드를 단일 스레딩으로 설정합니다.
        printingThread.SetApartmentState(ApartmentState.STA);

        // 인쇄 스레드를 시작합니다. Thread 생성자에 전달된 메서드가 실행됩니다.
        printingThread.Start();
    }//end Main

    private static void PrintPDF(string pdfFileName)
    {
        // 프린트 서버와 프린트 큐를 생성합니다.
        PrintQueue defaultPrintQueue = LocalPrintServer.GetDefaultPrintQueue();

        Aspose.Pdf.Document document = new Document(pdfFileName);
        var xpsFileName = pdfFileName.Replace(".pdf", ".xps");
        document.Save(xpsFileName,SaveFormat.Xps);

        try
        {
            // XPS 검증 및 진행 상황 알림을 제공하면서 Xps 파일을 인쇄합니다.
            PrintSystemJobInfo xpsPrintJob = defaultPrintQueue.AddJob(xpsFileName, xpsFileName, false);
            Console.WriteLine(xpsPrintJob.JobIdentifier);
        }
        catch (PrintJobException e)
        {
            Console.WriteLine("\n\t{0}을(를) 인쇄 큐에 추가할 수 없습니다.", pdfFileName);
            if (e.InnerException != null && e.InnerException.Message == "File contains corrupted data.")
            {
                Console.WriteLine("\t유효한 XPS 파일이 아닙니다. 이를 디버그하려면 isXPS Conformance Tool을 사용하세요.");
            }
            Console.WriteLine("\t다음 XPS 파일로 계속합니다.\n");
        }
    }
}//end Program class
```
이 예에서는 PDF 문서를 XPS로 변환하고 로컬 프린터의 대기열에 작업으로 추가합니다.

