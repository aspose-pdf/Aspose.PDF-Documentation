---
title: ツールチップの使用
linktitle: PDF ツールチップ
type: docs
weight: 20
url: ja/java/pdf-tooltip/
description: Java と Aspose.PDF を使用して PDF のテキストフラグメントにツールチップを追加する方法を学びます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 見えないボタンを追加して検索したテキストにツールチップを追加

PDF ドキュメント内のフレーズや特定の単語にツールチップとして詳細を追加し、ユーザーがテキスト上にマウスカーソルを置いたときにポップアップさせる必要があることがよくあります。Aspose.PDF for Java を使用すると、検索されたテキストの上に見えないボタンを追加することでツールチップを作成することができます。次のコードスニペットは、この機能を実現する方法を示します。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.ButtonField;
import com.aspose.pdf.Document;
import com.aspose.pdf.TextFragment;
import com.aspose.pdf.TextFragmentAbsorber;
import com.aspose.pdf.TextFragmentCollection;

public class ExampleToolTip {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddToolTip() {
        String outputFile = _dataDir + "Tooltip_out.pdf";

        // テキスト付きのサンプルドキュメントを作成
        Document doc = new Document();
        doc.getPages().add().getParagraphs().add(new TextFragment("ここにマウスカーソルを移動するとツールチップが表示されます"));
        doc.getPages().get_Item(1).getParagraphs().add(new TextFragment("ここにマウスカーソルを移動すると非常に長いツールチップが表示されます"));
        doc.save(outputFile);

        // テキスト付きのドキュメントを開く
        Document document = new Document(outputFile);
        // 正規表現に一致するすべてのフレーズを見つけるために TextAbsorber オブジェクトを作成
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("ここにマウスカーソルを移動するとツールチップが表示されます");
        // ドキュメントページに対してアブソーバーを適用
        document.getPages().accept(absorber);
        // 抽出されたテキストフラグメントを取得
        TextFragmentCollection textFragments = absorber.getTextFragments();

        // フラグメントをループする
        for(TextFragment fragment : textFragments)
        {
            // テキストフラグメントの位置に見えないボタンを作成
            ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
            // AlternateName の値はビューアーアプリケーションによってツールチップとして表示されます
            field.setAlternateName ("テキストのツールチップ。");
            // ボタンフィールドをドキュメントに追加
            document.getForm().add(field);
        }

        // 次は非常に長いツールチップのサンプルです
        absorber = new TextFragmentAbsorber("ここにマウスカーソルを移動すると非常に長いツールチップが表示されます");
        document.getPages().accept(absorber);
        textFragments = absorber.getTextFragments();

        for(TextFragment fragment : textFragments)
        {
            ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
            // 非常に長いテキストを設定
            field.setAlternateName ("Lorem ipsum dolor sit amet, consectetur adipiscing elit," +
                                    " sed do eiusmod tempor incididunt ut labore et dolore magna" +
                                    " aliqua. Ut enim ad minim veniam, quis nostrud exercitation" +
                                    " ullamco laboris nisi ut aliquip ex ea commodo consequat." +
                                    " Duis aute irure dolor in reprehenderit in voluptate velit" +
                                    " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint" +
                                    " occaecat cupidatat non proident, sunt in culpa qui officia" +
                                    " deserunt mollit anim id est laborum.");
            document.getForm().add(field);
        }

        // ドキュメントを保存
        document.save(outputFile);
    }
}
```


{{% alert color="primary" %}}

ツールチップの長さに関して、ツールチップのテキストはPDFドキュメント内のPDF文字列型として、コンテンツストリームの外に含まれています。PDFファイルにはそのような文字列に関する実質的な制限はありません（PDFリファレンス付録Cを参照）。しかし、特定のプロセッサ上で特定のオペレーティング環境にある準拠したリーダー（例：Adobe Acrobat）にはそのような制限があります。PDFリーダーアプリケーションのドキュメントを参照してください。

{{% /alert %}}

## 隠しテキストブロックを作成し、マウスオーバーで表示する

Aspose.PDFでは、アクションを隠す機能が実装されており、これにより、いくつかの見えないボタン上でのマウスのエンター/エグジットに応じてテキストボックスフィールド（または他のタイプの注釈）を表示/非表示にすることが可能です。この目的のために、Aspose.Pdf.Annotations.HideActionクラスが使用され、テキストブロックに対して表示/非表示のアクションを割り当てます。マウスエンター/エグジットでテキストブロックを表示/非表示にするための以下のコードスニペットを使用してください。

また、ドキュメント内のPDFアクションは準拠したリーダー（例：
 Adobe Reader) ですが、他のPDFリーダー（例: ウェブブラウザのプラグイン）については保証しません。簡単な調査を行い、以下のことがわかりました：

- PDF文書での非表示アクションのすべての実装は、Internet Explorer v.11.0で正常に動作します。
- 非表示アクションのすべての実装はOpera v.12.14でも動作しますが、文書を初めて開くときに応答の遅延が見られます。
- HideActionコンストラクタを使用してフィールド名を受け入れる実装のみが、Google Chrome v.61.0で文書を閲覧する場合に動作します。Google Chromeでの閲覧が重要である場合は、対応するコンストラクタを使用してください：

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```java
    public static void name() {
        String outputFile = _dataDir + "TextBlock_HideShow_MouseOverOut_out.pdf";

        // テキスト付きのサンプル文書を作成
        Document doc = new Document();
        doc.getPages().add().getParagraphs().add(new TextFragment("ここにマウスカーソルを移動してフローティングテキストを表示"));
        doc.save(outputFile);

        // テキスト付き文書を開く
        Document document = new Document(outputFile);
        // 正規表現に一致するすべてのフレーズを見つけるためにTextAbsorberオブジェクトを作成
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("ここにマウスカーソルを移動してフローティングテキストを表示");
        // ドキュメントページに吸収器を適用
        document.getPages().accept(absorber);
        // 最初に抽出されたテキストフラグメントを取得
        TextFragmentCollection textFragments = absorber.getTextFragments();
        TextFragment fragment = textFragments.get_Item(1);

        // ページの指定された矩形でフローティングテキストのための隠しテキストフィールドを作成
        TextBoxField floatingField = new TextBoxField(fragment.getPage(), new Rectangle(100, 700, 220, 740));
        // フィールド値として表示されるテキストを設定
        floatingField.setValue ("これは「フローティングテキストフィールド」です。");
        // このシナリオのためにフィールドを「読み取り専用」にすることをお勧めします
        floatingField.setReadOnly(true);

        // ドキュメントオープン時にフィールドを見えなくするために「hidden」フラグを設定
        floatingField.setFlags( floatingField.getFlags() | AnnotationFlags.Hidden);

        // ユニークなフィールド名を設定する必要はありませんが、許可されています
        floatingField.setPartialName ("FloatingField_1");

        // フィールドの外観の特性を設定する必要はありませんが、設定するとより良くなります
        DefaultAppearance da = new DefaultAppearance("Helvetica", 16, java.awt.Color.RED);
        floatingField.setDefaultAppearance(da);
        //new DefaultAppearance("Helv", 10, Color.getBlue()
        floatingField.getCharacteristics().setBackground(Color.getLightBlue());
        floatingField.getCharacteristics().setBorder(Color.getDarkBlue());;
        floatingField.setBorder(new Border(floatingField));
        floatingField.getBorder().setWidth(1);
        floatingField.setMultiline(true);

        // ドキュメントにテキストフィールドを追加
        document.getForm().add(floatingField);

        // テキストフラグメント位置に不可視のボタンを作成
        Field buttonField = new ButtonField(fragment.getPage(), fragment.getRectangle());
        // 指定されたフィールド（アノテーション）と不可視フラグのための新しい非表示アクションを作成
        // （上で指定した場合、フィールド名でフローティングフィールドを参照することもできます。）
        // 不可視ボタンフィールドにマウスのエンター/エグジット時のアクションを追加
        buttonField.getActions().setOnEnter(new HideAction(floatingField, false));
        buttonField.getActions().setOnExit (new HideAction(floatingField));

        // ドキュメントにボタンフィールドを追加
        document.getForm().add(buttonField);

        // ドキュメントを保存
        document.save(outputFile);
    }
```