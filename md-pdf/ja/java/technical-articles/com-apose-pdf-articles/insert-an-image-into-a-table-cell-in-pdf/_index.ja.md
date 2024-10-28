---
title: PDFの表セルに画像を挿入する
type: docs
weight: 20
url: /java/insert-an-image-into-a-table-cell-in-pdf/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

表はデータを表示するための重要な要素です。それらはデータ表現のための見栄えの良い形式を提供します。表はしばしば数値情報を表示するために使用されます。Aspose.PDF APIは、PDFファイルに表を作成する機能を提供するクラス、Tableを提供します。

単純な表を作成するのではなく、例えば表の枠のスタイル、余白情報、配置、背景色、列の幅、タイトル情報、各ページで繰り返される行の値など、さまざまなフォーマットオプションを設定することができます。

{{% /alert %}}

## Aspose.PDF アプローチ

私たちのDOM（ドキュメントオブジェクトモデル）によれば、ドキュメントはページで構成されています。
 ページには1つ以上の段落が含まれており、段落は画像、テキスト、フォームフィールド、見出し、フローティングボックス、グラフ、添付ファイル、またはテーブルのいずれかである可能性があります。テーブルは行の集まりを持ち、各行はセルの集まりを持ちます。セルは段落の集まりです。

したがって、私たちのDOMによれば、テーブルセルには上記で指定された段落要素（画像を含む）が含まれることがあります。

## セルの幅を理解する

特にテーブルセルに画像を表示する際は、セルの幅を明確に理解しておく必要があります。そうすることで、画像の幅をセルの幅に固定し、適切に表示されるようにできます。画像の幅は、ImageクラスのsetFixedWidth()メソッドを使用して設定できます。

## コード例

```java

 String dataDir = "C:\\temp\\";

// 空のコンストラクタを呼び出してDocumentオブジェクトをインスタンス化

Document pdfDocument = new Document();

// Documentオブジェクトにページを作成

com.aspose.pdf.Page page = pdfDocument.getPages().add();



// テーブルオブジェクトをインスタンス化

Table table = new Table();

// 希望のページの段落コレクションにテーブルを追加

page.getParagraphs().add(table);

// テーブルの列幅を設定

table.setColumnWidths("100 100 120");



// 別のカスタマイズされたBorderInfoオブジェクトを使用してテーブルの境界を設定

table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 1F));



// ページに画像オブジェクトを作成

com.aspose.pdf.Image img1 = new com.aspose.pdf.Image();

// 画像ファイルのパスを設定

img1.setFile(dataDir + "logo.jpg");



img1.setFixWidth(100);

img1.setFixHeight(100);

// テーブルに行を作成し、その行にセルを追加

Row row1 = table.getRows().add();

row1.getCells().add("セル内のサンプルテキスト");

// 画像を保持するセルを追加

Cell cell2 = row1.getCells().add();

// テーブルセルに画像を追加

cell2.getParagraphs().add(img1);



row1.getCells().add("画像付きの前のセル");

row1.getCells().get_Item(2).setVerticalAlignment(VerticalAlignment.Center);



// ドキュメントを保存

pdfDocument.save(dataDir + "Image_in_Cell.pdf");    

```