---
title: テンプレートの作成とエクスポート
linktitle: テンプレートの作成とエクスポート
type: docs
weight: 10
url: /ja/sharepoint/creating-and-exporting-template/
lastmod: "2026-06-18"
description: PDF SharePoint API を使用して、SharePoint でテンプレートを PDF に作成およびエクスポートできます。
---

{{% alert color="primary" %}}

この記事では、Aspose.PDF for SharePoint を使用してテンプレートを作成およびエクスポートする方法を示します。

Aspose.PDF for SharePoint 1.9.2 以降、PDF テンプレートのサポートは SharePoint のサブサイトも対象となります。

{{% /alert %}}

## **テンプレートの作成とエクスポート**
{{% alert color="primary" %}}

Aspose.PDF for SharePoint のエクスポート機能を使用するには、まず「PDF Templates」を使用したリストを作成します。

PDFテンプレートを使用したリストの作成:

![todo:image_alt_text](creating-and-exporting-template_1.png)

2つのドキュメントテンプレート、Task Form Templates と Task List Templates が作成されます:

![todo:image_alt_text](creating-and-exporting-template_2.png)



テンプレート フォームでは、次の情報を入力できます:

- **Name**: テンプレートのファイル名。
- **Title**: テンプレートのタイトルです。（デフォルトでは、ファイル名と同じです。）
- **Description**: テンプレートの説明です。良い説明はテンプレートの使いやすさを向上させます。
- **Assigned List Types**: カンマ区切りのリスト ID（テンプレートに関連しています。このフィールドは **AllListTypes** の値を含むこともできます。このフィールドは **Type** フィールドが **List** に設定されている場合にのみ適用されます）。
- **Assigned Content Types**: カンマ区切りのコンテンツタイプ ID（テンプレートに関連しています。このフィールドは **AllListTypes** に設定される場合があります。このフィールドは **Type** フィールドが **Item** に設定されている場合にのみ適用されます）。
- **Type**: リストテンプレートまたはアイテムテンプレートのいずれかです。
- **Status**: オプションは active、inactive（全員に対して非表示）、debugging（管理者のみ表示）です。

**The Task List Templates form:** タスクリストテンプレートフォーム:

![todo:image_alt_text](creating-and-exporting-template_3.png)




**The Task Form Templates form:** タスクフォームテンプレートフォーム:

![todo:image_alt_text](creating-and-exporting-template_4.png)




保存されると、新しいテンプレートがテンプレート一覧に表示され、すぐに使用できるようになります：

**2つのタスクリストテンプレート:**

![todo:image_alt_text](creating-and-exporting-template_5.png)



**タスクフォームテンプレート:**

![todo:image_alt_text](creating-and-exporting-template_6.png)



#### **テンプレートの開発**
テンプレートは Aspose XML PDF に基づく XML ファイルです。リスト用のテンプレートを作成するには、SharePoint の対象コンテンツタイプフィールドの内部名に関連する特殊マーカーを XML PDF ファイルに配置します。
##### **マーカー**
- **SPListItemsCount** – リスト項目の数に置き換えられます。
- **SPListTitle** – リストのタイトルに置き換えられます。
- **SPTableIterator** – 最初のテーブルセルに配置され、テーブル全体の反復用にマークされます。
- **SPRowIterator** – 最初のテーブルセルに配置され、行の反復用にテーブルがマークされます。
- **SPField** – 項目フィールドの値に置き換えられます。

参考のために、ダウンロードしてください [テンプレート XML ファイル](attachments/8421394/8618082.zip).
#### **PDFへエクスポート**
テンプレートが完全に構成されたら、リストまたはアイテムを PDF ファイルにエクスポートする準備が整います。

**タスクリストテンプレートを使用してリストを PDF にエクスポートする:**

![todo:image_alt_text](creating-and-exporting-template_7.png)

{{% /alert %}}
