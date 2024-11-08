---
title: 액션 작업하기
linktitle: Actions
type: docs
weight: 20
url: /ko/java/actions/
description: 이 섹션에서는 Java를 사용하여 문서 및 양식 필드에 액션을 프로그래밍 방식으로 추가하는 방법을 설명합니다. PDF 파일에서 하이퍼링크를 추가, 생성 및 가져오는 방법을 배웁니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF 파일에는 첨부된 파일 첨부가 포함될 수 있으며, 이러한 문서에 하이퍼링크를 설정해야 하는 경우가 종종 있습니다. 기본 PDF 문서에서 PDF 첨부 파일로 독자를 안내하려면 첨부 파일을 가리키는 부모 문서에 링크를 생성할 수 있습니다.

## PDF 파일에 하이퍼링크 추가하기

PDF 파일에 하이퍼링크를 추가하여 독자가 PDF의 다른 부분이나 외부 콘텐츠로 이동할 수 있도록 할 수 있습니다.

PDF 문서에 웹 하이퍼링크를 추가하려면:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스 객체를 생성합니다.

1. 링크를 추가하려는 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 클래스를 가져옵니다.
1. Page 및 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) 객체를 사용하여 [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) 객체를 생성합니다. Rectangle 객체는 링크가 추가될 페이지의 위치를 지정하는 데 사용됩니다.
1. 원격 URI의 위치를 지정하는 [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToURIAction) 객체에 getAction 메서드를 설정합니다.
1. 하이퍼링크 텍스트를 표시하려면 [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) 객체가 배치된 위치와 유사한 위치에 텍스트 문자열을 추가합니다.
1. 자유 텍스트를 추가하려면:

- [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/FreeTextAnnotation) 객체를 인스턴스화합니다.
 It 또한 Page 및 Rectangle 객체를 인수로 허용하므로 LinkAnnotation 생성자에 대해 지정된 것과 동일한 값을 제공할 수 있습니다.
- [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/FreeTextAnnotation) 객체의 Contents 속성을 사용하여 출력 PDF에 표시되어야 하는 문자열을 지정합니다.
- 선택적으로 [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) 및 FreeTextAnnotation 객체의 테두리 너비를 0으로 설정하여 PDF 문서에 나타나지 않도록 합니다.
- [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) 및 [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/FreeTextAnnotation) 객체가 정의되면 이러한 링크를 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 객체의 Annotations 컬렉션에 추가합니다.

- 마지막으로 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 Save 메서드를 사용하여 업데이트된 PDF를 저장합니다.
다음 코드 조각은 PDF 파일에 하이퍼링크를 추가하는 방법을 보여줍니다.

```java
package com.aspose.pdf.examples;

import java.util.List;

import com.aspose.pdf.*;

public class ExampleActions {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Actions/";

    private static String GetDataDir() {
        String os = System.getProperty("os.name");
        if (os.startsWith("Windows"))
            _dataDir = "C:\\Samples\\Actions";
        return _dataDir;
    }

    public static void AddHyperlinkInPDFFile() {
        // 문서 열기
        Document document = new Document(GetDataDir() + "AddHyperlink.pdf");
        // 링크 생성
        Page page = document.getPages().get_Item(1);
        // 링크 주석 객체 생성
        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(100, 100, 300, 300));
        // LinkAnnotation을 위한 경계 객체 생성
        Border border = new Border(link);
        // 경계 너비 값을 0으로 설정
        border.setWidth(0);
        // LinkAnnotation에 경계 설정
        link.setBorder(border);
        // 링크 유형을 원격 URI로 지정
        link.setAction(new GoToURIAction("www.aspose.com"));
        // PDF 파일의 첫 페이지 주석 컬렉션에 링크 주석 추가
        page.getAnnotations().add(link);

        // 자유 텍스트 주석 생성
        FreeTextAnnotation textAnnotation = new FreeTextAnnotation(page, new Rectangle(100, 100, 300, 300),
                new DefaultAppearance(FontRepository.findFont("TimesNewRoman"), 10, java.awt.Color.BLUE));

        // 자유 텍스트로 추가될 문자열
        textAnnotation.setContents("Aspose 웹사이트로의 링크");
        // 자유 텍스트 주석에 경계 설정
        textAnnotation.setBorder(border);
        // 문서의 첫 페이지 주석 컬렉션에 자유 텍스트 주석 추가
        page.getAnnotations().add(textAnnotation);

        // 업데이트된 문서 저장
        document.save(_dataDir + "AddHyperlink_out.pdf");

    }
```


## 동일한 PDF의 페이지에 하이퍼링크 생성하기

Aspose.PDF for Java는 PDF 생성뿐만 아니라 PDF 조작에 대한 훌륭한 기능을 제공합니다. 또한 PDF 페이지에 링크를 추가하는 기능도 제공하며, 링크는 다른 PDF 파일의 페이지로, 웹 URL로, 애플리케이션 실행 링크로, 또는 동일한 PDF 파일의 페이지로 직접 연결될 수 있습니다.

로컬 하이퍼링크를 추가하기 위해서는 텍스트 조각(TextFragment)을 생성하여 링크를 텍스트 조각과 연결해야 합니다. [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) 클래스에는 LocalHyperlink 인스턴스를 연결하는 데 사용되는 [getHyperlink](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#getHyperlink--)이라는 메서드가 있습니다. 다음 코드 스니펫은 이 요구 사항을 충족하는 단계를 보여줍니다.

```java
public static void CreateHyperlinkToPagesInSamePDF() {
        // Document 인스턴스 생성
        Document document = new Document();

        // PDF 파일의 페이지 컬렉션에 페이지 추가
        Page page = document.getPages().add();

        // 텍스트 조각(TextFragment) 인스턴스 생성
        TextFragment text = new TextFragment("link page number test to page 2");

        // 로컬 하이퍼링크 인스턴스 생성
        LocalHyperlink link = new LocalHyperlink();

        // 링크 인스턴스의 대상 페이지 설정
        link.setTargetPageNumber(2);

        // 텍스트 조각의 하이퍼링크 설정
        text.setHyperlink(link);

        // 페이지의 문단 컬렉션에 텍스트 추가
        page.getParagraphs().add(text);

        // 새로운 텍스트 조각 인스턴스 생성
        text = new TextFragment("link page number test to page 1");

        // 텍스트 조각은 새로운 페이지에 추가되어야 함
        text.setInNewPage(true);

        // 또 다른 로컬 하이퍼링크 인스턴스 생성
        link = new LocalHyperlink();

        // 두 번째 하이퍼링크의 대상 페이지 설정
        link.setTargetPageNumber(1);

        // 두 번째 텍스트 조각에 링크 설정
        text.setHyperlink(link);

        // 페이지 객체의 문단 컬렉션에 텍스트 추가
        page.getParagraphs().add(text);

        // 업데이트된 문서 저장
        document.save(GetDataDir() + "CreateLocalHyperlink_out.pdf");
    }
```


## PDF 하이퍼링크 대상 (URL) 가져오기

링크는 PDF 파일에서 주석으로 표현되며 추가, 업데이트 또는 삭제할 수 있습니다. Aspose.PDF for Java는 PDF 파일에서 하이퍼링크의 목적지(URL)를 가져오는 것도 지원합니다.

링크의 URL을 얻으려면:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체를 생성합니다.
1. 링크를 추출하려는 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)를 가져옵니다.
1. [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector) 클래스를 사용하여 지정된 페이지의 모든 [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) 객체를 추출합니다.
1. [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector) 객체를 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 객체의 Accept 메서드에 전달합니다.

1. [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector) 객체의 Selected 속성을 사용하여 선택된 링크 주석을 IList 객체로 가져옵니다.
1. 마지막으로, LinkAnnotation 액션을 GoToURIAction으로 추출합니다.

다음 코드 스니펫은 PDF 파일에서 하이퍼링크 목적지(URL)를 얻는 방법을 보여줍니다.

```java
    public static void GetPDFHyperlinkDestination() {
        Document document = new Document(GetDataDir() + "Aspose-app-list.pdf");
        // 동작 추출
        Page page = document.getPages().get_Item(1);
        AnnotationSelector selector = new AnnotationSelector(new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(selector);
        List<Annotation> list = selector.getSelected();
        // 리스트 내 개별 항목 반복
        if (list.size() == 0)
            System.out.println("하이퍼링크가 없습니다..");
        else {
            // 모든 북마크를 순회
            for (Annotation annot : list) {
                LinkAnnotation la = (annot instanceof LinkAnnotation ? (LinkAnnotation) annot : null);
                if (la != null) {
                    // 목적지 URL 출력
                    System.out.println("목적지: " + ((GoToURIAction) la.getAction()).getURI());
                }
            }
        } // else 끝
    }
```


## 하이퍼링크 텍스트 가져오기

하이퍼링크는 문서에 표시되는 텍스트와 대상 URL 두 부분으로 구성됩니다. 경우에 따라 필요한 것은 URL이 아니라 텍스트입니다.

PDF 파일의 텍스트와 주석/동작은 서로 다른 엔티티로 표현됩니다. 페이지의 텍스트는 단순히 단어와 문자들의 집합이지만, 주석은 하이퍼링크에 내재된 상호작용성을 제공합니다.

URL 콘텐츠를 찾기 위해서는 주석과 텍스트를 모두 다루어야 합니다. [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/Annotation) 객체 자체는 텍스트를 가지지 않으며, 페이지의 텍스트 아래에 위치합니다. 따라서 텍스트를 얻기 위해서는 Annotation이 URL의 경계를 제공하고, Text 객체가 URL의 내용을 제공합니다. 다음 코드 스니펫을 참조하세요.

```java
    public static void GetHyperlinkText() {
        Document document = new Document(GetDataDir() + "Aspose-app-list.pdf");
        // 작업 추출
        Page page = document.getPages().get_Item(1);

        for (Annotation annot : page.getAnnotations()) {
            LinkAnnotation la = (annot instanceof LinkAnnotation ? (LinkAnnotation) annot : null);
            if (la != null) {
                // 각 링크 주석의 URL 출력
                System.out.println("URI: " + ((GoToURIAction) la.getAction()).getURI());
                TextAbsorber absorber = new TextAbsorber();
                absorber.getTextSearchOptions().setLimitToPageBounds(true);
                absorber.getTextSearchOptions().setRectangle(annot.getRect());
                page.accept(absorber);
                String extractedText = absorber.getText();
                // 하이퍼링크에 연결된 텍스트 출력
                System.out.println(extractedText);
            }
        }
    }
```


## PDF 파일에서 문서 열기 작업 제거

[문서 보기 시 PDF 페이지 지정 방법](#how-to-specify-pdf-page-when-viewing-document)에서는 문서가 첫 페이지가 아닌 다른 페이지에서 열리도록 지시하는 방법을 설명했습니다. 여러 문서를 연결할 때, 하나 이상에 GoTo 작업이 설정되어 있으면 이를 제거하고 싶을 것입니다. 예를 들어, 두 문서를 결합하고 두 번째 문서에 두 번째 페이지로 이동하는 GoTo 작업이 있는 경우, 출력 문서는 결합된 문서의 첫 페이지가 아닌 두 번째 문서의 두 번째 페이지에서 열릴 것입니다. 이 동작을 피하려면 열기 작업 명령을 제거하십시오.

열기 작업을 제거하려면:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 [getOpenAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getOpenAction--) 메서드를 null로 설정합니다.
2. Document 객체의 Save 메서드를 사용하여 업데이트된 PDF를 저장합니다.

다음 코드 스니펫은 PDF 파일에서 문서 열기 작업을 제거하는 방법을 보여줍니다.

```java
    public static void RemoveDocumentOpenActionFromPDFFile()
    {
        // 문서 열기
        Document document = new Document(_dataDir + "RemoveOpenAction.pdf");
        // 문서 열기 작업 제거
        document.setOpenAction(null);
        
        // 업데이트된 문서 저장
        document.save(GetDataDir()+"RemoveOpenAction_out.pdf");
    }
```


## 문서 보기 시 PDF 페이지 지정 방법 {#how-to-specify-pdf-page-when-viewing-document}

Adobe Reader와 같은 PDF 뷰어에서 PDF 파일을 볼 때, 파일은 일반적으로 첫 번째 페이지에서 열립니다. 그러나 파일을 다른 페이지에서 열리도록 설정할 수 있습니다.

[XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/XYZExplicitDestination) 클래스는 PDF 파일에서 열고자 하는 페이지를 지정할 수 있게 해줍니다. GoToAction 객체 값을 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스의 getOpenAction 메서드에 전달할 때, 문서는 XYZExplicitDestination 객체에 지정된 페이지에서 열립니다. 다음 코드 스니펫은 문서 열기 동작으로 페이지를 지정하는 방법을 보여줍니다.

```java
    public static void HowToSpecifyPDFPageWhenViewingDocument()
    {
        // PDF 파일 로드
        Document document = new Document(GetDataDir()+ "SpecifyPageWhenViewing.pdf");
        // 문서의 두 번째 페이지 인스턴스 가져오기
        Page page2 = document.getPages().get_Item(2);
        // 대상 페이지의 확대 비율을 설정할 변수 생성
        double zoom = 1;
        // GoToAction 인스턴스 생성
        GoToAction action = new GoToAction(page2);
        // 2페이지로 이동
        action.setDestination (new XYZExplicitDestination(page2, 0, page2.getRect().getHeight(), zoom));
        // 문서 열기 동작 설정
        document.setOpenAction (action);
        // 업데이트된 문서 저장
        document.save(_dataDir + "goto2page_out.pdf");
    }
}
```