---
title: C#을 사용한 추가 주석
linktitle: 추가 주석
type: docs
weight: 60
url: ko/net/extra-annotations/
description: 이 섹션에서는 PDF 문서에서 추가 주석을 추가, 가져오기 및 삭제하는 방법을 설명합니다.
lastmod: "2023-09-12"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#을 사용한 추가 주석",
    "alternativeHeadline": "PDF에 추가 주석 추가 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "PDF, C#, 링크 주석, 캐럿 주석",
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
    "url": "/net/extra-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extra-annotations/"
    },
    "dateModified": "2022-02-04",
    "description": "이 섹션에서는 PDF 문서에서 추가 주석을 추가, 가져오기 및 삭제하는 방법을 설명합니다."
}
</script>

## 기존 PDF 파일에 캐럿 주석 추가하는 방법

캐럿 주석은 텍스트 편집을 나타내는 기호입니다. 캐럿 주석은 또한 마크업 주석이므로 캐럿 클래스는 마크업 클래스에서 파생되며 캐럿 주석의 속성을 가져오거나 설정하고 캐럿 주석 외관의 흐름을 재설정하는 기능을 제공합니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

캐럿 주석을 만드는 단계는 다음과 같습니다:

1. PDF 파일을 로드하세요 - 새 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. 새로운 [Caret Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/caretannotation)을 생성하고 캐럿 매개변수를 설정하세요 (새로운 Rectangle, 제목, 주제, 플래그, 색상, 너비, 시작 스타일 및 종료 스타일). 이 주석은 텍스트 삽입을 나타냅니다.
1. 새로운 [StrikeOutAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/strikeoutannotation)을 생성하고 매개변수 설정하기 (새로운 Rectangle, 제목, 색상, 새로운 QuadPoints 및 새로운 포인트, 주제, InReplyTo, ReplyType).
1. 페이지에 주석 추가하기.

다음 코드 스니펫은 PDF 파일에 Caret 주석을 추가하는 방법을 보여줍니다:

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleCaretAnnotation
    {
        // 문서 디렉토리로의 경로.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddCaretAnnotation()
        {
            // PDF 파일 불러오기
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
            // 이 주석은 텍스트 삽입을 나타냄
            var caretAnnotation1 = new CaretAnnotation(document.Pages[1], new Rectangle(299.988, 713.664, 308.708, 720.769))
            {
                Title = "Aspose User",
                Subject = "Inserted text 1",
                Flags = AnnotationFlags.Print,
                Color = Color.Blue
            };
            // 이 주석은 텍스트 교체를 나타냄
            var caretAnnotation2 = new CaretAnnotation(document.Pages[1], new Rectangle(361.246, 727.908, 370.081, 735.107))
            {
                Flags = AnnotationFlags.Print,
                Subject = "Inserted text 2",
                Title = "Aspose User",
                Color = Color.Blue
            };

            var strikeOutAnnotation = new StrikeOutAnnotation(document.Pages[1],
                new Rectangle(318.407, 727.826, 368.916, 740.098))
            {
                Color = Color.Blue,
                QuadPoints = new[] {
                new Point(321.66, 739.416),
                new Point(365.664, 739.416),
                new Point(321.66, 728.508),
                new Point(365.664, 728.508)
            },
                Subject = "Cross-out",
                InReplyTo = caretAnnotation2,
                ReplyType = ReplyType.Group
            };

            document.Pages[1].Annotations.Add(caretAnnotation1);
            document.Pages[1].Annotations.Add(caretAnnotation2);
            document.Pages[1].Annotations.Add(strikeOutAnnotation);

            document.Save(System.IO.Path.Combine(_dataDir, "sample_caret.pdf"));
        }
    }
```
### 커서 주석 가져오기

다음 코드 스니펫을 사용하여 PDF 문서에서 커서 주석을 가져보세요.

```csharp
public static void GetCaretAnnotation()
{
    // PDF 파일 로드
    Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_caret.pdf"));
    var caretAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Caret)
        .Cast<CaretAnnotation>();
    foreach (var ca in caretAnnotations)
    {
        Console.WriteLine($"{ca.Rect}");
    }
}
```

### 커서 주석 삭제

다음 코드 스니펫은 PDF 파일에서 커서 주석을 삭제하는 방법을 보여줍니다.

```csharp
public static void DeleteCaretAnnotation()
{
    // PDF 파일 로드
    Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_caret.pdf"));
    var caretAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Caret)
        .Cast<CaretAnnotation>();

    foreach (var ca in caretAnnotations)
    {
        document.Pages[1].Annotations.Delete(ca);
    }
    document.Save(System.IO.Path.Combine(_dataDir, "sample_caret_del.pdf"));
}
```
## 특정 페이지 영역을 레다크션 주석을 사용하여 편집하는 방법 Aspose.PDF for .NET

Aspose.PDF for .NET은 기존 PDF 파일에서 주석을 추가하고 조작하는 기능을 지원합니다. 최근 몇몇 고객들이 PDF 문서의 특정 페이지 영역에서 텍스트, 이미지 등의 요소를 제거(레다크션)하는 기능을 요청했습니다. 이 요구사항을 충족시키기 위해 RedactionAnnotation이라는 클래스가 제공됩니다. 이 클래스는 특정 페이지 영역을 레다크션하거나 기존 RedactionAnnotations을 조작하여 레다크션할 수 있습니다(즉, 주석을 평탄화하고 그 아래 텍스트를 제거합니다).

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해 주세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// 문서 열기
Document doc = new Document(dataDir + "input.pdf");

// 특정 페이지 영역에 대한 RedactionAnnotation 인스턴스 생성
RedactionAnnotation annot = new RedactionAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(200, 500, 300, 600));
annot.FillColor = Aspose.Pdf.Color.Green;
annot.BorderColor = Aspose.Pdf.Color.Yellow;
annot.Color = Aspose.Pdf.Color.Blue;
// 레다크션 주석에 인쇄될 텍스트
annot.OverlayText = "REDACTED";
annot.TextAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// 레다크션 주석에 오버레이 텍스트 반복
annot.Repeat = true;
// 첫 페이지의 주석 컬렉션에 주석 추가
doc.Pages[1].Annotations.Add(annot);
// 주석을 평탄화하고 페이지 내용을 레다크션합니다 (즉, 레다크션된 주석 아래의 텍스트와 이미지 제거)
annot.Redact();
dataDir = dataDir + "RedactPage_out.pdf";
doc.Save(dataDir);
```
### 파사드 접근법

Aspose.PDF.Facades 네임스페이스에는 PDF 파일 내에 있는 기존 주석을 조작할 수 있는 기능을 제공하는 [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor)라는 클래스가 있습니다. 이 클래스에는 특정 페이지 영역을 제거할 수 있는 기능을 제공하는 [RedactArea(..)](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/redactarea)라는 메소드가 포함되어 있습니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Aspose.Pdf.Facades.PdfAnnotationEditor editor = new Aspose.Pdf.Facades.PdfAnnotationEditor();
// 특정 페이지 영역을 삭제
editor.RedactArea(1, new Aspose.Pdf.Rectangle(100, 100, 20, 70), System.Drawing.Color.White);
editor.BindPdf(dataDir + "input.pdf");
editor.Save(dataDir + "FacadesApproach_out.pdf");
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

