---
title: Explorando recursos da classe FormEditor
type: docs
weight: 10
url: /pt/net/exploring-features-of-formeditor-class/
description: Você pode aprender detalhes sobre a exploração de recursos da classe FormEditor com a biblioteca Aspose.PDF para .NET
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Documentos PDF às vezes contêm formulários interativos, que são conhecidos como AcroForm. É como um formulário usado nas páginas da web. Esses formulários contêm diferentes tipos de controles, ou seja, Caixas de texto, Caixas de seleção e Botões, etc. Um desenvolvedor que trabalha com arquivos PDF pode, às vezes, precisar editar esses formulários. Neste artigo, analisaremos em detalhes como o [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) nos permite fazer isso.

{{% /alert %}}

## Detalhes da implementação

Os desenvolvedores podem usar o [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) não apenas para adicionar novos formulários e campos de formulário em um documento PDF, mas também para permitir que você edite campos existentes. O escopo deste artigo é limitado às funcionalidades do [Aspose.PDF for .NET](/pdf/pt/net/) que lidam com a edição de formulários.

[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) é a classe que contém a maioria dos métodos e propriedades que permitem aos desenvolvedores editar campos de formulário. Você pode não apenas adicionar novos campos, mas também remover campos existentes, mover um campo para outra posição, mudar o nome do campo ou atributos etc. A lista de funcionalidades fornecidas por esta classe é bastante abrangente, e é muito fácil trabalhar com os campos de formulário usando esta classe.

Esses métodos podem ser divididos em duas categorias principais, uma das quais é usada para manipular os campos, e a outra é usada para definir os novos atributos desses campos. Os métodos que podemos agrupar na primeira categoria incluem AddField, AddListItem, RemoveListItem, CopyInnerField, CopyOuterField, DelListItem, MoveField, RemoveField, e RenameField etc. Na segunda categoria dos métodos podem ser incluídos SetFieldAlignment, SetFieldAppearance, SetFieldAttribute, SetFieldLimit, SetFieldScript. O trecho de código a seguir mostra alguns dos métodos da classe FormEditor em funcionamento: 

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-FormEditorFeatures-FormEditorFeatures.cs" >}}