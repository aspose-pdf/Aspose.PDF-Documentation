---
title: Aspose.PDF for Javaのバージョン4.x.x以前からの移行
type: docs
weight: 20
url: ja/java/migration-from-pre-4-x-x-version-of-aspose-pdf-for-java/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

新しい自動移植版のAspose.PDF for Javaがリリースされ、この単一の製品でPDF文書をゼロから生成する機能と既存のPDF文書を操作する機能がサポートされるようになりました。

{{% /alert %}}

## 製品バイナリ

{{% alert color="primary" %}}

最初のリリースバージョン（v4.0.0）では、2つのjarファイル、すなわち**aspose.pdf-3.3.0.jdk15.jar**と**aspose.pdf-new-4.0.0.jar**を出荷しています。

- **aspose.pdf-3.3.0.jdk14.jar**

このjarファイルは、現在ダウンロードモジュールで利用可能な[Aspose.PDF for java 3.3.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry417659.aspx)と同じ製品バージョンです。今後、このリリースバージョンをレガシーAspose.PDF for Javaと呼ぶことにします。この最初のリリースでは、既存のAspose.PDF for Javaのユーザーには同じリリースバージョンが提供されるため、影響はないかもしれません。しかし、近いうちにこの個別のjarファイルを削除し、レガシーAspose.PDF for Java（4.x.x以前）のすべてのクラスと列挙型が単一のaspose.pdf-new-4.x.x.jarファイルのcom.aspose.pdf.generatorパッケージで利用可能になります。

- **aspose.pdf-new-4.0.0.jar**  
  このjarファイルは、Aspose.PDF for .NETをJavaプラットフォームに自動移植した実際の新バージョンです。
 このjarファイルには、新しいドキュメントオブジェクトモデル（DOM）が含まれており、既存のPDFファイルを作成および操作することができます。また、現在のAspose.PDF.Kit for Javaも含まれています。Aspose.PDF.Kit for Javaのすべてのクラスと列挙型はcom.aspose.pdf.facadesパッケージにまとめられており、2013年第3四半期にはAspose.PDF.Kit for Javaが廃止される予定です。したがって、現在のAspose.PDF.Kit for Javaの顧客には、新しい自動移植版へのコードの移行をお勧めします。

自動移植されたAspose.PDF for Javaの構造についての詳しい情報は、以下のブログ投稿をご覧ください。
{{% /alert %}}