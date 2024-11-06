---
title: PDFドキュメントを作成する
linktitle: 作成
type: docs
weight: 10
url: ja/java/create-document/
description: Aspose.PDF for JavaでPDFファイルを作成する方法を学びます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Java** APIは、Javaアプリケーション開発者がアプリケーションにPDFドキュメント処理機能を組み込むことを可能にします。他のソフトウェアを基盤となるマシンにインストールすることなく、PDFファイルの作成と読み取りを行うことができます。Aspose.PDF for Javaは、デスクトップ、JSP、JSFアプリケーションなど、さまざまなJavaアプリケーションタイプで使用できます。

## Javaを使用してPDFファイルを作成する方法

Javaを使用してPDFファイルを作成するには、次の手順を使用します。

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)オブジェクトをインスタンス化する
1. ドキュメントオブジェクトに[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)を追加する
1. [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment)オブジェクトを作成する

1. ページの[Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs)コレクションに[TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment)を追加する
1. 結果のPDFドキュメントを保存する

```java
// ドキュメントオブジェクトを初期化
Document document = new Document();
 
// ページを追加
Page page = document.getPages().add();
 
// 新しいページにテキストを追加
page.getParagraphs().add(new TextFragment("Hello World!"));
 
// 更新されたPDFを保存
document.save("HelloWorld_out.pdf");
```