---
title: レガシーAspose.Pdf.Kit for Javaからの移行
type: docs
weight: 10
url: /ja/java/migration-from-legacy-aspose-pdf-kit-for-java/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

現在のAspose.PDF.Kit for Javaコンポーネントは、既存のPDFファイルを操作する機能を提供していました。しかし、このコンポーネントは別製品としてはまもなく廃止される予定です。なぜなら、すべてのクラスと列挙型を新しい自動移植バージョンのAspose.PDF for Java (4.x.x) の**com.aspose.pdf.facades**パッケージに移植したからです。この単一の自動移植されたリリースは、既存のPDFファイルを作成および操作する能力を提供します。

{{% /alert %}}

## レガシーコードのサポート

移行活動全体を通じて、既存の顧客に対するこの活動の影響を確実に考慮し、可能な限りこの影響を最小限に抑えるよう努力しました。
 さらに、新しい自動移植リリースを既存の顧客のコードベースが最小限の変更で済むように下位互換性を持たせることにも重点を置いています。新しい自動移植リリースは、PDFファイルを作成および操作するためにcom.aspose.pdfパッケージの下にドキュメントオブジェクトモデル（DOM）を提供しますが、Aspose.PDF.Kit for Javaで開発されたレガシーコードを引き続き使用したい場合は、**com.aspose.pdf.facades**パッケージをインポートするだけで、コードは動作するはずです（*明示的なクラス参照の更新を除く*）。

次のコードスニペットは、新しい自動移植Aspose.PDF for Javaで既存のAspose.PDF.Kit for Javaコードを実行する方法を示しています。

```java

 import com.aspose.pdf.facades.*;

public class template {

    public static void main(String[] args) {

        try{

            // 既存のPDFファイルを読み込む

            com.aspose.pdf.facades.PdfFileInfo fileInfo = new com.aspose.pdf.facades.PdfFileInfo("input.pdf");

            System.out.println("TITLE: " + fileInfo.getTitle());

            System.out.println("AUTHOR:" + fileInfo.getAuthor());

            System.out.println("CREATIONDATE:" + fileInfo.getCreationDate());

            System.out.println("CREATOR:" + fileInfo.getCreator());

            System.out.println("KeyWORDS:" + fileInfo.getKeywords());

            System.out.println("MODDATE:" + fileInfo.getModDate());

           }


catch(Exception ex)


{System.out.println(ex);}


}

}
```

## ReplaceTextStrategy クラスの使用

ReplaceTextStrategy クラスのコードを移行するために、**setScope(..)** メソッドが **setReplaceScope(..)** に更新されました。以下のコードスニペットをご覧ください。

```java

 // PdfContentEditor オブジェクトをインスタンス化する

com.aspose.pdf.facades.PdfContentEditor editor = new com.aspose.pdf.facades.PdfContentEditor();

// ソース PDF ファイルをバインドする

editor.bindPdf("input.pdf");

// 置換テキスト戦略を作成する

com.aspose.pdf.facades.ReplaceTextStrategy strategy = new com.aspose.pdf.facades.ReplaceTextStrategy();

// テキスト置換のための配置を設定する

strategy.setAlignment(com.aspose.pdf.facades.AlignmentType.Left);

// テキスト置換のスコープ

strategy.setReplaceScope(com.aspose.pdf.facades.ReplaceTextStrategy.Scope.REPLACE_ALL);

// 置換戦略を設定する

editor.setReplaceTextStrategy(strategy);

editor.replaceText("test","replaced");

// 更新されたファイルを保存する

editor.save("TxtReplaceTest.pdf");
```