---
title: ワークフローアクティビティを介してファイルをPDFに変換する
type: docs
weight: 50
url: /ja/sharepoint/converting-a-file-to-pdf-via-workflow-activity/
lastmod: "2020-12-16"
description: PDF SharePoint APIは、ドキュメントをPDFに変換するSharePointワークフローで使用できます。
---

{{% alert color="primary" %}}

ワークフローのサポートは、Microsoft Office SharePoint Serverの主要な機能です。ワークフローは、ビジネスロジックに従ったドキュメントの移動を自動化し、ドキュメントの整理にかかるコストと時間を効率化します。この記事では、Aspose.PDF for SharePointを使用して、ドキュメントをPDFに変換するワークフローを作成する方法を示します。

{{% /alert %}}
## **ワークフローの設定**

この例では、ドキュメントライブラリ内の新しいアイテムをPDF形式に変換し、別のドキュメントライブラリに保存するワークフローを作成します。この例では、**個人用ドキュメント**ライブラリをソースライブラリとして使用し、**共有ドキュメント**ライブラリ内の**Pdf**サブフォルダを宛先ライブラリとして使用します。

Aspose.PDF for SharePointは、HTML、テキスト、画像ファイルの変換をサポートしています。

### **SharePoint Designerを使用してワークフローを設計する**

1. **SharePoint Designer**を開き、ワークフローを実装するサイトに接続します。
1. **サイトオブジェクト**から**ワークフロー**を選択し、**リストワークフロー**を開きます。
1. **個人用ドキュメント**ライブラリを選択して、新しいリストワークフローをドキュメントライブラリに作成して添付します。

   **メニューから個人用ドキュメントを選択する**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_1.png)


1. ワークフロー名と説明を入力して、**個人用ドキュメント**ライブラリにリストワークフローを作成して添付します。
1. このステップを完了するには、**OK**をクリックします。

   **リストワークフローを作成する**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_2.png)


ワークフローステップエディタが表示されます。これは、ワークフローの条件とアクションを定義するために使用されます。次に、**Aspose Actions**から条件なしで新しいドキュメントをPDFに変換するアクションを追加します。
1. **アクション** メニューから **Aspose.PDF を介してファイルを PDF に変換** アクションを選択します。

   **アクションの選択**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_3.png)


1. アクションパラメータを設定します:
   1. **このフォルダ** パラメータを宛先フォルダに設定します。
   1. 他のアクションパラメータをデフォルト値のままにするか、アクションプロパティウィンドウを使用して設定します。**上書き** パラメータのデフォルト値は false です。

      **ワークフローエディタ**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_4.png)



**宛先ライブラリの設定**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_5.png)



**プロパティの設定**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_6.png)




1. **ワークフロー** メニューから **ワークフロー設定** を選択します。
1. **新しいアイテムが作成されたときに自動的にワークフローを開始する** を選択し、**開始オプション** の他のオプションをクリアします。

   **開始オプションの設定**
![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_7.png)

ワークフローの設計が完了しました。

1. ワークフローを保存して公開し、SharePointサイトに実装します。

### **ワークフローをテストする**

ワークフローをテストするには：

1. SharePointサイトを開き、**個人用ドキュメント** ドキュメントライブラリに新しいドキュメントをアップロードします。  
   Aspose.PDF for SharePointは、HTMLファイル、テキストファイル、画像（JPG、PNG、GIF、TIFF、BMP*）からPDFへの変換をサポートしています。ワークフローは新しいアイテムが作成されたときに自動的に開始されるように設定されているため、ファイルは自動的に処理されます。
1. ブラウザを更新します。  
   ワークフローのステータスは、ワークフロー列に表示されます。この場合、**Aspose.PDF Workflow** です。

   **ソースライブラリにドキュメントを追加する**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_8.png)

1. 変換されたドキュメントを表示するために、宛先のドキュメントライブラリを開きます。この例では **Shared Documents/Pdf** がパスです。

   **宛先ライブラリ**
![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_9.png)

title: ファイルをPDFに変換するワークフローアクティビティ
changefreq: "monthly"
type: docs
```

## 概要

この文書は、ファイルをPDFに変換するためのワークフローアクティビティの使用方法を説明します。

## 前提条件

- ワークフローアクティビティのインストールが完了していること
- ファイルが正しい形式であることを確認してください

## 手順

1. ワークフローエディタを開きます。
2. 新しいアクティビティを追加します。
3. アクティビティの設定を開き、以下のオプションを設定します。

input_file: 入力ファイルのパス
output_file: 出力PDFファイルのパス
```

4. アクティビティを保存して、ワークフローを実行します。

## エラーハンドリング

以下のエラーが発生する可能性があります：

- `ファイル形式がサポートされていません。`: 入力ファイルの形式を確認してください。
- `出力ディレクトリへのアクセスが拒否されました。`: 出力先のパスを確認し、必要なアクセス権を持っていることを確認してください。

## 結論

この文書では、ファイルをPDFに変換するための基本的なワークフローアクティビティの設定手順を説明しました。このプロセスは、他のワークフローにも簡単に統合できます。