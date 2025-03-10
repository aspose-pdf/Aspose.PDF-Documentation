---
title: PDF 파일 복호화
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/decrypt-pdf-file/
description: Aspose.PDF를 사용하여 .NET에서 비밀번호로 보호된 PDF 파일을 복호화하는 방법을 탐색하여 문서의 내용에 접근할 수 있도록 합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Decrypt PDF File",
    "alternativeHeadline": "Unlock Encrypted PDFs with Ease Using PdfFileSecurity",
    "abstract": "PdfFileSecurity 클래스를 사용하여 새로운 PDF 파일 복호화 기능으로 PDF 문서를 손쉽게 잠금 해제하세요. 이 기능은 사용자가 암호화된 PDF에서 비밀번호 보호를 제거할 수 있게 하여 문서에 대한 원활한 접근 및 조작을 가능하게 합니다. 강력한 DecryptFile 메서드를 활용하여 안전한 PDF 처리를 통해 문서 관리에 대한 간단한 접근 방식을 경험하세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "235",
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
    "url": "/net/decrypt-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/decrypt-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

비밀번호 또는 인증서로 암호화된 PDF 문서는 다른 작업을 수행하기 전에 잠금을 해제해야 합니다. 암호화된 PDF 문서에서 작업을 시도하면 예외가 발생합니다. 암호화된 PDF의 잠금을 해제한 후에는 하나 이상의 작업을 수행할 수 있습니다.

## 소유자 비밀번호를 사용하여 PDF 파일 복호화

{{% alert color="primary" %}}
온라인으로 시도해 보세요 <br>
Aspose.PDF를 사용하여 문서의 잠금을 해제하고 이 링크에서 결과를 확인할 수 있습니다:
[products.aspose.app/pdf/unlock](https://products.aspose.app/pdf/unlock)

{{% /alert %}}

PDF 파일을 복호화하려면 [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) 객체를 생성한 다음 [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile) 메서드를 호출해야 합니다. 또한 [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile) 메서드에 소유자 비밀번호를 전달해야 합니다. 다음 코드 스니펫은 PDF 파일을 복호화하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DecryptPDFFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdfFileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample_encrypted.pdf"))
    {
        if (pdfFileInfo.IsEncrypted)
        {
            using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
            {
                // Bind PDF document
                fileSecurity.BindPdf(dataDir + "sample_encrypted.pdf");
                // Decrypt PDF document
                fileSecurity.DecryptFile("P@ssw0rd");
                // Save PDF document
                fileSecurity.Save(dataDir + "SampleDecrtypted_out.pdf");
            }
        }
    }
}
```