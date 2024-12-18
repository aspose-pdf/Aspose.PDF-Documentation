---
title: 埋め込みリソースとして追加する際のファイル圧縮を無効化する
linktitle: ファイル圧縮の無効化
type: docs
weight: 40
url: /ja/java/disable-files-compression-when-adding-as-embedded-resources/
description: この記事では、埋め込みリソースとして追加する際にファイル圧縮を無効化する方法を説明します
lastmod: "2021-06-05"
---

[FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) クラスは、開発者がPDFドキュメントに添付ファイルを追加することを可能にします。デフォルトでは、添付ファイルは圧縮されます。埋め込みリソースとしてファイルを追加する際に圧縮を無効にするためにAPIを更新しました。これにより、開発者はファイルの処理方法をより細かく制御できます。

開発者がファイル圧縮を制御できるようにするために、[FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) クラスに [setEncoding(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification#setEncoding-int-) メソッドが追加されました。
 このプロパティは、ファイル圧縮に使用されるエンコーディングを決定します。メソッドは、[FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding)列挙型からの値を受け入れます。可能な値は、[FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).Noneおよび[FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).Zipです。

エンコーディングが[FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).Noneに設定されている場合、添付ファイルは圧縮されません。デフォルトのエンコーディングは[FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).Zipです。

次のコードスニペットは、PDFドキュメントに添付ファイルを追加する方法を示しています。

```java
    public static void DisableFilesCompressionWhenAddingAsEmbeddedResources() throws IOException{
  // ソース/入力ファイルの参照を取得
  java.nio.file.Path path = java.nio.file.Paths.get(_dataDir+"input.pdf");
  // ソースファイルからすべての内容をByteArrayに読み込む
  byte[] data = java.nio.file.Files.readAllBytes(path);
  // ByteArrayの内容からStreamオブジェクトのインスタンスを作成
  InputStream is = new ByteArrayInputStream(data);
  // ストリームインスタンスからDocumentオブジェクトをインスタンス化
  Document pdfDocument = new Document(is);
  // 添付ファイルとして追加する新しいファイルを設定
  FileSpecification fileSpecification = new FileSpecification("test.txt", "サンプルテキストファイル");
  // エンコーディングプロパティをFileEncoding.Noneに設定
  fileSpecification.setEncoding(FileEncoding.None);
  // ドキュメントの添付ファイルコレクションに添付ファイルを追加
  pdfDocument.getEmbeddedFiles().add(fileSpecification);
  // 新しい出力を保存
  pdfDocument.save("output.pdf");
    }
```