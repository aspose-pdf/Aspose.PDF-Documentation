---
title: Obter Valor da Opção do Botão
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /pt/net/get-button-option-value/
description: Esta seção explica como obter o Valor da Opção do Botão com Aspose.PDF Facades usando a Classe Form.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get Button Option Value",
    "alternativeHeadline": "Retrieve Button Option Values from PDF Efficiently",
    "abstract": "Descubra como recuperar eficientemente os valores das opções de botão de arquivos PDF existentes usando as Facades do Aspose.PDF. Com os métodos GetButtonOptionValues e GetButtonOptionCurrentValue da classe Form, você pode facilmente obter todas as opções disponíveis para botões de rádio, bem como o valor atualmente selecionado, aprimorando suas capacidades de gerenciamento de formulários PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "275",
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
    "url": "/net/get-button-option-value/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-button-option-value/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Obter Valores da Opção do Botão de um Arquivo PDF Existente

Os botões de rádio fornecem uma maneira de mostrar diferentes opções. A classe [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) permite que você obtenha todos os valores das opções de botão para um botão de rádio específico. Você pode obter esses valores usando o método [GetButtonOptionValues](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getbuttonoptionvalues). Este método requer o nome do botão de rádio como parâmetro de entrada e retorna um Hashtable. Você pode iterar por este Hashtable para obter os valores das opções. O seguinte trecho de código mostra como obter os valores das opções do botão de um arquivo PDF existente.
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void GetButtonOptions()
{    
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "FormField.pdf");

        // Get button option values
        var optionValues = pdfForm.GetButtonOptionValues("Gender");

        IDictionaryEnumerator optionValueEnumerator = optionValues.GetEnumerator();

        while (optionValueEnumerator.MoveNext())
        {
            Console.WriteLine("Key : {0} , Value : {1} ", optionValueEnumerator.Key, optionValueEnumerator.Value);
        }
    }
}
```

## Obter o Valor da Opção do Botão Atual de um Arquivo PDF Existente

Os botões de rádio fornecem uma maneira de definir valores de opção, no entanto, apenas um deles pode ser selecionado por vez. Se você deseja obter o valor da opção atualmente selecionada, pode usar o método [GetButtonOptionCurrentValue](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getbuttonoptioncurrentvalue). A classe [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) fornece este método. O método [GetButtonOptionCurrentValue](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getbuttonoptioncurrentvalue) requer o nome do botão de rádio como parâmetro de entrada e retorna o valor como string. O seguinte trecho de código mostra como obter o valor da opção do botão atual de um arquivo PDF existente.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void GetCurremtButtonOptionValue()
{    
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "FormField.pdf");

        // Get button option values
        string optionValue = pdfForm.GetButtonOptionCurrentValue("Gender");

        Console.WriteLine("Current Value : {0} ", optionValue);
    }
}
```