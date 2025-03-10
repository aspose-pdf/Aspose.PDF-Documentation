---
title: Criando uma Montagem Wrapper
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /pt/net/creating-a-wrapper-assembly/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Creating a Wrapper Assembly",
    "alternativeHeadline": "Simplify COM Interop with Wrapper Assemblies",
    "abstract": "O novo recurso de Montagem Wrapper para Aspose.PDF for .NET permite que os desenvolvedores criem uma interface simplificada para interagir com classes, métodos e propriedades do Aspose.PDF a partir de código não gerenciado. Ao encapsular a complexidade do COM Interop, essa funcionalidade agiliza o desenvolvimento de projetos, tornando mais fácil gerenciar e utilizar funcionalidades de PDF sem precisar de habilidades avançadas em programação .NET",
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
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

{{% alert color="primary" %}}

Se você precisar usar muitas classes, métodos e propriedades de Aspose.PDF for .NET, considere criar uma montagem wrapper (usando C# ou qualquer outra linguagem de programação .NET). Montagens wrapper ajudam a evitar o uso de Aspose.PDF for .NET diretamente a partir de código não gerenciado.

Uma boa abordagem é desenvolver uma montagem .NET que referencia Aspose.PDF for .NET e faz todo o trabalho com ela, e apenas expõe um conjunto mínimo de classes e métodos para código não gerenciado. Sua aplicação deve então funcionar apenas com sua biblioteca wrapper.

Reduzir o número de classes e métodos que você precisa invocar via COM Interop simplifica o projeto. Usar classes .NET via COM Interop muitas vezes requer habilidades avançadas.

{{% /alert %}}

## Wrapper Aspose.PDF for .NET

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