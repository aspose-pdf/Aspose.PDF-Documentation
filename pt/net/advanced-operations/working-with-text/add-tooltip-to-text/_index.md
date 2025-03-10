---
title: PDF Tooltip usando C#
linktitle: Dica do PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /pt/net/pdf-tooltip/
description: Aprenda como adicionar tooltip ao fragmento de texto em PDF usando C# e Aspose.PDF
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF Tooltip using C#",
    "alternativeHeadline": "Add Interactive Tooltips to PDF Text in C#",
    "abstract": "Melhore seus documentos PDF com o novo recurso de Tooltip PDF usando C#. Essa funcionalidade permite que você adicione tooltips a fragmentos de texto em arquivos PDF, fornecendo aos usuários informações adicionais ao passar o mouse. Utilize botões invisíveis e blocos de texto ocultos para criar uma experiência de leitura dinâmica e interativa com Aspose.PDF",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1072",
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
    "url": "/net/pdf-tooltip/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-tooltip/"
    },
    "dateModified": "2024-11-26",
    "description": "Aprenda como adicionar tooltip ao fragmento de texto em PDF usando C# e Aspose.PDF"
}
</script>

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Adicionar Tooltip ao Texto Pesquisado adicionando Botão Invisível

É frequentemente necessário adicionar alguns detalhes para uma frase ou palavra específica como um tooltip no documento PDF para que ele possa aparecer quando o usuário passa o cursor do mouse sobre o texto. Aspose.PDF for .NET fornece esse recurso para criar tooltips adicionando um botão invisível sobre o texto pesquisado. O seguinte trecho de código mostrará como alcançar essa funcionalidade:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTooltipToSearchedText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.Pages.Add().Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Move the mouse cursor here to display a tooltip"));
        document.Pages[1].Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Move the mouse cursor here to display a very long tooltip"));
        // Save PDF document
        document.Save(dataDir + "Tooltip_out.pdf");
    }

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Tooltip_out.pdf"))
    {
        // Create TextAbsorber object to find all the phrases matching the regular expression
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("Move the mouse cursor here to display a tooltip");
        // Accept the absorber for the document pages
        document.Pages.Accept(absorber);
        // Get the extracted text fragments
        var textFragments = absorber.TextFragments;

        // Loop through the fragments
        foreach (var fragment in textFragments)
        {
            // Create invisible button on text fragment position
            var field = new Aspose.Pdf.Forms.ButtonField(fragment.Page, fragment.Rectangle);
            // AlternateName value will be displayed as tooltip by a viewer application
            field.AlternateName = "Tooltip for text.";
            // Add button field to the document
            document.Form.Add(field);
        }

        absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("Move the mouse cursor here to display a very long tooltip");
        document.Pages.Accept(absorber);
        textFragments = absorber.TextFragments;

        foreach (var fragment in textFragments)
        {
            var field = new Aspose.Pdf.Forms.ButtonField(fragment.Page, fragment.Rectangle);
            // Set very long text
            field.AlternateName = "Lorem ipsum dolor sit amet, consectetur adipiscing elit," +
                                    " sed do eiusmod tempor incididunt ut labore et dolore magna" +
                                    " aliqua. Ut enim ad minim veniam, quis nostrud exercitation" +
                                    " ullamco laboris nisi ut aliquip ex ea commodo consequat." +
                                    " Duis aute irure dolor in reprehenderit in voluptate velit" +
                                    " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint" +
                                    " occaecat cupidatat non proident, sunt in culpa qui officia" +
                                    " deserunt mollit anim id est laborum.";
            document.Form.Add(field);
        }

        // Save PDF document
        document.Save(dataDir + "Tooltip_out.pdf");
    }
}
```

{{% alert color="primary" %}}

Quanto ao comprimento do tooltip, o texto do tooltip é contido no documento PDF como tipo de string PDF, fora do fluxo de conteúdo. Não há restrição efetiva sobre tais strings em arquivos PDF (Veja o Apêndice C da Referência PDF.). No entanto, um leitor compatível (por exemplo, Adobe Acrobat) executando em um processador específico e em um ambiente operacional específico tem esse limite. Consulte a documentação do seu aplicativo leitor de PDF.

{{% /alert %}}

## Criar um Bloco de Texto Oculto e Exibi-lo ao Passar o Mouse

No Aspose.PDF, um recurso para ocultar ações é implementado pelo qual é possível mostrar/ocultar campo de caixa de texto (ou qualquer outro tipo de anotação) ao entrar/sair do mouse sobre algum botão invisível. Para esse propósito, a Classe Aspose.Pdf.Annotations.HideAction é usada para atribuir a ação de ocultar/exibir ao bloco de texto. Por favor, use o seguinte trecho de código para Mostrar/Ocultar um Bloco de Texto ao Entrar/Sair do Mouse.

Por favor, leve também em conta que as ações PDF nos documentos funcionam bem nos leitores compatíveis (por exemplo, Adobe Reader), mas não há garantias para outros leitores de PDF (por exemplo, plugins de navegador). Fizemos uma breve investigação e encontramos:

- Todas as implementações da ação de ocultar em documentos PDF funcionam bem no Internet Explorer v.11.0.
- Todas as implementações da ação de ocultar também funcionam no Opera v.12.14, mas notamos algum atraso na resposta na primeira abertura do documento.
- Apenas a implementação usando o construtor HideAction que aceita o nome do campo funciona se o Google Chrome v.61.0 navegar pelo documento; Por favor, use os construtores correspondentes se a navegação no Google Chrome for significativa:

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateHiddenTextBlock()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add paragraph with text
        document.Pages.Add().Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Move the mouse cursor here to display floating text"));
        // Save PDF document
        document.Save(dataDir + "TextBlock_HideShow_MouseOverOut_out.pdf");
    }

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextBlock_HideShow_MouseOverOut_out.pdf"))
    {
        // Create TextAbsorber object to find all the phrases matching the regular expression
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("Move the mouse cursor here to display floating text");
        // Accept the absorber for the document pages
        document.Pages.Accept(absorber);
        // Get the first extracted text fragment
        var textFragments = absorber.TextFragments;
        var fragment = textFragments[1];

        // Create hidden text field for floating text in the specified rectangle of the page
        var floatingField = new Aspose.Pdf.Forms.TextBoxField(fragment.Page, new Aspose.Pdf.Rectangle(100, 700, 220, 740));
        // Set text to be displayed as field value
        floatingField.Value = "This is the \"floating text field\".";
        // We recommend to make field 'readonly' for this scenario
        floatingField.ReadOnly = true;
        // Set 'hidden' flag to make field invisible on document opening
        floatingField.Flags |= Aspose.Pdf.Annotations.AnnotationFlags.Hidden;

        // Setting a unique field name isn't necessary but allowed
        floatingField.PartialName = "FloatingField_1";

        // Setting characteristics of field appearance isn't necessary but makes it better
        floatingField.DefaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance("Helv", 10, System.Drawing.Color.Blue);
        floatingField.Characteristics.Background = System.Drawing.Color.LightBlue;
        floatingField.Characteristics.Border = System.Drawing.Color.DarkBlue;
        floatingField.Border = new Aspose.Pdf.Annotations.Border(floatingField);
        floatingField.Border.Width = 1;
        floatingField.Multiline = true;

        // Add text field to the document
        document.Form.Add(floatingField);

        // Create invisible button on text fragment position
        var buttonField = new Aspose.Pdf.Forms.ButtonField(fragment.Page, fragment.Rectangle);
        // Create new hide action for specified field (annotation) and invisibility flag
        // (You also may reffer floating field by the name if you specified it above)
        // Add actions on mouse enter/exit at the invisible button field
        buttonField.Actions.OnEnter = new Aspose.Pdf.Annotations.HideAction(floatingField, false);
        buttonField.Actions.OnExit = new Aspose.Pdf.Annotations.HideAction(floatingField);

        // Add button field to the document
        document.Form.Add(buttonField);

        // Save PDF document
        document.Save(dataDir + "CreateHiddenTextBlock_out.pdf");
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