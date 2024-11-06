---
title: Aspose.PDF for Java 9.7.1におけるパブリックAPIの変更
type: docs
weight: 80
url: ja/java/public-api-changes-in-aspose-pdf-for-java-9-7-1/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

このページでは、[Aspose.PDF for Java 9.7.1](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry600386.aspx)で導入されたパブリックAPIの変更を一覧にしています。新しいパブリックメソッドや廃止されたメソッドだけでなく、Aspose.PDF for Javaの内部動作の変更によって既存のコードに影響を与える可能性のある変更の説明も含まれています。既存の動作を変更する可能性がある回帰と見なされる動作は特に重要であり、ここに記載されています。

{{% /alert %}}

**importXml(String inputXml)**というメソッドが**com.aspose.facades.Form**クラスに追加され、XMLデータをPDFフォームにインポートすることをサポートしています。

**com.aspose.pdf.generator.legacyxmlmodel.Heading**クラスで以下のメソッドが変更されました

- isAutoSequence(boolean) は setAutoSequence(boolean) に変更されました

- isInList(boolean) は setInList(boolean) に変更されました

## 新機能の実装

- [EPUBからPDFへの変換](http://www.aspose.com/docs/display/pdfjava/Convert+EPUB+File+to+PDF+Format)。
- [検索不可のPDFを検索可能なPDFドキュメントに変換](http://www.aspose.com/docs/display/pdfjava/Converting+non+searchable+PDF+to+searchable+PDF+document)