---
title: PDF에서 이미지 추출 및 바코드 인식
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/extract-images-from-pdf-and-recognize-barcodes/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Images from PDF and recognize BarCodes",
    "alternativeHeadline": "Extract Images and Barcodes from PDF files in C#",
    "abstract": "PDF 문서에서 이미지를 효율적으로 추출하고 내장된 바코드를 정확하게 인식하는 방법을 알아보세요. 이 새로운 기능은 PDF의 각 페이지에서 추출된 이미지를 처리하여 바코드 정보를 식별하는 과정을 단순화하여 데이터 검색 및 관리를 향상시킵니다. 문서 처리 워크플로를 최적화하기 위한 자세한 단계 및 코드 구현을 탐색하세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "317",
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
    "url": "/net/extract-images-from-pdf-and-recognize-barcodes/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-images-from-pdf-and-recognize-barcodes/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

{{% alert color="primary" %}}

PDF 문서는 일반적으로 텍스트, 이미지, 테이블, 첨부 파일, 그래프, 주석 및 기타 관련 객체로 구성됩니다. 바코드가 PDF 파일에 내장되어 있는 경우가 있으며, 일부 고객은 PDF 파일 내에 존재하는 바코드를 식별해야 할 필요가 있습니다. 다음 기사는 PDF 페이지에서 이미지를 추출하고 그 안의 바코드를 식별하는 방법에 대한 단계를 설명합니다.

{{% /alert %}}

Aspose.PDF for .NET의 문서 객체 모델에 따르면, PDF 파일은 하나 이상의 페이지로 구성되어 있으며 각 페이지는 리소스 객체에 이미지, 양식 및 글꼴의 컬렉션을 포함합니다. 따라서 PDF 파일에서 이미지를 추출하기 위해 PDF 파일의 개별 페이지를 탐색하고 특정 페이지에서 이미지 컬렉션을 가져와 메모리 스트림 객체에 저장하여 Aspose.BarCodeRecognition의 BarCodeReader 클래스를 사용하여 추가 처리합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IdentifyBarcodes()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "IdentifyBarcodes.pdf"))
    {
        // Traverse through individual pages of PDF file
        for (int pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
        {
            // Traverse through each image extracted from PDF pages
            foreach (var xImage in document.Pages[pageCount].Resources.Images)
            {
                using (var imageStream = new MemoryStream())
                {
                    // Save PDF document image
                    xImage.Save(imageStream, System.Drawing.Imaging.ImageFormat.Jpeg);
        
                    // Set the stream position to the begining of Stream
                    imageStream.Position = 0;
        
                    // Instantiate BarCodeReader object
                    var barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);
        
                    while (barcodeReader.Read())
                    {
                        // Get BarCode text from BarCode image
                        var code = barcodeReader.GetCodeText();
        
                        // Write the BarCode text to Console output
                        Console.WriteLine("BARCODE : " + code);
                    }
        
                    // Close BarCodeReader object to release the Image file
                    barcodeReader.Close();
                }
            }
        }
    }
}
```

이 기사에서 다룬 주제에 대한 자세한 내용은 다음 링크를 방문하세요:

- [PDF 파일에서 이미지 추출](/net/extract-images-from-the-pdf-file/)
- [바코드 읽기](https://docs.aspose.com/barcode/net/barcode-recognition/)