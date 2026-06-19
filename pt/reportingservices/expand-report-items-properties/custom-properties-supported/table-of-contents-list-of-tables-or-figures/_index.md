---
title: Sumário Lista de Tabelas ou Figuras
linktitle: Sumário Lista de Tabelas ou Figuras
type: docs
weight: 10
url: /pt/reportingservices/table-of-contents-list-of-tables-or-figures/
description: Aprenda como adicionar um Sumário, Lista de Tabelas ou Figuras em relatórios PDF usando Aspose.PDF for Reporting Services.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

O Report Designer não suporta a adição de sumário para documentos de relatório. Com Aspose.Pdf for Reporting Services você pode instruir facilmente o renderizador de PDF a gerar documentos PDF com Sumário, ou Lista de Tabelas ou Figuras. Você pode fazer isso nos passos a seguir:

{{% /alert %}}

{{% alert color="primary" %}}
Certifique-se de que o arquivo Aspose.Pdf.ListSectionStyle.xml existe em ```<Instance>```/bin, onde ```<Instance>``` é o diretório do Report Server. Se o arquivo não existir, crie-o em ```<Instance>```diretório /bin e coloque a marcação a seguir dentro.

## Sumário

**Exemplo**

```cs
<ListSection ListType="TableOfContents">
              <Title Alignment="Center">
            <Segment IsTrueTypeFontBold="true" FontSize="30">TableOfContents</Segment>
              </Title>
              <ListLevelFormat Level="1" LeftMargin="0">
            <TextInfo IsTrueTypeFontBold="true" IsTrueTypeFontItalic="true"></TextInfo>
              </ListLevelFormat>
              <ListLevelFormat Level="2" LeftMargin="10">
            <TextInfo IsUnderline="true" FontSize="10"></TextInfo>
              </ListLevelFormat>
              <ListLevelFormat Level="3" LeftMargin="20">
            <TextInfo IsTrueTypeFontBold="true"></TextInfo>
              </ListLevelFormat>
              <ListLevelFormat Level="4" LeftMargin="30">
            <TextInfo IsTrueTypeFontBold="true"></TextInfo>
              </ListLevelFormat>
</ListSection>
```

##  Lista de Tabelas

**Exemplo**

```cs
<ListSection ListType="ListOfTables">
              <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfTables</Segment>
              </Title>
</ListSection>
```

## Lista de Figuras

**Exemplo**

```cs
 <ListSection ListType="ListOfFigures">
    <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfFigures</Segment>
    </Title>
</ListSection>

```

Consulte a seção 'Working with TOC' da documentação online do Aspose.Pdf.

**2-** Adicione o parâmetro de relatório 'IsListSectionSupported' e defina o valor como True, conforme mostrado no parágrafo 'List Section'.
**3-** Adicione uma propriedade personalizada para o item de relatório que você deseja que seja listado no Sumário, na Lista de Tabelas ou na Lista de Figuras.

{{% /alert %}}

{{% alert color="primary" %}}

**Nome da Propriedade Personalizada** :IsInList
**Valor da Propriedade** :Boolean
**Valor da Propriedade Personalizada** : Verdadeiro ou Falso

{{% alert color="primary" %}}

Marca o item de relatório atual como listado por índice no sumário, ou na lista de tabelas ou figuras.

{{% /alert %}}

**Nome da Propriedade Personalizada** : Title
**Tipo da Propriedade Personalizada** : String

{{% alert color="primary" %}}

O título do item exibido no sumário, lista de tabelas ou figuras.
{{% /alert %}}

**Nome da Propriedade Personalizada** : ListLevel
**Tipo de Propriedade Personalizada** : Inteiro

{{% alert color="primary" %}}

O nível dos itens listados exibidos no sumário.

{{% /alert %}}

{{% /alert %}}

