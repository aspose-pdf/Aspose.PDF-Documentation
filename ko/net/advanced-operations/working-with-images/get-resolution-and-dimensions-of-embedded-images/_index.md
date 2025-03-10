---
title: 이미지의 해상도 및 크기 가져오기
linktitle: 해상도 및 크기 가져오기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ko/net/get-resolution-and-dimensions-of-embedded-images/
description: Aspose.PDF를 사용하여 .NET에서 PDF의 임베디드 이미지의 해상도와 크기를 검색하는 방법을 배웁니다.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get Resolution and Dimensions of Images",
    "alternativeHeadline": "Extract Image Resolution and Dimensions Efficiently",
    "abstract": "Aspose.PDF 라이브러리를 사용하여 PDF 문서 내의 임베디드 이미지의 해상도와 크기를 효율적으로 얻는 방법을 알아보세요. 이 기능은 개발자가 추출 없이 이미지 속성에 직접 접근할 수 있게 하여 PDF 파일에서 이미지 조작 프로세스를 간소화하고 이미지 데이터에 대한 기능과 제어를 향상시킵니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Get Resolution, Dimensions of Images, Embedded Images, Aspose.PDF.Drawing, ArrayList, Image Placement Classes, ConcatenateMatrix, XImage, PDF Manipulation Library, Image Resolution Computation",
    "wordcount": "827",
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
    "url": "/net/get-resolution-and-dimensions-of-embedded-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-resolution-and-dimensions-of-embedded-images/"
    },
    "dateModified": "2024-11-26",
    "description": "이 섹션에서는 임베디드 이미지의 해상도와 크기를 가져오는 방법에 대한 세부정보를 보여줍니다."
}
</script>

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

이 주제는 Aspose.PDF 네임스페이스의 연산자 클래스를 사용하는 방법을 설명하며, 이를 통해 이미지를 추출하지 않고도 해상도 및 크기 정보를 얻을 수 있는 기능을 제공합니다.

이를 달성하는 방법에는 여러 가지가 있습니다. 이 문서에서는 `arraylist`와 [이미지 배치 클래스](https://reference.aspose.com/pdf/net/aspose.pdf/imageplacement)를 사용하는 방법을 설명합니다.

1. 먼저, 소스 PDF 파일(이미지가 포함된)을 로드합니다.
1. 그런 다음 문서에 있는 이미지의 이름을 보관할 ArrayList 객체를 생성합니다.
1. Page.Resources.Images 속성을 사용하여 이미지를 가져옵니다.
1. 이미지의 그래픽 상태를 보관할 스택 객체를 생성하고 이를 사용하여 다양한 이미지 상태를 추적합니다.
1. 현재 변환을 정의하는 ConcatenateMatrix 객체를 생성합니다. 이 객체는 콘텐츠의 크기 조정, 회전 및 왜곡을 지원합니다. 이전 행렬과 새로운 행렬을 연결합니다. 변환을 처음부터 정의할 수는 없으며 기존 변환만 수정할 수 있다는 점에 유의하십시오.
1. ConcatenateMatrix로 행렬을 수정할 수 있으므로 원래 이미지 상태로 되돌릴 필요가 있을 수 있습니다. GSave 및 GRestore 연산자를 사용하십시오. 이 연산자는 쌍으로 호출되어야 합니다. 예를 들어, 복잡한 변환으로 그래픽 작업을 수행한 후 변환을 초기 상태로 되돌리려면 접근 방식은 다음과 같을 것입니다:

```csharp
// Draw some text
GSave

ConcatenateMatrix  // rotate contents after the operator

// Some graphics work

ConcatenateMatrix // scale (with previous rotation) contents after the operator

// Some other graphics work

GRestore

// Draw some text
```

결과적으로 텍스트는 일반 형태로 그려지지만 텍스트 연산자 사이에 일부 변환이 수행됩니다. 이미지를 표시하거나 형상 객체 및 이미지를 그리려면 Do 연산자를 사용해야 합니다.

우리는 또한 이미지 크기를 가져오는 데 사용할 수 있는 Width 및 Height라는 두 가지 속성을 제공하는 XImage라는 클래스를 가지고 있습니다.

1. 이미지 해상도를 계산하기 위한 일부 계산을 수행합니다.
1. 이미지 이름과 함께 명령 프롬프트에 정보를 표시합니다.

다음 코드 스니펫은 PDF 문서에서 이미지를 추출하지 않고 이미지의 크기와 해상도를 가져오는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImageInformationFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageInformation.pdf"))
    {
        // Define the default resolution for image
        int defaultResolution = 72;
        var graphicsState = new Stack();

        // Define list which will hold image names
        var imageNames = new List<string>(document.Pages[1].Resources.Images.Names);

        // Insert an object to stack
        graphicsState.Push(new System.Drawing.Drawing2D.Matrix(1, 0, 0, 1, 0, 0));

        // Get all the operators on first page of document
        foreach (var op in document.Pages[1].Contents)
        {
            // Use GSave/GRestore operators to revert the transformations back to previously set
            var opSaveState = op as Aspose.Pdf.Operators.GSave;
            var opRestoreState = op as Aspose.Pdf.Operators.GRestore;
            var opCtm = op as Aspose.Pdf.Operators.ConcatenateMatrix;
            var opDo = op as Aspose.Pdf.Operators.Do;

            if (opSaveState != null)
            {
                // Save previous state and push current state to the top of the stack
                graphicsState.Push(((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Clone());
            }
            else if (opRestoreState != null)
            {
                // Throw away current state and restore previous one
                graphicsState.Pop();
            }
            else if (opCtm != null)
            {
                var cm = new System.Drawing.Drawing2D.Matrix(
                   (float)opCtm.Matrix.A,
                   (float)opCtm.Matrix.B,
                   (float)opCtm.Matrix.C,
                   (float)opCtm.Matrix.D,
                   (float)opCtm.Matrix.E,
                   (float)opCtm.Matrix.F);

                // Multiply current matrix with the state matrix
                ((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Multiply(cm);

                continue;
            }
            else if (opDo != null)
            {
                // In case this is an image drawing operator
                if (imageNames.Contains(opDo.Name))
                {
                    var lastCTM = (System.Drawing.Drawing2D.Matrix)graphicsState.Peek();
                    // Create XImage object to hold images of first pdf page
                    var image = document.Pages[1].Resources.Images[opDo.Name];

                    // Get image dimensions
                    double scaledWidth = Math.Sqrt(Math.Pow(lastCTM.Elements[0], 2) + Math.Pow(lastCTM.Elements[1], 2));
                    double scaledHeight = Math.Sqrt(Math.Pow(lastCTM.Elements[2], 2) + Math.Pow(lastCTM.Elements[3], 2));
                    // Get Height and Width information of image
                    double originalWidth = image.Width;
                    double originalHeight = image.Height;

                    // Compute resolution based on above information
                    double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                    double resVertical = originalHeight * defaultResolution / scaledHeight;

                    // Display Dimension and Resolution information of each image
                    Console.Out.WriteLine(
                            string.Format(dataDir + "image {0} ({1:.##}:{2:.##}): res {3:.##} x {4:.##}",
                                         opDo.Name, scaledWidth, scaledHeight, resHorizontal,
                                         resVertical));
                }
            }
        }
    }
}
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
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