---
title: PDF 파일 비밀번호 변경
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ko/net/change-password/
description: Aspose.PDF를 사용하여 .NET에서 PDF 문서의 비밀번호를 수정하여 파일 보안을 향상시키는 방법을 알아보세요.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Change Password of PDF File",
    "alternativeHeadline": "Securely Change PDF Passwords with Ease",
    "abstract": "PdfFileSecurity 클래스를 사용하여 PDF 보안을 쉽게 강화할 수 있습니다. 이 기능은 사용자가 사용자 및 소유자 비밀번호를 모두 수정할 수 있도록 하여 무단 접근에 대한 강력한 보호를 보장하며 권한을 효과적으로 관리합니다. 간단한 구현으로 문서 보안 설정을 손쉽게 최적화하세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "250",
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
    "url": "/net/change-password/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/change-password/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 단순하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

## PDF 파일 비밀번호 변경

PDF 파일의 비밀번호를 변경하려면 [PdfFileSecurity](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffilesecurity) 객체를 생성한 다음 [ChangePassword](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2) 메서드를 호출해야 합니다. 기존 소유자 비밀번호와 새로운 사용자 및 소유자 비밀번호를 [ChangePassword](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2) 메서드에 전달해야 합니다.

{{% alert color="primary" %}}

- **사용자 비밀번호**가 설정된 경우, PDF를 열기 위해 제공해야 하는 비밀번호입니다. Acrobat/Reader는 사용자에게 사용자 비밀번호를 입력하라는 메시지를 표시합니다. 비밀번호가 올바르지 않으면 문서가 열리지 않습니다.
- **소유자 비밀번호**가 설정된 경우, 인쇄, 편집, 추출, 주석 달기 등의 권한을 제어합니다. Acrobat/Reader는 권한 설정에 따라 이러한 작업을 허용하지 않습니다. 권한을 설정/변경하려면 이 비밀번호가 필요합니다.

{{% /alert %}}

다음 코드 스니펫은 PDF 파일의 비밀번호를 변경하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangePassword()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdfFileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample_encrypted.pdf"))
    {
        // Create PdfFileSecurity object if the document is encrypted
        if (pdfFileInfo.IsEncrypted)    
        {
            using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
            {
                // Bind PDF document
                fileSecurity.BindPdf(dataDir + "sample_encrypted.pdf");
                fileSecurity.ChangePassword("OwnerP@ssw0rd", "Pa$$w0rd1", "Pa$$w0rd2", Aspose.Pdf.Facades.DocumentPrivilege.Print, Aspose.Pdf.Facades.KeySize.x256);
                // Save PDF document
                fileSecurity.Save(dataDir + "sample_encrtypted1.pdf");
            }
        }
    }
}
```