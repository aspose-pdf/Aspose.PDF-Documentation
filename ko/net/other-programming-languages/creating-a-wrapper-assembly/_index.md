---
title: 래퍼 어셈블리 만들기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /ko/net/creating-a-wrapper-assembly/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Creating a Wrapper Assembly",
    "alternativeHeadline": "Simplify COM Interop with Wrapper Assemblies",
    "abstract": "Aspose.PDF for .NET의 새로운 래퍼 어셈블리 기능은 개발자가 비관리 코드에서 Aspose.PDF 클래스, 메서드 및 속성과 상호 작용하기 위한 단순화된 인터페이스를 생성할 수 있도록 합니다. COM 상호 운용성의 복잡성을 캡슐화함으로써 이 기능은 프로젝트 개발을 간소화하여 .NET 프로그래밍에 대한 고급 기술 없이도 PDF 기능을 관리하고 활용하기 쉽게 만듭니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "244",
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
    "url": "/net/creating-a-wrapper-assembly/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/creating-a-wrapper-assembly/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 단순하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

{{% alert color="primary" %}}

Aspose.PDF for .NET 클래스, 메서드 및 속성을 많이 사용해야 하는 경우, 래퍼 어셈블리(C# 또는 기타 .NET 프로그래밍 언어 사용)를 만드는 것을 고려하십시오. 래퍼 어셈블리는 비관리 코드에서 Aspose.PDF for .NET을 직접 사용하는 것을 피하는 데 도움이 됩니다.

좋은 접근 방식은 Aspose.PDF for .NET을 참조하는 .NET 어셈블리를 개발하고, 이를 통해 모든 작업을 수행하며, 비관리 코드에 최소한의 클래스 및 메서드 집합만 노출하는 것입니다. 그러면 애플리케이션은 래퍼 라이브러리만 사용하여 작동해야 합니다.

COM 상호 운용성을 통해 호출해야 하는 클래스 및 메서드의 수를 줄이면 프로젝트가 단순해집니다. COM 상호 운용성을 통해 .NET 클래스를 사용하는 것은 종종 고급 기술을 요구합니다.

{{% /alert %}}

## Aspose.PDF for .NET 래퍼

```csharp
using System.Runtime.InteropServices;

namespace TextRetriever
{
    [InterfaceType(ComInterfaceType.InterfaceIsIDispatch)]
    public interface IRetriever
    {
        [DispId(1)]
        void SetLicense(string file);

        [DispId(2)]
        string GetText(string file);
    }

    [ClassInterface(ClassInterfaceType.None)]
    [ComSourceInterfaces(typeof(IRetriever))]
    public class Retriever : IRetriever
    {
        public void SetLicense(string file)
        {
            var lic = new Aspose.Pdf.License();
            lic.SetLicense(file);
        }

        public string GetText(string file)
        {
            // Open PDF document
            using (var document = new Aspose.Pdf.Document(file))
            {
                // Create TextAbsorber object to extract text
                var absorber = new Aspose.Pdf.Text.TextAbsorber();

                // Accept the absorber for all document's pages
                document.Pages.Accept(absorber);

                // Get the extracted text
                string text = absorber.Text;

                return text;
            }
        }
    }
}
```