---
title: PDF에 권한 설정
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ko/net/set-privileges/
description: Aspose.PDF를 사용하여 PDF 파일에서 사용자 권한을 수정하고 특정 작업을 제한하는 방법을 알아보세요.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set Privileges on PDF",
    "alternativeHeadline": "Set Custom Permissions for PDF Document Security",
    "abstract": "PdfFileSecurity 클래스를 사용하여 기존 PDF 파일에 권한을 설정하는 새로운 기능을 소개합니다. 이를 통해 사용자는 인쇄 및 복사와 같은 작업에 대한 권한을 지정할 수 있습니다. 또한 사용자는 이제 PDF 문서에서 확장된 권한을 쉽게 제거할 수 있어 문서 수정 및 보안에 대한 더 큰 제어를 보장합니다. 이 기능은 PDF 관리를 간소화하면서 보안 준수를 강화합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "436",
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
    "url": "/net/set-privileges/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-privileges/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

## 기존 PDF 파일에 권한 설정

PDF 파일의 권한을 설정하려면 [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) 객체를 생성하고 SetPrivilege 메서드를 호출합니다. DocumentPrivilege 객체를 사용하여 권한을 지정한 다음 이 객체를 SetPrivilege 메서드에 전달할 수 있습니다. 다음 코드 조각은 PDF 파일의 권한을 설정하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrivilege1()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Create DocumentPrivileges object and set needed privileges
    var privilege = Aspose.Pdf.Facades.DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "sample.pdf");
        // Set privilege
        fileSecurity.SetPrivilege(privilege);
        // Save PDF document
        fileSecurity.Save(dataDir + "SamplePrivileges_out.pdf");
    }
}
```

비밀번호를 지정하는 다음 메서드를 참조하세요:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrivilegeWithPassword()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Create DocumentPrivileges object and set needed privileges
    var privilege = Aspose.Pdf.Facades.DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "sample.pdf");
        // Set privilege and passwords
        fileSecurity.SetPrivilege(string.Empty, "P@ssw0rd", privilege);
        // Save PDF document
        fileSecurity.Save(dataDir + "SamplePrivilegesPassword_out.pdf");
    }
}
```

## PDF에서 확장된 권한 기능 제거

PDF 문서는 사용자가 Adobe Acrobat Reader를 사용하여 양식 필드에 데이터를 입력하고 채워진 양식의 복사본을 저장할 수 있도록 하는 확장된 권한 기능을 지원합니다. 그러나 이는 PDF 파일이 수정되지 않도록 보장하며, PDF 구조에 대한 수정이 이루어지면 확장된 권한 기능이 손실됩니다. 이러한 문서를 볼 때 문서가 수정되었기 때문에 확장된 권한이 제거되었다는 오류 메시지가 표시됩니다. 최근에 PDF 문서에서 확장된 권한을 제거하라는 요구가 있었습니다.

PDF 파일에서 확장된 권한을 제거하려면 PdfFileSignature 클래스에 RemoveUsageRights()라는 새로운 메서드가 추가되었습니다. 소스 PDF에 확장된 권한이 포함되어 있는지 확인하기 위해 ContainsUsageRights()라는 또 다른 메서드가 추가되었습니다.

{{% alert color="primary" %}}
Aspose.PDF for .NET 9.5.0부터 다음 메서드의 이름이 업데이트되었습니다. 이전 메서드는 여전히 API에 있지만 더 이상 사용되지 않도록 표시되었으며 제거될 예정입니다. 따라서 업데이트된 메서드를 사용해 보시기 바랍니다.

- IsContainSignature(.) 메서드는 ContainsSignature(..)로 이름이 변경되었습니다.
- IsCoversWholeDocument(..) 메서드는 CoversWholeDocument(..)로 이름이 변경되었습니다.
{{% /alert %}}

다음 코드는 문서에서 사용 권한을 제거하는 방법을 보여줍니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveExtendedRights()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_SecuritySignatures();
    
    using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfSign.BindPdf(dataDir + "DigitallySign.pdf");
        if (pdfSign.ContainsUsageRights())
        {
            pdfSign.RemoveUsageRights();
        }
        // Save PDF document
        pdfSign.Document.Save(dataDir + "RemoveRights_out.pdf");
    }
}
```