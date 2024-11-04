---
title: PDFファイルにリンクを作成する
linktitle: リンクを作成
type: docs
weight: 10
url: /java/create-links/
description: このセクションでは、JavaでPDFドキュメントにリンクを作成する方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## リンクを作成する

Aspose.PDF for Javaを使用すると、外部のPDFファイルにリンクを追加して、複数のドキュメントをリンクすることができます。 ドキュメントにアプリケーションへのリンクを追加することで、ドキュメントからアプリケーションにリンクすることが可能になります。これは、たとえばチュートリアルの特定のポイントで読者に特定のアクションを取ってもらいたい場合や、機能豊富なドキュメントを作成したい場合に便利です。アプリケーションリンクを作成するには：

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトを作成します。
1. リンクを追加したい [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) を取得します。

1. [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) オブジェクトと [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) オブジェクトを使用して [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) オブジェクトを作成します。
1. [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) オブジェクトを使用してリンク属性を設定します。
1. また、[LaunchAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/LaunchAction) オブジェクトを設定し、setAction(..) メソッドを呼び出します。
1. [LaunchAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/LaunchAction) オブジェクトを作成する際に、起動したいアプリケーションを指定します。
1. リンクを Page オブジェクトの [Annotations](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationCollection) コレクションに追加します。
1. 最後に、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトの Save メソッドを使用して更新された PDF を保存します。

次のコードスニペットは、PDFファイル内でアプリケーションへのリンクを作成する方法を示しています。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;


public class ExampleLinks {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    private static String GetDataDir() {
        String os = System.getProperty("os.name");
        if (os.startsWith("Windows"))
            _dataDir = "C:\\Samples\\Links-Actions";
        return _dataDir;
    }

    public static void CreateLink() {

        // ドキュメントを開く
        Document document = new Document(GetDataDir() + "CreateApplicationLink.pdf");

        // リンクを作成
        Page page = document.getPages().get_Item(1);
        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(100, 200, 300, 300));
        link.setColor(Color.getGreen());
        link.setAction(new LaunchAction(document, _dataDir + "sample.pdf"));
        page.getAnnotations().add(link);

        // 更新されたドキュメントを保存
        document.save(_dataDir + "CreateApplicationLink_out.pdf");
    }
```

### PDFファイル内にPDFドキュメントリンクを作成

Aspose.PDF for Javaを使用すると、外部のPDFファイルへのリンクを追加して、複数のドキュメントをリンクさせることができます。
 To create a PDF document link:

1. 最初に、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトを作成します。
1. 次に、リンクを追加したい特定の [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) を取得します。
1. [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) と [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) オブジェクトを使用して [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) オブジェクトを作成します。
1. [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) オブジェクトを使用してリンク属性を設定します。
1. setAction(..) メソッドを呼び出し、[GoToRemoteAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToRemoteAction) オブジェクトを渡します。
1. [GoToRemoteAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToRemoteAction) オブジェクトを作成する際に、起動すべきPDFファイルと開くべきページ番号を指定します。
1. リンクを Page オブジェクトの [Annotations](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationCollection) コレクションに追加します。
1. 最後に、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトの Save メソッドを使用して更新された PDF を保存します。

次のコードスニペットは、PDFファイル内にPDF文書リンクを作成する方法を示しています。

```java
    public static void CreatePDFDocumentLink() {

        // ドキュメントを開く
        Document document = new Document(_dataDir + "CreateDocumentLink.pdf");

        // リンクを作成
        Page page = document.getPages().get_Item(1);
        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(100, 200, 300, 300));
        link.setColor(Color.getGreen());
        link.setAction(new GoToRemoteAction(_dataDir + "sample.pdf", 1));
        page.getAnnotations().add(link);

        // 更新されたドキュメントを保存
        document.save(_dataDir + "CreateDocumentLink_out.pdf");
    }
```