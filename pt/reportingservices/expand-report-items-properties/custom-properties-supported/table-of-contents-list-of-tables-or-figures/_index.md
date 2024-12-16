---
title: Índice Lista de Tabelas ou Figuras
type: docs
weight: 10
url: /pt/reportingservices/table-of-contents-list-of-tables-or-figures/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

O Designer de Relatórios não suporta a adição de índice para documentos de relatório. Com Aspose.Pdf para Serviços de Relatórios, você pode facilmente instruir o renderizador PDF a produzir documentos PDF com Índice ou Lista de Tabelas ou Figuras. Você pode fazer isso nos seguintes passos:

{{% /alert %}}

{{% alert color="primary" %}}
Certifique-se de que o arquivo Aspose.Pdf.ListSectionStyle.xml exista em ```<Instance>```/bin, onde ```<Instance>``` é o diretório do Servidor de Relatórios. Se o arquivo não existir, crie-o no diretório ```<Instance>```/bin e coloque a seguinte marcação dentro.

## Índice

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

## Lista de Tabelas

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

Por favor, consulte a seção 'Trabalhando com TOC' da documentação online do Aspose.Pdf.

**2-** Adicione o parâmetro de relatório 'IsListSectionSupported' e defina o valor para True, conforme mostrado no parágrafo 'Seção de Lista'.
**3-** Adicione uma propriedade personalizada para o item de relatório que você deseja listar no Sumário, Lista de Tabelas ou Figuras.

{{% /alert %}}

{{% alert color="primary" %}}

**Nome da Propriedade Personalizada** :IsInList
**Valor da Propriedade** :Boolean
**Valor da Propriedade Personalizada** : True ou False

{{% alert color="primary" %}}


Marca o item de relatório atual como listado por índice no sumário, ou na lista de tabelas ou figuras.

{{% /alert %}}

**Custom Property Name** : Título  
**Custom Property Type** : String

{{% alert color="primary" %}}

O título do item exibido no índice, lista de tabelas ou figuras.  
{{% /alert %}}

**Custom Property Name** : ListLevel  
**Custom Property Type** : Integer

{{% alert color="primary" %}}

O nível dos itens listados exibidos no índice.

{{% /alert %}}

{{% /alert %}}