---
title: タグ付きPDFにおける構造要素のプロパティ設定
linktitle: 構造要素のプロパティ設定
type: docs
weight: 30
url: ja/java/set-tagged-pdfs-element-properties/
description: Aspose.PDF for Javaを使用すると、さまざまな構造要素のプロパティを設定できます。テキストブロック構造要素の設定、インライン構造要素の設定、構造要素の追加などがあります。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 構造要素のプロパティ設定

タグ付きPDFドキュメントに構造要素のプロパティを設定するために、Aspose.PDFは[ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent)インターフェースの**createSectElement()**および**createHeaderElement()**メソッドを提供しています。以下のコードスニペットは、タグ付きPDFドキュメントの構造要素のプロパティを設定する方法を示しています:

```java
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-Java を参照してください
// ドキュメントディレクトリへのパス
String path = "pathTodir";
// PDFドキュメントを作成
Document document = new Document();

// タグ付きPDFを扱うためのコンテンツを取得
ITaggedContent taggedContent = document.getTaggedContent();

// ドキュメントのタイトルと言語を設定
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// 構造要素を作成
StructureElement rootElement = taggedContent.getRootElement();

SectElement sect = taggedContent.createSectElement();
rootElement.appendChild(sect);

HeaderElement h1 = taggedContent.createHeaderElement(1);
sect.appendChild(h1);
h1.setText("The Header");

h1.setTitle("Title");
h1.setLanguage("en-US");
h1.setAlternativeText("Alternative Text");
h1.setExpansionText("Expansion Text");
h1.setActualText("Actual Text");

// タグ付きPDFドキュメントを保存
document.save(path + "StructureElementsProperties.pdf");
```


## テキスト構造要素の設定

Tagged PDF ドキュメントのテキスト構造要素を設定するために、Aspose.PDF は [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/class-use/ParagraphElement) クラスを提供しています。以下のコードスニペットは、Tagged PDF ドキュメントのテキスト構造要素を設定する方法を示しています:

```java
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-Java をご覧ください。
// ドキュメントディレクトリへのパス。
String path = "pathTodir";

// PDF ドキュメントを作成
Document document = new Document();

// TaggedPdf を扱うためのコンテンツを取得
ITaggedContent taggedContent = document.getTaggedContent();

// ドキュメントのタイトルと言語を設定
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// ルート構造要素を取得
StructureElement rootElement = taggedContent.getRootElement();

ParagraphElement p = taggedContent.createParagraphElement();
// テキストをテキスト構造要素に設定
p.setText("Paragraph.");
rootElement.appendChild(p);

// Tagged Pdf ドキュメントを保存
document.save(path + "TextStructureElement.pdf");
```


## テキストブロック構造要素の設定

タグ付きPDFドキュメントのテキストブロック構造要素を設定するために、Aspose.PDFは[HeaderElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls.class-use/headerelement)と[ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/class-use/ParagraphElement)クラスを提供します。これらのクラスのオブジェクトを**StructureElement**オブジェクトの子として追加できます。次のコードスニペットは、タグ付きPDFドキュメントのテキストブロック構造要素を設定する方法を示しています。

```java
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-Java をご覧ください。
// ドキュメントディレクトリへのパス。
String path = "pathTodir";

// Pdfドキュメントを作成
Document document = new Document();

// TaggedPdfで作業するためのコンテンツを取得
ITaggedContent taggedContent = document.getTaggedContent();

// ドキュメントのタイトルと言語を設定
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// ルート構造要素を取得
StructureElement rootElement = taggedContent.getRootElement();

HeaderElement h1 = taggedContent.createHeaderElement(1);
HeaderElement h2 = taggedContent.createHeaderElement(2);
HeaderElement h3 = taggedContent.createHeaderElement(3);
HeaderElement h4 = taggedContent.createHeaderElement(4);
HeaderElement h5 = taggedContent.createHeaderElement(5);
HeaderElement h6 = taggedContent.createHeaderElement(6);
h1.setText("H1. レベル1のヘッダー");
h2.setText("H2. レベル2のヘッダー");
h3.setText("H3. レベル3のヘッダー");
h4.setText("H4. レベル4のヘッダー");
h5.setText("H5. レベル5のヘッダー");
h6.setText("H6. レベル6のヘッダー");
rootElement.appendChild(h1);
rootElement.appendChild(h2);
rootElement.appendChild(h3);
rootElement.appendChild(h4);
rootElement.appendChild(h5);
rootElement.appendChild(h6);

ParagraphElement p = taggedContent.createParagraphElement();
p.setText("P. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
rootElement.appendChild(p);

// タグ付きPDFドキュメントを保存
document.save(path + "TextBlockStructureElements.pdf");
```


## インライン構造要素の設定

タグ付きPDFドキュメントのインライン構造要素を設定するために、Aspose.PDFは[SpanElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.ils/spanelement)と[ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/class-use/ParagraphElement)クラスを提供します。これらのクラスのオブジェクトを**StructureElement**オブジェクトの子として追加することができます。以下のコードスニペットは、タグ付きPDFドキュメントのインライン構造要素を設定する方法を示しています。

```java
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-Java をご覧ください。
// ドキュメントディレクトリへのパス。
String path = "pathTodir";
// PDFドキュメントを作成
Document document = new Document();

// TaggedPdfで作業するためのコンテンツを取得
ITaggedContent taggedContent = document.getTaggedContent();

// ドキュメントのタイトルと言語を設定
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// ルート構造要素を取得
StructureElement rootElement = taggedContent.getRootElement();

HeaderElement h1 = taggedContent.createHeaderElement(1);
HeaderElement h2 = taggedContent.createHeaderElement(2);
HeaderElement h3 = taggedContent.createHeaderElement(3);
HeaderElement h4 = taggedContent.createHeaderElement(4);
HeaderElement h5 = taggedContent.createHeaderElement(5);
HeaderElement h6 = taggedContent.createHeaderElement(6);
rootElement.appendChild(h1);
rootElement.appendChild(h2);
rootElement.appendChild(h3);
rootElement.appendChild(h4);
rootElement.appendChild(h5);
rootElement.appendChild(h6);

SpanElement spanH11 = taggedContent.createSpanElement();
spanH11.setText("H1. ");
h1.appendChild(spanH11);
SpanElement spanH12 = taggedContent.createSpanElement();
spanH12.setText("Level 1 Header");
h1.appendChild(spanH12);

SpanElement spanH21 = taggedContent.createSpanElement();
spanH21.setText("H2. ");
h2.appendChild(spanH21);
SpanElement spanH22 = taggedContent.createSpanElement();
spanH22.setText("Level 2 Header");
h2.appendChild(spanH22);

SpanElement spanH31 = taggedContent.createSpanElement();
spanH31.setText("H3. ");
h3.appendChild(spanH31);
SpanElement spanH32 = taggedContent.createSpanElement();
spanH32.setText("Level 3 Header");
h3.appendChild(spanH32);

SpanElement spanH41 = taggedContent.createSpanElement();
spanH41.setText("H4. ");
h4.appendChild(spanH41);
SpanElement spanH42 = taggedContent.createSpanElement();
spanH42.setText("Level 4 Header");
h4.appendChild(spanH42);

SpanElement spanH51 = taggedContent.createSpanElement();
spanH51.setText("H5. ");
h5.appendChild(spanH51);
SpanElement spanH52 = taggedContent.createSpanElement();
spanH52.setText("Level 5 Header");
h5.appendChild(spanH52);

SpanElement spanH61 = taggedContent.createSpanElement();
spanH61.setText("H6. ");
h6.appendChild(spanH61);
SpanElement spanH62 = taggedContent.createSpanElement();
spanH62.setText("Level 6 Header");
h6.appendChild(spanH62);

ParagraphElement p = taggedContent.createParagraphElement();
p.setText("P. ");
rootElement.appendChild(p);
SpanElement span1 = taggedContent.createSpanElement();
span1.setText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. ");
p.appendChild(span1);
SpanElement span2 = taggedContent.createSpanElement();
span2.setText("Aenean nec lectus ac sem faucibus imperdiet. ");
p.appendChild(span2);
SpanElement span3 = taggedContent.createSpanElement();
span3.setText("Sed ut erat ac magna ullamcorper hendrerit. ");
p.appendChild(span3);
SpanElement span4 = taggedContent.createSpanElement();
span4.setText("Cras pellentesque libero semper, gravida magna sed, luctus leo. ");
p.appendChild(span4);
SpanElement span5 = taggedContent.createSpanElement();
span5.setText("Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. ");
p.appendChild(span5);
SpanElement span6 = taggedContent.createSpanElement();
span6.setText("Interdum et malesuada fames ac ante ipsum primis in faucibus. ");
p.appendChild(span6);
SpanElement span7 = taggedContent.createSpanElement();
span7.setText("Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. ");
p.appendChild(span7);
SpanElement span8 = taggedContent.createSpanElement();
span8.setText("Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. ");
p.appendChild(span8);
SpanElement span9 = taggedContent.createSpanElement();
span9.setText("Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. ");
p.appendChild(span9);
SpanElement span10 = taggedContent.createSpanElement();
span10.setText("Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
p.appendChild(span10);

// タグ付きPDFドキュメントを保存
document.save(path + "InlineStructureElements.pdf");
```


## カスタムタグ名の設定

Tagged PDF ドキュメントの要素にカスタムタグ名を設定するために、Aspose.PDF は要素に対して **setTag()** メソッドを提供しています。次のコードスニペットは、カスタムタグ名を設定する方法を示しています:

```java
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-Java を参照してください。
// ドキュメントディレクトリへのパス。
String path = "pathTodir";
// Pdf ドキュメントを作成
Document document = new Document();

// TaggedPdf で作業するためのコンテンツを取得
ITaggedContent taggedContent = document.getTaggedContent();

// ドキュメントのタイトルと言語を設定
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// 論理構造要素を作成
SectElement sect = taggedContent.createSectElement();
taggedContent.getRootElement().appendChild(sect);

ParagraphElement p1 = taggedContent.createParagraphElement();
ParagraphElement p2 = taggedContent.createParagraphElement();
ParagraphElement p3 = taggedContent.createParagraphElement();
ParagraphElement p4 = taggedContent.createParagraphElement();

p1.setText("P1. ");
p2.setText("P2. ");
p3.setText("P3. ");
p4.setText("P4. ");

p1.setTag("P1");
p2.setTag("Para");
p3.setTag("Para");
p4.setTag("Paragraph");

sect.appendChild(p1);
sect.appendChild(p2);
sect.appendChild(p3);
sect.appendChild(p4);

SpanElement span1 = taggedContent.createSpanElement();
SpanElement span2 = taggedContent.createSpanElement();
SpanElement span3 = taggedContent.createSpanElement();
SpanElement span4 = taggedContent.createSpanElement();

span1.setText("Span 1.");
span2.setText("Span 2.");
span3.setText("Span 3.");
span4.setText("Span 4.");

span1.setTag("SPAN");
span2.setTag("Sp");
span3.setTag("Sp");
span4.setTag("TheSpan");

p1.appendChild(span1);
p2.appendChild(span2);
p3.appendChild(span3);
p4.appendChild(span4);

// Tagged Pdf ドキュメントを保存
document.save(path + "CustomTag.pdf");
```


## 要素への構造要素の追加

Aspose.PDF は、タグ付き PDF ドキュメントにリンク構造要素を設定するために、[ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent) インターフェースの **createLinkElement()** メソッドを提供します。次のコードスニペットは、タグ付き PDF ドキュメントのテキストを含む段落に構造要素を設定する方法を示しています。

```java
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-Java を参照してください。
// ドキュメントディレクトリへのパス。
String dataDir = Utils.getDataDir() + "TaggedPDFs\\";
String outFile = dataDir + "AddStructureElementIntoElement_Output.pdf";
String logFile = dataDir + "46144_log.xml";

// ドキュメントの作成とタグ付き PDF コンテンツの取得
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

// ドキュメントのタイトルと自然言語の設定
taggedContent.setTitle("テキスト要素の例");
taggedContent.setLanguage("en-US");

// ルート構造要素（ドキュメント構造要素）の取得
StructureElement rootElement = taggedContent.getRootElement();

ParagraphElement p1 = taggedContent.createParagraphElement();
rootElement.appendChild(p1);
SpanElement span11 = taggedContent.createSpanElement();
span11.setText("Span_11");
SpanElement span12 = taggedContent.createSpanElement();
span12.setText(" and Span_12.");
p1.setText("Paragraph with ");
p1.appendChild(span11);
p1.appendChild(span12);

ParagraphElement p2 = taggedContent.createParagraphElement();
rootElement.appendChild(p2);
SpanElement span21 = taggedContent.createSpanElement();
span21.setText("Span_21");
SpanElement span22 = taggedContent.createSpanElement();
span22.setText("Span_22.");
p2.appendChild(span21);
p2.setText(" and ");
p2.appendChild(span22);

ParagraphElement p3 = taggedContent.createParagraphElement();
rootElement.appendChild(p3);
SpanElement span31 = taggedContent.createSpanElement();
span31.setText("Span_31");
SpanElement span32 = taggedContent.createSpanElement();
span32.setText(" and Span_32");
p3.appendChild(span31);
p3.appendChild(span32);
p3.setText(".");

ParagraphElement p4 = taggedContent.createParagraphElement();
rootElement.appendChild(p4);
SpanElement span41 = taggedContent.createSpanElement();
SpanElement span411 = taggedContent.createSpanElement();
span411.setText("Span_411, ");
span41.setText("Span_41, ");
span41.appendChild(span411);
SpanElement span42 = taggedContent.createSpanElement();
SpanElement span421 = taggedContent.createSpanElement();
span421.setText("Span 421 and ");
span42.appendChild(span421);
span42.setText("Span_42");
p4.appendChild(span41);
p4.appendChild(span42);
p4.setText(".");

// タグ付き PDF ドキュメントを保存
document.save(outFile);
```


## ノート構造要素の設定

Aspose.PDF for Java APIを使用すると、タグ付きPDFドキュメントに**NoteElement**を追加することもできます。次のコードスニペットは、タグ付きPDFドキュメントにノート要素を追加する方法を示しています。

```java
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-Java を参照してください
// ドキュメントディレクトリへのパス。
String dataDir = Utils.getDataDir() + "TaggedPDFs\\";
String outFile = dataDir + "CreateNoteStructureElement.pdf";
String logFile = dataDir + "45929_log.xml";

// Pdf ドキュメントを作成
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("ノート要素のサンプル");
taggedContent.setLanguage("en-US");

// 段落要素を追加
ParagraphElement paragraph = taggedContent.createParagraphElement();
taggedContent.getRootElement().appendChild(paragraph);

// NoteElementを追加
NoteElement note1 = taggedContent.createNoteElement();
paragraph.appendChild(note1);
note1.setText("自動生成IDを持つノート。");

// NoteElementを追加
NoteElement note2 = taggedContent.createNoteElement();
paragraph.appendChild(note2);
note2.setText("ID = 'note_002' のノート。");
note2.setId("note_002");

// NoteElementを追加
NoteElement note3 = taggedContent.createNoteElement();
paragraph.appendChild(note3);
note3.setText("ID = 'note_003' のノート。");
note3.setId("note_003");
// タグ付きPDFドキュメントを保存
document.save(outFile);
```