---
title: 이미지의 해상도와 크기 얻기
linktitle: 해상도 및 크기 얻기
type: docs
weight: 40
url: ko/net/get-resolution-and-dimensions-of-embedded-images/
description: 이 섹션은 임베디드 이미지의 해상도와 크기를 얻는 세부사항을 보여줍니다
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "이미지의 해상도와 크기 얻기",
    "alternativeHeadline": "임베디드 이미지의 해상도 및 크기를 얻는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "PDF, C#, 해상도 얻기, 크기 얻기",
    "wordcount": "302",
    "proficiencyLevel":"초급",
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
    "url": "/net/get-resolution-and-dimensions-of-embedded-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-resolution-and-dimensions-of-embedded-images/"
    },
    "dateModified": "2022-02-04",
    "description": "이 섹션은 임베디드 이미지의 해상도와 크기를 얻는 세부사항을 보여줍니다"
}
</script>
다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

이 주제는 Aspose.PDF 네임스페이스의 연산자 클래스를 사용하는 방법을 설명합니다. 이 클래스는 이미지를 추출하지 않고도 이미지의 해상도와 크기 정보를 얻을 수 있는 기능을 제공합니다.

이를 달성하는 다양한 방법이 있습니다. 이 글은 `arraylist`와 [image placement classes](https://reference.aspose.com/pdf/net/aspose.pdf/imageplacement)를 사용하는 방법을 설명합니다.

1. 먼저 소스 PDF 파일(이미지 포함)을 로드합니다.
1. 문서에 있는 이미지의 이름을 저장할 ArrayList 객체를 생성합니다.
1. Page.Resources.Images 속성을 사용하여 이미지를 가져옵니다.
1. 이미지의 그래픽 상태를 담을 스택 객체를 생성하고 다양한 이미지 상태를 추적하는 데 사용합니다.
1.
1. ConcatenateMatrix를 사용하여 행렬을 수정할 수 있기 때문에 원래 이미지 상태로 되돌릴 필요가 있을 수 있습니다. GSave와 GRestore 연산자를 사용하세요. 이 연산자들은 짝을 이루어 호출되어야 하므로 함께 사용해야 합니다. 예를 들어, 복잡한 변환을 수행한 그래픽 작업을 하고 최종적으로 변환을 초기 상태로 되돌리는 경우, 접근 방식은 다음과 같습니다:

```csharp
// 텍스트 그리기
GSave

ConcatenateMatrix  // 연산자 이후 내용 회전

// 그래픽 작업 수행

ConcatenateMatrix // 이전 회전을 포함한 스케일 조정 (연산자 이후 내용)

// 다른 그래픽 작업 수행

GRestore

// 텍스트 그리기
```

결과적으로 텍스트는 정상적인 형태로 그려지지만 텍스트 연산자 사이에서 일부 변환이 수행됩니다. 이미지를 표시하거나 폼 객체 및 이미지를 그리기 위해서는 Do 연산자를 사용해야 합니다.

또한 XImage라는 클래스가 있으며, Width와 Height 두 가지 속성을 제공하여 이미지 크기를 얻을 수 있습니다.

1.
1.
1. 명령 프롬프트에서 이미지 이름과 함께 정보를 표시합니다.

다음 코드 스니펫은 PDF 문서에서 이미지를 추출하지 않고 이미지의 크기와 해상도를 얻는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하시기 바랍니다.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// 원본 PDF 파일을 로드합니다
Document doc = new Document(dataDir+ "ImageInformation.pdf");

// 이미지의 기본 해상도를 정의합니다
int defaultResolution = 72;
System.Collections.Stack graphicsState = new System.Collections.Stack();
// 이미지 이름을 저장할 배열 리스트 객체를 정의합니다
System.Collections.ArrayList imageNames = new System.Collections.ArrayList(doc.Pages[1].Resources.Images.Names);
// 스택에 객체를 삽입합니다
graphicsState.Push(new System.Drawing.Drawing2D.Matrix(1, 0, 0, 1, 0, 0));

// 문서의 첫 페이지에 있는 모든 연산자를 가져옵니다
foreach (Operator op in doc.Pages[1].Contents)
{
    // GSave/GRestore 연산자를 사용하여 이전에 설정된 변환으로 되돌립니다
    Aspose.Pdf.Operators.GSave opSaveState = op as Aspose.Pdf.Operators.GSave;
    Aspose.Pdf.Operators.GRestore opRestoreState = op as Aspose.Pdf.Operators.GRestore;
    // ConcatenateMatrix 객체를 인스턴스화합니다. 이 객체는 현재 변환 행렬을 정의합니다.
    Aspose.Pdf.Operators.ConcatenateMatrix opCtm = op as Aspose.Pdf.Operators.ConcatenateMatrix;
    // 리소스에서 객체를 그리는 Do 연산자를 생성합니다. Form 객체와 이미지 객체를 그립니다
    Aspose.Pdf.Operators.Do opDo = op as Aspose.Pdf.Operators.Do;

    if (opSaveState != null)
    {
        // 이전 상태를 저장하고 현재 상태를 스택의 맨 위로 푸시합니다
        graphicsState.Push(((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Clone());
    }
    else if (opRestoreState != null)
    {
        // 현재 상태를 버리고 이전 상태를 복원합니다
        graphicsState.Pop();
    }
    else if (opCtm != null)
    {
        System.Drawing.Drawing2D.Matrix cm = new System.Drawing.Drawing2D.Matrix(
           (float)opCtm.Matrix.A,
           (float)opCtm.Matrix.B,
           (float)opCtm.Matrix.C,
           (float)opCtm.Matrix.D,
           (float)opCtm.Matrix.E,
           (float)opCtm.Matrix.F);

        // 현재 행렬을 상태 행렬과 곱합니다
        ((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Multiply(cm);

        continue;
    }
    else if (opDo != null)
    {
        // 이것이 이미지를 그리는 연산자인 경우
        if (imageNames.Contains(opDo.Name))
        {
            System.Drawing.Drawing2D.Matrix lastCTM = (System.Drawing.Drawing2D.Matrix)graphicsState.Peek();
            // 첫 번째 PDF 페이지의 이미지를 보유할 XImage 객체를 생성합니다
            XImage image = doc.Pages[1].Resources.Images[opDo.Name];

            // 이미지 크기를 가져옵니다
            double scaledWidth = Math.Sqrt(Math.Pow(lastCTM.Elements[0], 2) + Math.Pow(lastCTM.Elements[1], 2));
            double scaledHeight = Math.Sqrt(Math.Pow(lastCTM.Elements[2], 2) + Math.Pow(lastCTM.Elements[3], 2));
            // 이미지의 높이와 너비 정보를 얻습니다
            double originalWidth = image.Width;
            double originalHeight = image.Height;

            // 위 정보를 바탕으로 해상도를 계산합니다
            double resHorizontal = originalWidth * defaultResolution / scaledWidth;
            double resVertical = originalHeight * defaultResolution / scaledHeight;

            // 각 이미지의 크기 및 해상도 정보를 표시합니다
            Console.Out.WriteLine(
                    string.Format(dataDir + "image {0} ({1:.##}:{2:.##}): res {3:.##} x {4:.##}",
                                 opDo.Name, scaledWidth, scaledHeight, resHorizontal,
                                 resVertical));
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
                "contactType": "판매",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "판매",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "판매",
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
    "applicationCategory": ".NET을 위한 PDF 조작 라이브러리",
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

