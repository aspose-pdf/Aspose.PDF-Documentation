---
title: 目次 表または図のリスト
linktitle: 目次 表または図のリスト
type: docs
weight: 10
url: /reportingservices/table-of-contents-list-of-tables-or-figures/
description: Aspose.PDF for Reporting Services を使用して、PDF レポートに目次、表のリスト、または図を追加する方法を学習します。
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

レポート デザイナーは、レポート ドキュメントの目次の追加をサポートしていません。 Aspose.PDF for Reporting Services を使用すると、PDF レンダリングに目次、表や図のリストを含む PDF ドキュメントを生成するよう簡単に指示できます。次の手順で実行できます。

{{% /alert %}}

Aspose.Pdf.ListSectionStyle.xml ファイルが ```<Instance>```/bin, where ```<Instance>``` is the directory of the Report Server. If the file does not exist, create it in the ```<Instance>```/bin ディレクトリに存在することを確認し、その中に次のマークアップを配置します。

## 目次

### 例

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

##  テーブルのリスト

### 例

```cs
<ListSection ListType="ListOfTables">
              <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfTables</Segment>
              </Title>
</ListSection>
```

## フィギュア一覧

### 例

```cs
 <ListSection ListType="ListOfFigures">
    <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfFigures</Segment>
    </Title>
</ListSection>

```

Aspose.Pdf オンライン ドキュメントの「目次の操作」セクションを参照してください。

**2-** レポート パラメータ `IsListSectionSupported` を追加し、`List Section` 段落に示すように値を True に設定します。
**3-** 目次、表または図のリストに表示するレポート アイテムのカスタム プロパティを追加します。

```text
Custom Property Name: IsInList
Property Value: Boolean
Custom Property Value: True or False
```

現在のレポート アイテムを、目次、または表や図のリストのインデックスによってリストされているようにマークします。

```text
Custom Property Name: Title
Custom Property Type: String
```

目次、表または図のリストに表示される項目のタイトル。

```text
Custom Property Name: ListLevel
Custom Property Type: Integer
```

目次に表示されるリスト項目のレベル。
