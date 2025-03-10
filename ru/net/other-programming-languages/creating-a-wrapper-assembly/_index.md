---
title: Создание оболочки сборки
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /ru/net/creating-a-wrapper-assembly/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Creating a Wrapper Assembly",
    "alternativeHeadline": "Simplify COM Interop with Wrapper Assemblies",
    "abstract": "Новая функция Wrapper Assembly для Aspose.PDF для .NET позволяет разработчикам создавать упрощённый интерфейс для взаимодействия с классами, методами и свойствами Aspose.PDF из неуправляемого кода. Эта функция упрощает разработку проекта, облегчая управление функциями PDF и их использование без необходимости глубоких знаний программирования на .NET, инкапсулируя сложность COM Interop",
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
    "description": "Aspose.PDF может выполнять не только простые и лёгкие задачи, но и справляться с более сложными целями. Ознакомьтесь со следующим разделом для опытных пользователей и разработчиков."
}
</script>

{{% alert color="primary" %}}

Если вам нужно использовать многие классы, методы и свойства Aspose.PDF for .NET, рассмотрите возможность создания оболочки сборки (используя C# или любой другой язык программирования .NET). Оболочки сборок помогают избежать прямого использования Aspose.PDF for .NET из неуправляемого кода.

Хорошим подходом является разработка сборки .NET, которая ссылается на Aspose.PDF for .NET и выполняет всю работу с ней, а также предоставляет неуправляемому коду только минимальный набор классов и методов. Ваше приложение должно работать только с вашей библиотекой-оболочкой.

Сокращение количества классов и методов, которые вам нужно вызывать через COM Interop, упрощает проект. Использование классов .NET через COM Interop часто требует продвинутых навыков.

{{% /alert %}}

## Оболочка Aspose.PDF for .NET

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