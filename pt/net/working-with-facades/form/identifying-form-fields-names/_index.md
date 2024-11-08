---
title: Identificando nomes de campos de formulário
type: docs
weight: 10
url: /pt/net/identifying-form-fields-names/
description: Aspose.PDF.Facades permite identificar nomes de campos de formulário usando a Classe Form.
lastmod: "2021-06-05"
draft: false
---

[Aspose.PDF for .NET](/pdf/pt/net/) fornece a capacidade de criar, editar e preencher formulários PDF já criados. O namespace [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) contém a classe [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form), que contém a função chamada [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) e ela recebe dois argumentos, ou seja, nome do campo e valor do campo. Portanto, para preencher os campos do formulário, você deve estar ciente do nome exato do campo do formulário.

## Detalhes de implementação

Freqüentemente nos deparamos com um cenário em que precisamos preencher o formulário que foi criado em alguma ferramenta, ou seja. Adobe Designer, e não temos certeza sobre os nomes dos campos do formulário. Portanto, para preencher os campos do formulário, primeiro precisamos ler os nomes de todos os campos do formulário PDF. A classe [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) fornece a propriedade chamada [FieldNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames) que retorna os nomes de todos os campos e retorna null se o PDF não contiver nenhum campo. No entanto, ao usar essa propriedade, obtemos os nomes de todos os campos no formulário PDF e talvez não tenhamos certeza de qual nome corresponde a qual campo no formulário.

Como solução para esse problema, usaremos os atributos de aparência de cada campo. A classe Form possui uma função chamada [GetFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getfieldfacade) que retorna atributos, incluindo localização, cor, estilo de borda, fonte, item de lista e assim por diante. Para salvar esses valores, precisamos usar a classe [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormFieldFacade), que é usada para registrar os atributos visuais dos campos. Uma vez que temos esses atributos, podemos adicionar um campo de texto abaixo de cada campo que exibiria o nome do campo.

{{% alert color="primary" %}}
Neste ponto, surge uma pergunta "como determinaríamos a localização onde adicionar o campo de texto?"
{{% /alert %}}

{{% alert color="primary" %}}
A solução para esse problema é a propriedade Box na classe [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormFieldFacade), que mantém a localização do campo. Precisamos salvar esses valores em um array do tipo retângulo e usar esses valores para identificar a posição onde adicionar os novos campos de texto.

No namespace [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades), temos uma classe chamada [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) que fornece a capacidade de manipular formulários PDF. Abra um formulário pdf; adicione um campo de texto abaixo de cada campo de formulário existente e salve o formulário Pdf com um novo nome.
{{% /alert %}}
