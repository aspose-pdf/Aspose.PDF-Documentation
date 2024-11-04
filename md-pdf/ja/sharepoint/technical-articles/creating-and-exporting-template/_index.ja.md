---
title: テンプレートの作成とエクスポート
type: docs
weight: 10
url: /sharepoint/creating-and-exporting-template/
lastmod: "2020-12-16"
description: SharePointでPDF SharePoint APIを使用してテンプレートを作成およびエクスポートできます。
---

{{% alert color="primary" %}}

この記事では、Aspose.PDF for SharePointを使用してテンプレートを作成およびエクスポートする方法を示します。

Aspose.PDF for SharePoint 1.9.2以降、PDFテンプレートのサポートはSharePointのサブサイトもカバーします。

{{% /alert %}}

## **テンプレートの作成とエクスポート**
{{% alert color="primary" %}}

Aspose.PDF for SharePointのエクスポート機能を使用するには、まず「PDFテンプレート」を使用するリストを作成します。

PDFテンプレートを使用するリストを作成する:

![todo:image_alt_text](creating-and-exporting-template_1.png)

タスクフォームテンプレートとタスクリストテンプレートの2つのドキュメントテンプレートが作成されます:

![todo:image_alt_text](creating-and-exporting-template_2.png)

テンプレートフォームでは、次の情報を入力できます:

- **Name**: テンプレートのファイル名。
- **Title**: テンプレートのタイトル。
  (デフォルトでは、ファイル名と同じです。)
- **説明**: テンプレートの説明。良い説明はテンプレートの使いやすさを向上させます。
- **割り当てられたリストタイプ**: カンマで区切られたリストID (テンプレートに関連しています。このフィールドは**AllListTypes**の値を含むこともあります。このフィールドは、**Type**フィールドが**List**に設定されている場合にのみ適用されます)。
- **割り当てられたコンテンツタイプ**: カンマで区切られたコンテンツタイプID (テンプレートに関連しています。このフィールドは**AllListTypes**に設定されることがあります。このフィールドは、**Type**フィールドが**Item**に設定されている場合にのみ適用されます)。
- **タイプ**: リストテンプレートまたはアイテムテンプレートのいずれか。
- **ステータス**: オプションはアクティブ、非アクティブ (すべてに対して不可視)、デバッグ中 (管理者にのみ可視) です。

**タスクリストテンプレートフォーム:**

![todo:image_alt_text](creating-and-exporting-template_3.png)




**タスクフォームテンプレートフォーム:**

![todo:image_alt_text](creating-and-exporting-template_4.png)




保存されると、新しいテンプレートがテンプレートリストに表示され、使用する準備が整います:


**2つのタスクリストテンプレート:**
![todo:image_alt_text](creating-and-exporting-template_5.png)

**タスクフォームテンプレート:**

![todo:image_alt_text](creating-and-exporting-template_6.png)

#### **テンプレートの開発**
テンプレートは、Aspose XML PDFに基づくXMLファイルです。リスト用のテンプレートを作成するには、SharePointのターゲットコンテンツタイプフィールドの内部名に関連する特別なマーカーをXML PDFファイルに配置します。
##### **マーカー**
- **SPListItemsCount** – リストアイテムの数で置き換えられます。
- **SPListTitle** – リストタイトルで置き換えられます。
- **SPTableIterator** – 最初のテーブルセルに配置し、テーブルを完全に繰り返すことを示します。
- **SPRowIterator** – 最初のテーブルセルに配置し、行繰り返しを示します。
- **SPField** – アイテムフィールドの値で置き換えられます。

参考のために、[テンプレートXMLファイル](attachments/8421394/8618082.zip)をダウンロードしてください。
#### **PDFへのエクスポート**
テンプレートが完全に設定されたら、リストやアイテムをPDFファイルにエクスポートする準備が整いました。

**タスクリストテンプレートを使用してリストをPDFにエクスポートする:**


![todo:画像の代替テキスト](creating-and-exporting-template_7.png)

{{% /alert %}}
