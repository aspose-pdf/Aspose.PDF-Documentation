---
title: Qual é a diferença entre os formatos FDF, XML e XFDF
type: docs
weight: 30
url: /net/whats-the-difference-between-xml-fdf-and-xfdf/
description: Esta seção diferencia entre os formulários XML, FDF e XFDF com Aspose.PDF Facades usando a Classe Form.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Misturamos muitos termos diferentes como FDF, XML e XFDF. Todos esses termos estão relacionados entre si de alguma forma. Este artigo explora esses conceitos e sua relação entre si.

{{% /alert %}}

## Desvendando Formulários

Aspose.PDF para .NET é usado para manipular documentos PDF padronizados pela Adobe. E documentos PDF contêm formulários interativos chamados AcroForms. Esses formulários interativos têm vários campos de formulário, como combo, caixa de texto e botão de rádio. Os formulários interativos da Adobe e os campos de formulário funcionam da mesma forma que um formulário HTML e seus campos de formulário.

É possível armazenar os valores dos campos de formulário em um arquivo separado: um arquivo FDF (Formato de Dados de Formulário). Este documento contém os valores dos campos de formulário no formato chave/valor. Os arquivos FDF ainda são usados para esse propósito. Mas a Adobe também fornece um tipo de FDF codificado em XML chamado XFDF. Um arquivo XFDF armazena os valores dos campos de formulário de maneira hierárquica usando tags XML.

Com o Aspose.PDF, os desenvolvedores podem não apenas exportar os valores dos campos de formulário PDF para um arquivo FDF ou XFDF, mas também para um arquivo XML. Todos esses arquivos usam sintaxes diferentes para salvar os valores dos campos de formulário PDF. O exemplo abaixo explica as diferenças.

Vamos supor que existam alguns campos de formulário PDF cujos valores precisam ser apresentados nos formatos FDF, XML e XFDF. Esses campos de formulário assumidos com seus nomes de campo e valores são mostrados abaixo:

|**Nome do Campo**|**Valor do Campo**|
| :- | :- |
|Company|Aspose.com|
|Address.1|Sydney, Australia|
|Address.2|Additional Address Line|

Vamos ver como representar esses valores nos formatos FDF, XML e XFDF.

### O que é o formato FDF?

Como sabemos, o arquivo FDF armazena dados no formato chave/valor, onde /T representa uma chave, /V representa o valor e os dados entre parênteses () representam o conteúdo de uma chave ou de um valor. Por exemplo, /T(Company) significa que Company é a chave do campo e /V(Aspose.com) é o valor do campo.

/T(Company) /V(Aspose.com)
/T(Address.1) /V( Sydney , Australia )
/T(Address.2) /V(Linha de Endereço Adicional)

### O que é o formato XML? 

Os desenvolvedores podem representar cada campo de formulário PDF na forma de uma tag de campo, `<field>`. Cada tag de campo tem um atributo, name, mostrando o nome do campo e uma subtaga, `<value>`, representando o valor do campo, como mostrado abaixo:

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
    <value>Linha de Endereço Adicional</value>
  </field>
 </fields>
```

### ### O que é o formato XFDF?  

A representação dos dados acima na forma XFDF é semelhante à forma XML, exceto por algumas diferenças. Em arquivos XFDF, adicionamos seu Namespace XML, que é <http://ns.adpbe.com/xfdf/> e há uma tag adicional, `<f>`, que é usada para apontar para o documento PDF contendo esses campos de formulário PDF. Como no XML, o XFDF também contém campos na forma de tags de campo, `<field>`, como mostrado abaixo:

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

### Identificando nomes de campos de formulário

Aspose.PDF para .NET fornece a capacidade de criar, editar e preencher formulários PDF já criados. Contém a classe [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form), que possui a função chamada [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index), e ela recebe dois parâmetros, ou seja, o nome do campo que precisa ser preenchido e o valor do campo. Portanto, para preencher os campos do formulário, você deve estar ciente do nome exato do campo do formulário. Frequentemente nos deparamos com o cenário em que precisamos preencher o formulário que foi criado em alguma ferramenta, ou seja. Adobe Designer, e não temos certeza sobre os nomes dos campos do formulário. Para cumprir nosso requisito, precisamos ler os nomes de todos os campos do formulário PDF. A classe [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) fornece a propriedade chamada [FieldsNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames) que retorna todos os nomes dos campos e retorna nulo se o PDF não tiver campo. Mas esta propriedade retornará todos os nomes dos campos do formulário PDF e não teremos certeza de qual nome corresponde a qual campo no formulário.

Como solução para este problema, precisaríamos dos atributos de aparência de cada campo. A classe [Form](http://www.aspose.com/documentation/file-format-components/aspose.pdf.kit-for-.net-and-java/aspose.pdf.kit.form.html) tem uma função chamada GetFieldFacade que retorna atributos, incluindo localização, cor, estilo de borda, fonte, item de lista e assim por diante. Para salvar esses valores, usaremos a classe [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade), que é usada para registrar atributos visuais dos campos. Uma vez que temos esses atributos, podemos adicionar um campo de texto abaixo de cada campo que exibiria o nome do campo. Aqui surge uma pergunta: como determinaríamos a localização onde adicionar o campo de texto? A solução para esse problema é a propriedade Box na classe [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade), que mantém a localização do campo. Nós salvaríamos esses valores em um array do tipo retângulo e usaríamos esses valores para identificar a posição onde adicionar os novos campos de texto. No namespace Aspose.Pdf.Facades, temos uma classe chamada [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) que fornece a capacidade de manipular o formulário PDF. Abra um formulário PDF, adicione um campo de texto abaixo de cada campo de formulário existente e salve o formulário PDF com um novo nome.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-DifferenceBetweenFile-DifferenceBetweenFile.cs" >}}