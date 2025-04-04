---
title: PDF 문서 비교
linktitle: PDF 비교
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 130
url: /ko/net/compare-pdf-documents/
description: 24.7 릴리스 이후로 주석 마크와 나란히 출력으로 PDF 문서 내용을 비교할 수 있습니다.
lastmod: "2024-08-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Compare PDF documents",
    "alternativeHeadline": "Enhanced PDF Document Comparison with Visual Highlights",
    "abstract": "Aspose.PDF for .NET의 새로운 PDF 비교 기능은 사용자가 특정 페이지 또는 전체 콘텐츠를 통해 두 PDF 문서 간의 차이를 효율적으로 식별할 수 있게 해줍니다. 나란히 출력 및 추가 변경 마커와 다양한 비교 모드와 같은 사용자 정의 옵션을 통해 이 강력한 도구는 수정 사항을 쉽게 추적하고 검토할 수 있도록 하여 협업을 향상시킵니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Compare PDF documents, PDF comparison, Aspose.PDF for .NET, comparing specific pages, comparing entire documents, graphical PDF comparer, side-by-side comparison, change markers, document accuracy, ImagesDifference",
    "wordcount": "1047",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "url": "/net/compare-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/compare-pdf-documents/"
    },
    "dateModified": "2025-04-04",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

모든 비교 도구는 [Aspose.PDF.Drawing](https://docs.aspose.com/pdf/net/drawing/) 라이브러리에서 사용할 수 있습니다.

## PDF 문서 비교 방법

PDF 문서 작업을 할 때 두 문서의 내용을 비교하여 차이를 식별해야 할 때가 있습니다. Aspose.PDF for .NET 라이브러리는 이를 위한 강력한 도구 세트를 제공합니다. 이 문서에서는 간단한 코드 스니펫을 사용하여 PDF 문서를 비교하는 방법을 살펴보겠습니다.

Aspose.PDF의 비교 기능을 사용하면 두 PDF 문서를 페이지별로 비교할 수 있습니다. 특정 페이지 또는 전체 문서를 비교하도록 선택할 수 있습니다. 결과 비교 문서는 차이를 강조 표시하여 두 파일 간의 변경 사항을 쉽게 식별할 수 있도록 합니다.

다음은 Aspose.PDF for .NET 라이브러리를 사용하여 PDF 문서를 비교하는 가능한 방법의 목록입니다:

1. **특정 페이지 비교** - 두 PDF 문서의 첫 페이지를 비교합니다.

1. **전체 문서 비교** - 두 PDF 문서의 전체 내용을 비교합니다.

1. **그래픽적으로 PDF 문서 비교**:

- GetDifference 메서드를 사용하여 PDF 비교 - 변경 사항이 표시된 개별 이미지.

- CompareDocumentsToPdf 메서드를 사용하여 PDF 비교 - 변경 사항이 표시된 이미지가 포함된 PDF 문서.

## 특정 페이지 비교

첫 번째 코드 스니펫은 두 PDF 문서의 첫 페이지를 비교하는 방법을 보여줍니다.

1. 문서 초기화.
코드는 각 PDF 문서를 해당 파일 경로(documentPath1 및 documentPath2)를 사용하여 초기화하는 것으로 시작합니다. 경로는 현재 빈 문자열로 지정되어 있지만, 실제로는 이를 실제 파일 경로로 교체해야 합니다.

2. 비교 과정.

- 페이지 선택 - 비교는 각 문서의 첫 페이지('Pages[1]')로 제한됩니다.
- 비교 옵션:

'AdditionalChangeMarks = true' - 이 옵션은 추가 변경 마커가 표시되도록 합니다. 이러한 마커는 현재 비교 중인 페이지에 없더라도 다른 페이지에 있을 수 있는 차이를 강조 표시합니다.

'ComparisonMode = ComparisonMode.IgnoreSpaces' - 이 모드는 비교자가 텍스트의 공백을 무시하고 단어 내의 변경 사항에만 집중하도록 지시합니다.

3. 두 페이지 간의 차이를 강조 표시하는 결과 비교 문서는 'resultPdfPath'에 지정된 파일 경로에 저장됩니다.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparingSpecificPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparingSpecificPages1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparingSpecificPages2.pdf"))
        {
            // Compare
            Aspose.Pdf.Comparison.SideBySidePdfComparer.Compare(document1.Pages[1], document2.Pages[1], dataDir + "ComparingSpecificPages_out.pdf", new Aspose.Pdf.Comparison.SideBySideComparisonOptions
            {
                AdditionalChangeMarks = true,
                ComparisonMode = Aspose.Pdf.Comparison.ComparisonMode.IgnoreSpaces
            });
        }
    }
}
```

## 전체 문서 비교

두 번째 코드 스니펫은 두 PDF 문서의 전체 내용을 비교하는 범위를 확장합니다.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparingEntireDocuments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparingEntireDocuments1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparingEntireDocuments2.pdf"))
        {
            // Compare
            Aspose.Pdf.Comparison.SideBySidePdfComparer.Compare(
                document1,
                document2,
                dataDir + "ComparingEntireDocuments_out.pdf",
                new Aspose.Pdf.Comparison.SideBySideComparisonOptions
                {
                    AdditionalChangeMarks = true,
                    ComparisonMode = Aspose.Pdf.Comparison.ComparisonMode.IgnoreSpaces
                });
        }
    }
}
```

이 스니펫에서 생성된 비교 결과는 Adobe Acrobat과 같은 뷰어에서 열 수 있는 PDF 문서입니다. Adobe Acrobat에서 두 페이지 보기 모드를 사용하면 변경 사항을 나란히 볼 수 있습니다:

- 삭제 - 왼쪽 페이지에 기록됩니다.
- 삽입 - 오른쪽 페이지에 기록됩니다.

'AdditionalChangeMarks'를 'true'로 설정하면 현재 보고 있는 페이지에 변경 사항이 없더라도 다른 페이지에서 발생할 수 있는 변경 사항에 대한 마커도 볼 수 있습니다.

**Aspose.PDF for .NET**은 특정 페이지 또는 전체 문서를 비교해야 할 때 PDF 문서를 비교하기 위한 강력한 도구를 제공합니다. 'AdditionalChangeMarks' 및 다양한 'ComparisonMode 설정'과 같은 옵션을 사용하여 비교 프로세스를 특정 요구 사항에 맞게 조정할 수 있습니다. 결과 문서는 변경 사항을 명확하게 나란히 보여주어 수정 사항을 추적하고 문서의 정확성을 보장하는 데 도움이 됩니다.

## GraphicalPdfComparer를 사용하여 PDF 문서 비교

문서에서 협업할 때, 특히 전문 환경에서는 동일한 파일의 여러 버전을 갖게 되는 경우가 많습니다.

[GraphicalPdfComparer](https://reference.aspose.com/pdf/ko/net/aspose.pdf.comparison.graphicalcomparison/graphicalpdfcomparer/) 클래스를 사용하여 PDF 문서와 페이지를 비교할 수 있습니다. 이 클래스는 페이지의 그래픽 콘텐츠에서 변경 사항을 비교하는 데 적합합니다.

Aspose.PDF for .NET을 사용하면 문서와 페이지를 비교하고 비교 결과를 PDF 문서 또는 이미지 파일로 출력할 수 있습니다.

다음 클래스 속성을 설정할 수 있습니다:

- 해상도 - 출력 이미지 및 비교 중 생성된 이미지의 DPI 단위 해상도.
- 색상 - 변경 마커의 색상.
- 임계값 - 변경 임계값(백분율). 기본값은 0입니다. 0이 아닌 값을 설정하면 귀하에게 중요하지 않은 그래픽 변경 사항을 무시할 수 있습니다.

이 클래스에는 추가 처리를 위해 적합한 형태로 페이지 이미지 차이를 가져오는 메서드가 있습니다: **ImagesDifference GetDifference(Page page1, Page page2)**.

이 메서드는 비교되는 첫 번째 페이지의 이미지와 차이 배열을 포함하는 [ImagesDifference](https://reference.aspose.com/pdf/ko/net/aspose.pdf.comparison.graphicalcomparison/imagesdifference/) 클래스의 객체를 반환합니다. 차이 배열과 원본 이미지는 **RGB24bpp** 픽셀 형식을 가집니다.

ImagesDifference를 사용하면 다른 이미지를 생성하고 차이 배열을 원본 이미지에 추가하여 비교되는 두 번째 페이지의 이미지를 얻을 수 있습니다. 이를 위해 **ImagesDifference.GetDestinationImage 및 ImagesDifference.DifferenceToImage** 메서드를 사용합니다.

### GetDifference 메서드를 사용하여 PDF 비교

제공된 코드는 두 PDF 문서를 비교하고 그들 간의 차이를 시각적으로 표현하는 [GetDifference](https://reference.aspose.com/pdf/ko/net/aspose.pdf.comparison.graphicalcomparison/imagesdifference/#methods) 메서드를 정의합니다.

이 메서드는 두 PDF 파일의 첫 페이지를 비교하고 두 개의 PNG 이미지를 생성합니다:

- 하나의 이미지는(diffPngFilePath) 페이지 간의 차이를 빨간색으로 강조 표시합니다.
- 다른 이미지는(destPngFilePath) 대상(두 번째) PDF 페이지의 시각적 표현입니다.

이 과정은 두 문서 버전 간의 변경 사항이나 차이를 시각적으로 비교하는 데 유용할 수 있습니다.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparePDFWithGetDifferenceMethod()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithGetDifferenceMethod1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithGetDifferenceMethod2.pdf"))
        {
            // Create comparer 
            var comparer = new Aspose.Pdf.Comparison.GraphicalPdfComparer();
            // Compare
            using (var imagesDifference = comparer.GetDifference(document1.Pages[1], document2.Pages[1]))
            {
                using (var diffImg = imagesDifference.DifferenceToImage(Aspose.Pdf.Color.Red, Aspose.Pdf.Color.White))
                {
                    diffImg.Save(dataDir + "ComparePDFWithGetDifferenceMethodDiffPngFilePath_out.png");
                }
                using (var destImg = imagesDifference.GetDestinationImage())
                {
                    destImg.Save(dataDir + "ComparePDFWithGetDifferenceMethodDestPngFilePath_out.png");
                }
            }
        }
    }
}
```

### CompareDocumentsToPdf 메서드를 사용하여 PDF 비교

제공된 코드 스니펫은 두 문서를 비교하고 비교 결과의 PDF 보고서를 생성하는 [CompareDocumentsToPdf](https://reference.aspose.com/pdf/ko/net/aspose.pdf.comparison.graphicalcomparison/graphicalpdfcomparer/comparedocumentstopdf/) 메서드를 사용했습니다.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparePDFWithCompareDocumentsToPdfMethod()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithCompareDocumentsToPdfMethod1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithCompareDocumentsToPdfMethod2.pdf"))
        {
            // Create comparer
            var comparer = new Aspose.Pdf.Comparison.GraphicalPdfComparer()
            {
                Threshold = 3.0,
                Color = Aspose.Pdf.Color.Blue,
                Resolution = new Aspose.Pdf.Devices.Resolution(300)
            };
            // Compare
            comparer.CompareDocumentsToPdf(document1, document2, dataDir + "compareDocumentsToPdf_out.pdf");
        }
    }
}
```