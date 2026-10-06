---
title: "Struts 1.3 での Aspose.PDF のダウンロードと構成"
linktitle: "Struts 1.3 での Aspose.PDF のダウンロードと構成"
type: docs
weight: 10
url: /ja/java/downloads-and-configure-aspose-pdf-in-struts-1-3/
description: Struts 1.3 プロジェクトで Aspose.PDF for Java を設定します。アプリケーションの PDF 機能を強化しましょう。
lastmod: "2026-10-06"
---
## Struts 1.3 用 Aspose.PDF for Java のダウンロード

以下の場所からプロジェクトのソースコードをダウンロードまたはチェックアウトしてください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_for_Struts)

## Struts 1.3 用 Aspose.PDF for Java をソースコードからビルド

上記のいずれかのリポジトリからソースコードをチェックアウトした後、以下の mvn コマンドを実行してください。

{{< highlight java >}}

 $ mvn -U clean package

{{< /highlight >}}

これにより、target フォルダーに "Strutsbookapp.war" がビルドされます。

.war ファイルをデプロイするには、実行中の Apache Tomcat サーバーの webapp ディレクトリにコピーしてください。
