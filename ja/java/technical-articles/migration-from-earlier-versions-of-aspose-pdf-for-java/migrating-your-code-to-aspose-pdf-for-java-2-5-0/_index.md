---
title: Aspose.PDF for Java 2.5.0へのコード移行
type: docs
weight: 10
url: /ja/java/migrating-your-code-to-aspose-pdf-for-java-2-5-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

この記事では、Aspose.PDF for Javaの既存のコードからいくつかの領域をハイライトし、最新のリリースバージョンに互換性を持たせるために試みました。

{{% /alert %}}

## 詳細

Aspose.PDF for Java 2.5.0のリリースにより、API構造とクラスの構築に多くの変更がありました。ほとんどのクラスメンバーの名前が更新され、一部の既存のクラスメンバーが削除され、また既存のクラスにいくつかのメソッドとプロパティが追加されました。変更の概要を簡単に示すために、以前に公開されたAspose.PDF for Javaバージョンに基づいた以下の簡単なコードを見ていきます。

この簡単なコードでは、同じPDFドキュメント内のページにハイパーリンクとリンクを追加します。

```java
import com.aspose.pdf.elements.*;
com.aspose.pdf.License lic = new com.aspose.pdf.License();

try {

lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));

    } catch (Exception e)

{

System.out.println(e.getMessage());

}


//Pdfオブジェクトを空のコンストラクタを呼び出してインスタンス化

Pdf pdf1 = new Pdf();

//Pdfオブジェクトにセクションを作成

Section sec1 = pdf1.getSections().add();

//セクションの参照を持つテキスト段落を作成

Text text1 = new Text(sec1);

//セクションの段落コレクションにテキスト段落を追加

sec1.getParagraphs().add(text1);

//テキスト段落にテキストセグメントを追加

Segment segment1 = text1.getSegments().add("this is a local link");

//テキストセグメントのテキストを下線付きに設定

segment1.getTextInfo().setUnderLine(true);


//テキストセグメントのリンクタイプをローカルに設定

//テキストセグメントのターゲットIDとして目的の段落のIDを割り当てる

segment1.setHyperLink(new HyperLinkToLocalPdf("product1"));

//テキストセグメントにリンクするテキスト段落を作成

Text text3 = new Text(sec1,"product 1 info ...");

//セクションの段落コレクションにテキスト段落を追加

sec1.getParagraphs().add(text3);

//この段落を最初の段落として設定し、ドキュメントの別のページに表示できるようにする

text3.setFirstParagraph(true);

//このテキストセグメントのIDを"product1"に設定

text3.setID("product1"); 


// PDFファイルを保存

FileOutputStream out = new FileOutputStream(new File("UpdateOfCode_Test.pdf"));

pdf1.save(out);
```


When using the versions earlier to Aspose.PDF for Java 2.5.0, the code can successfully be executed and a resultant PDF document containing a hyperlink towards a page within the same document , can be generated. But, when the same code is compiled with 2.5.0 , you will notice number of errors because , there ha ve been change s in the class members and also some of the methods in classes have been removed . Now let ’ s start with the modification of code for version 2.5.0

Aspose.PDF for Java 2.5.0より前のバージョンを使用する場合、コードは正常に実行され、同じドキュメント内のページへのハイパーリンクを含む結果のPDFドキュメントを生成できます。しかし、同じコードを2.5.0でコンパイルすると、クラスメンバーに変更が加えられ、クラス内のいくつかのメソッドが削除されたため、多くのエラーが発生することに気付くでしょう。では、バージョン2.5.0用のコードの修正を始めましょう。

Use `import aspose.pdf.*` ; instead of `import com.aspose.pdf.elements.*`; to include the package.

パッケージを含めるために、`import com.aspose.pdf.elements.*` の代わりに `import aspose.pdf.*` を使用してください。

For license initialization, please update your existing code from 

ライセンスの初期化のために、既存のコードを以下のように更新してください。

{{% alert color="primary" %}}
**com.aspose.pdf.License lic = new com.aspose.pdf.License();**

```java

 try
{
lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));
}

```

{{% /alert %}}

to 

次のように：

{{% alert color="primary" %}}
**aspose.pdf.License lic = new aspose.pdf.License();**

```java

 try
{
lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));
}

```


{{% /alert %}}

**TextInfo**には、もう**setUnderLine(...)**メソッドが含まれていません。代わりに**TextInfo.setIsUnderline(...)**を使用してください。

**HyperLinkToLocalPdf**という名前のクラスは削除されました。そのため、既存のコードを次のように更新してください。

{{% alert color="primary" %}}
**// テキストセグメントのリンクタイプをローカルに設定**

```java

 // 必要な段落のIDをテキストセグメントのターゲットIDとして割り当てる

segment1.setHyperLink(new HyperLinkToLocalPdf("product1"));

```

{{% /alert %}}

次のように

{{% alert color="primary" %}}
**segment1.getHyperlink().setLinkType(HyperlinkType.Local);**

```java

 segment1.getHyperlink().setTargetID("product1");

```

{{% /alert %}}

**setFirstParagraph**というメソッド名はTextクラスから削除されました。
 新しいページにテキストセグメントを表示するためには、新しいSectionオブジェクトを作成し、そのセクションにテキストオブジェクトを追加する必要があります。デフォルトでは、すべてのセクションは新しいページに表示されるため、**sec2.setIsNewPage(true)** のようなメソッドを呼び出す必要はありません。

## 更新された保存メソッド

FileOutputStreamオブジェクトを引数として取っていたPdfクラスのsaveメソッドは削除されました。新しいバージョンでは、次のオーバーロードされたsaveメソッドのいずれかを使用できます。

- save(BasicStream stream)
- save(java.lang.String pdfFile)
- save(java.lang.String fileName, SaveType saveType, aspose.pdf.HttpResponse response)

上記の変更をすべて行った後、Aspose.PDF for Java 2.5.0を使用する際には、コードはエラーメッセージを表示することなくコンパイルおよび実行されます。更新された完全なコードスニペットは以下に示されています。

```java
import aspose.pdf.*;
aspose.pdf.License lic = new aspose.pdf.License();

try {

lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));

    } catch (Exception e)

{

System.out.println(e.getMessage());

}

try {

// 空のコンストラクタを呼び出してPdfオブジェクトをインスタンス化する

Pdf pdf1 = new Pdf();

// Pdfオブジェクトにセクションを作成する

Section sec1 = pdf1.getSections().add();

// セクションの参照を持つテキスト段落を作成する

Text text1 = new Text(sec1);

// セクションの段落コレクションにテキスト段落を追加する

sec1.getParagraphs().add(text1);

// テキスト段落にテキストセグメントを追加する

Segment segment1 = text1.getSegments().add("this is a local link");

// テキストセグメントのテキストを下線付きに設定する

segment1.getTextInfo().setIsUnderline(true);


// テキストセグメントのリンクタイプをLocalに設定する

// テキストセグメントのターゲットIDとして目的の段落のIDを割り当てる

segment1.getHyperlink().setLinkType(HyperlinkType.Local);

segment1.getHyperlink().setTargetID("product1");

// "Product 1"のIDを持つテキストオブジェクトを保持する新しいセクションを追加する

Section sec2 = pdf1.getSections().add();

// テキストセグメントとリンクするためのテキスト段落を作成する

Text text3 = new Text(sec1,"product 1 info ...");

// セクションの段落コレクションにテキスト段落を追加する

sec2.getParagraphs().add(text3);

// このテキストセグメントのIDを"product1"に設定する

text3.setID("product1");


// PDFファイルを保存する

pdf1.save("UpdateOfCode_Test.pdf");


     }catch(Exception e)

{

System.out.println(e.getMessage());

}
```

## 結論

上記のトピックでは、新しいリリースで変更されたクラスとメソッドの一部を説明しました。すべてのクラスとそのメンバーの完全なリストについては、[Aspose.PDF for Java API Reference](http://www.aspose.com/documentation/java-components/aspose.pdf-for-java/aspose.pdf-for-java-api-reference.html) をご覧ください。

Asposeとその製品についてもっと学ぶには、こちらをクリックしてください <http://www.aspose.com/>