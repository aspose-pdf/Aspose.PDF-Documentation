---
title: PDF Tooltip usando C#
linktitle: PDF Tooltip
type: docs
weight: 20
url: pt/net/pdf-tooltip/
description: Aprenda como adicionar tooltip a um fragmento de texto em PDF usando C# e Aspose.PDF
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF Tooltip usando C#",
    "alternativeHeadline": "Adicionar PDF Tooltip ao Texto",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, c#, adicionar pdf tooltip",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipe de Documentação Aspose.PDF",
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
                "contactType": "vendas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vendas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vendas",
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
    "dateModified": "2022-02-04",
    "description": "Aprenda como adicionar tooltip a um fragmento de texto em PDF usando C# e Aspose.PDF"
}
</script>
O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Adicionar Dica de Ferramenta ao Texto Pesquisado adicionando um Botão Invisível

É frequentemente necessário adicionar alguns detalhes para uma frase ou palavra específica como uma dica de ferramenta no documento PDF, de modo que ela apareça quando o usuário passar o cursor do mouse sobre o texto. O Aspose.PDF para .NET oferece essa funcionalidade para criar dicas de ferramentas adicionando um botão invisível sobre o texto pesquisado. O seguinte trecho de código mostrará como alcançar essa funcionalidade:

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
string outputFile = dataDir + "Tooltip_out.pdf";

// Criar documento de amostra com texto
Document doc = new Document();
doc.Pages.Add().Paragraphs.Add(new TextFragment("Mova o cursor do mouse aqui para exibir uma dica de ferramenta"));
doc.Pages[1].Paragraphs.Add(new TextFragment("Mova o cursor do mouse aqui para exibir uma dica de ferramenta muito longa"));
doc.Save(outputFile);

// Abrir documento com texto
Document document = new Document(outputFile);
// Criar objeto TextAbsorber para encontrar todas as frases que correspondem à expressão regular
TextFragmentAbsorber absorber = new TextFragmentAbsorber("Mova o cursor do mouse aqui para exibir uma dica de ferramenta");
// Aceitar o absorvedor para as páginas do documento
document.Pages.Accept(absorber);
// Obter os fragmentos de texto extraídos
TextFragmentCollection textFragments = absorber.TextFragments;

// Loop através dos fragmentos
foreach (TextFragment fragment in textFragments)
{
    // Criar botão invisível na posição do fragmento de texto
    ButtonField field = new ButtonField(fragment.Page, fragment.Rectangle);
    // O valor AlternateName será exibido como dica de ferramenta por uma aplicação visualizadora
    field.AlternateName = "Dica de ferramenta para texto.";
    // Adicionar campo de botão ao documento
    document.Form.Add(field);
}

// A seguir será um exemplo de dica de ferramenta muito longa
absorber = new TextFragmentAbsorber("Mova o cursor do mouse aqui para exibir uma dica de ferramenta muito longa");
document.Pages.Accept(absorber);
textFragments = absorber.TextFragments;

foreach (TextFragment fragment in textFragments)
{
    ButtonField field = new ButtonField(fragment.Page, fragment.Rectangle);
    // Definir texto muito longo
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

// Salvar documento
document.Save(outputFile);
```
{{% alert color="primary" %}}

No que diz respeito ao comprimento do tooltip, o texto do tooltip está contido no documento PDF como tipo de string PDF, fora do fluxo de conteúdo. Não há restrição efetiva para essas strings em arquivos PDF (Veja o Apêndice C da Referência PDF.). Contudo, um leitor conforme (por exemplo, Adobe Acrobat) executando em um determinado processador e em um determinado ambiente operacional possui tal limite. Por favor, consulte a documentação da sua aplicação leitora de PDF.

{{% /alert %}}

## Criar um Bloco de Texto Oculto e Exibi-lo ao Passar o Mouse

No Aspose.PDF, uma funcionalidade para ocultar ações é implementada pela qual é possível mostrar/esconder campo de caixa de texto (ou qualquer outro tipo de anotação) ao entrar/sair do mouse sobre algum botão invisível. Para esse propósito, a Classe Aspose.Pdf.Annotations.HideAction é utilizada para atribuir a ação de mostrar/esconder ao bloco de texto. Por favor, use o seguinte trecho de código para Mostrar/Esconder um Bloco de Texto ao Entrar/Sair do Mouse.

Por favor, também leve em conta que as ações PDF nos documentos funcionam bem nos leitores conformes (por exemplo,
Por favor, leve em consideração que as ações PDF nos documentos funcionam bem nos leitores compatíveis (por exemplo,

- Todas as implementações da ação de ocultar em documentos PDF funcionam bem no Internet Explorer v.11.0.
- Todas as implementações da ação de ocultar também funcionam no Opera v.12.14, mas observamos algum atraso de resposta na primeira abertura do documento.
- Apenas a implementação usando o construtor HideAction que aceita o nome do campo funciona se o Google Chrome v.61.0 navega pelo documento; Por favor, use os construtores correspondentes se a navegação no Google Chrome for significativa:

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

string outputFile = dataDir + "TextBlock_HideShow_MouseOverOut_out.pdf";

// Criar documento de exemplo com texto
Document doc = new Document();
doc.Pages.Add().Paragraphs.Add(new TextFragment("Mova o cursor do mouse aqui para exibir o texto flutuante"));
doc.Save(outputFile);

// Abrir documento com texto
Document document = new Document(outputFile);
// Criar objeto TextAbsorber para encontrar todas as frases que correspondam à expressão regular
TextFragmentAbsorber absorber = new TextFragmentAbsorber("Mova o cursor do mouse aqui para exibir o texto flutuante");
// Aceitar o absorvedor para as páginas do documento
document.Pages.Accept(absorber);
// Obter o primeiro fragmento de texto extraído
TextFragmentCollection textFragments = absorber.TextFragments;
TextFragment fragment = textFragments[1];

// Criar campo de texto oculto para texto flutuante no retângulo especificado da página
TextBoxField floatingField = new TextBoxField(fragment.Page, new Rectangle(100, 700, 220, 740));
// Definir texto a ser exibido como valor do campo
floatingField.Value = "This is the \"floating text field\".";
// Recomendamos tornar o campo 'readonly' para este cenário
floatingField.ReadOnly = true;
// Definir a bandeira 'hidden' para tornar o campo invisível na abertura do documento
floatingField.Flags |= AnnotationFlags.Hidden;

// Definir um nome de campo único não é necessário, mas é permitido
floatingField.PartialName = "FloatingField_1";

// Definir características da aparência do campo não é necessário, mas torna melhor
floatingField.DefaultAppearance = new DefaultAppearance("Helv", 10, System.Drawing.Color.Blue);
floatingField.Characteristics.Background = System.Drawing.Color.LightBlue;
floatingField.Characteristics.Border = System.Drawing.Color.DarkBlue;
floatingField.Border = new Border(floatingField);
floatingField.Border.Width = 1;
floatingField.Multiline = true;

// Adicionar campo de texto ao documento
document.Form.Add(floatingField);

// Criar botão invisível na posição do fragmento de texto
ButtonField buttonField = new ButtonField(fragment.Page, fragment.Rectangle);
// Criar nova ação de ocultar para o campo especificado (anotação) e bandeira de invisibilidade.
// (Você também pode referenciar o campo flutuante pelo nome se o especificou acima.)
// Adicionar ações na entrada/saída do mouse no campo de botão invisível
buttonField.Actions.OnEnter = new HideAction(floatingField, false);
buttonField.Actions.OnExit = new HideAction(floatingField);

// Adicionar campo de botão ao documento
document.Form.Add(buttonField);

// Salvar documento
document.Save(outputFile);
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
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/destaque",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "vendas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vendas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vendas",
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
    "applicationCategory": "Biblioteca de Manipulação de PDF para .NET",
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
```

