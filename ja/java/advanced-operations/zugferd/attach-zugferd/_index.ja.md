---
title: PDF/3-A準拠のPDFを作成し、ZUGFeRD請求書をJavaで添付する
linktitle: PDFにZUGFeRDを添付
type: docs
weight: 10
url: /java/attach-zugferd/
description: Aspose.PDF for JavaでZUGFeRDを使用してPDFドキュメントを生成する方法を学ぶ
lastmod: "2024-01-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDFにZUGFeRDを添付

PDFにZUGFeRDを添付するために、次の手順をお勧めします：

* 入力および出力PDFファイルがあるフォルダを指すパス変数を定義します。
* 処理されるPDFファイルのパスを格納する文字列変数pathを定義します。`Paths.get`メソッドを使用してフルパスの部分を結合します。
* try-with-resourcesステートメントを作成し、パス変数から作成されたDocumentオブジェクトがステートメントの終了後に自動的に閉じられることを保証します。Documentオブジェクトは、変更および保存されるPDFドキュメントを表します。

* ZUGFeRD標準に準拠した請求書メタデータを含む別のファイルのパスと説明を提供して[FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/)オブジェクトを作成します。
* ファイル仕様オブジェクトにプロパティを追加します。例えば、説明、MIMEタイプ、AFrelationshipなどです。AFrelationshipは、埋め込みファイルがPDFドキュメントとどのように関連しているかを示します。この場合、「Alternative」に設定されており、埋め込みファイルがPDFコンテンツの代替表現であることを意味します。
* ファイル仕様オブジェクトをドキュメントの埋め込みファイルコレクションに追加します。ファイル名はZUGFeRD標準に従って指定する必要があります。例: "factor-x.xml"。
* ドキュメントをPDF/A-3Uフォーマットに変換します。これは、電子ドキュメントの長期保存を保証するPDFのサブセットです。PDF/A-3Uは、PDFドキュメントに任意のフォーマットのファイルを埋め込むことを許可します。
* 変換されたドキュメントを新しいPDFファイルとして保存します（例: "ZUGFeRD-res.pdf"）。
* try-with-resourcesステートメントを閉じて、Documentオブジェクトを解放します。

```java
String _dataDir = "/home/aspose/pdf-examples/Samples/";
String path = Paths.get(_dataDir, "ZUGFeRD", "ZUGFeRD-test.pdf").toString();
try (Document document = new Document(path)) {
    String description = "ZUGFeRD標準に準拠した請求書のメタデータ";
    path = Paths.get(_dataDir, "ZUGFeRD", "factur-x.xml").toString();
    FileSpecification fileSpecification = new FileSpecification(path.toString(), description);
    fileSpecification.setMIMEType("text/xml");
    fileSpecification.setAFRelationship(com.aspose.pdf.AFRelationship.Alternative);

    // ドキュメントの添付ファイルコレクションに添付ファイルを追加
    document.getEmbeddedFiles().add(fileSpecification);
    path = Paths.get(_dataDir, "ZUGFeRD", "log.xml").toString();
    document.convert(path, PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);
    path = Paths.get(_dataDir, "ZUGFeRD", "ZUGFeRD-res.pdf").toString();
    document.save(path);
}
```