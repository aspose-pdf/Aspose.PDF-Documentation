---
title: ワークフロー アクティビティによるファイルの PDF 変換
linktitle: ワークフロー アクティビティによるファイルの PDF 変換
type: docs
weight: 50
url: /ja/sharepoint/converting-a-file-to-pdf-via-workflow-activity/
lastmod: "2026-06-18"
description: PDF SharePoint API は、ドキュメントを PDF に変換する SharePoint ワークフローで使用できます。
---

{{% alert color="primary" %}}

ワークフローのサポートは Microsoft Office SharePoint Server の重要な機能です。ワークフローは、ビジネス ロジックに従ったドキュメントの移動を自動化し、ドキュメント管理のコストと時間を効率化します。本稿では、ドキュメントを PDF に変換するワークフローで Aspose.PDF for SharePoint の使用方法を示します。

{{% /alert %}}
## **ワークフローの設定**

この例は、ドキュメント ライブラリ内の新しいアイテムを PDF 形式に変換し、別のドキュメント ライブラリに保存するワークフローを作成します。この例では、ソース ライブラリとして **Personal Documents** ライブラリを使用し、宛先ライブラリとして **Shared Documents** ライブラリ内の **Pdf** サブフォルダーを使用します。

Aspose.PDF for SharePoint は、HTML、テキスト、画像ファイルの変換をサポートします。

### **SharePoint Designer を使用してワークフローを設計**

1. **SharePoint Designer** を開き、ワークフローが実装されるサイトに接続します。
1. **site objects** から **Workflows** を選択し、次に **List Workflow** を開きます。
1. **Personal Documents** ライブラリを選択し、ドキュメント ライブラリに新しいリスト ワークフローを作成して添付します。

   **メニューから Personal Documents を選択**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_1.png)


1. ワークフロー名と説明を入力して、**Personal Documents** ライブラリにリスト ワークフローを作成し、添付します。
1. この手順を完了するには **OK** をクリックしてください。

   **リストワークフローの作成**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_2.png)



ワークフローステップエディタが表示されます。これはワークフローの条件とアクションを定義するために使用されます。次に、**Aspose Actions** から条件なしで新しいドキュメントを PDF に変換するアクションを追加します。

1. **Action** メニューから **Convert file to PDF via Aspose.PDF** アクションを選択します。

   **アクションの選択**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_3.png)


1. アクションのパラメータを構成します：
   1. **this folder** パラメータを宛先フォルダーに設定します。
   1. 他のアクションパラメータはデフォルト値のままにするか、アクションプロパティウィンドウで設定してください。**Overwrite** パラメータのデフォルト値は false です。

      **Workflow エディタ**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_4.png)



**宛先ライブラリの設定**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_5.png)



**プロパティの設定**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_6.png)




1. **Workflow** メニューから **Workflow Settings** を選択します。
1. 「**新しいアイテムが作成されたときにワークフローを自動的に開始**」を選択し、**開始オプション**から他のオプションをすべてクリアします。

   **開始オプションの設定**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_7.png)



ワークフローの設計が完了しました。

1. ワークフローを保存して公開し、SharePoint サイトで実装します。

### **ワークフローのテスト**

ワークフローをテストするには:

1. SharePoint サイトを開き、**Personal Documents** ドキュメント ライブラリに新しいドキュメントをアップロードします。
   Aspose.PDF for SharePoint は HTML ファイル、テキスト ファイル、および画像（JPG、PNG、GIF、TIFF、BMP*）から PDF への変換をサポートします。ワークフローは新しいアイテムが作成されたときに自動的に開始するように構成されているため、ファイルは自動的に処理されます。
1. ブラウザを更新します。
   ワークフロー ステータスはワークフロー列に表示されます。この例では **Aspose.PDF Workflow** です。

   **ソース ライブラリにドキュメントを追加**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_8.png)




1. 変換されたドキュメントを表示するには、宛先のドキュメント ライブラリを開きます。この例ではパスは **Shared Documents/Pdf** です。

   **宛先ライブラリ**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_9.png)

