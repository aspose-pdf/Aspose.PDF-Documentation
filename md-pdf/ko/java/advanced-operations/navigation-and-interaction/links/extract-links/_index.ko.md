---
title: PDF 파일에서 링크 추출하기
linktitle: 링크 추출
type: docs
weight: 30
url: /java/extract-links/
description: Java를 사용하여 PDF에서 링크를 추출합니다. 이 주제는 AnnotationSelector 클래스를 사용하여 링크를 추출하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 파일에서 링크 추출하기

링크는 PDF 파일에서 주석으로 표현되므로 링크를 추출하려면 모든 [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) 객체를 추출해야 합니다.

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체를 생성합니다.
2. 링크를 추출하고자 하는 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)를 가져옵니다.
3. [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationselector) 클래스를 사용하여 지정된 페이지에서 모든 [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) 객체를 추출합니다.

1. [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationselector) 객체를 Page 객체의 Accept 메소드에 전달합니다.  
1. [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationselector) 객체의 [getSelected](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector#getSelected--) 메소드를 사용하여 선택된 모든 링크 주석을 IList 객체로 가져옵니다.

다음 코드 스니펫은 PDF 파일에서 링크를 추출하는 방법을 보여줍니다.

```java
    public static void ExtractLinksFromThePDFFile() {        
        // PDF 파일을 로드합니다.
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
           
        AnnotationSelector selector = new AnnotationSelector(new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(selector);
        java.util.List<Annotation> list = selector.getSelected();
        for(Annotation annot : list)
        {
            System.out.println("주석 위치: " + annot.getRect());
        }
                
        // 업데이트된 링크로 문서를 저장합니다.
        //document.save(_dataDir + "ExtractLinks_out.pdf");
    }
```