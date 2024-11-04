---
title: C#을 사용하여 PDF 생성하기
linktitle: PDF 문서 생성
type: docs
weight: 10
url: /net/create-pdf-document/
description: Aspose.PDF for .NET을 이용하여 PDF 문서를 생성하고 형식을 지정합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#을 사용하여 PDF 생성하기",
    "alternativeHeadline": "처음부터 PDF 문서 생성",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "pdf, dotnet, create pdf document",
    "wordcount": "302",
    "proficiencyLevel":"초급",
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
    "url": "/net/create-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET을 이용하여 PDF 문서를 생성하고 형식을 지정합니다."
}
</script>
우리는 항상 C# 프로젝트에서 PDF 문서를 생성하고 이를 더 정확하고 효과적으로 다루는 방법을 찾고 있습니다. 라이브러리의 쉽게 사용할 수 있는 기능을 사용하면 작업 추적을 더 많이 하고 PDF 생성의 시간이 많이 걸리는 세부 사항에 대해 덜 신경 쓸 수 있습니다. .NET에서든 그렇습니다.

다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

## C# 언어를 사용하여 PDF 문서 생성(또는 생성)

Aspose.PDF for .NET API는 C# 및 VB.NET을 사용하여 PDF 파일을 생성하고 읽을 수 있습니다. 이 API는 WinForms, ASP.NET 및 기타 여러 .NET 애플리케이션에서 사용할 수 있습니다. 이 문서에서는 Aspose.PDF for .NET API를 사용하여 .NET 애플리케이션에서 PDF 파일을 쉽게 생성하고 읽는 방법을 보여줍니다.

### 간단한 PDF 파일 생성 방법

C#을 사용하여 PDF 파일을 생성하려면 다음 단계를 사용할 수 있습니다.

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스의 객체를 생성합니다
1.
1.
1. [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) 를 페이지의 [Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) 컬렉션에 추가하세요.
1. 결과 PDF 문서를 저장하세요.

```csharp
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

// 문서 객체 초기화
Document document = new Document();
// 페이지 추가
Page page = document.Pages.Add();
// 새 페이지에 텍스트 추가
page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
// 업데이트된 PDF 저장
document.Save(dataDir + "HelloWorld_out.pdf");
```

### 검색 가능한 PDF 문서 만들기

Aspose.PDF for .NET은 PDF 문서를 생성하고 기존 문서를 조작하는 기능을 제공합니다.
Aspose.PDF for .NET은 PDF 문서를 생성하고 기존 PDF 문서를 조작하는 기능을 제공합니다.

아래에 명시된 로직은 PDF 이미지의 텍스트를 인식합니다. 인식을 위해 외부 OCR이 HOCR 표준을 지원해야 합니다. 테스트 목적으로 우리는 무료 Google tesseract OCR을 사용했습니다. 따라서 먼저 시스템에 Tesseract-OCR을 설치해야 하며, 그러면 tesseract 콘솔 응용 프로그램을 사용할 수 있습니다.

다음은 이 요구 사항을 완료하는 완전한 코드입니다:

```csharp
using System;

namespace Aspose.Pdf.Examples.Advanced.WorkingWithDocuments
{
    class ExampleCreateDocument
    {
        private const string _dataDir = "C:\\Samples";
        public static void CreateSearchableDocuments(string file)
        {
            Aspose.Pdf.Document doc = new Aspose.Pdf.Document(file);
            bool convertResult = false;
            try
            {
                convertResult = doc.Convert(CallBackGetHocr);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            doc.Save(file);
            doc.Dispose();
        }

        static string CallBackGetHocr(System.Drawing.Image img)
        {
            string tmpFile = System.IO.Path.GetTempFileName();
            try
            {
                System.Drawing.Bitmap bmp = new System.Drawing.Bitmap(img);

                bmp.Save(tmpFile, System.Drawing.Imaging.ImageFormat.Bmp);
                string inputFile = string.Concat('"', tmpFile, '"');
                string outputFile = string.Concat('"', tmpFile, '"');
                string arguments = string.Concat(inputFile, " ", outputFile, " -l eng hocr");
                string tesseractProcessName = @"C:\Program Files\Tesseract-OCR\Tesseract.exe";

                System.Diagnostics.ProcessStartInfo psi =
                    new System.Diagnostics.ProcessStartInfo(tesseractProcessName, arguments)
                    {
                        UseShellExecute = true,
                        CreateNoWindow = true,
                        WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden,
                        WorkingDirectory = System.IO.Path.GetDirectoryName(tesseractProcessName)
                    };

                System.Diagnostics.Process p = new System.Diagnostics.Process
                {
                    StartInfo = psi
                };
                p.Start();
                p.WaitForExit();

                System.IO.StreamReader streamReader = new System.IO.StreamReader(tmpFile + ".hocr");
                string text = streamReader.ReadToEnd();
                streamReader.Close();

                return text;
            }
            finally
            {
                if (System.IO.File.Exists(tmpFile))
                    System.IO.File.Delete(tmpFile);
                if (System.IO.File.Exists(tmpFile + ".hocr"))
                    System.IO.File.Delete(tmpFile + ".hocr");
            }
        }
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET 라이브러리",
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

