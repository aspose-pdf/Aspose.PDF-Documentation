---
title: ダウンロードとAspose.PdfのStruts 1.3への設定
type: docs
weight: 10
url: /java/downloads-and-configure-aspose-pdf-in-struts-1-3/
lastmod: "2021-06-05"
---

## Struts 1.3用のAspose.PDF Javaのダウンロード

以下の場所からプロジェクトのソースコードをダウンロードまたはチェックアウトできます：

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_for_Struts)

## ソースコードからStruts 1.3用のAspose.PDF Javaのビルド

上記のリポジトリからソースコードをチェックアウトした後、以下のmvnコマンドを適用します：

{{< highlight java >}}

 $ mvn -U clean package

{{< /highlight >}}

これにより、ターゲットフォルダに「Strutsbookapp.war」がビルドされます。

.warファイルをデプロイするには、実行中のApache tomcatサーバーのwebappディレクトリにコピーするだけです。