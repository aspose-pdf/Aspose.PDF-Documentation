---
title: PDF에서 링크 업데이트 
linktitle: 링크 업데이트
type: docs
weight: 20
url: /java/update-links/
description: PDF의 링크를 프로그래밍 방식으로 업데이트합니다. 이 가이드는 Java 언어로 PDF의 링크를 업데이트하는 방법에 관한 것입니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 파일에서 링크 업데이트

PDF 파일에 하이퍼링크 추가에서 논의한 바와 같이, [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) 클래스는 PDF 파일에 링크를 추가할 수 있게 합니다. 기존의 링크를 PDF 파일 내에서 가져오는 데 사용되는 유사한 클래스도 있습니다. 기존 링크를 업데이트해야 할 경우 이를 사용하십시오. 기존 링크를 업데이트하려면:

1. PDF 파일을 로드합니다.
1. PDF 파일의 특정 페이지로 이동합니다.
1. [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction) 객체의 Destination 속성을 사용하여 링크 대상지를 지정합니다.

1. 대상 페이지는 [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/XYZExplicitDestination) 생성자를 사용하여 지정됩니다.

### 같은 문서 내의 페이지로 링크 대상 설정

다음 코드 스니펫은 PDF 파일의 링크를 업데이트하고 그 대상을 문서의 두 번째 페이지로 설정하는 방법을 보여줍니다.

```java
    public static void SetLinkTargetToAPageInTheSameDocument() {
        
        // PDF 파일 로드
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
        // 문서의 첫 번째 페이지에서 첫 번째 링크 주석 가져오기
        LinkAnnotation linkAnnot = (LinkAnnotation)page.getAnnotations().get_Item(1);

        // 링크 수정: 링크 대상 변경
        GoToAction goToAction = (GoToAction)linkAnnot.getAction();
        // 링크 객체의 대상을 지정
        // 명시적 대상을 나타내며, 페이지를 좌상단 모서리에 위치한 좌표 (left, top)로 표시하고 페이지 내용을 확대 비율로 확대하여 표시합니다.
        // 첫 번째 매개변수는 대상 페이지 번호입니다.
        // 두 번째는 왼쪽 좌표입니다.
        // 세 번째는 상단 좌표입니다.
        // 네 번째 인수는 해당 페이지를 표시할 때의 확대 비율입니다. 2를 사용하면 페이지가 200% 확대되어 표시됩니다.
        goToAction.setDestination(new XYZExplicitDestination(1, 1, 2, 2 ));
        
        // 업데이트된 링크로 문서 저장
        document.save(_dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");        
    }
```


### 웹 주소로 링크 대상 설정

하이퍼링크를 웹 주소로 가리키도록 업데이트하려면, [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction) 객체를 인스턴스화하고 LinkAnnotation의 Action 속성에 전달합니다. 다음 코드 스니펫은 PDF 파일의 링크를 업데이트하고 그 대상을 웹 주소로 설정하는 방법을 보여줍니다.

```java
    public static void SetLinkDestinationToWebAddress() {        
        // PDF 파일 로드
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
    
        // 문서의 첫 번째 페이지에서 첫 번째 링크 주석 가져오기
        LinkAnnotation linkAnnot = (LinkAnnotation)page.getAnnotations().get_Item(1);

        // 링크 수정: 링크 동작을 변경하고 대상을 웹 주소로 설정
        linkAnnot.setAction(new GoToURIAction("www.aspose.com"));
        
        // 업데이트된 링크와 함께 문서 저장
        document.save(_dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");        
    }
```


### 링크 대상 다른 PDF 파일로 설정하기

다음 코드 스니펫은 PDF 파일의 링크를 업데이트하고 그 대상을 다른 PDF 파일로 설정하는 방법을 보여줍니다.

```java
    public static void SetLinkTargetToAnotherPDFFile() {        
        // PDF 파일 불러오기
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
    
        LinkAnnotation linkAnnot = (LinkAnnotation)page.getAnnotations().get_Item(1);

        GoToRemoteAction goToR = (GoToRemoteAction)linkAnnot.getAction();
        // 다음 줄은 목적지를 업데이트하고, 파일은 업데이트하지 않음
        goToR.setDestination(new XYZExplicitDestination(2, 0, 0, 1.5));
        // 다음 줄은 파일을 업데이트함
        goToR.setFile (new FileSpecification(_dataDir +  "input.pdf"));

        // 업데이트된 링크와 함께 문서 저장
        document.save(_dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");        
    }
```

### LinkAnnotation 텍스트 색상 업데이트하기

링크 주석에는 텍스트가 포함되어 있지 않습니다.
 대신 텍스트는 주석 아래 페이지의 내용에 배치됩니다. 따라서 주석의 색상을 변경하려고 하는 대신 페이지 텍스트의 색상을 변경하여 텍스트의 색상을 바꿉니다. 다음 코드 스니펫은 PDF 파일에서 링크 주석의 색상을 업데이트하는 방법을 보여줍니다.

```java
    public static void UpdateLinkAnnotationTextColor () {        
        // PDF 파일 로드
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
           
        for (Annotation annotation : page.getAnnotations())
        {
            if (annotation.getAnnotationType() == AnnotationType.Link)
            {
                // 주석 아래의 텍스트 검색
                TextFragmentAbsorber ta = new TextFragmentAbsorber();
                Rectangle rect = annotation.getRect();
                rect.setLLX(rect.getLLX()-10);
                rect.setLLY(rect.getLLY()-10);
                rect.setURX(rect.getURX()+ 10);
                rect.setURY(rect.getURY()+ 10);

                ta.setTextSearchOptions(new TextSearchOptions(rect));
                ta.visit(page);
                // 텍스트의 색상 변경.
                for (TextFragment tf : ta.getTextFragments())
                {
                    tf.getTextState().setForegroundColor(Color.getRed());
                }
            }
        
        }                       
        // 업데이트된 링크로 문서 저장
        document.save(_dataDir + "UpdateLinkTextColor_out.pdf");        
    }
```