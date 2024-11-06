---
title: Actionsを使用する
linktitle: Actions
type: docs
weight: 20
url: ja/java/actions/
description: このセクションでは、Javaを使用してドキュメントやフォームフィールドにアクションをプログラムで追加する方法を説明します。PDFファイルにハイパーリンクを追加、作成、取得する方法を学びます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDFファイルには埋め込みのファイル添付が含まれることがあり、これらのドキュメントへのハイパーリンクが必要になることがあります。親ドキュメントに添付ファイルを指すリンクを作成することで、メインのPDFドキュメントからPDF添付ファイルに読者を誘導できます。

## PDFファイルにハイパーリンクを追加する

PDFファイルにハイパーリンクを追加することができます。これにより、読者がPDFの別の部分や外部コンテンツに移動できるようになります。

PDFドキュメントにウェブハイパーリンクを追加するには：

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) クラスオブジェクトを作成します。

1. リンクを追加したい[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)クラスを取得します。
1. [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation)オブジェクトをPageオブジェクトと[Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle)オブジェクトを使用して作成します。Rectangleオブジェクトは、リンクを追加するページ上の位置を指定するために使用されます。
1. getActionメソッドを[GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToURIAction)オブジェクトに設定し、リモートURIの位置を指定します。
1. ハイパーリンクテキストを表示するには、[LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation)オブジェクトが配置されているのと同様の位置にテキスト文字列を追加します。
1. フリーテキストを追加するには：

- [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/FreeTextAnnotation)オブジェクトをインスタンス化します。
 それはまた、PageとRectangleオブジェクトを引数として受け入れるので、LinkAnnotationコンストラクタに対して指定されたのと同じ値を提供することが可能です。
- [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/FreeTextAnnotation)オブジェクトのContentsプロパティを使用して、出力PDFに表示される文字列を指定します。
- 必要に応じて、[LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation)とFreeTextAnnotationオブジェクトの両方の枠線の幅を0に設定し、PDFドキュメントに表示されないようにします。
- 一旦、[LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation)と[FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/FreeTextAnnotation)オブジェクトが定義されたら、これらのリンクを[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)オブジェクトのAnnotationsコレクションに追加します。

- 最後に、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)オブジェクトのSaveメソッドを使用して更新されたPDFを保存します。
以下のコードスニペットは、PDFファイルにハイパーリンクを追加する方法を示しています。

```java
package com.aspose.pdf.examples;

import java.util.List;

import com.aspose.pdf.*;

public class ExampleActions {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Actions/";

    private static String GetDataDir() {
        String os = System.getProperty("os.name");
        if (os.startsWith("Windows"))
            _dataDir = "C:\\Samples\\Actions";
        return _dataDir;
    }

    public static void AddHyperlinkInPDFFile() {
        // ドキュメントを開く
        Document document = new Document(GetDataDir() + "AddHyperlink.pdf");
        // リンクを作成
        Page page = document.getPages().get_Item(1);
        // リンク注釈オブジェクトを作成
        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(100, 100, 300, 300));
        // LinkAnnotationの境界オブジェクトを作成
        Border border = new Border(link);
        // 境界の幅を0に設定
        border.setWidth(0);
        // LinkAnnotationの境界を設定
        link.setBorder(border);
        // リンクタイプをリモートURIとして指定
        link.setAction(new GoToURIAction("www.aspose.com"));
        // PDFファイルの最初のページの注釈コレクションにリンク注釈を追加
        page.getAnnotations().add(link);

        // フリーテキスト注釈を作成
        FreeTextAnnotation textAnnotation = new FreeTextAnnotation(page, new Rectangle(100, 100, 300, 300),
                new DefaultAppearance(FontRepository.findFont("TimesNewRoman"), 10, java.awt.Color.BLUE));

        // フリーテキストとして追加する文字列
        textAnnotation.setContents("Asposeウェブサイトへのリンク");
        // フリーテキスト注釈の境界を設定
        textAnnotation.setBorder(border);
        // ドキュメントの最初のページの注釈コレクションにフリーテキスト注釈を追加
        page.getAnnotations().add(textAnnotation);

        // 更新されたドキュメントを保存
        document.save(_dataDir + "AddHyperlink_out.pdf");

    }
```


## 同じPDF内のページにハイパーリンクを作成する

Aspose.PDF for Javaは、PDFの作成とその操作に優れた機能を提供します。また、PDFページへのリンクを追加する機能もあり、リンクは別のPDFファイル内のページ、ウェブURL、アプリケーションの起動リンク、さらには同じPDFファイル内のページへのリンクにすることができます。

ローカルハイパーリンクを追加するには、TextFragmentを作成してリンクをTextFragmentに関連付ける必要があります。[TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment)クラスには、LocalHyperlinkインスタンスを関連付けるための[getHyperlink](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#getHyperlink--)というメソッドがあります。以下のコードスニペットは、この要件を達成する手順を示しています。

```java
public static void CreateHyperlinkToPagesInSamePDF() {
        // Documentインスタンスを作成
        Document document = new Document();

        // PDFファイルのページコレクションにページを追加
        Page page = document.getPages().add();

        // Text Fragmentインスタンスを作成
        TextFragment text = new TextFragment("link page number test to page 2");

        // ローカルハイパーリンクインスタンスを作成
        LocalHyperlink link = new LocalHyperlink();

        // リンクインスタンスのターゲットページを設定
        link.setTargetPageNumber(2);

        // TextFragmentにハイパーリンクを設定
        text.setHyperlink(link);

        // テキストをPageの段落コレクションに追加
        page.getParagraphs().add(text);

        // 新しいTextFragmentインスタンスを作成
        text = new TextFragment("link page number test to page 1");

        // TextFragmentは新しいページに追加する必要があります
        text.setInNewPage(true);

        // 別のローカルハイパーリンクインスタンスを作成
        link = new LocalHyperlink();

        // 2番目のハイパーリンクのターゲットページを設定
        link.setTargetPageNumber(1);

        // 2番目のTextFragmentにリンクを設定
        text.setHyperlink(link);

        // テキストをpageオブジェクトの段落コレクションに追加
        page.getParagraphs().add(text);

        // 更新されたドキュメントを保存
        document.save(GetDataDir() + "CreateLocalHyperlink_out.pdf");
    }
```


## PDFハイパーリンクの宛先（URL）の取得

リンクはPDFファイル内で注釈として表され、追加、更新、削除が可能です。Aspose.PDF for Javaは、PDFファイル内のハイパーリンクの宛先（URL）を取得することもサポートしています。

リンクのURLを取得するには：

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトを作成します。
1. リンクを抽出したい [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) を取得します。
1. [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector) クラスを使用して、指定されたページからすべての [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) オブジェクトを抽出します。
1. [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector) オブジェクトを [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) オブジェクトのAcceptメソッドに渡します。

1. [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector) オブジェクトの Selected プロパティを使用して、選択されたリンク注釈をすべて IList オブジェクトに取得します。
1. 最後に、LinkAnnotation アクションを GoToURIAction として抽出します。

次のコードスニペットは、PDF ファイルからハイパーリンクの宛先 (URL) を取得する方法を示しています。

```java
    public static void GetPDFHyperlinkDestination() {
        Document document = new Document(GetDataDir() + "Aspose-app-list.pdf");
        // アクションを抽出
        Page page = document.getPages().get_Item(1);
        AnnotationSelector selector = new AnnotationSelector(new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(selector);
        List<Annotation> list = selector.getSelected();
        // リスト内の個々のアイテムを反復処理
        if (list.size() == 0)
            System.out.println("ハイパーリンクが見つかりません..");
        else {
            // すべてのブックマークをループ処理
            for (Annotation annot : list) {
                LinkAnnotation la = (annot instanceof LinkAnnotation ? (LinkAnnotation) annot : null);
                if (la != null) {
                    // 宛先 URL を出力
                    System.out.println("宛先: " + ((GoToURIAction) la.getAction()).getURI());
                }
            }
        } // end else
    }
```


## ハイパーリンクテキストを取得する

ハイパーリンクには2つの部分があります。文書に表示されるテキストと、目的地のURLです。場合によっては、必要なのはURLではなくテキストです。

PDFファイル内のテキストと注釈/アクションは、異なるエンティティによって表されます。ページ上のテキストは単なる単語と文字のセットですが、注釈はハイパーリンクに内在するような対話性をもたらします。

URLコンテンツを見つけるには、注釈とテキストの両方を操作する必要があります。[Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/Annotation) オブジェクト自体にはテキストはありませんが、ページ上のテキストの下に位置しています。したがって、テキストを取得するには、AnnotationがURLの境界を提供し、TextオブジェクトがURLの内容を提供します。以下のコードスニペットをご覧ください。

```java
    public static void GetHyperlinkText() {
        Document document = new Document(GetDataDir() + "Aspose-app-list.pdf");
        // アクションを抽出
        Page page = document.getPages().get_Item(1);

        for (Annotation annot : page.getAnnotations()) {
            LinkAnnotation la = (annot instanceof LinkAnnotation ? (LinkAnnotation) annot : null);
            if (la != null) {
                // 各リンク注釈のURLを出力
                System.out.println("URI: " + ((GoToURIAction) la.getAction()).getURI());
                TextAbsorber absorber = new TextAbsorber();
                absorber.getTextSearchOptions().setLimitToPageBounds(true);
                absorber.getTextSearchOptions().setRectangle(annot.getRect());
                page.accept(absorber);
                String extractedText = absorber.getText();
                // ハイパーリンクに関連付けられたテキストを出力
                System.out.println(extractedText);
            }
        }
    }
```


## PDFファイルからドキュメントオープンアクションを削除する

[ドキュメントを表示する際にPDFページを指定する方法](#how-to-specify-pdf-page-when-viewing-document)では、ドキュメントを最初のページ以外で開くように指示する方法について説明しました。複数のドキュメントを結合する際に、1つ以上にGoToアクションが設定されている場合、それらを削除することをお勧めします。例えば、2つのドキュメントを結合し、2つ目に2ページ目に移動するGoToアクションがあると、出力されたドキュメントは結合されたドキュメントの最初のページではなく、2つ目のドキュメントの2ページ目で開きます。この動作を避けるために、オープンアクションコマンドを削除します。

オープンアクションを削除するには:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトの [getOpenAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getOpenAction--) メソッドをnullに設定します。
1. DocumentオブジェクトのSaveメソッドを使用して更新されたPDFを保存します。

以下のコードスニペットは、PDFファイルからドキュメントオープンアクションを削除する方法を示しています。

```java
    public static void RemoveDocumentOpenActionFromPDFFile()
    {
        // ドキュメントを開く
        Document document = new Document(_dataDir + "RemoveOpenAction.pdf");
        // ドキュメントオープンアクションを削除
        document.setOpenAction(null);
        
        // 更新されたドキュメントを保存
        document.save(GetDataDir()+"RemoveOpenAction_out.pdf");
    }
```


## ドキュメントを表示する際のPDFページを指定する方法 {#how-to-specify-pdf-page-when-viewing-document}

Adobe ReaderなどのPDFビューアでPDFファイルを表示する際、通常は最初のページが開かれます。しかし、異なるページを開くように設定することも可能です。

[XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/XYZExplicitDestination)クラスを使用すると、開きたいPDFファイル内のページを指定することができます。[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスのgetOpenActionメソッドにGoToActionオブジェクトの値を渡すと、ドキュメントはXYZExplicitDestinationオブジェクトに対して指定されたページで開きます。以下のコードスニペットは、ドキュメントのオープンアクションとしてページを指定する方法を示しています。

```java
    public static void HowToSpecifyPDFPageWhenViewingDocument()
    {
        // PDFファイルを読み込む
        Document document = new Document(GetDataDir()+ "SpecifyPageWhenViewing.pdf");
        // ドキュメントの2ページ目のインスタンスを取得
        Page page2 = document.getPages().get_Item(2);
        // ターゲットページのズームファクターを設定する変数を作成
        double zoom = 1;
        // GoToActionインスタンスを作成
        GoToAction action = new GoToAction(page2);
        // 2ページ目に移動
        action.setDestination (new XYZExplicitDestination(page2, 0, page2.getRect().getHeight(), zoom));
        // ドキュメントのオープンアクションを設定
        document.setOpenAction (action);
        // 更新されたドキュメントを保存
        document.save(_dataDir + "goto2page_out.pdf");
    }
}
```