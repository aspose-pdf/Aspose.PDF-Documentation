---
title: Qual é a diferença entre os formatos FDF, XML e XFDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /pt/net/whats-the-difference-between-xml-fdf-and-xfdf/
description: Esta seção diferencia entre os formulários XML, FDF e XFDF com as Facades Aspose.PDF usando a Classe Form.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Whats is the difference between FDF, XML, and XFDF formats",
    "alternativeHeadline": "Understanding FDF, XML, and XFDF Formats in Aspose.PDF for .NET",
    "abstract": "Descubra as diferenças entre os formatos FDF, XML e XFDF na manipulação de dados de formulários PDF através de Aspose.PDF for .NET. Este recurso permite que os desenvolvedores exportem de forma contínua os valores dos campos de formulários interativos em vários formatos, cada um com sua própria sintaxe, enquanto aprimora a compreensão e o uso desses tipos de arquivos essenciais no processamento de PDF. Otimize o manuseio de formulários PDF com insights detalhados sobre como representar campos de formulários em diferentes formatos de dados.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1045",
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
    "url": "/net/whats-the-difference-between-xml-fdf-and-xfdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/whats-the-difference-between-xml-fdf-and-xfdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

{{% alert color="primary" %}}

Misturamos muitos termos diferentes como FDF, XML e XFDF. Todos esses termos estão relacionados de alguma forma. Este artigo explora esses conceitos e sua relação entre si.

{{% /alert %}}

## Desvendando Formulários

Aspose.PDF for .NET é usado para manipular documentos PDF padronizados pela Adobe. E os documentos PDF contêm formulários interativos chamados AcroForms. Esses formulários interativos têm uma série de campos de formulário, como combo, caixa de texto e botão de opção. Os formulários interativos da Adobe e os campos de formulário funcionam da mesma maneira que um formulário HTML e seus campos de formulário.

É possível armazenar os valores dos campos de formulário em um arquivo separado: um arquivo FDF (Forms Data Format). Isso contém os valores dos campos de formulário de forma chave/valor. Os arquivos FDF ainda são usados para esse propósito. Mas a Adobe também fornece um tipo de FDF codificado em XML chamado XFDF. Um arquivo XFDF armazena os valores dos campos de formulário de maneira hierárquica usando tags XML.

Com Aspose.PDF, os desenvolvedores podem não apenas exportar os valores dos campos de formulário PDF para um arquivo FDF ou XFDF, mas também para um arquivo XML. Todos esses arquivos usam sintaxes diferentes para salvar os valores dos campos de formulário PDF. O exemplo abaixo explica as diferenças.

Vamos supor que existem alguns campos de formulário PDF cujos valores precisam ser apresentados nos formatos FDF, XML e XFDF. Esses campos de formulário assumidos com seus nomes e valores estão mostrados abaixo:

|**Nome do Campo**|**Valor do Campo**|
| :- | :- |
|Empresa|Aspose.com|
|Endereço.1|Sydney, Austrália|
|Endereço.2|Linha de Endereço Adicional|
Vamos ver como representar esses valores nos formatos FDF, XML e XFDF.

### O que é o formato FDF?

Como sabemos, o arquivo FDF armazena dados na forma chave/valor, onde /T representa uma chave, /V representa o valor e os dados entre parênteses () representam o conteúdo de uma chave ou um valor. Por exemplo, /T(Company) significa que Company é a chave do campo e /V(Aspose.com) é destinado a um valor de campo.

/T(Company) /V(Aspose.com)
/T(Address.1) /V( Sydney , Australia )
/T(Address.2) /V(Linha de Endereço Adicional)

### O que é o formato XML? 

Os desenvolvedores podem representar cada campo de formulário PDF na forma de uma tag de campo, `<field>`. Cada tag de campo tem um atributo, name, que mostra o nome do campo e uma subtags, `<value>`, representando o valor do campo, como mostrado abaixo:

```xml
 <?xml version="1.0" ?>
 <fields>
  <field name="Company">
    <value>Aspose.com</value>
  </field>
  <field name="Address.1">
    <value>Sydney, Australia</value>
  </field>
  <field name="Address.2">
    <value>Additional Address Line</value>
  </field>
 </fields>
```

### O que é o formato XFDF?  

A representação dos dados acima no formato XFDF é semelhante ao formato XML, exceto por algumas diferenças. Nos arquivos XFDF, adicionamos seu Namespace XML, que é <http://ns.adpbe.com/xfdf/> e há uma tag adicional, `<f>`, que é usada para apontar para o documento PDF que contém esses campos de formulário PDF. Assim como no XML, o XFDF também contém campos na forma de tags de campo, `<field>`, como mostrado abaixo:

```xml

<?xml version="1.0" encoding="UTF-8"?>
<xfdf xmlns="http://ns.adobe.com/xfdf/" xml:space="preserve">   
   <f href="CompanyForm.pdf"/> 
   <fields>
      <field name="Company">
         <value>Aspose.com</value>
      </field>
      <field name="Address">
         <field name="1">
            <value>Sydney, Australia</value>
         </field>
         <field name="2">
            <value>Additional Address Line</value>
         </field>
      </field>
   </fields>
 </xfdf>
```

### Identificando os nomes dos campos de formulário

Aspose.PDF for .NET fornece a capacidade de criar, editar e preencher formulários PDF já criados. Ele contém a classe [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form), que possui a função chamada [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index), e ela recebe dois parâmetros, ou seja, o nome do campo que precisa ser preenchido e o valor do campo. Portanto, para preencher os campos do formulário, você deve estar ciente do nome exato do campo do formulário.
Frequentemente nos deparamos com o cenário em que precisamos preencher um formulário que foi criado em alguma ferramenta, ou seja, Adobe Designer, e não temos certeza sobre os nomes dos campos do formulário. Para atender à nossa necessidade, precisamos ler os nomes de todos os campos de formulário PDF. A classe [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) fornece a propriedade chamada [FieldsNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames), que retorna todos os nomes dos campos e retorna nulo se o PDF não tiver campo. Mas essa propriedade retornará todos os nomes dos campos do formulário PDF e não teremos certeza de qual nome corresponde a qual campo no formulário.

Como solução para esse problema, precisaríamos dos atributos de aparência de cada campo. A classe [Form](http://www.aspose.com/documentation/file-format-components/aspose.pdf.kit-for-.net-and-java/aspose.pdf.kit.form.html) possui uma função chamada GetFieldFacade, que retorna atributos, incluindo localização, cor, estilo de borda, fonte, item de lista e assim por diante. Para salvar esses valores, usaremos a classe [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade), que é usada para registrar atributos visuais dos campos. Uma vez que temos esses atributos, podemos adicionar um campo de texto abaixo de cada campo que exibirá o nome do campo. Aqui surge a questão de como determinar a localização onde adicionar o campo de texto? A solução para esse problema é a propriedade Box na classe [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade), que contém a localização do campo. Salvaremos esses valores em um array do tipo retângulo e usaremos esses valores para identificar a posição onde adicionar os novos campos de texto.
No namespace Aspose.Pdf.Facades, temos uma classe chamada [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) que fornece a capacidade de manipular formulários PDF. Abra um formulário PDF, adicione um campo de texto abaixo de cada campo de formulário existente e salve o formulário PDF com um novo nome.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DifferenceBetweenFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // First a input pdf file should be assigned
    using (var form = new Aspose.Pdf.Facades.Form(dataDir + "FilledForm.pdf"))
    {
        // Get all field names
        String[] allfields = form.FieldNames;
        // Create an array which will hold the location coordinates of Form fields
        var box = new System.Drawing.Rectangle[allfields.Length];
        for (int i = 0; i < allfields.Length; i++)
        {
            // Get the appearance attributes of each field, consecutively
            var facade = form.GetFieldFacade(allfields[i]);
            // Box in FormFieldFacade class holds field's location.
            box[i] = facade.Box;
        }
        // Save PDF document
        form.Save(dataDir + "DifferenceBetweenFile_out.pdf");
            
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(dataDir + "FilledForm - 2.pdf"))
        {
            // Now we need to add a textfield just upon the original one
            FormEditor editor = new Aspose.Pdf.Facades.FormEditor(document);
            for (int i = 0; i < allfields.Length; i++)
            {
                // Add text field beneath every existing form field
                editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "TextField" + i, allfields[i], 1, box[i].Left, box[i].Top, box[i].Left + 50, box[i].Top + 10);
            }
            // Save PDF document
            editor.Save(dataDir + "DifferenceBetweenFile_out.pdf");
        }
    }
}
```