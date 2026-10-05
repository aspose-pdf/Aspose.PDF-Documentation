---
title: "Java での PDFからタグ付きコンテンツの抽出"
linktitle: "タグ付きコンテンツの抽出"
type: docs
weight: 20
url: /ja/java/extract-tagged-content-from-tagged-pdfs/
description: Aspose.PDF を使用して Java でタグ付き PDF コンテンツを検査する方法を学びます。これにはタグ付きコンテンツへのアクセス、ルート構造へのアクセス、子構造要素が含まれます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
タグ付き PDF の論理構造ツリーを検査し、構造要素のメタデータを確認または更新する必要がある場合に、これらの APIs を使用してください。

## タグ付けされたコンテンツのメタデータの取得

タイトルや言語などの基本的なドキュメントメタデータを定義し、タグ付けされたコンテンツコンテナにアクセスする必要がある場合にこの例を使用します。

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成してください。
1. 取得する [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf/itaggedcontent/) オブジェクトをドキュメントから取得してください。
1. タグ付けされたコンテンツのメタデータを設定し、出力ファイルを保存してください。

```java
public static void getTaggedContent(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Simple Tagged Pdf Document");
        taggedContent.setLanguage("en-US");
        document.save(outputFile.toString());
    }
}
```

## タグ付けされた PDF のルート構造の取得

この例は、タグ付けされた PDF の構造ツリーを表すルートオブジェクトを検査する方法を示しています。

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、そのタグ付けされたコンテンツを取得してください。
1. 必要なドキュメント メタデータを設定してください。
1. 構造ツリーのルートと論理ルート要素を読み取り、出力し、ファイルを保存してください。

```java
public static void getRootStructure(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        System.out.println("StructTreeRootElement: " + taggedContent.getStructTreeRootElement());
        System.out.println("RootElement: " + taggedContent.getRootElement());

        document.save(outputFile.toString());
    }
}
```

## 子構造要素にアクセスして更新する

構造ツリーの子要素を反復処理し、プロパティを検査し、選択されたメタデータを更新する必要がある場合にこの例を使用してください。

1. ソース のタグ付けされた PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 構造ツリーのルートから子要素を読み取り、利用可能なプロパティを出力してください。
1. 最初のルート子の子要素にアクセスし、メタデータを更新して、文書を保存します。

```java
public static void accessChildElements(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ITaggedContent taggedContent = document.getTaggedContent();

        ElementList elementList = taggedContent.getStructTreeRootElement().getChildElements();
        for (Object element : elementList) {
            if (element instanceof StructureElement structureElement) {
                System.out.println("StructureElement properties - "
                        + "title: " + structureElement.getTitle()
                        + ", language: " + structureElement.getLanguage()
                        + ", actual_text: " + structureElement.getActualText()
                        + ", expansion_text: " + structureElement.getExpansionText()
                        + ", alternative_text: " + structureElement.getAlternativeText());
            }
        }

        Element firstChild = taggedContent.getRootElement().getChildElements().get_Item(1);
        for (Object element : firstChild.getChildElements()) {
            if (element instanceof StructureElement structureElement) {
                structureElement.setTitle("title");
                structureElement.setLanguage("fr-FR");
                structureElement.setActualText("actual text");
                structureElement.setExpansionText("exp");
                structureElement.setAlternativeText("alt");
            }
        }

        document.save(outputFile.toString());
    }
}
```
