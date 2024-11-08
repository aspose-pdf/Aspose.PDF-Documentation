---
title: 目次 図表の一覧
type: docs
weight: 10
url: /ja/reportingservices/table-of-contents-list-of-tables-or-figures/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

レポートデザイナーはレポート文書の目次の追加をサポートしていません。Aspose.Pdf for Reporting Servicesを使用すると、PDFレンダーに指示して目次や図表の一覧を含むPDF文書を簡単に作成できます。次の手順で行うことができます。

{{% /alert %}}

{{% alert color="primary" %}}
Aspose.Pdf.ListSectionStyle.xmlファイルが```<Instance>```/binに存在することを確認してください。ここで```<Instance>```はレポートサーバーのディレクトリです。ファイルが存在しない場合は、```<Instance>```/binディレクトリに作成し、以下のマークアップを配置してください。

## 目次

**例**

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


## List of TableS

**Example**

```cs
<ListSection ListType="ListOfTables">
              <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfTables</Segment>
              </Title>
</ListSection>
```

## List of Figures

**Example**

```cs
 <ListSection ListType="ListOfFigures">
    <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfFigures</Segment>
    </Title>
</ListSection>

```

Aspose.Pdf のオンラインドキュメントの「TOC の操作」セクションを参照してください。

**2-** レポートパラメータ 'IsListSectionSupported' を追加し、「リストセクション」パラグラフに示されているように値を True に設定します。
**3-** 目次、表のリストまたは図のリストにリストされるレポートアイテムのカスタムプロパティを追加します。

{{% /alert %}}

{{% alert color="primary" %}}

**Custom Property Name** :IsInList
**Property Value** :Boolean
**Custom Property Value** : True or False

{{% alert color="primary" %}}

現在のレポートアイテムを目次、表のリスト、または図のリストにインデックスでリストされているものとしてマークします。

{{% /alert %}}

**Custom Property Name** : Title
**Custom Property Type** : String

{{% alert color="primary" %}}

目次、表や図の一覧に表示されるアイテムのタイトル。
{{% /alert %}}

**Custom Property Name** : ListLevel
**Custom Property Type** : Integer

{{% alert color="primary" %}}

目次に表示されるリストアイテムのレベル。

{{% /alert %}}

{{% /alert %}}