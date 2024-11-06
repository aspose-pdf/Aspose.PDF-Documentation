---
title: Tagged PDFを作成する
linktitle: Tagged PDFを作成する
type: docs
weight: 10
lastmod: "2021-06-05"
url: ja/java/create-tagged-pdf-documents/
description: この記事では、Aspose.PDF for Javaを使用してプログラムでTagged PDFドキュメントの構造要素を作成する方法を説明します。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 構造要素の作成

Tagged PDFドキュメントに構造要素を作成するために、Aspose.PDFは[ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent)インターフェースを使用して構造要素を作成するためのメソッドを提供します。以下のコードスニペットは、Tagged PDFの構造要素を作成する方法を示しています。

```java
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-Java をご覧ください。
// ドキュメントディレクトリへのパス。
String path = "pathTodir";

// PDFドキュメントを作成
Document document = new Document();

// TaggedPdfと作業するためのコンテンツを取得
ITaggedContent taggedContent = document.getTaggedContent();

// ドキュメントのタイトルと言語を設定
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// グループ要素を作成
PartElement partElement = taggedContent.createPartElement();
ArtElement artElement = taggedContent.createArtElement();
SectElement sectElement = taggedContent.createSectElement();
DivElement divElement = taggedContent.createDivElement();
BlockQuoteElement blockQuoteElement = taggedContent.createBlockQuoteElement();
CaptionElement captionElement = taggedContent.createCaptionElement();
TOCElement tocElement = taggedContent.createTOCElement();
TOCIElement tociElement = taggedContent.createTOCIElement();
IndexElement indexElement = taggedContent.createIndexElement();
NonStructElement nonStructElement = taggedContent.createNonStructElement();
PrivateElement privateElement = taggedContent.createPrivateElement();

// テキストブロックレベルの構造要素を作成
ParagraphElement paragraphElement = taggedContent.createParagraphElement();
HeaderElement headerElement = taggedContent.createHeaderElement();
HeaderElement h1Element = taggedContent.createHeaderElement(1);

// テキストインラインレベルの構造要素を作成
SpanElement spanElement = taggedContent.createSpanElement();
QuoteElement quoteElement = taggedContent.createQuoteElement();
NoteElement noteElement = taggedContent.createNoteElement();

// イラストレーション構造要素を作成
FigureElement figureElement = taggedContent.createFigureElement();
FormulaElement formulaElement = taggedContent.createFormulaElement();

// メソッドは開発中です
ListElement listElement = taggedContent.createListElement();
TableElement tableElement = taggedContent.createTableElement();
ReferenceElement referenceElement = taggedContent.createReferenceElement();
BibEntryElement bibEntryElement = taggedContent.createBibEntryElement();
CodeElement codeElement = taggedContent.createCodeElement();
LinkElement linkElement = taggedContent.createLinkElement();
AnnotElement annotElement = taggedContent.createAnnotElement();
RubyElement rubyElement = taggedContent.createRubyElement();
WarichuElement warichuElement = taggedContent.createWarichuElement();
FormElement formElement = taggedContent.createFormElement();

// Tagged Pdfドキュメントを保存
document.save(path + "StructureElements.pdf");
```


## 構造要素ツリーの作成

Tagged PDFドキュメントで構造要素ツリーを作成するために、Aspose.PDFは[ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent)インターフェースを使用して構造要素ツリーを作成する方法を提供しています。以下のコードスニペットは、Tagged PDFドキュメントの構造要素ツリーを作成する方法を示しています:

```java
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-Java を参照してください。
// ドキュメントディレクトリへのパス。
String path = "pathTodir";
// PDFドキュメントを作成
Document document = new Document();

// TaggedPdfで作業するためのコンテンツを取得
ITaggedContent taggedContent = document.getTaggedContent();

// ドキュメントのタイトルと言語を設定
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// ルート構造要素（ドキュメント）を取得
StructureElement rootElement = taggedContent.getRootElement();

// 論理構造を作成
SectElement sect1 = taggedContent.createSectElement();
rootElement.appendChild(sect1);

SectElement sect2 = taggedContent.createSectElement();
rootElement.appendChild(sect2);

DivElement div11 = taggedContent.createDivElement();
sect1.appendChild(div11);

DivElement div12 = taggedContent.createDivElement();
sect1.appendChild(div12);

ArtElement art21 = taggedContent.createArtElement();
sect2.appendChild(art21);

ArtElement art22 = taggedContent.createArtElement();
sect2.appendChild(art22);

DivElement div211 = taggedContent.createDivElement();
art21.appendChild(div211);

DivElement div212 = taggedContent.createDivElement();
art21.appendChild(div212);

DivElement div221 = taggedContent.createDivElement();
art22.appendChild(div221);

DivElement div222 = taggedContent.createDivElement();
art22.appendChild(div222);

SectElement sect3 = taggedContent.createSectElement();
rootElement.appendChild(sect3);

DivElement div31 = taggedContent.createDivElement();
sect3.appendChild(div31);

// Tagged Pdf Documentを保存
document.save(path + "StructureElementsTree.pdf");
```


## テキスト構造のスタイリング

Tagged PDF ドキュメント内でテキスト構造をスタイリングするために、Aspose.PDF は [StructureTextState](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.class-use/StructureTextState) クラスの **setFont()**、**setFontSize()**、**setFontStyle()**、**setForegroundColor()** プロパティを提供します。次のコードスニペットは、Tagged PDF ドキュメント内でテキスト構造をスタイリングする方法を示しています。

```java
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-Java をご覧ください。
// ドキュメントディレクトリへのパス。
String path = "pathTodir";
// PDF ドキュメントを作成
Document document = new Document();

// TaggedPdf を操作するためにコンテンツを取得
ITaggedContent taggedContent = document.getTaggedContent();

// ドキュメントのタイトルと言語を設定
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

ParagraphElement p = taggedContent.createParagraphElement();
taggedContent.getRootElement().appendChild(p);

// 開発中
p.getStructureTextState().setFontSize(18F);
p.getStructureTextState().setForegroundColor(Color.getRed());
p.getStructureTextState().setFontStyle(FontStyles.Italic);

p.setText("赤い斜体のテキスト。");

// Tagged Pdf ドキュメントを保存
document.save(path + "StyleTextStructure.pdf");
```


## 構造要素の説明

Tagged PDF ドキュメントで構造要素を説明するために、Aspose.PDF は [IllustrationElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.class-use/IllustrationElement) クラスを提供します。次のコードスニペットは、Tagged PDF ドキュメントで構造要素を説明する方法を示しています:

```java
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-Java を参照してください
// ドキュメントディレクトリへのパス
String path = "pathTodir";
// Pdf ドキュメントの作成
Document document = new Document();

// TaggedPdf を扱うためのコンテンツを取得
ITaggedContent taggedContent = document.getTaggedContent();

// ドキュメントのタイトルと言語を設定
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// 開発中
IllustrationElement figure1 = taggedContent.createFigureElement();
taggedContent.getRootElement().appendChild(figure1);
figure1.setActualText("図1");
figure1.setTitle("画像 1");
figure1.setTag("Fig1");
figure1.setImage("image.png");

// Tagged Pdf ドキュメントを保存
document.save(path + "IllustrationStructureElements.pdf");
```


## **タグ付き画像でPDFを作成**

タグ付き画像でPDFを作成するには、Aspose.PDFは[ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent) インターフェイスの[createFigureElement()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#createFigureElement--) メソッドを提供します。以下のコードスニペットはその機能を示しています。

```java
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-Java をご覧ください
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("CreatePDFwithTaggedImage");
taggedContent.setLanguage("en-US");

IllustrationElement figure1 = taggedContent.createFigureElement();
taggedContent.getRootElement().appendChild(figure1);
figure1.setAlternativeText("Aspose ロゴ");
figure1.setTitle("画像 1");
figure1.setTag("Fig");
// 解像度300 DPIで画像を追加（デフォルト）
figure1.setImage("aspose-logo.jpg");
// PDFドキュメントを保存
document.save("PDFwithTaggedImage.pdf");
```


## タグ付きテキストでPDFを作成

タグ付きテキストでPDFを作成するために、Aspose.PDFは[ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent)インターフェースを提供します。以下のコードスニペットは、その機能を示しています。

```java
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-Java を参照してください。
// ドキュメントディレクトリへのパス。
String dataDir = Utils.getDataDir() + "TaggedPDFs\\";
// Pdf ドキュメントを作成
Document document = new Document();

// タグ付きPDFを操作するためのコンテンツを取得
ITaggedContent taggedContent = document.getTaggedContent();

// ドキュメントのタイトルと言語を設定
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// テキストブロックレベルの構造要素を作成
HeaderElement headerElement = taggedContent.createHeaderElement();
headerElement.setActualText("Heading 1");
ParagraphElement paragraphElement1 = taggedContent.createParagraphElement();
paragraphElement1.setActualText("test1");
ParagraphElement paragraphElement2 = taggedContent.createParagraphElement();
paragraphElement2.setActualText("test 2");
ParagraphElement paragraphElement3 = taggedContent.createParagraphElement();
paragraphElement3.setActualText("test 3");
ParagraphElement paragraphElement4 = taggedContent.createParagraphElement();
paragraphElement4.setActualText("test 4");
ParagraphElement paragraphElement5 = taggedContent.createParagraphElement();
paragraphElement5.setActualText("test 5");
ParagraphElement paragraphElement6 = taggedContent.createParagraphElement();
paragraphElement6.setActualText("test 6");
ParagraphElement paragraphElement7 = taggedContent.createParagraphElement();
paragraphElement7.setActualText("test 7");

// PDFドキュメントを保存
document.save( dataDir + "PDFwithTaggedText.pdf");
```