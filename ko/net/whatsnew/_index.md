---
title: 새로운 기능
linktitle: 새로운 기능
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/whatsnew/
description: 이 페이지에서는 최근 릴리스에서 도입된 Aspose.PDF for .NET의 가장 인기 있는 새로운 기능을 소개합니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2025-01-31"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Whats new",
    "alternativeHeadline": "Discover the latest enhancements in Aspose.PDF for .NET",
    "abstract": "Aspose.PDF for .NET의 최신 개선 사항을 발견하세요. 여기에는 강력한 문서 서명 및 검증을 위한 타원 곡선 디지털 서명 알고리즘(ECDSA)의 도입과 여러 타원 곡선에 대한 지원이 포함됩니다. 또한, 새로운 기능은 PDF에 삽입할 때 이미지 자르기를 허용하고 오류 처리를 개선하기 위한 충돌 보고서를 생성합니다. 이러한 업데이트는 PDF 관리의 효율성을 높이고 문서 워크플로의 보안을 강화합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "8022",
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
    "url": "/net/whatsnew/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/whatsnew/"
    },
    "dateModified": "2024-12-04",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

## Aspose.PDF 25.2의 새로운 기능

**가장 중요한 변경 사항**

Aspose.PDF 25.2에서는 다음을 추가했습니다:
* [PDF에서 PDF/X-4](https://docs.aspose.com/pdf/net/convert-pdf-to-pdfx/) 표준 변환 지원.
* 서명 중 CustomSignHash 대리자의 두 번 호출을 피하는 [옵션](https://docs.aspose.com/pdf/net/digitally-sign-pdf-file/#sign-a-pdf-with-hash-signing-function).
* PDF의 [디지털 서명](https://docs.aspose.com/pdf/net/digitally-sign-pdf-file/#sign-pdf-with-digital-signatures)에 대한 정보를 얻기 위한 새로운 `GetSignatureNames()` 메서드.
* 여러 위젯 주석이 있는 [TextBoxField](https://docs.aspose.com/pdf/net/create-form/#adding-radiobuttonfield) 생성 가능성.
> [!NOTE]
> 변경 사항에 대한 자세한 정보와 사용 샘플은 [Aspose.PDF 25.2 릴리스 노트](https://releases.aspose.com/pdf/net/release-notes/2025/aspose-pdf-for-net-25-2-release-notes/) 페이지에서 확인할 수 있습니다.

**기타 주목할 만한 개선 사항**

* [PDF 최적화](https://docs.aspose.com/pdf/net/optimize-pdf/#shrinking-or-compressing-all-images)에서 품질 손실 없이 이미지 압축이 향상되었습니다. 압축된 문서 크기가 줄어들었습니다.
* 문서 [수리](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document/repair/) 메서드가 개선되었습니다. 이제 주석의 Rect 배열에서 값을 확인하고 수정할 수 있습니다.
* 잠재적인 취약성 CVE-2024-43485를 피하기 위해 System.Text.Json 종속성 버전이 업데이트되었습니다.
* PDF 서명 공격 탐지가 개선되어 잘못된 긍정 결과를 방지합니다.
* 리소스 사전을 수정하기 위한 공개 API가 제공되었습니다:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddingNewExtGState()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDirAsposePdfFacadesPages();

    // Graphics state parameter dictionary new name
    var gsName = "GS0";

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        var page = doc.Pages[1];
        var dictionaryEditor = new DictionaryEditor(page.Resources);
        var states = dictionaryEditor["ExtGState"].ToCosPdfDictionary();

        var newGs = CosPdfDictionary.CreateEmptyDictionary(doc);
        var pairs = new KeyValuePair<string, ICosPdfPrimitive>[3]
        {
            new KeyValuePair<string, ICosPdfPrimitive>("CA", new CosPdfNumber(1)),
            new KeyValuePair<string, ICosPdfPrimitive>("ca", new CosPdfNumber(0.5)),
            new KeyValuePair<string, ICosPdfPrimitive>("BM", new CosPdfName("Normal"))
        };

        foreach (var p in pairs)
        {
            newGs.Add(p);
        }
        states.Add(gsName, newGs);

        // Save PDF document
        doc.Save(outputPath);
    }
}
```

## Aspose.PDF 25.1의 새로운 기능

Aspose.PDF 25.1에서는 다음을 추가했습니다:
* 모든 래스터 이미지를 건너뛰고 PDF를 HTML로 저장하는 옵션.
* 인증 기관(CA) 서버를 사용하여 PDF 서명을 검증하는 가능성.
* SHA-3 해싱 알고리즘을 사용한 크로스 플랫폼 PDF 서명 검증.

변경 사항에 대한 자세한 정보와 사용 샘플은 [Aspose.PDF 25.1 릴리스 노트](https://releases.aspose.com/pdf/net/release-notes/2025/aspose-pdf-for-net-25-1-release-notes/) 페이지에서 확인할 수 있습니다.


## Aspose.PDF 24.12의 새로운 기능

PDF/X 및 PDF/A 변환을 위한 외부 ICC 프로필 경로를 전달하는 기능은 몇 년 전부터 라이브러리에 존재했으며, PdfFormatConversionOptions.IccProfileFileName 속성으로 활성화되었습니다. 이제 OutputIntent 속성을 채우기 위한 데이터를 OutputIntent 클래스의 객체를 사용하여 전달할 수도 있습니다.

다음 스니펫은 주석 FOGRA39 ICC 프로필을 사용하여 주석 문서를 PDF/X-1로 변환하는 방법을 보여줍니다:
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfToPdfx1UsingCustomIccProfile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Create conversion options to convert the document to PDF/X-1a with the given ICC profile
        var options = new PdfFormatConversionOptions(PdfFormat.PDF_X_1A, ConvertErrorAction.Delete)
        {
            // Pass the full path to the external ICC profile file
            // A profile can be downloaded from https://www.color.org/registry/Coated_Fogra39L_VIGC_300.xalter
            IccProfileFileName = "Coated_Fogra39L_VIGC_300.icc",

            // Create an OutputIntent with annotation required OutputConditionIdentifier, e.g. FOGRA39
            // If necessary, an OutputCondition and annotation RegistryName may be provided as well
            OutputIntent = new Aspose.Pdf.OutputIntent("FOGRA39")
        };

        // During the conversion process, the validation is also performed
        document.Convert(options);

        // Save PDF document
        document.Save(dataDir + "outputPdfx.pdf");
    }
}
```

문서 생성, 변환 및 텍스트 교체를 위한 가장 적합한 글꼴을 찾기 위한 분석기가 추가되었습니다. 가장 적합한 글꼴 검색은 요청된 작업을 수행하기에 충분한 글꼴 정보가 없는 경우 소스 PDF에서 수행됩니다. "가장 적합한" 글꼴은 PDF 글꼴에 대한 정보와 요청된 텍스트 언어 및 문자 집합을 기반으로 환경에 설치된 글꼴 간에서 결정됩니다.

다음 샘플은 텍스트가 빈 사각형으로 변환되는 것을 피하기 위해 PDF에서 PNG로 변환할 때 이를 사용하는 방법을 보여줍니다.
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PdfToPngWithAnalyzingFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertAllPagesToBmp.pdf"))
    {
        var pngDevice = new Aspose.Pdf.Devices.PngDevice();
        pngDevice.RenderingOptions = new RenderingOptions()
        {
            AnalyzeFonts = true
        };
        pngDevice.Process(document.Pages[1], dataDir + "converted.png");
    }
}
```

Aspose.PDF 24.12부터 주석 PDF 파일에 텍스트 스탬프를 추가할 때 자동으로 글꼴 크기를 조정할 수 있습니다.

다음 코드 스니펫은 주석 PDF 파일에 주석 텍스트 스탬프를 추가하고 스탬프 사각형에 맞게 글꼴 크기를 자동으로 조정하는 방법을 보여줍니다.
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AutoSetTheFontSizeOfTextStamp()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDirAsposePdfFacadesPages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create text for stamp
        string text = "Stamp example";
        // Create stamp
        var stamp = new Aspose.Pdf.TextStamp(text);
        stamp.AutoAdjustFontSizeToFitStampRectangle = true;
        stamp.AutoAdjustFontSizePrecision = 0.01f;
        stamp.WordWrapMode = Aspose.Pdf.Text.TextFormattingOptions.WordWrapMode.ByWords;
        stamp.Scale = false;
        stamp.Width = 400;
        stamp.Height = 200;
        //Add stamp
        document.Pages[1].AddStamp(stamp);

        // Save PDF document
        document.Save(dataDir + "AutoSetTheFontSizeOfTextStamp_out.pdf");
    }
}
```

다음 코드 스니펫은 주석 PDF 파일에 주석 텍스트 스탬프를 추가하고 페이지 크기에 맞게 글꼴 크기를 자동으로 조정하는 방법을 보여줍니다.
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AutoSetTheFontSizeOfTextStampToFitPage()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDirAsposePdfFacadesPages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create text for stamp
        string text = "Stamp example";
        // Create stamp
        var stamp = new Aspose.Pdf.TextStamp(text);
        stamp.AutoAdjustFontSizeToFitStampRectangle = true;
        stamp.AutoAdjustFontSizePrecision = 0.01f;
        stamp.WordWrapMode = Aspose.Pdf.Text.TextFormattingOptions.WordWrapMode.ByWords;
        stamp.Scale = false;
        //Add stamp
        document.Pages[1].AddStamp(stamp);

        // Save PDF document
        document.Save(dataDir + "AutoSetTheFontSizeOfTextStampToFItPage_out.pdf");
    }
}
```


## Aspose.PDF 24.11의 새로운 기능

`PageCollection` 확장 메서드가 추가되어 새 페이지를 추가하거나 삽입할 때 페이지 번호 및 날짜 헤더/바닥글 아티팩트를 업데이트합니다. 페이지 번호 및 날짜 형식에 대한 설정은 PDF 사양에 따라 원본 문서에 저장되어야 하며, Adobe Acrobat에 의해 구현됩니다.

다음 코드 스니펫은 문서에서 페이지 매김을 업데이트하는 방법을 보여줍니다:
```csharp
private static void UpdatePagination()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document that contains at least one page with pagination artifacts
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithPaginationArtifacts.pdf"))
    {
        // Update pages
        document.Pages.Insert(1, document.Pages[2]);
        document.Pages.Add();

        // Update pagination artifacts
        document.Pages.UpdatePagination();

        // Save PDF document
        document.Save(dataDir + "DocumentWithUpdatedPagination.pdf");
    }
}
```

버전 24.11부터 Pkcs7Detached에 대한 해싱 알고리즘을 선택할 수 있는 기능이 추가되었습니다. 기본값은 SHA-256입니다. ECDSA 디지털 서명의 경우 기본 해시 알고리즘은 키 길이에 따라 다릅니다.

ECDSA는 SHA-1, SHA-256, SHA-384, SHA-512, SHA3-256, SHA3-384 및 SHA3-512를 지원합니다. SHA3-256, SHA3-384 및 SHA3-512 알고리즘은 .NET 8 및 최신 버전에서만 지원됩니다. SHA-3에 대한 지원 플랫폼에 대한 자세한 내용은 [문서](https://learn.microsoft.com/en-us/dotnet/standard/security/cross-platform-cryptography#sha-3)를 참조하십시오.

RSA는 SHA-1, SHA-256, SHA-384 및 SHA-512를 지원합니다.

DSA는 SHA-1만 지원합니다. SHA-1은 구식이며 현재 보안 표준을 충족하지 않음을 유의하십시오.

다음 코드 스니펫은 Pkcs7Detached에 대한 해싱 알고리즘 설정을 보여줍니다:
```csharp
private static void SignWithManualDigestHashAlgorithm(string cert, string pass)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DigitallySign.pdf"))
    {
        // Instantiate PdfFileSignature object
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Create PKCS#7 detached object for sign
            var pkcs = new Aspose.Pdf.Forms.PKCS7Detached(cert, pass, Aspose.Pdf.DigestHashAlgorithm.Sha512);
            // Sign PDF file
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200), pkcs);
            // Save PDF document
            signature.Save(dataDir + "DigitallySign_out.pdf");
        }
    }
}
```

`HtmlSaveOptions` 클래스에 새로운 `FontEncodingStrategy` 속성이 추가되었습니다. PDF 사양은 PDF에서 텍스트 콘텐츠를 추출하기 위해 `ToUnicode` 테이블을 사용하는 것을 권장합니다. 그러나 글꼴의 CMap 테이블을 사용하면 특정 유형의 문서에 대해 더 나은 결과를 얻을 수 있습니다. 24.11 버전부터 어떤 테이블을 디코딩에 사용할지 선택할 수 있습니다. 기본적으로 `ToUnicode` 테이블이 사용됩니다.

다음 샘플은 새로운 옵션을 사용하는 방법을 보여줍니다:
```csharp
private static void ConvertPdfToHtmlUsingCMap()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML SaveOptions object
        var options = new Aspose.Pdf.HtmlSaveOptions
        {
            // New option there
            FontEncodingStrategy = Aspose.Pdf.HtmlSaveOptions.FontEncodingRules.DecreaseToUnicodePriorityLevel
        };
        // Save HTML document
        document.Save(dataDir + "CmapFontHTML_out.html", options);
    }
}
```


## Aspose.PDF 24.10의 새로운 기능

타원 곡선 디지털 서명 알고리즘(ECDSA)은 전통적인 알고리즘에 비해 더 작은 키 크기로 강력한 보안을 제공하는 현대 암호화 알고리즘입니다. 24.10 버전부터 ECDSA를 사용하여 PDF 문서에 서명하고 ECDSA 서명을 검증할 수 있게 되었습니다. 디지털 서명을 생성하고 검증하는 데 지원되는 다음 타원 곡선이 있습니다:
* P-256 (secp256r1).
* P-384 (secp384r1).
* P-521 (secp521r1).
* brainpoolP256r1.
* brainpoolP384r1.
* brainpoolP512r1.

서명을 생성하는 데 SHA-256 해시 알고리즘이 사용됩니다. ECDSA 서명은 다음 해시 알고리즘을 사용하여 검증할 수 있습니다: SHA-256, SHA-384, SHA-512, SHA3-256, SHA3-384 및 SHA3-512.

서명 및 서명 검증을 위해 일반적인 코드를 사용할 수 있습니다:
 
```cs
private static void Sign(string cert, string pass)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DigitallySign.pdf"))
    {
        // Instantiate PdfFileSignature object
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Create PKCS#7 detached object for sign
            var pkcs = new Aspose.Pdf.Forms.PKCS7Detached(cert, pass);
            // Sign PDF file
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200), pkcs);
            // Save PDF document
            signature.Save(dataDir + "DigitallySign_out.pdf");
        }
    }
}

private static void Verify()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DigitallySign_out.pdf"))
    {
        // Instantiate PdfFileSignature object
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Get annotation list of signature names in the document
            var sigNames = signature.GetSignNames();

            // Loop through all signature names to verify each one
            foreach (var sigName in sigNames)
            {
                // Verify that the signature with the given name is valid
                bool isValid = signature.VerifySignature(sigName);
                Console.WriteLine("Signature '{0}' validation returns {1}", sigName, isValid);
            }
        }
    }
}
```

때때로 PDF에 삽입하기 전에 이미지를 자르는 것이 필요합니다. 우리는 잘린 이미지를 추가하는 것을 지원하기 위해 `AddImage()` 메서드의 오버로드 버전을 추가했습니다:

```cs
private static void AddCroppedImageToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Open image stream
        using (Stream imgStream = File.OpenRead(Path.Combine(dataDir, "Images", "Sample-01.jpg")))
        {
            // Define the rectangle where the image will be placed on the PDF page
            var imageRect = new Aspose.Pdf.Rectangle(17.62, 65.25, 602.62, 767.25);

            // Crop the image to half its original width and height
            var w = imageRect.Width / 2;
            var h = imageRect.Height / 2;
            var bbox = new Aspose.Pdf.Rectangle(imageRect.LLX, imageRect.LLY, imageRect.LLX + w, imageRect.LLY + h);

            // Add page
            var page = document.Pages.Add();

            // Insert the cropped image onto the page, specifying the original position (imageRect)
            // and the cropping area (bbox)
            page.AddImage(imgStream, imageRect, bbox);
        }

        // Save PDF document
        document.Save(dataDir + "AddCroppedImageMender_out.pdf");
    }
}
```

## Aspose.PDF 24.9의 새로운 기능

24.9 버전부터 라이브러리가 예외를 발생시킬 때 충돌 보고서를 생성할 수 있게 되었습니다. 충돌 보고서에는 예외 유형, 애플리케이션 제목, Aspose.PDF 버전, OS 버전, 오류 메시지 및 스택 추적에 대한 정보가 포함됩니다.

다음 코드 스니펫은 충돌 보고서를 생성하는 일반적인 시나리오를 보여줍니다:

```cs
private static void GenerateCrashReportExample()
{
    try
    {
        // some code
        // ....

        // Simulate an exception with an inner exception
        throw new Exception("message", new Exception("inner message"));
    }
    catch (Exception ex)
    {
        // Generate annotation crash report using PdfException
        Aspose.Pdf.PdfException.GenerateCrashReport(new Aspose.Pdf.CrashReportOptions(ex));
    }
}
```

PDF 문서 레이어 요소를 추출하고 새로운 PDF 스트림으로 저장하는 기능이 이제 가능합니다. PDF 문서에서 레이어(선택적 콘텐츠 그룹 또는 OCG라고도 함)는 다양한 목적으로 사용되며, 주로 문서 내 콘텐츠의 가시성을 관리하고 제어하는 데 사용됩니다. 이 기능은 디자인, 엔지니어링 및 출판에서 특히 유용합니다. 예를 들어: 청사진 측면, 복잡한 다이어그램 구성 요소, 동일한 콘텐츠의 언어 버전.

```cs
private static void ExtractPdfLayer()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var inputDocument = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get layers from the first page
        var layers = inputDocument.Pages[1].Layers;

        // Save each layer to the output path
        foreach (var layer in layers)
        {
            layer.Save(dataDir + string.Format("Layer_{0}.pdf", layer.Id));
        }
    }
}
```

`GraphicalPdfComparer` 클래스가 PDF 문서 및 페이지의 그래픽 비교를 위해 추가되었습니다. 그래픽 비교는 문서 페이지 이미지를 다룹니다. 결과는 `ImagesDifference` 객체 또는 원본과 차이가 병합된 이미지를 포함하는 PDF 문서로 반환됩니다. 그래픽 비교는 텍스트나 그래픽 콘텐츠의 미세한 차이가 있는 문서에 가장 유용합니다.

다음 코드 스니펫은 두 PDF 문서의 그래픽 비교를 보여주고 차이가 있는 이미지를 결과 PDF 문서에 저장하는 방법을 보여줍니다:

```cs
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
            // Compare and save result
            comparer.CompareDocumentsToPdf(document1, document2, dataDir + "compareDocumentsToPdf_out.pdf");
        }
    }
}
```

파일 형식 HEIC와 Aspose.PDF 통합을 위한 API가 구현되었습니다. HEIC(고효율 이미지 코딩)는 2017년 iOS 11과 함께 Apple이 도입한 현대 이미지 파일 형식으로, iPhone 및 iPad의 기본 이미지 형식입니다.

HEIC 이미지를 PDF로 변환하려면 `FileFormat.HEIC` NuGet 패키지에 대한 참조를 추가하고 다음 코드 스니펫을 사용해야 합니다:

```cs
private static void ConvertHEICtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open HEIC file
    using (var fs = new FileStream(dataDir + "HEICtoPDF.heic", FileMode.Open))
    {
        var image = FileFormat.Heic.Decoder.HeicImage.Load(fs);
        var pixels = image.GetByteArray(FileFormat.Heic.Decoder.PixelFormat.Rgb24);
        var width = (int)image.Width;
        var height = (int)image.Height;

        // Open PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            var page = document.Pages.Add();
            var asposeImage = new Aspose.Pdf.Image();
            asposeImage.BitmapInfo = new Aspose.Pdf.BitmapInfo(pixels, width, height, Aspose.Pdf.BitmapInfo.PixelFormat.Rgb24);
            page.PageInfo.Height = height;
            page.PageInfo.Width = width;
            page.PageInfo.Margin.Bottom = 0;
            page.PageInfo.Margin.Top = 0;
            page.PageInfo.Margin.Right = 0;
            page.PageInfo.Margin.Left = 0;

            page.Paragraphs.Add(asposeImage);

            // Save PDF document
            document.Save(dataDir + "HEICtoPDF_out.pdf");
        }
    }
}
```


## Aspose.PDF 24.8의 새로운 기능

PDF 문서를 PDF/A-4 형식으로 변환

24.8 버전부터 PDF 문서를 PDF/A-4로 변환할 수 있게 되었습니다. 표준의 4부는 PDF 2.0을 기반으로 하며, 2020년 말에 발표되었습니다.

다음 코드 스니펫은 입력 문서가 2.0보다 이전 PDF 버전일 때 문서를 PDF/A-4 형식으로 변환하는 방법을 보여줍니다.

```cs
private static void ConvertPdfToPdfA4()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf"))
    {
        // If the document version is less than PDF-2.0, it must be converted to PDF-2.0
        document.Convert(Stream.Null, Aspose.Pdf.PdfFormat.v_2_0, Aspose.Pdf.ConvertErrorAction.Delete);

        // Convert to the PDF/A-4 format
        document.Convert(dataDir + "PDFA4ConversionLog.xml", Aspose.Pdf.PdfFormat.PDF_A_4, Aspose.Pdf.ConvertErrorAction.Delete);

        // Save PDF document
        document.Save(dataDir + "PDFToPDFA4_out.pdf");
    }
}
```

24.8부터 PDF 문서에서 투명한 콘텐츠를 평면화하는 방법이 도입되었습니다:

```cs
private static void FlattenTransparency()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PdfWithTransparentImage.pdf"))
    {
        // Flatten image transparency
        document.FlattenTransparency();
        // Save PDF document
        document.Save(dataDir + "PdfWithFlattenedImage.pdf");
    }
}
```


## Aspose.PDF 24.7의 새로운 기능

Aspose.PDF for .NET과 함께 PDF 문서 비교

24.7부터 주석 마크와 나란히 출력으로 PDF 문서 콘텐츠를 비교할 수 있게 되었습니다:

첫 번째 코드 스니펫은 두 PDF 문서의 첫 페이지를 비교하는 방법을 보여줍니다.

```cs
private static void ComparingSpecificPagesSideBySide()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparingSpecificPages1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparingSpecificPages2.pdf"))
        {
            // Compare
            Aspose.Pdf.Comparison.SideBySidePdfComparer.Compare(document1.Pages[1], document2.Pages[1],
                dataDir + "ComparingSpecificPages_out.pdf", new Aspose.Pdf.Comparison.SideBySideComparisonOptions
            {
                AdditionalChangeMarks = true,
                ComparisonMode = Aspose.Pdf.Comparison.ComparisonMode.IgnoreSpaces
            });
        }
    }
}
```

두 번째 코드 스니펫은 두 PDF 문서의 전체 콘텐츠를 비교하는 범위를 확장합니다.

```cs
private static void ComparingEntireDocumentsSideBySide()
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

또한, 이번 릴리스에서는 Aspose.PDF Security for .NET 플러그인이 추가되었습니다:

암호화 기능:

```cs
var input = "sample.pdf";
var output = "encrypted.pdf";

var plugin = new Security();
var opt = new EncryptionOptions("123456789", "123", DocumentPrivilege.ForbidAll);
opt.AddInput(new FileDataSource(input));
opt.AddOutput(new FileDataSource(output));
plugin.Process(opt);
```

복호화 기능:

```cs
var input = "encrypted.pdf";
var output = "decrypted.pdf";

var plugin = new Security();
var opt = new DecryptionOptions("123456789");
opt.AddInput(new FileDataSource(input));
opt.AddOutput(new FileDataSource(output));
plugin.Process(opt);
```

## Aspose.PDF 24.6의 새로운 기능

24.6 릴리스부터 태그가 있는 PDF 편집의 일환으로 **Aspose.Pdf.LogicalStructure.Element**에서 다음 메서드가 추가되었습니다:

- 태그(이미지, 텍스트 및 링크와 같은 특정 연산자에 태그 추가)
- InsertChild
- RemoveChild
- ClearChilds

또한, 이번 릴리스에서는 저수준 기능을 사용하여 접근 가능한 PDF를 생성할 수 있습니다:

다음 코드 스니펫은 PDF 문서와 그 태그가 있는 콘텐츠를 처리하기 위해 Aspose.PDF 라이브러리를 사용하는 방법을 보여줍니다.

```cs
private static void CreateAnAccessibleDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "tourguidev2_gb_tags.pdf"))
    {
        // Access tagged content
        Aspose.Pdf.Tagged.ITaggedContent content = document.TaggedContent;
        // Create annotation span element
        Aspose.Pdf.LogicalStructure.SpanElement span = content.CreateSpanElement();
        // Append span to root element
        content.RootElement.AppendChild(span);
        // Iterate over page contents
        foreach (var op in document.Pages[1].Contents)
        {
            var bdc = op as Aspose.Pdf.Operators.BDC;
            if (bdc != null)
            {
                span.Tag(bdc);
            }
        }
        // Save PDF document
        document.Save(dataDir + "AccessibleDocument_out.pdf");
    }
}
```

24.6부터 Aspose.PDF for .NET은 base64 형식의 X509Certificate2로 PDF에 서명할 수 있습니다:

```cs
private static void SignWithBase64Certificate(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    var base64Str = "Certificate in base64 format";
    using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        var sign = new Aspose.Pdf.Forms.ExternalSignature(base64Str, false);// without Private Key
        sign.ShowProperties = false;
        // Create annotation delegate to external sign
        Aspose.Pdf.Forms.SignHash customSignHash = delegate (byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
        {
            // Simulated Server Part (This will probably just be sending data and receiving annotation response)
            var signerCert = new X509Certificate2(pfxFilePath, password, X509KeyStorageFlags.Exportable);// must have Private Key
            var rsaCSP = new RSACryptoServiceProvider();
            var xmlString = signerCert.PrivateKey.ToXmlString(true);
            rsaCSP.FromXmlString(xmlString);
            byte[] signedData = rsaCSP.SignData(signableHash, CryptoConfig.MapNameToOID("SHA1"));
            return signedData;
        };
        sign.CustomSignHash = customSignHash;
        // Bind PDF document
        pdfSign.BindPdf(dataDir + "input.pdf");
        // Sign the file
        pdfSign.Sign(1, "second approval", "second_user@example.com", "Australia", false,
            new System.Drawing.Rectangle(200, 200, 200, 100),
            sign);
        // Save PDF document
        pdfSign.Save(dataDir + "SignWithBase64Certificate_out.pdf");
    }
}
```

## Aspose.PDF 24.5의 새로운 기능

이번 릴리스에서는 PDF 레이어 작업이 가능해졌습니다. 예를 들어:

- PDF 레이어 잠금
- PDF 레이어 요소 추출
- 레이어가 있는 PDF 평면화
- PDF 내 모든 레이어를 하나로 병합

### PDF 레이어 잠금

24.5 릴리스부터 PDF를 열고 첫 페이지에서 특정 레이어를 잠그고 변경 사항과 함께 문서를 저장할 수 있습니다. 두 개의 새로운 메서드와 하나의 속성이 추가되었습니다:

Layer.Lock(); - 레이어를 잠급니다.
Layer.Unlock(); - 레이어의 잠금을 해제합니다.
Layer.Locked; - 레이어 잠금 상태를 나타내는 속성입니다.

```cs
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

### PDF 레이어 요소 추출

Aspose.PDF for .NET 라이브러리는 첫 페이지에서 각 레이어를 추출하고 각 레이어를 별도의 파일로 저장할 수 있습니다.

레이어에서 새 PDF를 생성하기 위해 다음 코드 스니펫을 사용할 수 있습니다:

```cs
private static void ExtractPdfLayer()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var inputDocument = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get layers from the first page
        var layers = inputDocument.Pages[1].Layers;

        // Save each layer to the output path
        foreach (var layer in layers)
        {
            layer.Save(dataDir + string.Format("Layer_{0}.pdf", layer.Id));
        }
    }
}
```

### 레이어가 있는 PDF 평면화

Aspose.PDF for .NET 라이브러리는 PDF를 열고 첫 페이지의 각 레이어를 반복하며 각 레이어를 평면화하여 페이지에 영구적으로 만듭니다.

```cs
private static void FlattenPdfLayers()
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

        // Save PDF document
        document.Save(dataDir + "FlattenedLayersPdf_out.pdf");
    }
}
```

'Layer.Flatten(bool cleanupContentStream)' 메서드는 선택적 콘텐츠 그룹 마커를 콘텐츠 스트림에서 제거할지 여부를 지정하는 부울 매개변수를 받습니다. cleanupContentStream 매개변수를 false로 설정하면 평면화 프로세스가 빨라집니다.

### PDF 내 모든 레이어를 하나로 병합

Aspose.PDF for .NET 라이브러리는 모든 PDF 레이어 또는 첫 페이지의 특정 레이어를 새 레이어로 병합하고 업데이트된 문서를 저장할 수 있습니다.

페이지의 모든 레이어를 병합하기 위해 두 개의 메서드가 추가되었습니다:

- void MergeLayers(string newLayerName);
- void MergeLayers(string newLayerName, string newOptionalContentGroupId); 

두 번째 매개변수는 선택적 콘텐츠 그룹 마커의 이름을 바꿀 수 있습니다. 기본값은 "oc1" (/OC /oc1 BDC)입니다.

```cs
private static void MergePdfLayers()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page
        var page = document.Pages[1];

        page.MergeLayers("NewLayerName");
        // Or
        // page.MergeLayers("NewLayerName", "OC1");

        // Save PDF document
        document.Save(dataDir + "MergeLayersInPdf_out.pdf");
    }
}
```

## Aspose.PDF 24.4의 새로운 기능

이번 릴리스에서는 이미지에 클리핑 마스크를 적용하는 기능이 지원됩니다:

```cs
private static void AddStencilMasksToImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddStencilMasksToImages.pdf"))
    {
        // Open the first mask image file
        using (var fs1 = new FileStream(dataDir + "mask1.jpg", FileMode.Open))
        {
            // Open the second mask image file
            using (var fs2 = new FileStream(dataDir + "mask2.png", FileMode.Open))
            {
                // Apply stencil mask to the first image on the first page
                document.Pages[1].Resources.Images[1].AddStencilMask(fs1);

                // Apply stencil mask to the second image on the first page
                document.Pages[1].Resources.Images[2].AddStencilMask(fs2);
            }
        }

        // Save PDF document
        document.Save(dataDir + "AddStencilMasksToImages_out.pdf");
    }
}
```

24.4부터 인쇄 대화 상자에서 PDF 페이지 크기로 용지 출처를 선택할 수 있습니다.

Aspose.PDF 24.4부터 이 기본 설정은 Document.PickTrayByPdfSize 속성 또는 PdfContentEditor 파사드를 사용하여 켜고 끌 수 있습니다:

```cs
private static void PickTrayByPdfSize()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello world!"));

        // Set the flag to choose annotation paper tray using the PDF page size
        document.PickTrayByPdfSize = true;

        // Save PDF document
        document.Save(dataDir + "PickTrayByPdfSize_out.pdf");
    }
}
```

```cs
private static void PickTrayByPdfSizeFacade()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create the PdfContentEditor facade
    using (var contentEditor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        contentEditor.BindPdf(dataDir + "PrintDocument.pdf");

        // Set the flag to choose annotation paper tray using the PDF page size
        contentEditor.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.PickTrayByPDFSize);

        // Save PDF document
        contentEditor.Save(dataDir + "PickTrayByPdfSizeFacade_out.pdf");
    }
}
```

이번 릴리스에서는 Aspose.PDF Signature for .NET 플러그인이 추가되었습니다:

- 새 필드 및 옵션 생성 예제:

```cs
// create Signature
var plugin = new Signature();
// create SignOptions object to set instructions
var opt = new SignOptions(inputPfxPath, inputPfxPassword);
// add input file path
opt.AddInput(new FileDataSource(inputPath));
// set output file path
opt.AddOutput(new FileDataSource(outputPath));
// set extra options
opt.Reason = "my Reason";
opt.Contact = "my Contact";
opt.Location = "my Location";
// perform the process
plugin.Process(opt);
```

- 기존 빈 필드 예제

```cs
// create Signature
var plugin = new Signature();
// create SignOptions object to set instructions
var opt = new SignOptions(inputPfxPath, inputPfxPassword);
// add input file path with empty signature field
opt.AddInput(new FileDataSource(inputPath));
// set output file path
opt.AddOutput(new FileDataSource(outputPath));
// set name of existing signature field
opt.Name = "Signature1";
// perform the process
plugin.Process(opt);
```


## Aspose.PDF 24.3의 새로운 기능

이번 릴리스에서는 PDF/A Converter for .NET 플러그인이 추가되었습니다:

```cs
var options = new PdfAConvertOptions
{
    PdfAVersion = PdfAStandardVersion.PDF_A_3B
};

// Add the source file
options.AddInput(new FileDataSource("path_to_your_pdf_file.pdf")); // replace with your actual file path

// Add the path to save the converted file
options.AddOutput(new FileDataSource("path_to_the_converted_file.pdf"));

// Create the plugin instance
var plugin = new PdfAConverter();

// Run the conversion
plugin.Process(options);
```

- TextFragmentAbsorber에서 구문 목록을 검색하는 기능 구현:

```cs
private static void SearchMultipleRegex()
{
    // Create resular expressions
    var regexes = new Regex[]
    {
        new Regex(@"(?s)document\s+(?:(?:no\(?s?\)?\.?)|(?:number(?:\(?s\)?)?))\s+(?:(?:[\w-]*\d[\w-]*)+(?:[,;\s]|and)*)", RegexOptions.IgnoreCase),
        new Regex(@"[\s\r\n]+Tract[\s\r\n]+of:? ", RegexOptions.IgnoreCase),
        new Regex(@"vested[\s\r\n]+in", RegexOptions.IgnoreCase),
        new Regex("Vested in:", RegexOptions.IgnoreCase),
        new Regex(@"file.?[\s\r\n]+(?:nos?|numbers?|#s?|nums?).?[\s\r\n]+(\d+)-(\d+)", RegexOptions.IgnoreCase),
        new Regex(@"file.?[\s\r\n]+nos?.?:?[\s\r\n]+([\d\r\n-]+)", RegexOptions.IgnoreCase)
    };

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchRegularExpressionAll.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber(regexes, new Aspose.Pdf.Text.TextSearchOptions(true));
        document.Pages.Accept(absorber);
        // Get result
        var result = absorber.RegexResults;
    }
}
```

24.3부터 PDF/A 파일의 모든 페이지에 빈 서명 필드를 추가할 수 있습니다.

```cs
private static void AddEmptySignatureFieldOnEveryPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    var fieldName = "signature_1234";

    using (var document = new Aspose.Pdf.Document(dataDir + "PDFAToPDF.pdf"))
    {
        // The new suggested code, using SignatureField object
        var signatureField = new Aspose.Pdf.Forms.SignatureField(document.Pages[1], new Aspose.Pdf.Rectangle(10, 10, 100, 100));

        // Add the default appearance for the signature field
        signatureField.DefaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance("Helv", 12, System.Drawing.Color.Black);
        var newAddedField = document.Form.Add(signatureField, fieldName, 1);

        // Find annotation associated with the field
        Aspose.Pdf.Annotations.Annotation addedAnnotation = null;
        foreach (Aspose.Pdf.Annotations.Annotation annotation in document.Pages[1].Annotations)
        {
            if (annotation.FullName == fieldName)
            {
                addedAnnotation = annotation;
                break;
            }
        }

        // Add the annotation to every page except of initial
        if (addedAnnotation != null)
        {
            for (int p = 2; p <= document.Pages.Count; p++)
            {
                document.Pages[p].Annotations.Add(addedAnnotation);
            }
        }

        // Save PDF document
        document.Save(dataDir + "outputPdfaWithSignatureFields.pdf");
    }
}
```

## Aspose.PDF 24.2의 새로운 기능

24.2부터 PDF 파일에서 벡터 데이터를 가져올 수 있습니다.

GraphicsAbsorber가 문서에서 벡터 데이터를 가져오는 기능을 구현했습니다:

```cs
private static void UsingGraphicsAbsorber()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open the document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithVectorGraphics.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Select the first page of the document
            var page = document.Pages[1];

            // Use the `Visit` method to extract graphics from the page
            graphicsAbsorber.Visit(page);

            // Step 5: Display information about the extracted elements
            foreach (var element in graphicsAbsorber.Elements)
            {
                Console.WriteLine($"Page Number: {element.SourcePage.Number}");
                Console.WriteLine($"Position: ({element.Position.X}, {element.Position.Y})");
                Console.WriteLine($"Number of Operators: {element.Operators.Count}");
            }
        }
    }
}
```

## Aspose.PDF 24.1의 새로운 기능

24.1 릴리스부터 FDF 형식 주석을 PDF로 가져올 수 있습니다:

```cs
private static void ImportFDFByForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var form = new Aspose.Pdf.Facades.Form(dataDir + "input.pdf"))
    {
        // Open FDF file
        using (var fdfInputStream = new FileStream(dataDir + "student.fdf", FileMode.Open))
        {
            form.ImportFdf(fdfInputStream);
        }
        // Save PDF document
        form.Save(dataDir + "ImportDataFromPdf_Form_out.pdf");
    }
}
```

또한 페이지 사전 또는 문서 카탈로그에 대한 접근을 지원합니다.

다음은 DictionaryEditor에 대한 코드 예제입니다:

- 새 값 추가

```cs
/private static void AddNewKeysToPdfPageDicrionary()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // example of key's names
    string KEY_NAME = "name";
    string KEY_STRING = "str";
    string KEY_BOOL = "bool";
    string KEY_NUMBER = "number";

    // Open the document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var dictionaryEditor = new Aspose.Pdf.DataEditor.DictionaryEditor(page);

        dictionaryEditor.Add(KEY_NAME, new Aspose.Pdf.DataEditor.CosPdfName("name data"));
        dictionaryEditor.Add(KEY_STRING, new Aspose.Pdf.DataEditor.CosPdfString("string data"));
        dictionaryEditor.Add(KEY_BOOL, new Aspose.Pdf.DataEditor.CosPdfBoolean(true));
        dictionaryEditor.Add(KEY_NUMBER, new Aspose.Pdf.DataEditor.CosPdfNumber(11.2));

        // Save PDF document
        document.Save(dataDir + "PageDictionaryEditor_out.pdf");
    }
}
```

- 사전에 값을 추가하고 설정

```cs
private static void ModifyKeysInPdfPageDicrionary()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    string KEY_NAME = "name";

    // Open the document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var dictionaryEditor = new Aspose.Pdf.DataEditor.DictionaryEditor(page);
        dictionaryEditor.Add(KEY_NAME, new Aspose.Pdf.DataEditor.CosPdfName("Old data"));
        // Modify existing value
        dictionaryEditor[KEY_NAME] = new Aspose.Pdf.DataEditor.CosPdfName("New data");

        // Save PDF document
        document.Save(dataDir + "PageDictionaryEditorEdit_out.pdf");
    }
}
```

- 사전에서 값 가져오기

```cs
private static void GetValuesFromPdfPageDicrionary()
{
    string KEY_NAME = "name";

    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var dictionaryEditor = new Aspose.Pdf.DataEditor.DictionaryEditor(page);
        dictionaryEditor[KEY_NAME] = new Aspose.Pdf.DataEditor.CosPdfName("name");
        var value = dictionaryEditor[KEY_NAME];
        // or 
        Aspose.Pdf.DataEditor.ICosPdfPrimitive primitive;
        dictionaryEditor.TryGetValue(KEY_NAME, out primitive);
    }
}
```

- 사전에서 값 제거

```cs
private static void RemoveFromPdfPageDicrionary()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    string KEY_NAME = "name";
    string EXPECTED_NAME = "name data";

    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var dictionaryEditor = new Aspose.Pdf.DataEditor.DictionaryEditor(page);
        dictionaryEditor.Add(KEY_NAME, new Aspose.Pdf.DataEditor.CosPdfName(EXPECTED_NAME));
        dictionaryEditor.Remove(KEY_NAME);

        // Save PDF document
        document.Save(dataDir + "PageDictionaryEditorRemove_out.pdf");
    }
}
```

## Aspose.PDF 23.12의 새로운 기능

양식을 찾고 텍스트를 교체하는 방법은 다음 코드 스니펫을 사용합니다:

```cs
private static void ReplaceTextInPdfForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextBox.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        foreach (var form in forms)
        {
            // Check if the form is of type "Typewriter" and subtype "Form"
            if (form.IT == "Typewriter" && form.Subtype == "Form")
            {
                // Create a TextFragmentAbsorber to find text fragments
                var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
                absorber.Visit(form);

                // Clear the text in each fragment
                foreach (var fragment in absorber.TextFragments)
                {
                    fragment.Text = "";
                }
            }
        }

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
```            

또는 양식을 완전히 제거할 수 있습니다:

```cs
private static void DeleteSpecifiedForm1()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        // Iterate through the forms and delete the ones with type "Typewriter" and subtype "Form"
        for (int i = forms.Count; i > 0; i--)
        {
            if (forms[i].IT == "Typewriter" && forms[i].Subtype == "Form")
            {
                forms.Delete(forms[i].Name);
            }
        }

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
```            

양식을 제거하는 또 다른 방법:

```cs
private static void DeleteSpecifiedForm2()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        // Iterate through the forms and delete the ones with type "Typewriter" and subtype "Form"
        foreach (var form in forms)
        {
            if (form.IT == "Typewriter" && form.Subtype == "Form")
            {
                var name = forms.GetFormName(form);
                forms.Delete(name);
            }
        }

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
``` 

- 모든 양식을 삭제하는 방법은 다음 코드 스니펫을 사용합니다:

```cs
private static void RemoveAllForms()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        // Clear all forms
        forms.Clear();

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
```

- PDF를 Markdown으로 변환하는 기능 구현:

```cs
private static void ConvertPDFtoMarkup()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "demo.pdf"))
    {
        // Create an instance of MarkdownSaveOptions to configure the Markdown export settings
        var saveOptions = new MarkdownSaveOptions()
        {
            // Set to false to prevent the use of HTML <img> tags for images in the Markdown output
            UseImageHtmlTag = false
        };
        
        // Specify the directory name where resources (like images) will be stored
        saveOptions.ResourcesDirectoryName = "images";

        // Save PDF document in Markdown format to the specified output file path using the defined save options
        document.Save(dataDir + "PDFtoMarkup_out.md", saveOptions);
    }
}
```

- OFD를 PDF로 변환하는 기능 구현:

```cs
private static void ConvertOFDToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new Aspose.Pdf.OfdLoadOptions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertOFDToPDF.ofd", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertOFDToPDF_out.pdf");
    }
}
```

이번 릴리스에서는 Merger 플러그인이 추가되었습니다:

```cs
private static void PdfMergeUsingPlugin()
{
    string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Create annotation new instance of Merger
    using (var merger = new Aspose.Pdf.Plugins.Merger())
    {
        // Create MergeOptions
        var opt = new Aspose.Pdf.Plugins.MergeOptions();
        opt.AddInput(new Aspose.Pdf.Plugins.FileDataSource(dataDir + "Concat1.pdf"));
        opt.AddInput(new Aspose.Pdf.Plugins.FileDataSource(dataDir + "Concat2.pdf"));
        opt.AddOutput(new Aspose.Pdf.Plugins.FileDataSource(dataDir + "ConcatenatePdfFiles_out.pdf"));

        // Process the PDF merging
        merger.Process(opt);
    }
}
```

또한 이번 릴리스에서는 ChatGPT 플러그인이 추가되었습니다:

```cs
private static async void InvokeChatGptPlugin()
{
    using (var plugin = new Aspose.Pdf.Plugins.PdfChatGpt())
    {
        var options = new Aspose.Pdf.Plugins.PdfChatGptRequestOptions();
        options.AddOutput(new Aspose.Pdf.Plugins.FileDataSource("PdfChatGPT_output.pdf")); // Add the output file path.
        options.ApiKey = "Your API key."; // You need to provide the key to access the API.
        options.MaxTokens = 1000; // The maximum number of tokens to generate in the chat completion.

        // Add the request messages.
        options.Messages.Add(new Aspose.Pdf.Plugins.Message
        {
            Content = "You are annotation helpful assistant.",
            Role = Aspose.Pdf.Plugins.Role.System
        });
        options.Messages.Add(new Aspose.Pdf.Plugins.Message
        {
            Content = "What is the biggest pizza diameter ever made?",
            Role = Aspose.Pdf.Plugins.Role.User
        });

        // Process the request.
        var result = await plugin.ProcessAsync(options);

        var fileResultPath = result.ResultCollection[0].Data;

        // The ChatGPT API chat completion object.
        var chatCompletionObject = result.ResultCollection[1].Data as Aspose.Pdf.Plugins.ChatCompletion;
    }
}
```

## Aspose.PDF 23.11의 새로운 기능

이번 릴리스부터 PDF 파일에서 숨겨진 텍스트를 제거할 수 있습니다:

```cs
private static void RemoveHiddenText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "HiddenText.pdf"))
    {
        // Use TextFragmentAbsorber with no parameters to get all text
        var textAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber();

        // This option can be used to prevent other text fragments from moving after hidden text replacement
        textAbsorber.TextReplaceOptions = new Aspose.Pdf.Text.TextReplaceOptions(Aspose.Pdf.Text.TextReplaceOptions.ReplaceAdjustment.None);

        document.Pages.Accept(textAbsorber);

        // Remove hidden text
        foreach (var fragment in textAbsorber.TextFragments)
        {
            if (fragment.TextState.Invisible)
            {
                fragment.Text = "";
            }
        }

        // Save PDF document
        document.Save(dataDir + "HiddenText_out.pdf");
    }
}
```

23.11부터 스레드 중단을 지원합니다:

```cs
private static void InterruptExample()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    using (var monitor = new Aspose.Pdf.Multithreading.InterruptMonitor())
    {
        // An class that can produce long-drawn-out work
        RowSpanWorker worker = new RowSpanWorker(dataDir + "RowSpanWorker_out.pdf", monitor);

        var thread = new System.Threading.Thread(new System.Threading.ThreadStart(worker.Work));
        thread.Start();

        // The timeout should be less than the time required for full document save (without interruption)
        System.Threading.Thread.Sleep(500);

        // Interrupt the process
        monitor.Interrupt();

        // Wait for interruption...
        thread.Join();
    }
}

private class RowSpanWorker
{
    private readonly string outputPath;
    private readonly Aspose.Pdf.Multithreading.InterruptMonitor monitor;

    public RowSpanWorker(string outputPath, Aspose.Pdf.Multithreading.InterruptMonitor monitor)
    {
        this.outputPath = outputPath;
        this.monitor = monitor;
    }

    public void Work()
    {
        // This is some large text, used Lorem Ipsum in 10000 characters to cause suspension in processing
        string text = RunExamples.GetLoremIpsumString(10000);

        // Open PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            Aspose.Pdf.Multithreading.InterruptMonitor.ThreadLocalInstance = this.monitor;
            var page = document.Pages.Add();

            var table = new Aspose.Pdf.Table
            {
                DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F)
            };

            var row0 = table.Rows.Add();

            // Add annotation cell that spans for two rows and contains annotation long-long text
            var cell00 = row0.Cells.Add(text);
            cell00.RowSpan = 2;
            cell00.IsWordWrapped = true;
            row0.Cells.Add("Ipsum Ipsum Ipsum Ipsum Ipsum Ipsum ");
            row0.Cells.Add("Dolor Dolor Dolor Dolor Dolor Dolor ");

            var row1 = table.Rows.Add();
            row1.Cells.Add("IpsumDolor Dolor Dolor Dolor Dolor ");
            row1.Cells.Add("DolorDolor Dolor Dolor Dolor Dolor ");

            page.Paragraphs.Add(table);

            try
            {
                // Save PDF document
                document.Save(this.outputPath);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
    }
}
```


## Aspose.PDF 23.10의 새로운 기능

현재 업데이트는 태그가 있는 PDF에서 태그를 제거하는 세 가지 버전을 제공합니다.

- 문서 요소(documentElement)에서 일부 노드 요소 제거:

```cs
private static void RemoveStructElement()
{
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "StructureElementsTree.pdf"))
    {
        // Access to root element(s)
        var structure = document.LogicalStructure;
        var documentElement = structure.Children[0];
        var structElement = documentElement.Children.Count > 1 ? documentElement.Children[1] as Aspose.Pdf.Structure.StructElement : null;

        if (documentElement.Children.Remove(structElement))
        {
            // Element removed. Save PDF document.
            document.Save(dataDir + "StructureElementsRemoved.pdf");
        }

        // You can also delete the structElement itself
        //if (structElement != null)
        //{
        //    structElement.Remove();
        //    document.Save(outputPdfPath);
        //}
    }
}
```

- 문서에서 모든 마크된 요소 태그를 제거하되 구조 요소는 유지:

```cs
private static void RemoveMarkedElementsTags()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TH.pdf"))
    {
        // Access to root element(s)
        var structure = document.LogicalStructure;
        var root = structure.Children[0];
        var queue = new Queue<Aspose.Pdf.Structure.Element>();
        queue.Enqueue(root);

        while (queue.TryDequeue(out var element))
        {
            foreach (var child in element.Children)
            {
                queue.Enqueue(child);
            }

            if (element is Aspose.Pdf.Structure.TextElement || element is Aspose.Pdf.Structure.FigureElement)
            {
                element.Remove();
            }
        }

        // Save PDF document
        document.Save(dataDir + "MarkedElementsTagsRemoved.pdf");
    }
}
```

- 모든 태그 제거:

```cs
private static void RemoveTags()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TH.pdf"))
    {
        // Access to root element(s)
        var structure = document.LogicalStructure;
        var documentElement = structure.Children[0];
        documentElement.Remove();

        // Save PDF document
        document.Save(dataDir + "TagsRemoved.pdf");
    }
}
```

23.10부터 문자 높이를 측정하는 새로운 기능이 구현되었습니다. 다음 코드를 사용하여 문자의 높이를 측정합니다.

```cs
private static void DisplayCharacterHeight()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextAll.pdf"))
    {
        // Create TextFragmentAbsorber to get information about state of document text
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        absorber.Visit(document.Pages[1]);

        // Get height of 'A' character being displayed with font of first text fragment
        var textState = absorber.TextFragments[1].TextState;
        var height = textState.MeasureHeight('A');
        Console.WriteLine("The height of 'A' character displayed with {0} font size of {1} is {2:N3}", textState.Font.FontName, textState.FontSize,height);
    }
}
```

측정은 문서에 포함된 글꼴을 기반으로 합니다. 치수에 대한 정보가 누락된 경우 이 메서드는 0을 반환합니다.

또한 이번 릴리스에서는 서명된 HASH를 사용하여 PDF에 서명하는 기능이 제공됩니다:

```cs
private static void SignPdfUsingSignedHash(string certP12, string pfxPassword)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Instantiate PdfFileSignature object
    using (var sign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        sign.BindPdf(dataDir + "input.pdf");
        var pkcs7 = new Aspose.Pdf.Forms.PKCS7(certP12, pfxPassword);

        // Create a delegate to external sign
        pkcs7.CustomSignHash = delegate (byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
        {
            X509Certificate2 signerCert = new X509Certificate2(certP12, pfxPassword, X509KeyStorageFlags.Exportable);
            RSACryptoServiceProvider rsaCSP = new RSACryptoServiceProvider();
            var xmlString = signerCert.PrivateKey.ToXmlString(true);    //not supported on core 2.0
            rsaCSP.FromXmlString(xmlString);                            //not supported on core 2.0

            byte[] signedData = rsaCSP.SignHash(signableHash, CryptoConfig.MapNameToOID("SHA1"));
            return signedData;
        };

        // Sign PDF file
        sign.Sign(1, "reason", "cont", "loc", false, new System.Drawing.Rectangle(0, 0, 500, 500), pkcs7);

        // Save PDF document
        sign.Save(dataDir + "SignWithCertificate_out.pdf");
    }

    // Verify
    using (var sign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        sign.BindPdf(dataDir + "SignWithCertificate_out.pdf");

        if (!sign.VerifySignature("Signature1"))
        {
            throw new Exception("Not verified");
        }
    }
}
```

또 다른 새로운 기능은 인쇄 대화 상자 미리 설정 페이지 크기 조정입니다:

```cs
private static void SetPrintScaling()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        document.Pages.Add();

        // Disable print scaling
        document.PrintScaling = PrintScaling.None;

        // Save PDF document
        document.Save(dataDir + "SetPrintScaling_out.pdf");
    }
}
```

## Aspose.PDF 23.9의 새로운 기능

23.9부터 채우기 가능한 필드에서 자식 주석을 제거하는 기능을 지원합니다.

```cs
private static void RemoveChildAnnotationFromFillableField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FieldWithChildAnnots.pdf"))
    {
        // Get field with child annotations
        var field = (Aspose.Pdf.Forms.Field)document.Form["1 Vehicle Identification Number"];
        // Get first child annotation
        var annotation = field[1];
        // Remove the annotation
        document.Pages[annotation.PageIndex].Annotations.Remove(annotation);

        // Save PDF document
        document.Save(dataDir + "RemoveChildAnnotation_out.pdf");
    }
}
```

## Aspose.PDF 23.8의 새로운 기능

23.8부터 증분 업데이트 감지 추가를 지원합니다.

PDF 문서에서 증분 업데이트를 감지하는 기능이 추가되었습니다. 이 기능은 문서가 증분 업데이트로 저장된 경우 'true'를 반환하고, 그렇지 않으면 'false'를 반환합니다.

```cs
private static bool HasIncrementalUpdate()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PdfWithIncrementalUpdate.pdf"))
    {
        // New method
        bool hasIncrementalUpdate = document.HasIncrementalUpdate();

        Console.WriteLine("Document {0} incremental update check returns: {1}", document.FileName, hasIncrementalUpdate);
        return hasIncrementalUpdate;
    }
}
```

또한 23.8에서는 중첩된 체크박스 필드 작업 방법을 지원합니다. 많은 채우기 가능한 PDF 양식에는 라디오 그룹처럼 작동하는 체크박스 필드가 있습니다:

- 다중 값 체크박스 필드 생성:

```cs
private static void CreateMultivalueCheckboxField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        var checkbox = new Aspose.Pdf.Forms.CheckboxField(page, new Aspose.Pdf.Rectangle(50, 50, 70, 70));

        // Set the first checkbox group option value
        checkbox.ExportValue = "option 1";

        // Add new option right under existing ones
        checkbox.AddOption("option 2");

        // Add new option at the given rectangle
        checkbox.AddOption("option 3", new Aspose.Pdf.Rectangle(100, 100, 120, 120));

        document.Form.Add(checkbox);

        // Select the added checkbox
        checkbox.Value = "option 2";

        // Save PDF document
        document.Save(dataDir + "MultivalueCheckboxField.pdf");
    }
}
```

- 다중 값 체크박스의 값 가져오기 및 설정:

```cs
private static void GetAndSetValueOfMultivalueCheckboxField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "MultivalueCheckboxField.pdf"))
    {
        var form = document.Form;
        var checkbox = form.Fields[0] as Aspose.Pdf.Forms.CheckboxField;

        // Allowed values may be retrieved from the AllowedStates collection
        // Set the checkbox value using Value property
        checkbox.Value = checkbox.AllowedStates[0];
        var checkboxValue = checkbox.Value; // the previously set value, e.g. "option 1"

        // The value should be any element of AllowedStates
        checkbox.Value = "option 2";
        checkboxValue = checkbox.Value; // option 2

        // Uncheck boxes by either setting Value to "Off" or setting Checked to false
        checkbox.Value = "Off";
        // or, alternately:
        // checkbox.Checked = false;
        checkboxValue = checkbox.Value; // Off
    }
}
```

## Aspose.PDF 23.7의 새로운 기능

Aspose.PDF 23.7부터 도형 추출 추가를 지원합니다:

```cs
private static void CopyShape()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Graphs();

    // Open PDF document
    using (var sourceDocument = new Aspose.Pdf.Document(dataDir + "test.pdf"))
    {
        // Create PDF document
        using (var destDocument = new Aspose.Pdf.Document())
        {
            // Absorb vector graphics from the source document
            var graphicAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber();
            graphicAbsorber.Visit(sourceDocument.Pages[1]);

            // Copy the graphics into the destination document specified page and area
            var area = new Aspose.Pdf.Rectangle(90, 250, 300, 400);
            destDocument.Pages[1].AddGraphics(graphicAbsorber.Elements, area);

            // Save PDF document
            destDocument.Save(dataDir + "CopyShape_out.pdf");
        }
    }
}
```

또한 텍스트 추가 시 오버플로우를 감지하는 기능을 지원합니다:

```cs
private static void FitTextIntoRectangle()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document()) 
    {
        // Generate text to add: "Lorem Ipsum" text of 1000 characters
        var paragraphContent = RunExamples.GetLoremIpsumString(1000);
        // Create a text fragment with the desired text
        var fragment = new Aspose.Pdf.Text.TextFragment(paragraphContent);
        // Declare the rectangle to fit text into
        var rectangle = new Aspose.Pdf.Rectangle(100, 600, 500, 700, false);
        
        // Check whether the text fits into the rectangle
        var isFitRectangle = fragment.TextState.IsFitRectangle(paragraphContent, rectangle);

        // Iteratively decrease font size until text fits the rectangle
        while (!isFitRectangle)
        {
            fragment.TextState.FontSize -= 0.5f;
            isFitRectangle = fragment.TextState.IsFitRectangle(paragraphContent, rectangle);
        }

        // Create a paragraph from the text fragment in the specified rectangle. Now you may be sure it fits.
        var paragraph = new Aspose.Pdf.Text.TextParagraph();
        paragraph.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        paragraph.FormattingOptions.WrapMode = Aspose.Pdf.Text.TextFormattingOptions.WordWrapMode.ByWords;
        paragraph.Rectangle = rectangle;
        paragraph.AppendLine(fragment);

        // Create a text builder to place the paragraph on the document page
        var builder = new Aspose.Pdf.Text.TextBuilder(document.Pages.Add());
        builder.AppendParagraph(paragraph);

        // Save PDF document
        document.Save(dataDir + "FitTextIntoRectangle_out.pdf");
    }
}
```

## Aspose.PDF 23.6의 새로운 기능

Aspose.PDF 23.6부터 다음 플러그인을 추가하는 기능을 지원합니다:

- Aspose PdfConverter HTML에서 PDF로 
- Aspose PdfOrganizer 크기 조정 API
- Aspose PdfOrganizer 압축 API

Aspose.PdfForm 업데이트 
- 문서의 필드에서 "값"을 CSV 파일로 내보내는 기능 추가
- 개별 필드에 대한 속성 설정 기능 추가

또한 HTML, Epub 페이지의 제목을 설정하는 기능을 추가합니다:

```cs
private static void SetHtmlTitle()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        var options = new Aspose.Pdf.HtmlSaveOptions
        {
            ExplicitListOfSavedPages = new[] { 1 },
            SplitIntoPages = false,
            FixedLayout = true,
            CompressSvgGraphicsIfAny = false,
            SaveTransparentTexts = true,
            SaveShadowedTextsAsTransparentTexts = true,
            FontSavingMode = Aspose.Pdf.HtmlSaveOptions.FontSavingModes.AlwaysSaveAsWOFF,
            RasterImagesSavingMode = Aspose.Pdf.HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground,
            PartsEmbeddingMode = Aspose.Pdf.HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml,
            // New property
            Title = "Title for page"
        };

        // Save HTML document
        document.Save(dataDir + "SetHtmlTitle_out.html", options);
    }
}
```

## Aspose.PDF 23.5의 새로운 기능

23.5부터 RedactionAnnotation FontSize 옵션을 추가하는 기능을 지원합니다. 이 작업을 해결하기 위해 다음 코드 스니펫을 사용합니다:

```cs
private static void AddRedactionAnnotationFontSize() 
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf")) 
    {
        // Create RedactionAnnotation instance for specific page region
        var annot = new Aspose.Pdf.Annotations.RedactionAnnotation(document.Pages[1],
            new Aspose.Pdf.Rectangle(367, 756.919982910156, 420, 823.919982910156));
        annot.FillColor = Aspose.Pdf.Color.Black;

        annot.BorderColor = Aspose.Pdf.Color.Yellow;
        annot.Color = Aspose.Pdf.Color.Blue;
        // Text to be printed on redact annotation
        annot.OverlayText = "(Unknown)";
        annot.TextAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        // Repat Overlay text over redact Annotation
        annot.Repeat = false;

        // New property
        annot.FontSize = 20;

        // Add annotation to annotations collection of first page
        document.Pages[1].Annotations.Add(annot);
        // Flattens annotation and redacts page contents (i.e. removes text and image under redacted annotation)
        annot.Redact();
        // Save PDF document
        document.Save(dataDir + "AddRedactionAnnotationFontSize_out.pdf");
    }
}
```

## Aspose.PDF 23.4의 새로운 기능

Aspose.PDF는 .NET 7 SDK의 출시를 발표했습니다.

## Aspose.PDF 23.3.1의 새로운 기능

Aspose.PDF 23.3부터 다음 플러그인을 추가하는 기능을 지원합니다:

- Aspose.PdfForm
- Aspose.PdfConverter PDF에서 HTML로
- Aspose.PdfConverter PDF에서 XLSX로
- Aspose.PdfOrganizer 회전
- Aspose.PdfExtrator 이미지용

## Aspose.PDF 23.3의 새로운 기능

23.3 버전에서는 페이지에 삽입할 때 이미지 비율과 해상도를 유지하는 기능이 도입되었습니다. 이 문제를 해결하기 위해 두 가지 방법을 사용할 수 있습니다:

```cs
private static void InsertImageWithNativeResolutionAsTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        var table = new Aspose.Pdf.Table
        {
            ColumnWidths = "600"
        };

        for (var j = 0; j < 2; j++)
        {
            var row = table.Rows.Add();
            var cell = row.Cells.Add();
            cell.Paragraphs.Add(new Aspose.Pdf.Image()
            {
                IsApplyResolution = true,
                File = dataDir + "Image1.jpg"
            });
        }

        page.Paragraphs.Add(table);

        // Save PDF document
        document.Save(dataDir + "ImageWithNativeResolutionAsTable_out.pdf");
    }
}
```

두 번째 접근 방식:

```cs
private static void InsertImageWithNativeResolutionAsParagraph()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        for (var j = 0; j < 2; j++)
        {
            page.Paragraphs.Add(new Aspose.Pdf.Image()
            {
                IsApplyResolution = true,
                File = dataDir + "Image1.jpg"
            });
        }

        // Save PDF document
        document.Save(dataDir + "ImageWithNativeResolutionAsParagraph_out.pdf");
    }
}
```

이미지는 크기가 조정된 크기와 원래 해상도로 배치됩니다. FixedWidth 또는 FixedHeight 속성을 IsApplyResolution과 조합하여 설정할 수 있습니다.


## Aspose.PDF 23.1.1의 새로운 기능

Aspose.PDF 23.1.1부터 다음 플러그인을 추가하는 기능을 지원합니다:

- Aspose.PdfOrganizer 플러그인
- Aspose.PdfExtractor 플러그인

## Aspose.PDF 23.1의 새로운 기능

23.1 버전부터 PrinterMark 주석을 생성하는 기능을 지원합니다.

프린터 마크는 다중 판 작업의 구성 요소를 식별하고 생산 중 일관된 출력을 유지하는 데 도움을 주기 위해 페이지에 추가된 그래픽 기호 또는 텍스트입니다. 인쇄 산업에서 일반적으로 사용되는 예로는:

- 판 정렬을 위한 등록 목표
- 색상 및 잉크 밀도를 측정하기 위한 회색 램프 및 색상 막대
- 출력 매체가 잘릴 위치를 나타내는 컷 마크

색상 및 잉크 밀도를 측정하기 위한 색상 막대 옵션의 예를 보여드리겠습니다. 기본 추상 클래스 PrinterMarkAnnotation에서 자식 ColorBarAnnotation이 구현되어 있습니다. 예제를 확인해 보겠습니다:

```cs
private static void AddPrinterMarkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        page.TrimBox = new Aspose.Pdf.Rectangle(20, 20, 580, 820);

        var rectBlack = new Aspose.Pdf.Rectangle(100, 300, 300, 320);
        var rectCyan = new Aspose.Pdf.Rectangle(200, 600, 260, 690);
        var rectMagenta = new Aspose.Pdf.Rectangle(10, 650, 140, 670);

        var colorBarBlack = new Aspose.Pdf.Annotations.ColorBarAnnotation(page, rectBlack);
        var colorBarCyan = new Aspose.Pdf.Annotations.ColorBarAnnotation(page, rectCyan,
            Aspose.Pdf.Annotations.ColorsOfCMYK.Cyan);
        var colorBarMagenta = new Aspose.Pdf.Annotations.ColorBarAnnotation(page, rectMagenta);
        colorBarMagenta.ColorOfCMYK = Aspose.Pdf.Annotations.ColorsOfCMYK.Magenta;
        var colorBarYellow = new Aspose.Pdf.Annotations.ColorBarAnnotation(page,
            new Aspose.Pdf.Rectangle(400, 250, 450, 700), Aspose.Pdf.Annotations.ColorsOfCMYK.Yellow);

        page.Annotations.Add(colorBarBlack);
        page.Annotations.Add(colorBarCyan);
        page.Annotations.Add(colorBarMagenta);
        page.Annotations.Add(colorBarYellow);

        // Save PDF document
        document.Save(dataDir + "PrinterMarkAnnotation_out.pdf");
    }
}
```
또한 벡터 이미지 추출을 지원합니다. 다음 코드를 사용하여 벡터 그래픽을 감지하고 추출해 보세요:

```cs
private static void SavePdfVectorGraphicToSvg()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Graphs();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "test.pdf"))
    {
        // Attempt to save the vector graphics into a specified SVG file
        document.Pages[1].TrySaveVectorGraphics(dataDir + "PdfVectorGraphicToSvg.svg");
    }
}
```

## Aspose.PDF 22.12의 새로운 기능

이번 릴리스에서는 PDF를 DICOM 이미지로 변환하는 기능을 지원합니다.

```cs
private static void PdfToDicom()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PagesToImages.pdf"))
    {
        var dicom = new Aspose.Pdf.Devices.DicomDevice();
        FileStream outStream = new FileStream(dataDir + "PdfToDicom_out.dcm", FileMode.Create, FileAccess.ReadWrite);
        dicom.Process(document.Pages[1], outStream);
    }
}
```    

## Aspose.PDF 22.09의 새로운 기능

22.09부터 서명에서 주제 제목의 순서를 수정하는 속성을 추가하는 기능을 지원합니다 (E=, CN=, O=, OU=, ).

```cs
private static void SignPdfWithModifiedOrderOfSubjectRubrics(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Instantiate PdfFileSignature object
    using (var fileSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        fileSign.BindPdf(dataDir + "DigitallySign.pdf");

        var rect = new System.Drawing.Rectangle(100, 100, 400, 100);
        var signature = new Aspose.Pdf.Forms.PKCS7Detached(pfxFilePath, password);

        // Set signature custom appearance
        signature.CustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance()
        {
            UseDigitalSubjectFormat = true,
            DigitalSubjectFormat = new Aspose.Pdf.Forms.SubjectNameElements[] { Aspose.Pdf.Forms.SubjectNameElements.CN, Aspose.Pdf.Forms.SubjectNameElements.O }
            //or
            //DigitalSubjectFormat = new Aspose.Pdf.Forms.SubjectNameElements[] { Aspose.Pdf.Forms.SubjectNameElements.OU, Aspose.Pdf.Forms.SubjectNameElements.S, Aspose.Pdf.Forms.SubjectNameElements.C }
        };

        // Sign PDF file
        fileSign.Sign(1, true, rect, signature);
        // Save PDF document
        fileSign.Save(dataDir + "SignPdfWithModifiedOrderOfSubjectRubrics_out.pdf");
    }
}
```

## Aspose.PDF 22.6의 새로운 기능

22.5부터 PDF에서 SubScript 및 SuperScript 텍스트를 추출하는 기능을 지원합니다.

PDF 문서에 H2O와 같은 SubScript 및 SuperScript 텍스트가 포함된 경우 PDF에서 텍스트를 추출할 때 해당 서식 정보도 추출해야 합니다(추출된 일반 텍스트에서).
PDF에 기울임꼴 텍스트가 포함된 경우에도 추출된 콘텐츠에 포함되어야 합니다.

```cs
private static void ExtractTextSuperscript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextWithSubscriptsSuperscripts.pdf"))
    {
        // Use TextFragmentAbsorber with no parameters to get all text
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        absorber.Visit(document.Pages[1]);

        // Iterate through text fragments to find superscript text
        foreach (var textFragment in absorber.TextFragments) 
        {
            if (textFragment.TextState.Superscript)
            {
                Console.WriteLine(String.Format("Text {0} at {1} is superscript!", textFragment.Text, textFragment.Position));
            }
        }
    }
}
```

## Aspose.PDF 22.4의 새로운 기능

이번 릴리스에는 Aspose.PDF for .NET에 대한 정보가 포함되어 있습니다:

- PDF에서 ODS로: SubScript 및 SuperScript의 텍스트 인식;

**예제**

```cs
private static void ConvertPdfToOds()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            // Specify the desired table file format
            Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.ODS
        };

        // Save the file in ODS format
        document.Save(dataDir + "PDFToODS_out.ods", saveOptions);
    }
}
```

- PDF에서 XMLSpreadSheet2003으로: SubScript 및 SuperScript의 텍스트 인식;

- PDF에서 Excel로: SubScript 및 SuperScript의 텍스트 인식;

- 문서를 저장할 때 UR 서명 제거;

- 문서를 저장할 때 MarkInfo에서 Suspects 플래그 제거;

- 문서를 저장할 때 정보 제거

## Aspose.PDF 22.3의 새로운 기능

이번 릴리스에는 다음 업데이트가 포함되어 있습니다:

- AFRelationship 지원;

- PDF 헤더 검증;

- 문서를 저장할 때 adbe.x509.rsa_sha1 서브필터 제거;

- 필드를 숫자 및 날짜 형식으로 포맷;

- FDF 2.0에서 RC4 암호화 사용 금지;

## Aspose.PDF 22.2의 새로운 기능

22.2 버전부터 LTV와 함께 PdfFileSignature를 사용하여 문서에 서명할 수 있으며, SHA1에서 SHA256으로 해싱을 변경할 수 있습니다.

```csharp
private static void SignPdfWithSha256(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Instantiate PdfFileSignature object
    using (var fileSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        fileSign.BindPdf(dataDir + "DigitallySign.pdf");

        var rect = new System.Drawing.Rectangle(300, 100, 1, 1);
        var signature = new Aspose.Pdf.Forms.PKCS7(pfxFilePath, password)
        {
            UseLtv = true,
            TimestampSettings = new Aspose.Pdf.TimestampSettings("http://freetsa.org/tsr", string.Empty, Aspose.Pdf.DigestHashAlgorithm.Sha256)
        };

        // Sign PDF file
        fileSign.Sign(1, false, rect, signature);
        // Save PDF document
        fileSign.Save(dataDir + "SignPdfWithSha256_out.pdf");
    }
}
```

## Aspose.PDF 22.1의 새로운 기능

이제 Aspose.PDF for .NET은 가장 인기 있는 문서 형식 중 하나인 Portable Document Format (PDF) 버전 2.0에서 문서를 로드하는 것을 지원합니다.

## Aspose.PDF 21.11의 새로운 기능

### 비라틴 문자를 비밀번호에 허용

```csharp
private static void EncriptPdfNonlatinPassCharacters()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "input.pdf");
        // Encrypt file using 256-bit encryption
        bool isSuccessful = fileSecurity.EncryptFile("æøå", "æøå", Aspose.Pdf.Facades.DocumentPrivilege.Print,
            Aspose.Pdf.Facades.KeySize.x256, Aspose.Pdf.Facades.Algorithm.AES);
        Console.WriteLine(isSuccessful);
        // Save PDF document
        fileSecurity.Save(dataDir + "PdfNonlatinPassEncrypted_out.pdf");
    }
}
```

## Aspose.PDF 21.10의 새로운 기능

### 숨겨진 텍스트를 감지하는 방법은?

TextState.Invisible을 사용하여 렌더링 모드 설정에서 텍스트의 가시성에 대한 정보를 얻으십시오.

테스트에 사용한 코드는 다음과 같습니다:

```csharp
private static void DisplayTextInvisibility()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PdfWithHiddenText.pdf"))
    {
        Console.WriteLine(document.FileName);

        // Use TextFragmentAbsorber with no parameters to get all text
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        absorber.Visit(document.Pages[1]);
        var textFragmentCollection = absorber.TextFragments;

        // Iterate through text fragments to find hidden text
        for (int i = 1; i <= textFragmentCollection.Count; i++)
        {
            var fragment = textFragmentCollection[i];
            Console.WriteLine("Fragment {0} at {1}", i, fragment.Rectangle.ToString());
            Console.WriteLine("Text: {0}", fragment.Text);
            Console.WriteLine("RenderingMode: {0}", fragment.TextState.RenderingMode.ToString());
            Console.WriteLine("Invisibility: {0}", fragment.TextState.Invisible);
            Console.WriteLine("---");
        }
    }
}
```

### PDF 문서에서 레이어 수에 대한 정보를 얻는 방법은?

```csharp
private static void GetPdfLayers()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Layers();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PdfWithLayers.pdf"))
    {
        // Get layers from the first page
        var layers = document.Pages[1].Layers;
        // Save each layer to the output path
        foreach (var layer in layers)
        {
            Console.WriteLine("Document {0} contains a layer named: {1} ", document.FileName, layer.Name);
        }
    }
}
```

## Aspose.PDF 21.9의 새로운 기능

Aspose.PDF for .NET을 사용하여 서명 영역의 레이블의 배경색과 글꼴 색상을 사용자 정의합니다.

```csharp
private static void SignPdfWithCustomColorsInAppearance(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Instantiate PdfFileSignature object
    using (var pdfFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "DigitallySign.pdf");
        var rect = new System.Drawing.Rectangle(310, 45, 200, 50);
        // Create PKCS#7 object for sign
        var pkcs = new Aspose.Pdf.Forms.PKCS7(pfxFilePath, password);

        // Set signature custom appearance
        pkcs.CustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance()
        {
            // Set colors
            ForegroundColor = Aspose.Pdf.Color.DarkGreen,
            BackgroundColor = Aspose.Pdf.Color.LightSeaGreen,
        };
        // Sign PDF file
        pdfFileSignature.Sign(1, true, rect, pkcs);
        // Save PDF document
        pdfFileSignature.Save(dataDir + "SignPdfWithCustomColorsInAppearance_out.pdf");
    }
}
```

## Aspose.PDF 21.8의 새로운 기능

### 디지털 서명에서 텍스트 색상을 변경하는 방법은?

21.8 버전에서 ForegroundColor 속성을 사용하여 디지털 서명에서 텍스트 색상을 변경할 수 있습니다.

```csharp
private static void SignPdfWithForegroundColorInAppearance(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Instantiate PdfFileSignature object
    using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfSign.BindPdf(dataDir + "DigitallySign.pdf");
        var rect = new System.Drawing.Rectangle(310, 45, 200, 50);
        // Create PKCS#7 object for sign
        var pkcs = new Aspose.Pdf.Forms.PKCS7(pfxFilePath, password);

        // Set signature custom appearance
        pkcs.CustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance()
        {
            // Set text color
            ForegroundColor = Aspose.Pdf.Color.Green
        };
        // Sign PDF file
        pdfSign.Sign(1, true, rect, pkcs);
        // Save PDF document
        pdfSign.Save(dataDir + "SignPdfWithForegroundInAppearance_out.pdf");
    }
}
```

## Aspose.PDF 21.7의 새로운 기능

### 매개변수를 사용하여 XML 및 XLS 기반 PDF 생성

XSL 매개변수를 추가하려면 [XsltArgumentList](https://docs.microsoft.com/en-us/dotnet/api/system.xml.xsl.xsltargumentlist?view=net-5.0)를 생성하고 [XslFoLoadOptions](https://reference.aspose.com/pdf/ko/net/aspose.pdf/xslfoloadoptions)에서 속성으로 설정해야 합니다. 다음 스니펫은 위에서 설명한 샘플 파일과 함께 이 클래스를 사용하는 방법을 보여줍니다.

```csharp
private static void ConvertXslfoToPdfWithArgumentList()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Create convert options
    var options = new Aspose.Pdf.XslFoLoadOptions(dataDir + "XSLFOToPdfInput.xslt");

    // Example of using XsltArgumentList
    options.XsltArgumentList = new XsltArgumentList();
    options.XsltArgumentList.AddParam("isBoldName", "", "yes");

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "XSLFOToPdfInput.xml", options))
    {
        // Save PDF document
        document.Save(dataDir + "XslfoToPdfWithArgumentList_out.pdf");
    }
}
```

## Aspose.PDF 21.6의 새로운 기능

Aspose.PDF for .NET을 사용하여 문서에서 ImagePlacementAbsorber를 사용하여 이미지를 숨길 수 있습니다:

```csharp
private static void HideImageInPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImagePlacement.pdf"))
    {
        // Create ImagePlacementAbsorber instance
        var absorber = new Aspose.Pdf.ImagePlacementAbsorber();
        // Load the images of the first page
        document.Pages[1].Accept(absorber);

        // Iterate through each image placement on the first page
        foreach (var imagePlacement in absorber.ImagePlacements)
        {
            // Hide image
            imagePlacement.Hide();
        }

        // Save PDF document
        document.Save(dataDir + "HideImageInPdf_out.pdf");
    }
}
```

## Aspose.PDF 21.5의 새로운 기능

### PDF에서 설명/리소스에서 글꼴 전체 이름을 추출하는 방법은?

Font 클래스의 BaseFont 속성을 사용하여 접두사가 있는 전체 글꼴을 얻을 수 있습니다.

```csharp
private static void DisplayFontFullNames()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "BreakfastMenu.pdf"))
    {
        // Get document fonts
        var fonts = document.FontUtilities.GetAllFonts();

        // Iterate through the fonts
        foreach (var font in fonts)
        {
            // Show font names
            Console.WriteLine($"font name : {font.FontName} BaseFont name : {font.BaseFont}");
        }
    }
}
```

## Aspose.PDF 21.4의 새로운 기능

### 이미지를 병합하는 API 추가

Aspose.PDF 21.4에서는 이미지를 결합할 수 있습니다. 다음 코드 스니펫을 따르십시오:

```csharp
private static void MergeAsJpeg()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    List<Stream> inputImagesStreams = new List<Stream>();
    using (FileStream firstImageStream = new FileStream(dataDir + "aspose.jpg", FileMode.Open))
    {
        inputImagesStreams.Add(firstImageStream);
        using (FileStream secondImageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open))
        {
            inputImagesStreams.Add(secondImageStream);

            // Invoke PdfConverter.MergeImages to perform merge
            using (Stream inputStream = Aspose.Pdf.Facades.PdfConverter.MergeImages(inputImagesStreams,
                  Aspose.Pdf.Drawing.ImageFormat.Jpeg, Aspose.Pdf.Facades.ImageMergeMode.Vertical, 1, 1))
            {
                using (FileStream outputStream = new FileStream(dataDir + "Merge_out.jpg", FileMode.Create))
                {
                    byte[] buffer = new byte[32768];
                    int read;
                    while ((read = inputStream.Read(buffer, 0, buffer.Length)) > 0)
                    {
                        outputStream.Write(buffer, 0, read);
                    }
                }
            }
        }
    }
}
```

또한 이미지를 Tiff 형식으로 병합할 수 있습니다:

```csharp
private static void MergeAsTiff()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    List<Stream> inputImagesStreams = new List<Stream>();
    using (FileStream firstImageStream = new FileStream(dataDir + "aspose.jpg", FileMode.Open))
    {
        inputImagesStreams.Add(firstImageStream);
        using (FileStream secondImageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open))
        {
            inputImagesStreams.Add(secondImageStream);

            // Invoke PdfConverter.MergeImagesAsTiff to perform merge
            using (Stream inputStream = Aspose.Pdf.Facades.PdfConverter.MergeImagesAsTiff(inputImagesStreams))
            {
                using (FileStream outputStream = new FileStream(dataDir + "Merge_out.tiff", FileMode.Create))
                {
                    byte[] buffer = new byte[32768];
                    int read;
                    while ((read = inputStream.Read(buffer, 0, buffer.Length)) > 0)
                    {
                        outputStream.Write(buffer, 0, read);
                    }
                }
            }
        }
    }
}
```

## Aspose.PDF 21.3의 새로운 기능

### Azure 정보 보호 감지를 위한 속성 공개

다음 코드 스니펫을 사용하여 Azure 정보 보호로 보호된 PDF 파일의 암호화된 페이로드에 접근할 수 있어야 합니다:

```csharp
private static void AzureInformationProtection()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetAlltheAttachments.pdf"))
    {
        if (document.EmbeddedFiles[1].AFRelationship == Aspose.Pdf.AFRelationship.EncryptedPayload)
        {
            if (document.EmbeddedFiles[1].EncryptedPayload != null)
            {
                // document.EmbeddedFiles[1].EncryptedPayload.Type == "EncryptedPayload"
                // document.EmbeddedFiles[1].EncryptedPayload.Subtype == "MicrosoftIRMServices"
                // document.EmbeddedFiles[1].EncryptedPayload.Version == "2"
            }
        }
    }
}
```

## Aspose.PDF 21.1의 새로운 기능

### TextFragment의 배경색을 검색하는 기능 추가

이 버전의 Aspose.PDF에서는 배경색을 검색하는 기능이 제공됩니다. TextFragmentAbsorber 객체의 옵션에서 searchOptions.SearchForTextRelatedGraphics = true;를 지정해야 합니다.

다음 코드를 고려하십시오:

```csharp
private static void DisplayPdfTextBackgroundColor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PdfWithTextBackgroundColor.pdf"))
    {
        // Use TextFragmentAbsorber with no parameters to get all text
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber();

        var searchOptions = new Aspose.Pdf.Text.TextSearchOptions(false);
        // Setting this option into the 'true' is necessary 
        searchOptions.SearchForTextRelatedGraphics = true;
        textFragmentAbsorber.TextSearchOptions = searchOptions;

        // Accept the absorber for all the pages
        document.Pages.Accept(textFragmentAbsorber);
        
        // Loop through the fragments
        foreach (var textFragment in textFragmentAbsorber.TextFragments)
        {
            Console.WriteLine("Text: '{0}'", textFragment.Text);
            Console.WriteLine("BackgroundColor: '{0}'", textFragment.TextState.BackgroundColor);
            Console.WriteLine("ForegroundColor: '{0}'", textFragment.TextState.ForegroundColor);
            Console.WriteLine("Segment BackgroundColor: '{0}'", textFragment.Segments[1].TextState.BackgroundColor);
        }
    }
}
```

### HTML로 변환 후 글꼴이 출력에 완전히 포함됩니다.

또한 Aspose.PDF 21.1에서는 PDF를 HTML로 변환한 후 출력 HTML 문서에 포함된 글꼴이 제공됩니다. 이는 새로운 부울 저장 옵션 HtmlSaveParameter.SaveFullFont 덕분입니다.

다음은 코드 스니펫입니다:

```csharp
private static void PdfToHtmlWithFullFont()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML SaveOptions object
        var options = new Aspose.Pdf.HtmlSaveOptions
        {
            RasterImagesSavingMode = Aspose.Pdf.HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground,
            PartsEmbeddingMode = Aspose.Pdf.HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml,
            LettersPositioningMethod = Aspose.Pdf.HtmlSaveOptions.LettersPositioningMethods.UseEmUnitsAndCompensationOfRoundingErrorsInCss,
            FontSavingMode = Aspose.Pdf.HtmlSaveOptions.FontSavingModes.AlwaysSaveAsTTF,
            SaveTransparentTexts = true,
            // New option
            SaveFullFont = true
        };
        // Save HTML document
        document.Save(dataDir + "PdfToHtmlWithFullFont_out.html", options);
    }
}
```