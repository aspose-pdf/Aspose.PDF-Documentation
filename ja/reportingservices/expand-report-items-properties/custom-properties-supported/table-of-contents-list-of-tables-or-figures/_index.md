---
title: 目次・表一覧・図一覧
linktitle: 目次・表一覧・図一覧
type: docs
weight: 10
url: /ja/reportingservices/table-of-contents-list-of-tables-or-figures/
description: Aspose.PDF for Reporting Services を使用して、PDF レポートに目次、表一覧、または図一覧を追加する方法を学びます。
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Report Designer はレポート ドキュメントに目次を追加することをサポートしていません。Aspose.Pdf for Reporting Services を使用すると、PDF レンダラーに目次や表一覧、図一覧を含む PDF ドキュメントを簡単に生成させることができます。以下の手順で実行できます：

{{% /alert %}}

{{% alert color="primary" %}}
Aspose.Pdf.ListSectionStyle.xml ファイルが存在することを確認してください ```<Instance>```/bin、どこ ```<Instance>``` Report Server のディレクトリです。ファイルが存在しない場合は、その中に作成してください。 ```<Instance>```/bin ディレクトリに、以下のマークアップを配置します。

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

##  表のリスト

**例**

```cs
<ListSection ListType="ListOfTables">
              <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfTables</Segment>
              </Title>
</ListSection>
```

## 図の一覧

**例**

```cs
 <ListSection ListType="ListOfFigures">
    <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfFigures</Segment>
    </Title>
</ListSection>

```

Aspose.Pdf のオンラインドキュメントの 'Working with TOC' セクションをご参照ください。

**2-** 'IsListSectionSupported' レポート パラメータを追加し、'List Section' 段落に示すように値を True に設定します。
**3-** 目次、表一覧、または図一覧に掲載したいレポート アイテムのカスタム プロパティを追加します。

{{% /alert %}}

{{% alert color="primary" %}}

**カスタム プロパティ名** :IsInList
**プロパティ値** :Boolean
**カスタム プロパティ値** : True または False

{{% alert color="primary" %}}

現在のレポート項目を目次、表、図の一覧のインデックスでリストされたものとしてマークします。

{{% /alert %}}

**カスタム プロパティ名** : タイトル
**カスタム プロパティタイプ** : 文字列

{{% alert color="primary" %}}

目次、表一覧、または図一覧に表示される項目のタイトルです。
{{% /alert %}}

**カスタム プロパティ名** : リストレベル
**カスタム プロパティ タイプ** : 整数

{{% alert color="primary" %}}

目次に表示されるリスト項目のレベル。

{{% /alert %}}

{{% /alert %}}

