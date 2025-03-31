---
title: Explorando recursos da classe FormEditor
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /pt/net/exploring-features-of-formeditor-class/
description: Você pode aprender detalhes sobre a exploração de recursos da classe FormEditor com a biblioteca Aspose.PDF para .NET
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Exploring features of FormEditor class",
    "alternativeHeadline": "Enhancing PDF Forms with FormEditor Class",
    "abstract": "Descubra as capacidades aprimoradas da classe FormEditor dentro da biblioteca Aspose.PDF for .NET, projetada para manipulação sem esforço de formulários PDF interativos. Este recurso capacita os desenvolvedores a adicionar, editar e configurar campos de formulário de maneira fluida, com métodos amigáveis ao usuário para simplificar o processo de modificação. Otimize o manuseio de seus formulários PDF aproveitando as funcionalidades abrangentes do FormEditor para elevar seus fluxos de trabalho de documentos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "358",
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
    "url": "/net/exploring-features-of-formeditor-class/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/exploring-features-of-formeditor-class/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

{{% alert color="primary" %}}

Documentos PDF às vezes contêm formulários interativos, que são conhecidos como AcroForm. É como um formulário usado em páginas da web. Esses formulários contêm diferentes tipos de controles, ou seja, caixas de texto, caixas de seleção e botões, etc. Um desenvolvedor que trabalha com arquivos PDF pode, às vezes, precisar editar esses formulários. Neste artigo, vamos analisar os detalhes de como o [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades) nos permite fazer isso.

{{% /alert %}}

## Detalhes da implementação

Os desenvolvedores podem usar o [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades) não apenas para adicionar novos formulários e campos de formulário em um documento PDF, mas também para editar campos existentes. O escopo deste artigo é limitado aos recursos de [Aspose.PDF for .NET](/pdf/pt/net/) que lidam com a edição de formulários.

[FormEditor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/formeditor) é a classe que contém a maioria dos métodos e propriedades que permitem aos desenvolvedores editar campos de formulário. Você pode não apenas adicionar novos campos, mas também remover campos existentes, mover um campo para outra posição, alterar o nome do campo ou atributos, etc. A lista de recursos fornecidos por esta classe é bastante abrangente, e é muito fácil trabalhar com os campos de formulário usando esta classe.

Esses métodos podem ser divididos em duas categorias principais, uma das quais é usada para manipular os campos, e a outra é usada para definir os novos atributos desses campos. Os métodos que podemos agrupar na primeira categoria incluem AddField, AddListItem, RemoveListItem, CopyInnerField, CopyOuterField, DelListItem, MoveField, RemoveField e RenameField, etc. Na segunda categoria de métodos, podem ser incluídos SetFieldAlignment, SetFieldAppearance, SetFieldAttribute, SetFieldLimit, SetFieldScript. O seguinte trecho de código mostra alguns dos métodos da classe FormEditor em funcionamento:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ExploringFormEditorFeatures()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "inFile.pdf"))
    {
        // Create instance of FormEditor
        using (var editor = new Aspose.Pdf.Facades.FormEditor(document))
        {
            // Add field in the PDF file
            editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "field1", 1, 300, 500, 350, 525);

            // Add List field in PDF file
            editor.AddField(Aspose.Pdf.Facades.FieldType.ListBox, "field2", 1, 300, 200, 350, 225);

            // Add list items
            editor.AddListItem("field2", "item 1");
            editor.AddListItem("field2", "item 2");

            // Add submit button
            editor.AddSubmitBtn("submitbutton", 1, "Submit Form", "http:// Testwebsite.com/testpage", 200, 200, 250, 225);

            // Delete list item
                editor.DelListItem("field2", "item 1");

            // Move field to new position
            editor.MoveField("field1", 10, 10, 50, 50);

            // Remove existing field from the PDF
            editor.RemoveField("field1");

            // Rename an existing field
            editor.RenameField("field1", "newfieldname");

            // Reset all visual attributes to empty value
            editor.ResetFacade();

            // Set the alignment style of a text field
            editor.SetFieldAlignment("field1", Aspose.Pdf.Facades.FormFieldFacade.AlignLeft);

            // Set appearance of the field
            editor.SetFieldAppearance("field1", Aspose.Pdf.Annotations.AnnotationFlags.NoRotate);

            // Set field attributes i.e. ReadOnly, Required
            editor.SetFieldAttribute("field1", Aspose.Pdf.Facades.PropertyFlag.ReadOnly);

            // Set field limit
            editor.SetFieldLimit("field1", 25);

            // Save modifications in the output file
            editor.Save(dataDir + "FormEditorFeatures2_out.pdf");                    
        }
    }
}
```