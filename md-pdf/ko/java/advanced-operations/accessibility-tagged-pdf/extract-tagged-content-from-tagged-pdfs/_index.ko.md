---
title: PDF에서 태그가 지정된 콘텐츠 추출 
linktitle: 태그가 지정된 콘텐츠 추출
type: docs
weight: 20
url: /java/extract-tagged-content-from-tagged-pdfs/
description: 이 문서에서는 Aspose.PDF for Java를 사용하여 태그가 지정된 PDF 문서에서 콘텐츠를 추출하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 태그가 지정된 PDF 콘텐츠 가져오기

태그가 지정된 텍스트가 있는 PDF 문서의 콘텐츠를 가져오기 위해 Aspose.PDF는 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스의 [getTaggedContent()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getTaggedContent--) 메서드를 제공합니다. 다음 코드 스니펫은 태그가 지정된 텍스트가 있는 PDF 문서의 콘텐츠를 가져오는 방법을 보여줍니다:

```java
// 완전한 예제 및 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-Java를 참조하세요.
// 문서 디렉토리 경로.
String path = "pathTodir";

// PDF 문서 생성
Document document = new Document();

// 태그가 지정된 PDF로 작업할 콘텐츠 가져오기
ITaggedContent taggedContent = document.getTaggedContent();

//
// 태그가 지정된 PDF 콘텐츠로 작업
//

// 문서의 제목 및 언어 설정
taggedContent.setTitle("Simple Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// 태그가 지정된 PDF 문서 저장
document.save(path + "TaggedPDFContent.pdf");
```


## 루트 구조 가져오기

태그가 지정된 PDF 문서의 루트 구조를 가져오기 위해 Aspose.PDF는 [getStructTreeRootElement]()(https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#getStructTreeRootElement--) 및 [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent) 인터페이스의 **getStructureElement()** 메서드를 제공합니다. 다음 코드 스니펫은 태그가 지정된 PDF 문서의 루트 구조를 가져오는 방법을 보여줍니다:

```java
// 전체 예제 및 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-Java를 참조하세요.
// 문서 디렉터리 경로입니다.
String path = "pathTodir";
// PDF 문서 생성
Document document = new Document();

// 태그가 지정된 PDF와 작업할 콘텐츠 가져오기
ITaggedContent taggedContent = document.getTaggedContent();

// 문서의 제목과 언어 설정
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// 속성 StructTreeRootElement와 RootElement는
// pdf 문서의 StructTreeRoot 객체와 루트 구조 요소(문서 구조 요소)에 액세스하는 데 사용됩니다.
StructTreeRootElement structTreeRootElement = taggedContent.getStructTreeRootElement();
StructureElement rootElement = taggedContent.getRootElement();
```


## 자식 요소에 접근하기

태그된 PDF 문서의 자식 요소에 접근하기 위해 Aspose.PDF는 **ElementList** 클래스를 제공합니다. 다음 코드 스니펫은 태그된 PDF 문서의 자식 요소에 접근하는 방법을 보여줍니다:

```java
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-Java 에서 확인하세요.
String path = "pathTodir";
// PDF 문서 열기
Document document = new Document( path +"StructureElements.pdf");

// 태그된 PDF로 작업하기 위한 컨텐츠 가져오기
ITaggedContent taggedContent = document.getTaggedContent();

// 루트 요소에 접근하기
ElementList elementList = taggedContent.getStructTreeRootElement().getChildElements();
for (Element element : elementList)
{
    if (element instanceof StructureElement)
    {
        StructureElement structureElement =  (StructureElement)element;

        // 속성 가져오기
        String title = structureElement.getTitle();
        String language = structureElement.getLanguage();
        String actualText = structureElement.getActualText();
        String expansionText = structureElement.getExpansionText();
        String alternativeText = structureElement.getAlternativeText();
    }
}

// 루트 요소의 첫 번째 요소의 자식 요소에 접근하기
elementList = taggedContent.getRootElement().getChildElements().get_Item(1).getChildElements();
for (Element element : elementList)
{
    if (element instanceof StructureElement)
    {
        StructureElement structureElement = (StructureElement)element;

        // 속성 설정하기
        structureElement.setTitle("title");
        structureElement.setLanguage("fr-FR");
        structureElement.setActualText("actual text");
        structureElement.setExpansionText("exp");
        structureElement.setAlternativeText("alt");
    }
}

// 태그된 PDF 문서 저장
document.save( path +"AccessChildrenElements.pdf");
```