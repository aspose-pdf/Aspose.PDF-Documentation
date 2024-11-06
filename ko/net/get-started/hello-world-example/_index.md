---
title: C# 언어를 사용한 Hello World 예제
linktitle: Hello World 예제
type: docs
weight: 40
url: ko/net/hello-world-example/
description: 이 샘플은 Aspose.PDF를 사용하여 간단한 PDF 문서와 Hello World 텍스트를 생성하는 방법을 보여줍니다.
aliases:
    - /net/hello-world/
lastmod: "2022-02-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C# 언어를 사용한 Hello World 예제",
    "alternativeHeadline": "Aspose.PDF C# 예제",
    "author": {
        "@type": "Person",
        "givenName": "안드리",
        "familyName": "안드루호프스키",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "pdf, c#, 문서 생성",
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
    "url": "http://docs.aspose.com/pdf/net/hello-world-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "http://docs.aspose.com/pdf/net/hello-world-example/"
    },
    "dateModified": "2022-02-04",
    "description": "이 샘플은 Aspose.PDF를 사용하여 간단한 PDF 문서와 Hello World 텍스트를 생성하는 방법을 보여줍니다.",
    "articleBody": "프로그래밍 언어나 소프트웨어의 기능을 소개하는 데 전통적으로 사용되는 \"Hello World\" 예제입니다.\n.NET 응용 프로그램에서 PDF 문서 생성, 조작 및 변환 기능을 포함할 수 있도록 해주는 기능이 풍부한 PDF API인 Aspose.PDF for .NET을 사용하고 있습니다. PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX 및 이미지 파일 포맷을 지원합니다. 본 기사에서는 \"Hello World!\" 텍스트를 포함하는 PDF 문서를 생성합니다. Aspose.PDF for .NET을 환경에 설치한 후, 아래 코드 샘플을 실행하여 Aspose.PDF API의 작동 방식을 확인할 수 있습니다.\n아래 코드 스니펫은 다음과 같은 단계를 따릅니다:\n1. Document 객체를 인스턴스화합니다\n2. 문서 객체에 페이지를 추가합니다\n3. TextFragment를 생성합니다\n4. 페이지의 Paragraph 컬렉션에 TextFragment를 추가합니다\n5. 결과 PDF 문서를 저장합니다\n다음 코드 스니펫은 Aspose.PDF for .NET API의 작동을 보여주는 Hello World 프로그램입니다."
}
</script>
"Hello World" 예제는 전통적으로 프로그래밍 언어나 소프트웨어의 특징을 간단한 사용 사례로 소개하는 데 사용됩니다.

Aspose.PDF for .NET은 개발자들이 .NET 애플리케이션에서 PDF 문서 생성, 조작 및 변환 기능을 내장할 수 있게 해주는 풍부한 기능을 갖춘 PDF API입니다. 이는 PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX 및 이미지 파일 형식을 포함한 많은 인기 있는 파일 형식을 지원합니다. 이 글에서는 "Hello World!"라는 텍스트를 포함한 PDF 문서를 생성하고 있습니다. Aspose.PDF for .NET을 환경에 설치한 후, 아래 코드 샘플을 실행하여 Aspose.PDF API가 어떻게 작동하는지 확인할 수 있습니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

아래 코드 스니펫은 다음 단계를 따릅니다:

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체를 인스턴스화합니다
1. 문서 객체에 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)를 추가합니다
1.
1. 페이지의 [Paragraph](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) 컬렉션에 TextFragment를 추가하세요.
1. 결과 PDF 문서를 [저장](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4)하세요.

다음 코드 스니펫은 Aspose.PDF for .NET API의 작동을 보여주는 Hello World 프로그램입니다.

```csharp
namespace Aspose.Pdf.Examples
{
    public static class ExampleGetStarted
    {
        private static readonly string _dataDir = "..\\..\\..\\Samples";
        public static void HelloWorld()
        {
            // 문서 객체 초기화
            Document document = new Document();
            // 페이지 추가
            Page page = document.Pages.Add();
            // 새 페이지에 텍스트 추가
            page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
            // 업데이트된 PDF 저장
            var outputFileName = System.IO.Path.Combine(_dataDir, "HelloWorld_out.pdf");
            document.Save( outputFileName );
        }
    }
}
```
