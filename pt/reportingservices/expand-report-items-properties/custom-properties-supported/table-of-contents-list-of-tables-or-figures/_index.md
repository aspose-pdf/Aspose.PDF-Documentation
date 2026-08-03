---
title: Índice Lista de tabelas ou figuras
linktitle: Table of Contents List of Tables or Figures
type: docs
weight: 10
url: /reportingservices/table-of-contents-list-of-tables-or-figures/
description: Aprenda como adicionar um índice, uma lista de tabelas ou figuras em relatórios PDF usando Aspose.PDF para Reporting Services.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

O Designer de Relatórios não oferece suporte à adição de sumário para documentos de relatório. Com Aspose.PDF for Reporting Services você pode facilmente instruir o renderizador de PDF para produzir documentos PDF com Índice ou Lista de Tabelas ou Figuras. Você pode fazer isso nas seguintes etapas:

{{% /alert %}}

Certifique-se de que o arquivo Aspose.Pdf.ListSectionStyle.xml exista no diretório ```<Instance>```/bin, where ```<Instance>``` is the directory of the Report Server. If the file does not exist, create it in the ```<Instance>```/bin e coloque a seguinte marcação dentro dele.

## Índice

### Exemplo

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

### Exemplo

```cs
<ListSection ListType="ListOfTables">
              <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfTables</Segment>
              </Title>
</ListSection>
```

## Lista de Figuras

### Exemplo

```cs
 <ListSection ListType="ListOfFigures">
    <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfFigures</Segment>
    </Title>
</ListSection>

```

Consulte a seção 'Trabalhando com TOC' da documentação online do Aspose.Pdf.

**2-** Adicione o parâmetro de relatório `IsListSectionSupported` e defina o valor como True conforme mostrado no parágrafo `List Section`.
**3-** Adicione uma propriedade personalizada para o item do relatório que você deseja que seja listado no Índice, Lista de Tabelas ou Figuras.

```text
Custom Property Name: IsInList
Property Value: Boolean
Custom Property Value: True or False
```

Marca o item do relatório atual como listado por índice no índice ou na lista de tabelas ou figuras.

```text
Custom Property Name: Title
Custom Property Type: String
```

O título do item exibido no índice, lista de tabelas ou figuras.

```text
Custom Property Name: ListLevel
Custom Property Type: Integer
```

O nível dos itens listados exibidos no índice.
