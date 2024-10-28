---
title: PDFドキュメントでのポートフォリオの作業
linktitle: ポートフォリオ
type: docs
weight: 40
url: /java/portfolio/
description: JavaでPDFポートフォリオを作成する方法。Microsoft Excelファイル、Wordドキュメント、および画像ファイルを使用してPDFポートフォリオを作成する必要があります。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

まず、**PDFポートフォリオファイル形式とは何か**を理解しましょう。

例えば、Word、Excel、PowerPointプレゼンテーションなどを添付ファイルとして含むPDFポートフォリオファイルを考えてみましょう。ここで、各添付ファイルはその元のドキュメント形式を保持していますが、1つのPDFポートフォリオファイルに埋め込まれたり組み立てられたりしています。もちろん、PDFポートフォリオの各個別ファイルをドライブやフォルダ上にあるかのように開いたり、読んだり、編集したりすることができます。さらに、通常のPDFドキュメントと同様に、透かしを適用したり、添付ファイルの表示、印刷、変更の権限を設定したりすることもできます。

元のタイプや形式のままのネイティブファイルをPDFポートフォリオファイルに添付ファイルとして配置または組み立てることができます。

## PDFポートフォリオの作成方法

Aspose.PDFは、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスを使用してPDFポートフォリオドキュメントを作成することができます。[FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification)クラスを使用して取得した後、Document.Collectionオブジェクトにファイルを追加します。ファイルが追加されたら、DocumentクラスのSaveメソッドを使用してポートフォリオドキュメントを保存します。

以下の例では、Microsoft Excelファイル、Wordドキュメント、画像ファイルを使用してPDFポートフォリオを作成します。

以下のコードは、次のポートフォリオを生成します。

### Aspose.PDFを使用して作成されたPDFポートフォリオ

![Aspose.PDF for Javaを使用して作成されたPDFポートフォリオ](working-with-pdf-portfolio_1.jpg)

```java
    public static void CreatePortfolio() throws IOException {
        // Documentオブジェクトのインスタンスを作成
        Document pdfDocument = new Document();

        // ドキュメントコレクションオブジェクトのインスタンスを作成
        pdfDocument.setCollection(new Collection());

        // ポートフォリオに追加するファイルを取得
        FileSpecification excel = new FileSpecification(_dataDir + "HelloWorld.xlsx");
        FileSpecification word = new FileSpecification(_dataDir + "HelloWorld.docx");
        FileSpecification image = new FileSpecification(_dataDir + "aspose-logo.jpg");

        // ファイルの説明を提供
        excel.setDescription ("Excelファイル");
        word.setDescription ("Wordファイル");
        image.setDescription ("画像ファイル");

        // ドキュメントコレクションにファイルを追加
        pdfDocument.getCollection().add(excel);
        pdfDocument.getCollection().add(word);
        pdfDocument.getCollection().add(image);

        // ポートフォリオドキュメントを保存
        pdfDocument.save(_dataDir + "CreatePDFPortfolio_out.pdf");
    }
```


## PDFポートフォリオからファイルを抽出する

PDFポートフォリオを使用すると、さまざまなソース（例えば、PDF、Word、Excel、JPEGファイル）からのコンテンツを1つの統一されたコンテナにまとめることができます。元のファイルは個々のアイデンティティを保持しますが、PDFポートフォリオファイルに組み込まれます。ユーザーは、各コンポーネントファイルを他のコンポーネントファイルとは独立して開き、読み、編集し、フォーマットすることができます。

Aspose.PDFは、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) クラスを使用してPDFポートフォリオ文書を作成することができます。また、PDFポートフォリオからファイルを抽出する機能も提供します。

以下のコードスニペットは、PDFポートフォリオからファイルを抽出する手順を示しています。

![PDFポートフォリオからファイルを抽出する](working-with-pdf-portfolio_2.jpg)

```java
    public static void ExtractPortfolio() throws IOException {
        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "PDFPortfolio.pdf");
        // 埋め込みファイルのコレクションを取得する
        EmbeddedFileCollection embeddedFiles = pdfDocument.getEmbeddedFiles();

        // ポートフォリオの個々のファイルを反復処理する
        for (FileSpecification fileSpecification : embeddedFiles) {
            InputStream initialStream = fileSpecification.getContents();
            byte[] buffer = new byte[fileSpecification.getContents().available()];
            initialStream.read(buffer);

            File targetFile = new File(_dataDir + fileSpecification.getName());
            OutputStream outStream = new FileOutputStream(targetFile);
            outStream.write(buffer);
            outStream.close();
        }
    }
```


## PDFポートフォリオからファイルを削除する

PDFポートフォリオからファイルを削除するには、以下のコード行を使用してみてください。

```java
public static void RemoveFilesFromPDFPortfolio() {
    // ソースPDFポートフォリオを読み込む
    Document pdfDocument = new Document(_dataDir + "PDFPortfolio.pdf");
    pdfDocument.getCollection().delete();
    pdfDocument.save(_dataDir + "No_PortFolio_out.pdf");
}
```