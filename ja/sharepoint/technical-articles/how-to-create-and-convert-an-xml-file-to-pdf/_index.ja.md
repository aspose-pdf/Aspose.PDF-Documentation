---
title: XMLファイルを作成しPDFに変換する方法
type: docs
weight: 30
url: /sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/
lastmod: "2020-12-16"
description: PDF SharePoint APIはXMLファイルをPDF形式に作成および変換することができます。
---

{{% alert color="primary" %}}

Aspose.PDF for SharePointは、受賞歴のあるAspose.PDF for .NETコンポーネントを基に構築されています。Aspose.PDF for .NETは、ゼロからPDFドキュメントを作成することから既存のPDFファイルを操作することまで、驚くべき機能を提供します。これらの機能の中で、XMLからPDFへの変換は、この製品がサポートする素晴らしい機能の一つです。したがって、Aspose.PDF for SharePointもまた、XMLファイルをPDF形式に変換することができると信じています。

{{% /alert %}}

## **XMLファイルを作成しPDFに変換する**

{{% alert color="primary" %}}

ステップバイステップで、この記事はXMLファイルを作成しPDFに変換するプロセスを案内します：


1. [XMLファイルを作成する](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-1-create-xml-file).
2. [PDFテンプレートを作成する](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-2-create-pdf-template).
3. [XMLテンプレートを読み込む](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-3-load-xml-template).
4. [ソースパスを指定する](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-4-specify-source-file-path).
5. [ファイルプロパティを指定する](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-5-specify-file-properties).
6. [PDFにファイルをエクスポートする](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-6-export-to-pdf).
7. [PDFファイルを保存する](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-7-save-pdf-document).

#### **ステップ1: XMLファイルを作成する**
まず、Aspose.PDF for .NET ドキュメントオブジェクトモデルに基づいてXMLファイルを作成します。

Aspose.PDF for .NET DOMによると、PDFドキュメントはセクションオブジェクトのコレクションを含み、セクションは1つ以上の段落要素を含みます。
 Textは段落レベルのオブジェクトであり、1つ以上のセグメントを含むことができます。以下に、サンプルテキスト文字列をSegmentオブジェクトに追加し、Textオブジェクトに追加する例を示します。最後に、Text要素をSectionオブジェクトの段落コレクションに追加します。

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
#### **ステップ2: PDFテンプレートを作成する**
続行する前に、変換を行うシステムにSharePoint Foundationサーバー2010が正しくインストールされ、設定されていることを確認してください。

1. SharePointサイトにログインします。
1. **サイトの操作**および**すべてのアイテム**を選択します。
1. **作成**オプションを選択し、リストから**PDFテンプレート**を選択します。
1. テンプレート名を入力します。
1. **作成**をクリックします。

![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_1.png)
#### **ステップ3: XMLテンプレートを読み込む**

テンプレートが作成されたら、[XMLファイル](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/)を読み込みます。
1. PDFテンプレートページで、**新しいアイテムを追加**を選択します。




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_2.png)
#### **ステップ 4: ソースファイルパスを指定**

ドキュメントアップロードダイアログで：

1. **参照**をクリックし、システム上のXMLファイルを見つけます。既存のファイルを上書きするオプションを有効にするチェックボックスをオンにすることができます。
1. **OK**ボタンを押します。




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_3.png)
#### **ステップ 5: ファイルプロパティを指定**

ファイルが読み込まれると、必須フィールド（赤いアスタリスクでマークされたもの: *）に情報を追加します。

この例では、サンプルの説明が追加され、次のフィールドが入力されました：

1. ドキュメントの簡単な説明。
1. **割り当てられたリストタイプ**フィールドに**AllListTypes**を入力します。
1. **タイプ**メニューから**リスト**を選択します。
   ステータスが**アクティブ**のままであることを確認してください。
1. **保存**をクリックしてプロパティを保存します。




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_4.png)
#### **ステップ 6: PDFへエクスポート**

XMLファイルがPDFテンプレートに追加されたとき：
Either:

1. test.xmlファイルを右クリックします。
1. メニューから**PDFにエクスポート**を選択します。

Or:

1. **ライブラリツール**から**Asposeツール**を選択します。
1. **エクスポート**をクリックします。

![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_5.png)
#### **ステップ7: PDFドキュメントを保存する**
1. PDFへのエクスポートダイアログで、**テンプレートストレージ**（ソースファイルが保存されている場所）を選択します。
1. **テンプレート名**メニューからエクスポートするファイルを選択します。
1. **PDFにエクスポート**をクリックして最終的なPDFドキュメントを保存します。

![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_6.png)
#### **PDFを開く**
PDFドキュメントが保存され、開くことができます。以下の画像では、XMLの{segment]タグにあったフレーズ「Hello World」に注目してください。また、PDFプロデューサーがAspose.PDF for SharePointであることにも注意してください。

![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_7.png)

{{% /alert %}}