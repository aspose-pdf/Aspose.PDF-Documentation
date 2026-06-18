---
title: XML ファイルを作成し PDF に変換する方法
linktitle: XML ファイルを作成し PDF に変換する方法
type: docs
weight: 30
url: /ja/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/
lastmod: "2026-06-18"
description: PDF SharePoint API は XML ファイルを作成し、PDF 形式に変換することができます。
---

{{% alert color="primary" %}}

Aspose.PDF for SharePoint は、受賞歴のある Aspose.PDF for .NET コンポーネントの上に構築されています。Aspose.PDF for .NET は、ゼロから PDF ドキュメントを作成することから既存の PDF ファイルを操作することまで、優れた機能を提供します。これらの機能の中で、XML から PDF への変換はこの製品がサポートする重要な機能の一つです。そのため、Aspose.PDF for SharePoint も XML ファイルを PDF 形式に変換できると考えています。

{{% /alert %}}

## **XML ファイルの作成と PDF への変換**

{{% alert color="primary" %}}

ステップバイステップで、この記事は XML ファイルを作成し PDF に変換するプロセスをご案内します：

1. [XML ファイルを作成する](/pdf/ja/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-1-create-xml-file).
2. [PDFテンプレートを作成する](/pdf/ja/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-2-create-pdf-template).
3. [XMLテンプレートをロードする](/pdf/ja/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-3-load-xml-template).
4. [ソースパスへのパスを指定する](/pdf/ja/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-4-specify-source-file-path).
5. [ファイルのプロパティを指定する](/pdf/ja/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-5-specify-file-properties).
6. [ファイルをPDFにエクスポートする](/pdf/ja/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-6-export-to-pdf).
7. [PDFファイルを保存する](/pdf/ja/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-7-save-pdf-document).
#### **ステップ 1: XML ファイルの作成**
まず、Aspose.PDF for .NET のドキュメントオブジェクトモデルに基づいて XML ファイルを作成します。

Aspose.PDF for .NET DOM によると、PDF ドキュメントは Section オブジェクトのコレクションを含み、Section は 1 つ以上の Paragraph 要素を含みます。Text は Paragraph レベルのオブジェクトで、1 つ以上のセグメントを含むことができます。以下では、サンプルのテキスト文字列を Segment オブジェクトに追加し、さらに Text オブジェクトに追加します。最後に、Text 要素を Section オブジェクトの paragraphs コレクションに追加します。

**XML**

{{< highlight csharp >}}



<?xml version="1.0" encoding="utf-8" ?>

  <Pdf xmlns="Aspose.PDF">

   <Section>

    <Text>

            <Segment>こんにちは世界</Segment>

    </Text>

   </Section>

  </Pdf>



{{< /highlight >}}
#### **ステップ 2: PDF テンプレートの作成**
続行する前に、変換が行われるシステムに SharePoint Foundation server 2010 が正しくインストールされ、構成されていることを確認してください。

1. SharePoint サイトにログインします。
1. **Site Action** と **All Items** を選択します。
1. リストから **Create** オプションを選択し、**PDF Template** を選択します。
1. テンプレート名を入力します。
1. **Create** をクリックします。




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_1.png)
#### **ステップ 3: XML テンプレートの読み込み**
テンプレートが作成されたら、ロードします [XML ファイル](/pdf/ja/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/):

1. PDFテンプレートページで、**Add new item** を選択します。




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_2.png)
#### **ステップ 4: ソース ファイル パス の 指定**
ドキュメントアップロード ダイアログで：

1. **Browse** をクリックして、システム上の XML ファイルを見つけます。既存のファイルを上書きするオプションのチェック ボックスを有効にすることができます。
1. **OK** ボタンを押します。




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_3.png)
#### **ステップ 5: ファイル プロパティ の 指定**
ファイルがロードされたら、必須フィールド（赤いアスタリスク * でマークされたもの）に情報を追加してください。

この例では、サンプルの説明が追加され、以下のフィールドが入力されました:

1. ドキュメントの簡単な説明。
1. **Assigned List Types** フィールドに **AllListTypes** を入力してください。
1. **Type** メニューから **List** を選択してください。
   ステータスが **Active** のままであることを確認してください。
1. プロパティを保存するには、**Save** をクリックしてください。




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_4.png)
#### **ステップ 6: PDF にエクスポート**
XML ファイルが PDF テンプレートに追加されたとき:
いずれか:

1. test.xml ファイルを右クリックします。
1. メニューから **Export to PDF** を選択します。

または:

1. **Library Tools** から **Aspose Tools** を選択してください。
1. **Export** をクリックしてください。




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_5.png)
#### **Step 7: PDF ドキュメントを保存**
1. Export to PDF ダイアログで、**Template storage**（ソースファイルが保存されている場所）を選択してください。
1. **Template name** メニューからエクスポートするファイルを選択してください。
1. 最終的な PDF ドキュメントを保存するには、**Export to PDF** をクリックしてください。




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_6.png)
#### **PDF を開く**
PDF ドキュメントが保存され、開くことができます。下の画像では、XML の {segment] タグにあったフレーズ "Hello World" に注目してください。また、PDF Producer が Aspose.PDF for SharePoint であることにも注目してください。




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_7.png)

{{% /alert %}}
