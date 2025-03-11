---
title: PDF 레이어 작업하기 C#
linktitle: PDF 레이어 작업하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ko/net/work-with-pdf-layers/
description: 다음 작업에서는 PDF 레이어를 잠그고, PDF 레이어 요소를 추출하고, 레이어가 있는 PDF를 평면화하고, PDF 내의 모든 레이어를 하나로 병합하는 방법을 설명합니다.
lastmod: "2024-09-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Work with PDF layers using C#",
    "alternativeHeadline": "Manage PDF layers effortlessly with C#",
    "abstract": "사용자가 PDF 레이어를 효과적으로 작업할 수 있도록 해주는 새로운 Aspose.PDF for .NET 기능으로 향상된 PDF 문서 관리를 경험하세요. 이 기능은 레이어의 잠금 및 잠금 해제, 요소를 별도의 파일로 추출, 레이어가 있는 콘텐츠 평면화, 여러 레이어를 하나로 병합할 수 있게 하여 문서 가시성과 조직에 대한 더 큰 제어를 제공합니다. PDF 문서의 잠재력을 열고 이러한 강력한 도구로 작업 흐름을 간소화하세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF layers, lock PDF layer, extract PDF layer elements, flatten layered PDF, merge PDF layers, Aspose.PDF for .NET, layer.Lock(), layer.Flatten(), layer.Save()",
    "wordcount": "501",
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
    "url": "/net/work-with-pdf-layers/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/work-with-pdf-layers/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

PDF 레이어는 PDF 문서가 선택적으로 볼 수 있거나 숨길 수 있는 다양한 콘텐츠 세트를 포함할 수 있게 해줍니다. PDF의 각 레이어는 텍스트, 이미지 또는 그래픽을 포함할 수 있으며, 사용자는 필요에 따라 이러한 레이어를 켜거나 끌 수 있습니다. 레이어는 서로 다른 콘텐츠를 조직하거나 분리해야 하는 복잡한 문서에서 자주 사용됩니다.

## PDF 레이어 잠그기

Aspose.PDF for .NET을 사용하면 PDF를 열고 첫 페이지에서 특정 레이어를 잠그고 변경 사항과 함께 문서를 저장할 수 있습니다.

24.5 릴리스 이후 이 기능이 구현되었습니다.

두 개의 새로운 메서드와 하나의 속성이 추가되었습니다:

- Layer.Lock(); - 레이어를 잠급니다.
- Layer.Unlock(); - 레이어의 잠금을 해제합니다.
- Layer.Locked; - 레이어 잠금 상태를 나타내는 속성입니다.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void LockLayerInPDF()
{
	// The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Layers();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page and the first layer
        var page = document.Pages[1];
        var layer = page.Layers[0];

        // Lock the layer
        layer.Lock();

        // Save PDF document
        document.Save(dataDir + "LockLayerInPDF_out.pdf");
    }
}
```

## PDF 레이어 요소 추출

Aspose.PDF for .NET 라이브러리는 첫 페이지에서 각 레이어를 추출하고 각 레이어를 별도의 파일로 저장할 수 있습니다.

레이어에서 새 PDF를 만들기 위해 다음 코드 스니펫을 사용할 수 있습니다:

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveLayersFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get layers from the first page
        var layers = document.Pages[1].Layers;

        // Save each layer to the output path
        foreach (var layer in layers)
        {
            layer.Save(dataDir + "Layers_out.pdf");
        }
    }
}
```

24.9 릴리스로 인해 이 기능이 업데이트되었습니다.

PDF 레이어 요소를 추출하고 새 PDF 파일 스트림에 저장할 수 있습니다:

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveLayersToOutputStream(Stream outputStream)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
	
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get layers from the first page
        var layers = document.Pages[1].Layers;

        // Save each layer to the output stream
        foreach (var layer in layers)
        {
            layer.Save(outputStream);
        }
    }
}
```

## 레이어가 있는 PDF 평면화

Aspose.PDF for .NET 라이브러리는 PDF를 열고 첫 페이지의 각 레이어를 반복하며 각 레이어를 평면화하여 페이지에 영구적으로 만듭니다.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenLayersInPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page
        var page = document.Pages[1];

        // Flatten each layer on the page
        foreach (var layer in page.Layers)
        {
            layer.Flatten(true);
        }
    }
}
```

'Layer.Flatten(bool cleanupContentStream)' 메서드는 콘텐츠 스트림에서 선택적 콘텐츠 그룹 마커를 제거할지 여부를 지정하는 부울 매개변수를 받습니다. cleanupContentStream 매개변수를 false로 설정하면 평면화 프로세스가 빨라집니다.

## PDF 내의 모든 레이어를 하나로 병합

Aspose.PDF for .NET 라이브러리는 모든 PDF 레이어 또는 첫 페이지의 특정 레이어를 새 레이어로 병합하고 업데이트된 문서를 저장할 수 있습니다.

페이지의 모든 레이어를 병합하기 위해 두 개의 메서드가 추가되었습니다:

- void MergeLayers(string newLayerName).
- void MergeLayers(string newLayerName, string newOptionalContentGroupId).

두 번째 매개변수는 선택적 콘텐츠 그룹 마커의 이름을 바꿀 수 있게 해줍니다. 기본값은 "oc1" (/OC /oc1 BDC)입니다.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeLayersInPdf(string newLayerName, string optionalLayerName = null)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page
        var page = document.Pages[1];

        // Merge layers with a new layer name
        if (optionalLayerName != null)
        {
            page.MergeLayers(newLayerName, optionalLayerName);
        }
        else
        {
            page.MergeLayers(newLayerName);
        }

        // Save PDF document
        document.Save(dataDir + "MergeLayersInPdf_out.pdf");
    }
}
```