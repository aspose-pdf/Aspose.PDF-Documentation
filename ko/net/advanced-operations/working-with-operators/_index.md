---
title: 연산자 사용하기
linktitle: 연산자 사용하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /ko/net/working-with-operators/
description: 이 주제는 Aspose.PDF와 함께 연산자를 사용하는 방법을 설명합니다. 연산자 클래스는 PDF 조작을 위한 훌륭한 기능을 제공합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Operators",
    "alternativeHeadline": "Empowered PDF Manipulation with Operators Integration",
    "abstract": "Aspose.PDF for .NET의 연산자 기능은 사용자가 이미지를 추가하고 그래픽을 제거하는 등의 작업을 위해 특정 연산자 클래스를 활용할 수 있도록 하여 PDF 조작 기능을 향상시킵니다. 이 기능은 PDF 내에서 그래픽 요소와 그 상태를 정의하는 과정을 단순화하여 개발자에게 세밀한 문서 편집 및 처리 도구를 제공합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "operators, Aspose.PDF, PDF manipulation, GSave operator, ConcatenateMatrix operator, Do operator, GRestore operator, graphics state, remove graphics",
    "wordcount": "1233",
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
    "url": "/net/working-with-operators/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-operators/"
    },
    "dateModified": "2024-11-26",
    "description": "이 주제는 Aspose.PDF와 함께 연산자를 사용하는 방법을 설명합니다. 연산자 클래스는 PDF 조작을 위한 훌륭한 기능을 제공합니다."
}
</script>

## PDF 연산자 소개 및 사용법

연산자는 페이지에 그래픽 모양을 그리는 것과 같은 특정 작업을 수행하도록 지정하는 PDF 키워드입니다. 연산자 키워드는 초기 슬래시 문자(2Fh)가 없기 때문에 명명된 객체와 구별됩니다. 연산자는 콘텐츠 스트림 내에서만 의미가 있습니다.

콘텐츠 스트림은 페이지에 그려질 그래픽 요소를 설명하는 명령으로 구성된 PDF 스트림 객체입니다. PDF 연산자에 대한 더 많은 세부정보는 [PDF 사양](https://opensource.adobe.com/dc-acrobat-sdk-docs/)에서 확인할 수 있습니다.

### 구현 세부정보

이 주제는 Aspose.PDF와 함께 연산자를 사용하는 방법을 설명합니다. 선택된 예제는 개념을 설명하기 위해 PDF 파일에 이미지를 추가합니다. PDF 파일에 이미지를 추가하려면 다양한 연산자가 필요합니다. 이 예제에서는 [GSave](https://reference.aspose.com/pdf/net/aspose.pdf.ioperatorselector/visit/methods/28), [ConcatenateMatrix](https://reference.aspose.com/pdf/net/aspose.pdf.ioperatorselector/visit/methods/10), [Do](https://reference.aspose.com/pdf/net/aspose.pdf.ioperatorselector/visit/methods/14), 및 [GRestore](https://reference.aspose.com/pdf/net/aspose.pdf.ioperatorselector/visit/methods/26) 연산자를 사용합니다.

- **GSave** 연산자는 PDF의 현재 그래픽 상태를 저장합니다.
- **ConcatenateMatrix** (행렬 연결) 연산자는 이미지가 PDF 페이지에 어떻게 배치될지를 정의하는 데 사용됩니다.
- **Do** 연산자는 페이지에 이미지를 그립니다.
- **GRestore** 연산자는 그래픽 상태를 복원합니다.

PDF 파일에 이미지를 추가하려면:

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체를 생성하고 입력 PDF 문서를 엽니다.
1. 이미지를 추가할 특정 페이지를 가져옵니다.
1. 페이지의 리소스 컬렉션에 이미지를 추가합니다.
1. 연산자를 사용하여 페이지에 이미지를 배치합니다:
   - 먼저 GSave 연산자를 사용하여 현재 그래픽 상태를 저장합니다.
   - 그런 다음 ConcatenateMatrix 연산자를 사용하여 이미지가 배치될 위치를 지정합니다.
   - Do 연산자를 사용하여 페이지에 이미지를 그립니다.
1. 마지막으로 GRestore 연산자를 사용하여 업데이트된 그래픽 상태를 저장합니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

다음 코드 스니펫은 PDF 연산자를 사용하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageUsingPDFOperators()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFOperators.pdf"))
    {
        // Set coordinates for the image placement
        int lowerLeftX = 100;
        int lowerLeftY = 100;
        int upperRightX = 200;
        int upperRightY = 200;

        // Get the page where the image needs to be added
        var page = document.Pages[1];

        // Load the image into a file stream
        using (var imageStream = new FileStream(dataDir + "PDFOperators.jpg", FileMode.Open))
        {
            // Add the image to the page's Resources collection
            page.Resources.Images.Add(imageStream);
        }

        // Save the current graphics state using the GSave operator
        page.Contents.Add(new Aspose.Pdf.Operators.GSave());

        // Create a rectangle and matrix for positioning the image
        var rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        var matrix = new Aspose.Pdf.Matrix(new double[]
        {
            rectangle.URX - rectangle.LLX, 0,
            0, rectangle.URY - rectangle.LLY,
            rectangle.LLX, rectangle.LLY
        });

        // Define how the image must be placed using the ConcatenateMatrix operator
        page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));

        // Get the image from the Resources collection
        var ximage = page.Resources.Images[page.Resources.Images.Count];

        // Draw the image using the Do operator
        page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));

        // Restore the graphics state using the GRestore operator
        page.Contents.Add(new Aspose.Pdf.Operators.GRestore());

        // Save PDF document
        document.Save(dataDir + "PDFOperators_out.pdf");
    }
}
```

## 연산자를 사용하여 페이지에 XForm 그리기

이 주제는 GSave/GRestore 연산자, ContatenateMatrix 연산자를 사용하여 xForm의 위치를 지정하고 Do 연산자를 사용하여 페이지에 xForm을 그리는 방법을 보여줍니다.

아래 코드는 PDF 파일의 기존 내용을 GSave/GRestore 연산자 쌍으로 감쌉니다. 이 접근 방식은 기존 내용의 끝에서 초기 그래픽 상태를 가져오는 데 도움이 됩니다. 이 접근 방식이 없으면 기존 연산자 체인의 끝에 원치 않는 변환이 남을 수 있습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DrawXFormOnPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DrawXFormOnPage.pdf"))
    {
        var pageContents = document.Pages[1].Contents;

        // Wrap existing contents with GSave/GRestore operators to preserve graphics state
        pageContents.Insert(1, new Aspose.Pdf.Operators.GSave());
        pageContents.Add(new Aspose.Pdf.Operators.GRestore());

        // Add GSave operator to start new graphics state
        pageContents.Add(new Aspose.Pdf.Operators.GSave());

        // Create an XForm
        var form = Aspose.Pdf.XForm.CreateNewForm(document.Pages[1], document);
        document.Pages[1].Resources.Forms.Add(form);

        form.Contents.Add(new Aspose.Pdf.Operators.GSave());
        // Define image width and height
        form.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0));

        // Load image into stream
        using (var imageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open))
        {
            // Add the image to the XForm's resources
            form.Resources.Images.Add(imageStream);
        }

        var ximage = form.Resources.Images[form.Resources.Images.Count];
        // Draw the image on the XForm
        form.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
        form.Contents.Add(new Aspose.Pdf.Operators.GRestore());

        // Place and draw the XForm at two different coordinates

        // Draw the XForm at (100, 500)
        pageContents.Add(new Aspose.Pdf.Operators.GSave());
        pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500));
        pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
        pageContents.Add(new Aspose.Pdf.Operators.GRestore());

        // Draw the XForm at (100, 300)
        pageContents.Add(new Aspose.Pdf.Operators.GSave());
        pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300));
        pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
        pageContents.Add(new Aspose.Pdf.Operators.GRestore());

        // Restore graphics state
        pageContents.Add(new Aspose.Pdf.Operators.GRestore());

        // Save PDF document
        document.Save(dataDir + "DrawXFormOnPage_out.pdf");
    }
}
```

## 연산자 클래스를 사용하여 그래픽 객체 제거

연산자 클래스는 PDF 조작을 위한 훌륭한 기능을 제공합니다. PDF 파일에 [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 클래스의 [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteimage) 메서드를 사용하여 제거할 수 없는 그래픽이 포함된 경우, 대신 연산자 클래스를 사용하여 제거할 수 있습니다.

다음 코드 스니펫은 그래픽을 제거하는 방법을 보여줍니다. PDF 파일에 그래픽에 대한 텍스트 레이블이 포함되어 있는 경우, 이 접근 방식을 사용하면 PDF 파일에 남아 있을 수 있습니다. 따라서 이러한 이미지를 삭제하기 위한 대체 방법으로 그래픽 연산자를 검색하십시오.

```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
  private static void RemoveGraphicsObjects()
  {
      // The path to the documents directory
      var dataDir = RunExamples.GetDataDir_AsposePdf();

      // Open PDF document
      using (var document = new Aspose.Pdf.Document(dataDir + "RemoveGraphicsObjects.pdf"))
      {
          // Get the specific page (page 2 in this case)
          var page = document.Pages[2];

          // Get the operator collection from the page contents
          var oc = page.Contents;

          // Define the path-painting operators to be removed
          var operators = new Aspose.Pdf.Operator[]
          {
              new Aspose.Pdf.Operators.Stroke(),
              new Aspose.Pdf.Operators.ClosePathStroke(),
              new Aspose.Pdf.Operators.Fill()
          };

          // Delete the specified operators from the page contents
          oc.Delete(operators);

          // Save PDF document
          document.Save(dataDir + "NoGraphics_out.pdf");
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