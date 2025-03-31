---
title: Identificando nomes de campos de formulário
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /pt/net/identifying-form-fields-names/
description: Aspose.Pdf.Facades permite identificar nomes de campos de formulário usando a classe Form.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Identifying form fields names",
    "alternativeHeadline": "Identify and Label PDF Form Fields Easily",
    "abstract": "A funcionalidade em Aspose.PDF for .NET simplifica o processo de identificação de nomes de campos de formulário em documentos PDF. Ao utilizar a classe Form e seus atributos, os usuários podem facilmente recuperar e exibir os nomes dos campos ao lado de seus respectivos campos, agilizando o preenchimento e a edição de formulários PDF. Este recurso melhora a experiência do usuário, garantindo uma manipulação precisa dos campos, especialmente ao trabalhar com formulários criados em ferramentas externas como o Adobe Designer.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "511",
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
    "url": "/net/identifying-form-fields-names/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/identifying-form-fields-names/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

[Aspose.PDF for .NET](/pdf/pt/net/) fornece a capacidade de criar, editar e preencher formulários PDF já criados. O namespace [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades) contém a classe [Form](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/form), que contém a função chamada [FillField](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/form/methods/fillfield/index) e aceita dois argumentos, ou seja, nome do campo e valor do campo. Portanto, para preencher os campos do formulário, você deve estar ciente do nome exato do campo do formulário.

## Detalhes da implementação

Frequentemente nos deparamos com um cenário em que precisamos preencher um formulário criado em alguma ferramenta, ou seja, Adobe Designer, e não temos certeza sobre os nomes dos campos do formulário. Portanto, para preencher os campos do formulário, primeiro precisamos ler os nomes de todos os campos do formulário PDF. A classe [Form](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/form) fornece a propriedade chamada [FieldNames](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/form/properties/fieldnames) que retorna todos os nomes dos campos e retorna nulo se o PDF não contiver nenhum campo. No entanto, ao usar essa propriedade, obtemos os nomes de todos os campos no formulário PDF e podemos não ter certeza de qual nome corresponde a qual campo no formulário.

Como solução para esse problema, usaremos os atributos de aparência de cada campo. A classe Form possui uma função chamada [GetFieldFacade](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/form/methods/getfieldfacade) que retorna atributos, incluindo localização, cor, estilo de borda, fonte, item de lista e assim por diante. Para salvar esses valores, precisamos usar a classe [FormFieldFacade](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/FormFieldFacade), que é usada para registrar atributos visuais dos campos. Uma vez que temos esses atributos, podemos adicionar um campo de texto abaixo de cada campo que exibirá o nome do campo.

{{% alert color="primary" %}}
Neste ponto, surge a pergunta "como determinaríamos a localização onde adicionar o campo de texto?"
{{% /alert %}}

{{% alert color="primary" %}}
A solução para esse problema é a propriedade Box na classe [FormFieldFacade](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/FormFieldFacade), que contém a localização do campo. Precisamos salvar esses valores em um array do tipo retângulo e usar esses valores para identificar a posição onde adicionar os novos campos de texto.
{{% /alert %}}

No namespace [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades) temos uma classe chamada [FormEditor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/FormEditor) que fornece a capacidade de manipular formulários PDF. Abra um formulário PDF; adicione um campo de texto abaixo de cada campo de formulário existente e salve o formulário PDF com um novo nome.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IdentifyFormFieldsNames()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();
    // First a input pdf file should be assigned
    var form = new Aspose.Pdf.Facades.Form(dataDir + "FilledForm.pdf");
    // Get all field names
    var allfields = form.FieldNames;
    // Create an array which will hold the location coordinates of Form fields
    var box = new System.Drawing.Rectangle[allfields.Length];
    for (int i = 0; i < allfields.Length; i++)
    {
        // Get the appearance attributes of each field, consequtively
        var facade = form.GetFieldFacade(allfields[i]);
        // Box in FormFieldFacade class holds field's location
        box[i] = facade.Box;
    }
    // Save PDF document
    form.Save(dataDir + "IdentifyFormFields_1_out.pdf");

    // Create PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FilledForm - 2.pdf"))
    {
        // Now we need to add a textfield just upon the original one
        using (var editor = new Aspose.Pdf.Facades.FormEditor(document))
        {
            for (int i = 0; i < allfields.Length; i++)
            {
                // Add text field beneath every existing form field
                editor.AddField(Aspose.Pdf.Facades.FieldType.Text, 
                "TextField" + i, allfields[i], 1, 
                box[i].Left, box[i].Top, box[i].Left + 50, box[i].Top + 10);
            }
            // Save PDF document
            editor.Save(dataDir + "IdentifyFormFields_out.pdf");
        }
    }
}
```