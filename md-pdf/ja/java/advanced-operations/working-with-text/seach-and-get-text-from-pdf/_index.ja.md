---
title: PDFドキュメントのページからテキストを検索して取得する
linktitle: 検索してテキストを取得する
type: docs
weight: 60
url: /java/search-and-get-text-from-pdf/
description: この記事では、さまざまなツールを使用してPDFドキュメントからテキストを検索し取得する方法を説明します。特定のページまたはすべてのページから正規表現で検索できます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDFドキュメントのすべてのページからテキストを検索して取得する

TextFragmentAbsorberを使用すると、PDFドキュメントのすべてのページから特定のフレーズに一致するテキストを見つけることができます。

ドキュメント全体でテキストを検索するには、[Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) コレクションの accept() メソッドを呼び出します。
 [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) メソッドは、TextFragmentAbsorber オブジェクトをパラメータとして受け取り、TextFragment オブジェクトのコレクションを返します。すべてのフラグメントをループして、そのプロパティ（例えば、テキスト、位置、Xインデント、Yインデント、フォント名、フォントサイズ、アクセシビリティ、埋め込みか否か、サブセットか否か、前景色など）を取得します。

次のコードスニペットは、ドキュメント全体を検索し、すべての一致をコンソールに表示する方法を示しています。

```java
// ドキュメントを開く
Document pdfDocument = new Document("input.pdf");

// 入力検索フレーズのすべてのインスタンスを見つけるための TextAbsorber オブジェクトを作成
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("sample");

// すべてのページにアブソーバーを適用
pdfDocument.getPages().accept(textFragmentAbsorber);

// 抽出されたテキストフラグメントをコレクションに取得
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

// フラグメントをループ
for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
    System.out.println("テキスト :- " + textFragment.getText());
    System.out.println("位置 :- " + textFragment.getPosition());
    System.out.println("Xインデント :- " + textFragment.getPosition().getXIndent());
    System.out.println("Yインデント :- " + textFragment.getPosition().getYIndent());
    System.out.println("フォント - 名前 :- " + textFragment.getTextState().getFont().getFontName());
    System.out.println("フォント - アクセシブルか :- " + textFragment.getTextState().getFont().isAccessible());
    System.out.println("フォント - 埋め込みか - " + textFragment.getTextState().getFont().isEmbedded());
    System.out.println("フォント - サブセットか :- " + textFragment.getTextState().getFont().isSubset());
    System.out.println("フォントサイズ :- " + textFragment.getTextState().getFontSize());
    System.out.println("前景色 :- " + textFragment.getTextState().getForegroundColor());
}
```

特定のページでテキストを検索し、それに関連するプロパティを取得するには、ページインデックスを指定します。

```java
// ドキュメントの最初のページにアブソーバーを適用
pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber);
```

## PDFのページからテキストセグメントを検索して取得

ドキュメント内のすべてのページでテキストセグメントを検索するには、ドキュメントのTextFragmentオブジェクトを取得します。

TextFragmentAbsorberを使用すると、PDFドキュメント内のすべてのページから特定のフレーズに一致するテキストを見つけることができます。ドキュメント全体でテキストを検索するには、[Pages](https://reference.aspose.com/pdf//java/com.aspose.pdf/pagecollection)コレクションの[accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber)メソッドを呼び出します。[accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber)メソッドはTextFragmentAbsorberオブジェクトをパラメータとして受け取り、TextFragmentオブジェクトのコレクションを返します。

{{% alert color="primary" %}}

ドキュメントからTextFragmentCollectionコレクションを取得したら、それをループして各TextFragmentオブジェクトのTextSegmentCollectionコレクションを取得します。
 その後、個々のTextSegmentオブジェクトのプロパティを取得できます。
{{% /alert %}}

次のコードスニペットは、すべてのページでテキストセグメントを検索する方法を示しています。

```java
// ドキュメントを開く
Document pdfDocument = new Document("input.pdf");

// 入力された検索フレーズのすべてのインスタンスを見つけるためのTextAbsorberオブジェクトを作成
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("sample");

// ドキュメントの最初のページに対してアブソーバーを適用
pdfDocument.getPages().accept(textFragmentAbsorber);

// 抽出されたテキストフラグメントをコレクションに取得
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

// テキストフラグメントをループ
for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
    // テキストセグメントを繰り返し処理
    for (TextSegment textSegment : (Iterable<TextSegment>) textFragment.getSegments()) {
        System.out.println("Text :- " + textSegment.getText());
        System.out.println("Position :- " + textSegment.getPosition());
        System.out.println("XIndent :- " + textSegment.getPosition().getXIndent());
        System.out.println("YIndent :- " + textSegment.getPosition().getYIndent());
        System.out.println("Font - Name :- " + textSegment.getTextState().getFont().getFontName());
        System.out.println("Font - IsAccessible :- " + textSegment.getTextState().getFont().isAccessible());
        System.out.println("Font - IsEmbedded - " + textSegment.getTextState().getFont().isEmbedded());
        System.out.println("Font - IsSubset :- " + textSegment.getTextState().getFont().isSubset());
        System.out.println("Font Size :- " + textSegment.getTextState().getFontSize());
        System.out.println("Foreground Color :- " + textSegment.getTextState().getForegroundColor());
    }
}
```

特定のテキストセグメントを検索して関連するプロパティを取得するには、検索したいページのページインデックスを指定します。

```java
// ドキュメントの最初のページの吸収を受け入れます。
pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber);
```

## 正規表現を使用してページからテキストを検索および取得する

TextFragmentAbsorber は、正規表現に基づいて、ドキュメント内のすべてのページからテキストを検索および取得するのに役立ちます。

ドキュメントからテキストを検索および取得するには:

1. 検索用語を正規表現として TextFragmentAbsorber のコンストラクタに渡します。
2. TextFragmentAbsorber オブジェクトの TextSearchOptions プロパティを設定します。
   このプロパティには TextSearchOptions オブジェクトが必要です: 新しいオブジェクトを作成するときに、そのコンストラクタに true を渡します。
3. すべてのページから一致するテキストを取得するには、[Pages](https://reference.aspose.com/pdf//java/com.aspose.pdf/pagecollection) コレクションの [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) メソッドを呼び出します。

   TextFragmentAbsorber は、正規表現で指定された条件に一致するすべてのフラグメントを含む TextFragmentCollection を返します。

ドキュメント内のすべてのページを検索し、正規表現に基づいてテキストを取得する方法を示す次のコードスニペット。

```java
// ドキュメントを開く
Document pdfDocument = new Document("source.pdf");

// 入力された検索フレーズのすべてのインスタンスを見つけるためのTextAbsorberオブジェクトを作成
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // 例: 1999-2000

// 正規表現の使用を指定するためにテキスト検索オプションを設定
TextSearchOptions textSearchOptions = new TextSearchOptions(true);
textFragmentAbsorber.setTextSearchOptions(textSearchOptions);

// ドキュメントの最初のページにアブソーバーを適用
pdfDocument.getPages().accept(textFragmentAbsorber);

// 抽出されたテキストフラグメントをコレクションに取得
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

// フラグメントをループ
for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
    System.out.println("テキスト :- " + textFragment.getText());
    System.out.println("位置 :- " + textFragment.getPosition());
    System.out.println("Xインデント :- " + textFragment.getPosition().getXIndent());
    System.out.println("Yインデント :- " + textFragment.getPosition().getYIndent());
    System.out.println("フォント - 名前 :- " + textFragment.getTextState().getFont().getFontName());
    System.out.println("フォント - アクセス可能 :- " + textFragment.getTextState().getFont().isAccessible());
    System.out.println("フォント - 埋め込み済み - " + textFragment.getTextState().getFont().isEmbedded());
    System.out.println("フォント - サブセット :- " + textFragment.getTextState().getFont().isSubset());
    System.out.println("フォントサイズ :- " + textFragment.getTextState().getFontSize());
    System.out.println("前景色 :- " + textFragment.getTextState().getForegroundColor());
}
```


特定のページでテキストを検索し、そのプロパティを取得するには、ページインデックスを指定します。

```java
// ドキュメントの最初のページに対してアブソーバーを受け入れます。
pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber)
```

文字列を大文字または小文字で検索するには、正規表現を使用することを検討できます。

```java
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("(?i)Line", new TextSearchOptions(true));
```

例:

```java
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[\\S]+");
```