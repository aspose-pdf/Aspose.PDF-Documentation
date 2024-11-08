---
title: PDF内のリンクを更新する
linktitle: リンクを更新
type: docs
weight: 20
url: /ja/java/update-links/
description: プログラムでPDF内のリンクを更新します。このガイドはJava言語でPDF内のリンクを更新する方法についてです。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFファイル内のリンクを更新する

PDFファイルにハイパーリンクを追加する際に説明したように、[LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) クラスを使用すると、PDFファイルにリンクを追加することができます。PDFファイル内の既存のリンクを取得するために使われる似たクラスもあります。既存のリンクを更新する必要がある場合にこれを使用します。既存のリンクを更新するには、次の手順に従います。

1. PDFファイルを読み込む。
1. PDFファイル内の特定のページに移動する。
1. [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction) オブジェクトのDestinationプロパティを使用してリンク先を指定する。

1. [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/XYZExplicitDestination) コンストラクターを使用して、宛先ページを指定します。

### 同じドキュメント内のページにリンクターゲットを設定

次のコードスニペットは、PDFファイル内のリンクを更新し、そのターゲットをドキュメントの2ページ目に設定する方法を示しています。

```java
    public static void SetLinkTargetToAPageInTheSameDocument() {
        
        // PDFファイルを読み込む
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
        // ドキュメントの最初のページから最初のリンク注釈を取得する
        LinkAnnotation linkAnnot = (LinkAnnotation)page.getAnnotations().get_Item(1);

        // リンクを変更: リンクの宛先を変更する
        GoToAction goToAction = (GoToAction)linkAnnot.getAction();
        // リンクオブジェクトの宛先を指定
        // ウィンドウの左上隅に位置する座標 (left, top) でページを表示し、ページの内容をズームの係数で拡大する明示的な宛先を表します。
        // 第1パラメーターは宛先ページ番号です。
        // 第2は左座標です
        // 第3は上座標です
        // 第4引数は該当ページを表示する際のズーム係数です。 2を使用すると、ページは200％ズームで表示されます。
        goToAction.setDestination(new XYZExplicitDestination(1, 1, 2, 2 ));
        
        // 更新されたリンクでドキュメントを保存する
        document.save(_dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");        
    }
```


### Webアドレスにリンク先を設定する

ハイパーリンクを更新してWebアドレスを指すようにするには、[GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction)オブジェクトをインスタンス化し、それをLinkAnnotationのActionプロパティに渡します。以下のコードスニペットは、PDFファイル内のリンクを更新し、そのターゲットをWebアドレスに設定する方法を示しています。

```java
    public static void SetLinkDestinationToWebAddress() {        
        // PDFファイルを読み込む
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
    
        // ドキュメントの最初のページから最初のリンク注釈を取得
        LinkAnnotation linkAnnot = (LinkAnnotation)page.getAnnotations().get_Item(1);

        // リンクの変更：リンクアクションを変更し、ターゲットをWebアドレスとして設定
        linkAnnot.setAction(new GoToURIAction("www.aspose.com"));
        
        // 更新されたリンクでドキュメントを保存
        document.save(_dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");        
    }
```


### 別のPDFファイルへのリンクターゲットを設定する

次のコードスニペットは、PDFファイル内のリンクを更新し、そのターゲットを別のPDFファイルに設定する方法を示しています。

```java
    public static void SetLinkTargetToAnotherPDFFile() {        
        // PDFファイルをロード
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
    
        LinkAnnotation linkAnnot = (LinkAnnotation)page.getAnnotations().get_Item(1);

        GoToRemoteAction goToR = (GoToRemoteAction)linkAnnot.getAction();
        // 次の行では宛先を更新します。ファイルは更新しません
        goToR.setDestination(new XYZExplicitDestination(2, 0, 0, 1.5));
        // 次の行ではファイルを更新します
        goToR.setFile (new FileSpecification(_dataDir +  "input.pdf"));

        // 更新されたリンクでドキュメントを保存
        document.save(_dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");        
    }
```

### LinkAnnotationのテキストカラーを更新する

リンクアノテーションにはテキストが含まれていません。
 ページの内容にアノテーションの下にテキストが配置されているため、テキストの色を変更するには、アノテーションの色を変更しようとするのではなく、ページのテキストの色を置き換えます。次のコードスニペットは、PDFファイル内のリンクアノテーションの色を更新する方法を示しています。

```java
    public static void UpdateLinkAnnotationTextColor () {        
        // PDFファイルを読み込む
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
           
        for (Annotation annotation : page.getAnnotations())
        {
            if (annotation.getAnnotationType() == AnnotationType.Link)
            {
                // アノテーションの下のテキストを検索
                TextFragmentAbsorber ta = new TextFragmentAbsorber();
                Rectangle rect = annotation.getRect();
                rect.setLLX(rect.getLLX()-10);
                rect.setLLY(rect.getLLY()-10);
                rect.setURX(rect.getURX()+ 10);
                rect.setURY(rect.getURY()+ 10);

                ta.setTextSearchOptions(new TextSearchOptions(rect));
                ta.visit(page);
                // テキストの色を変更する
                for (TextFragment tf : ta.getTextFragments())
                {
                    tf.getTextState().setForegroundColor(Color.getRed());
                }
            }
        
        }                       
        // 更新されたリンクでドキュメントを保存する
        document.save(_dataDir + "UpdateLinkTextColor_out.pdf");        
    }
```