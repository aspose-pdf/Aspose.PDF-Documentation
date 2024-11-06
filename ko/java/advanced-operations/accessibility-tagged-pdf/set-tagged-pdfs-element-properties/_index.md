---
title: 태그된 PDF에서 구조 요소 속성 설정
linktitle: 구조 요소 속성 설정
type: docs
weight: 30
url: ko/java/set-tagged-pdfs-element-properties/
description: Aspose.PDF for Java를 사용하여 다양한 구조 요소 속성을 설정할 수 있습니다. 텍스트 블록 구조 요소 설정, 인라인 구조 요소 설정, 요소에 구조 요소 추가 등이 있습니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 구조 요소 속성 설정

태그된 PDF 문서에서 구조 요소 속성을 설정하기 위해 Aspose.PDF는 [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent) 인터페이스의 **createSectElement()** 및 **createHeaderElement()** 메서드를 제공합니다. 다음 코드 스니펫은 태그된 PDF 문서의 구조 요소 속성을 설정하는 방법을 보여줍니다:

```java
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-Java를 참조하세요.
// 문서 디렉토리의 경로.
String path = "pathTodir";
// Pdf 문서 생성
Document document = new Document();

// TaggedPdf 작업을 위한 컨텐츠 가져오기
ITaggedContent taggedContent = document.getTaggedContent();

// 문서에 제목과 언어 설정
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// 구조 요소 생성
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

// 태그된 Pdf 문서 저장
document.save(path + "StructureElementsProperties.pdf");
```


## 텍스트 구조 요소 설정

태그가 지정된 PDF 문서의 텍스트 구조 요소를 설정하기 위해, Aspose.PDF는 [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/class-use/ParagraphElement) 클래스를 제공합니다. 다음 코드 스니펫은 태그가 지정된 PDF 문서의 텍스트 구조 요소를 설정하는 방법을 보여줍니다:

```java
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-Java를 참조하세요
// 문서 디렉토리의 경로.
String path = "pathTodir";

// PDF 문서 생성
Document document = new Document();

// 태그가 지정된 PDF와 작업할 콘텐츠 가져오기
ITaggedContent taggedContent = document.getTaggedContent();

// 문서에 제목과 언어 설정
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// 루트 구조 요소 가져오기
StructureElement rootElement = taggedContent.getRootElement();

ParagraphElement p = taggedContent.createParagraphElement();
// 텍스트 구조 요소에 텍스트 설정
p.setText("단락.");
rootElement.appendChild(p);


// 태그가 지정된 PDF 문서 저장
document.save(path + "TextStructureElement.pdf");
```


## 텍스트 블록 구조 요소 설정

태그가 있는 PDF 문서의 텍스트 블록 구조 요소를 설정하기 위해, Aspose.PDF는 [HeaderElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls.class-use/headerelement) 및 [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/class-use/ParagraphElement) 클래스를 제공합니다. 이러한 클래스의 객체를 **StructureElement** 객체의 자식으로 추가할 수 있습니다. 다음 코드 스니펫은 태그가 있는 PDF 문서의 텍스트 블록 구조 요소를 설정하는 방법을 보여줍니다:

```java
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-Java를 참조하십시오.
// 문서 디렉터리의 경로
String path = "pathTodir";

// PDF 문서 생성
Document document = new Document();

// 태그가 있는 PDF와 작업할 콘텐츠 가져오기
ITaggedContent taggedContent = document.getTaggedContent();

// 문서의 제목과 언어 설정
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// 루트 구조 요소 가져오기
StructureElement rootElement = taggedContent.getRootElement();

HeaderElement h1 = taggedContent.createHeaderElement(1);
HeaderElement h2 = taggedContent.createHeaderElement(2);
HeaderElement h3 = taggedContent.createHeaderElement(3);
HeaderElement h4 = taggedContent.createHeaderElement(4);
HeaderElement h5 = taggedContent.createHeaderElement(5);
HeaderElement h6 = taggedContent.createHeaderElement(6);
h1.setText("H1. 레벨 1의 헤더");
h2.setText("H2. 레벨 2의 헤더");
h3.setText("H3. 레벨 3의 헤더");
h4.setText("H4. 레벨 4의 헤더");
h5.setText("H5. 레벨 5의 헤더");
h6.setText("H6. 레벨 6의 헤더");
rootElement.appendChild(h1);
rootElement.appendChild(h2);
rootElement.appendChild(h3);
rootElement.appendChild(h4);
rootElement.appendChild(h5);
rootElement.appendChild(h6);

ParagraphElement p = taggedContent.createParagraphElement();
p.setText("P. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
rootElement.appendChild(p);

// 태그가 있는 PDF 문서 저장
document.save(path + "TextBlockStructureElements.pdf");
```


## 인라인 구조 요소 설정

태그된 PDF 문서의 인라인 구조 요소를 설정하기 위해, Aspose.PDF는 [SpanElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.ils/spanelement) 및 [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/class-use/ParagraphElement) 클래스를 제공합니다. 이 클래스의 객체를 **StructureElement** 객체의 자식으로 추가할 수 있습니다. 다음 코드 스니펫은 태그된 PDF 문서의 인라인 구조 요소를 설정하는 방법을 보여줍니다:

```java
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-Java를 참조하세요.
// 문서 디렉토리의 경로.
String path = "pathTodir";
// PDF 문서 생성
Document document = new Document();

// 태그된 PDF 작업을 위한 콘텐츠 가져오기
ITaggedContent taggedContent = document.getTaggedContent();

// 문서의 제목과 언어 설정
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// 루트 구조 요소 가져오기
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
spanH12.setText("레벨 1 헤더");
h1.appendChild(spanH12);

SpanElement spanH21 = taggedContent.createSpanElement();
spanH21.setText("H2. ");
h2.appendChild(spanH21);
SpanElement spanH22 = taggedContent.createSpanElement();
spanH22.setText("레벨 2 헤더");
h2.appendChild(spanH22);

SpanElement spanH31 = taggedContent.createSpanElement();
spanH31.setText("H3. ");
h3.appendChild(spanH31);
SpanElement spanH32 = taggedContent.createSpanElement();
spanH32.setText("레벨 3 헤더");
h3.appendChild(spanH32);

SpanElement spanH41 = taggedContent.createSpanElement();
spanH41.setText("H4. ");
h4.appendChild(spanH41);
SpanElement spanH42 = taggedContent.createSpanElement();
spanH42.setText("레벨 4 헤더");
h4.appendChild(spanH42);

SpanElement spanH51 = taggedContent.createSpanElement();
spanH51.setText("H5. ");
h5.appendChild(spanH51);
SpanElement spanH52 = taggedContent.createSpanElement();
spanH52.setText("레벨 5 헤더");
h5.appendChild(spanH52);

SpanElement spanH61 = taggedContent.createSpanElement();
spanH61.setText("H6. ");
h6.appendChild(spanH61);
SpanElement spanH62 = taggedContent.createSpanElement();
spanH62.setText("레벨 6 헤더");
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

// 태그된 PDF 문서 저장
document.save(path + "InlineStructureElements.pdf");
```


## 사용자 지정 태그 이름 설정

태그가 지정된 PDF 문서의 요소에 사용자 지정 태그 이름을 설정하기 위해 Aspose.PDF는 요소에 대해 **setTag()** 메서드를 제공합니다. 다음 코드는 사용자 지정 태그 이름을 설정하는 방법을 보여줍니다:

```java
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-Java를 참조하세요.
// 문서 디렉토리 경로.
String path = "pathTodir";
// PDF 문서 생성
Document document = new Document();

// 태그가 지정된 PDF 작업을 위한 콘텐츠 가져오기
ITaggedContent taggedContent = document.getTaggedContent();

// 문서에 제목과 언어 설정
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// 논리 구조 요소 생성
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

// 태그가 지정된 PDF 문서 저장
document.save(path + "CustomTag.pdf");
```


## 구조 요소를 요소에 추가하기

태그된 PDF 문서에서 링크 구조 요소를 설정하기 위해 Aspose.PDF는 [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent) 인터페이스의 **createLinkElement()** 메서드를 제공합니다. 다음 코드 스니펫은 태그된 PDF 문서의 텍스트가 포함된 단락에서 구조 요소를 설정하는 방법을 보여줍니다:

```java
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-Java를 참조하세요.
// 문서 디렉토리의 경로입니다.
String dataDir = Utils.getDataDir() + "TaggedPDFs\\";
String outFile = dataDir + "AddStructureElementIntoElement_Output.pdf";
String logFile = dataDir + "46144_log.xml";

// 문서 생성 및 태그된 PDF 콘텐츠 가져오기
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();


// 문서에 제목과 자연어 설정
taggedContent.setTitle("텍스트 요소 예제");
taggedContent.setLanguage("en-US");

// 루트 구조 요소 가져오기 (문서 구조 요소)
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


// 태그된 PDF 문서 저장
document.save(outFile);
```


## 노트 구조 요소 설정

Aspose.PDF for Java API를 사용하면 태그된 PDF 문서에 **NoteElement**를 추가할 수 있습니다. 다음 코드 스니펫은 태그된 PDF 문서에 노트 요소를 추가하는 방법을 보여줍니다:

```java
// 전체 예제 및 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-Java를 참조하세요.
// 문서 디렉터리의 경로입니다.
String dataDir = Utils.getDataDir() + "TaggedPDFs\\";
String outFile = dataDir + "CreateNoteStructureElement.pdf";
String logFile = dataDir + "45929_log.xml";

// PDF 문서 생성
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("노트 요소 샘플");
taggedContent.setLanguage("en-US");

// 단락 요소 추가
ParagraphElement paragraph = taggedContent.createParagraphElement();
taggedContent.getRootElement().appendChild(paragraph);

// 노트 요소 추가
NoteElement note1 = taggedContent.createNoteElement();
paragraph.appendChild(note1);
note1.setText("자동 생성 ID가 있는 노트. ");

// 노트 요소 추가
NoteElement note2 = taggedContent.createNoteElement();
paragraph.appendChild(note2);
note2.setText("ID가 'note_002'인 노트. ");
note2.setId("note_002");

// 노트 요소 추가
NoteElement note3 = taggedContent.createNoteElement();
paragraph.appendChild(note3);
note3.setText("ID가 'note_003'인 노트. ");
note3.setId("note_003");
// 태그된 PDF 문서 저장
document.save(outFile);
```