---
title: PDFからタグ付きコンテンツを抽出する
linktitle: タグ付きコンテンツを抽出
type: docs
weight: 20
url: /ja/java/extract-tagged-content-from-tagged-pdfs/
description: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントからタグ付きコンテンツを抽出する方法について説明します
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## タグ付きPDFコンテンツの取得

タグ付きテキストを含むPDFドキュメントのコンテンツを取得するために、Aspose.PDFは[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスの[getTaggedContent()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getTaggedContent--)メソッドを提供します。以下のコードスニペットは、タグ付きテキストを含むPDFドキュメントのコンテンツを取得する方法を示しています。

```java
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-Java を参照してください
// ドキュメントディレクトリへのパス。
String path = "pathTodir";

// PDFドキュメントを作成
Document document = new Document();

// タグ付きPDFで作業するためのコンテンツを取得
ITaggedContent taggedContent = document.getTaggedContent();

//
// タグ付きPDFコンテンツの操作
//

// ドキュメントのタイトルと言語を設定
taggedContent.setTitle("Simple Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// タグ付きPDFドキュメントを保存
document.save(path + "TaggedPDFContent.pdf");
```


## ルート構造の取得

Tagged PDF ドキュメントのルート構造を取得するために、Aspose.PDF は [getStructTreeRootElement]()(https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#getStructTreeRootElement--) および [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent) インターフェイスの **getStructureElement()** メソッドを提供しています。以下のコードスニペットは、Tagged PDF ドキュメントのルート構造を取得する方法を示しています。

```java
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-Java を参照してください。
// ドキュメントディレクトリへのパス。
String path = "pathTodir";
// PDF ドキュメントを作成
Document document = new Document();

// TaggedPdf で作業するためのコンテンツを取得
ITaggedContent taggedContent = document.getTaggedContent();

// ドキュメントのタイトルと言語を設定
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// プロパティ StructTreeRootElement と RootElement は、PDF ドキュメントの StructTreeRoot オブジェクトおよび
// ルート構造要素（ドキュメント構造要素）へのアクセスに使用されます。
StructTreeRootElement structTreeRootElement = taggedContent.getStructTreeRootElement();
StructureElement rootElement = taggedContent.getRootElement();
```


## 子要素へのアクセス

タグ付きPDFドキュメントの子要素にアクセスするために、Aspose.PDFは**ElementList**クラスを提供します。以下のコードスニペットは、タグ付きPDFドキュメントの子要素にアクセスする方法を示しています。

```java
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-Java をご覧ください。
String path = "pathTodir";
// PDFドキュメントを開く
Document document = new Document( path +"StructureElements.pdf");

// タグ付きPDFを操作するためのコンテンツを取得
ITaggedContent taggedContent = document.getTaggedContent();

// ルート要素にアクセス
ElementList elementList = taggedContent.getStructTreeRootElement().getChildElements();
for (Element element : elementList)
{
    if (element instanceof StructureElement)
    {
        StructureElement structureElement =  (StructureElement)element;

        // プロパティを取得
        String title = structureElement.getTitle();
        String language = structureElement.getLanguage();
        String actualText = structureElement.getActualText();
        String expansionText = structureElement.getExpansionText();
        String alternativeText = structureElement.getAlternativeText();
    }
}

// ルート要素の最初の要素の子要素にアクセス
elementList = taggedContent.getRootElement().getChildElements().get_Item(1).getChildElements();
for (Element element : elementList)
{
    if (element instanceof StructureElement)
    {
        StructureElement structureElement = (StructureElement)element;

        // プロパティを設定
        structureElement.setTitle("title");
        structureElement.setLanguage("fr-FR");
        structureElement.setActualText("actual text");
        structureElement.setExpansionText("exp");
        structureElement.setAlternativeText("alt");
    }
}

// タグ付きPDFドキュメントを保存
document.save( path +"AccessChildrenElements.pdf");
```