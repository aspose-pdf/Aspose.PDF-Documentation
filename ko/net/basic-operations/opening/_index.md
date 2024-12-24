---
title: 프로그래밍적으로 PDF 문서 열기
linktitle: PDF 열기
type: docs
weight: 20
url: /ko/net/open-pdf-document/
description: C# Aspose.PDF for .NET PDF 라이브러리를 사용하여 PDF 파일을 여는 방법을 알아보세요. 기존 PDF, 스트림에서의 문서, 암호화된 PDF 문서를 열 수 있습니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리에서도 작동합니다.

## 기존 PDF 문서 열기

문서를 열 수 있는 몇 가지 방법이 있습니다. 가장 쉬운 방법은 파일 이름을 지정하는 것입니다.

```csharp
public static void OpenDocument()
{
    var fileName = @"C:\tmp\tourguidev2_gb_tags.pdf";
    using (var pdfDocument = new Aspose.Pdf.Document(fileName))
    {
        Console.WriteLine($"페이지 수 {pdfDocument.Pages.Count}");
    }
}
```

## 스트림에서 기존 PDF 문서 열기

```csharp
public static void OpenDocumentStream()
{
    const string fileName = "SJPR0033_Folder_Utland_16sid_ENG_web3.pdf";
    var remoteUri = "https://www.sj.se/content/dam/SJ/pdf/Engelska/";
    // 새 WebClient 인스턴스를 생성합니다.
    var webClient = new WebClient();
    // 도메인과 웹 리소스 파일 이름을 연결합니다.
    var strWebResource = remoteUri + fileName;
    Console.WriteLine("파일 \"{0}\"을(를) \"{1}\"에서 다운로드 중 .......\n\n", fileName, strWebResource);

    var stream = new MemoryStream();
    webClient.OpenRead(strWebResource)?.CopyTo(stream);

    using (var pdfDocument = new Aspose.Pdf.Document(stream))
    {
        Console.WriteLine($"페이지 수 {pdfDocument.Pages.Count}");
    }
}
```
## 암호화된 PDF 문서 열기

```csharp
    public static void OpenDocumentWithPassword()
    {
        const string fileName = @"C:\tmp\DocSite.pdf";
        const string password = "Aspose2020";
        try
        {
            using (var pdfDocument = new Aspose.Pdf.Document(fileName, password))
            {
                Console.WriteLine($"Pages {pdfDocument.Pages.Count}");
            }
        }
        catch (InvalidPasswordException e)
        {
            Console.WriteLine(e);
        }
    }
```
