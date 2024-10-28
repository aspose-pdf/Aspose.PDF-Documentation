---
title: 태그된 PDF 생성
linktitle: 태그된 PDF 생성
type: docs
weight: 10
lastmod: "2021-06-05"
url: /java/create-tagged-pdf-documents/
description: 이 문서에서는 Aspose.PDF for Java를 사용하여 태그된 PDF 문서의 구조 요소를 프로그래밍 방식으로 생성하는 방법을 설명합니다.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 구조 요소 생성

태그된 PDF 문서에서 구조 요소를 생성하기 위해, Aspose.PDF는 [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent) 인터페이스를 사용하여 구조 요소를 생성하는 메서드를 제공합니다. 다음 코드 스니핏은 태그된 PDF의 구조 요소를 생성하는 방법을 보여줍니다:

```java
// 완전한 예제와 데이터 파일을 보려면 https://github.com/aspose-pdf/Aspose.PDF-for-Java를 방문하세요.
// 문서 디렉터리 경로.
String path = "pathTodir";

// PDF 문서 생성
Document document = new Document();

// 태그된 PDF와 작업하기 위한 콘텐츠 가져오기
ITaggedContent taggedContent = document.getTaggedContent();

// 문서의 제목과 언어 설정
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// 그룹 요소 생성
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

// 텍스트 블록 레벨 구조 요소 생성
ParagraphElement paragraphElement = taggedContent.createParagraphElement();
HeaderElement headerElement = taggedContent.createHeaderElement();
HeaderElement h1Element = taggedContent.createHeaderElement(1);

// 텍스트 인라인 레벨 구조 요소 생성
SpanElement spanElement = taggedContent.createSpanElement();
QuoteElement quoteElement = taggedContent.createQuoteElement();
NoteElement noteElement = taggedContent.createNoteElement();

// 삽화 구조 요소 생성
FigureElement figureElement = taggedContent.createFigureElement();
FormulaElement formulaElement = taggedContent.createFormulaElement();

// 메서드가 개발 중입니다
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

// 태그된 PDF 문서 저장
document.save(path + "StructureElements.pdf");
```


## 구조 요소 트리 생성

태그가 지정된 PDF 문서에서 구조 요소 트리를 생성하기 위해, Aspose.PDF는 [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent) 인터페이스를 사용하여 구조 요소 트리를 생성하는 방법을 제공합니다. 다음 코드 스니펫은 태그가 지정된 PDF 문서의 구조 요소 트리를 생성하는 방법을 보여줍니다:

```java
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-Java을 참조하세요.
// 문서 디렉토리의 경로.
String path = "pathTodir";
// PDF 문서 생성
Document document = new Document();

// TaggedPdf로 작업하기 위한 콘텐츠 가져오기
ITaggedContent taggedContent = document.getTaggedContent();

// 문서의 제목과 언어 설정
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// 루트 구조 요소 가져오기 (문서)
StructureElement rootElement = taggedContent.getRootElement();

// 논리 구조 생성
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

// 태그가 지정된 PDF 문서 저장
document.save(path + "StructureElementsTree.pdf");
```


## 텍스트 구조 스타일링

태그된 PDF 문서에서 텍스트 구조를 스타일링하기 위해, Aspose.PDF는 **setFont()**, **setFontSize()**, **setFontStyle()** 및 **setForegroundColor()** 속성을 [StructureTextState](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.class-use/StructureTextState) 클래스에 제공합니다. 다음 코드 스니펫은 태그된 PDF 문서에서 텍스트 구조를 스타일링하는 방법을 보여줍니다:

```java
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-Java를 참조하세요.
// 문서 디렉토리의 경로.
String path = "pathTodir";
// PDF 문서 생성
Document document = new Document();

// 태그된 PDF로 작업하기 위한 콘텐츠 가져오기
ITaggedContent taggedContent = document.getTaggedContent();

// 문서의 제목과 언어 설정
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

ParagraphElement p = taggedContent.createParagraphElement();
taggedContent.getRootElement().appendChild(p);

// 개발 중
p.getStructureTextState().setFontSize(18F);
p.getStructureTextState().setForegroundColor(Color.getRed());
p.getStructureTextState().setFontStyle(FontStyles.Italic);

p.setText("빨간색 이탤릭체 텍스트.");

// 태그된 PDF 문서 저장
document.save(path + "StyleTextStructure.pdf");
```


## 구조 요소 설명

태그가 지정된 PDF 문서에서 구조 요소를 설명하기 위해 Aspose.PDF는 [IllustrationElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.class-use/IllustrationElement) 클래스를 제공합니다. 다음 코드 스니펫은 태그가 지정된 PDF 문서에서 구조 요소를 설명하는 방법을 보여줍니다:

```java
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-Java를 참조하십시오.
// 문서 디렉토리 경로.
String path = "pathTodir";
// PDF 문서 생성
Document document = new Document();

// TaggedPdf로 작업할 콘텐츠 가져오기
ITaggedContent taggedContent = document.getTaggedContent();

// 문서의 제목과 언어 설정
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// 개발 중
IllustrationElement figure1 = taggedContent.createFigureElement();
taggedContent.getRootElement().appendChild(figure1);
figure1.setActualText("Figure One");
figure1.setTitle("Image 1");
figure1.setTag("Fig1");
figure1.setImage("image.png");

// 태그가 지정된 PDF 문서 저장
document.save(path + "IllustrationStructureElements.pdf");
```


## **태그된 이미지가 포함된 PDF 생성**

태그된 이미지가 포함된 PDF를 생성하기 위해, Aspose.PDF는 [createFigureElement()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#createFigureElement--) 메서드를 [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent) 인터페이스에서 제공합니다. 다음 코드 스니펫은 그 기능을 보여줍니다.

```java
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-Java 를 방문하세요
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("CreatePDFwithTaggedImage");
taggedContent.setLanguage("en-US");

IllustrationElement figure1 = taggedContent.createFigureElement();
taggedContent.getRootElement().appendChild(figure1);
figure1.setAlternativeText("Aspose Logo");
figure1.setTitle("Image 1");
figure1.setTag("Fig");
// 해상도 300 DPI로 이미지 추가 (기본값)
figure1.setImage("aspose-logo.jpg");
// PDF 문서 저장
document.save("PDFwithTaggedImage.pdf");
```


## 태그가 지정된 텍스트로 PDF 생성

태그가 지정된 텍스트로 PDF를 생성하기 위해 Aspose.PDF는 [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent) 인터페이스를 제공합니다. 다음 코드 스니펫은 기능을 보여줍니다.

```java
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-Java를 참조하세요
// 문서 디렉토리의 경로입니다.
String dataDir = Utils.getDataDir() + "TaggedPDFs\\";
// PDF 문서 생성
Document document = new Document();

// TaggedPdf 작업을 위한 콘텐츠 가져오기
ITaggedContent taggedContent = document.getTaggedContent();

// 문서의 제목과 언어 설정
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// 텍스트 블록 레벨 구조 요소 생성
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

// PDF 문서 저장
document.save( dataDir + "PDFwithTaggedText.pdf");
```