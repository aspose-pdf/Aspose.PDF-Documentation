---
title: PDF 하이라이트 주석
linktitle: 하이라이트 주석
type: docs
weight: 20
url: /ko/java/highlights-annotation/
description: 마크업 주석은 문서의 텍스트에 하이라이트, 밑줄, 취소선 또는 물결 밑줄로 표시됩니다.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

텍스트 마크업 주석은 문서의 텍스트에서 하이라이트, 밑줄, 취소선 또는 물결 모양의 밑줄로 나타납니다. 열리면 관련 메모의 텍스트가 포함된 팝업 창을 표시합니다.

PDF 문서의 텍스트 마크업 주석 속성은 PDF 뷰어 컨트롤에서 제공하는 속성 창을 사용하여 편집할 수 있습니다. 텍스트 마크업 주석의 색상, 불투명도, 작성자 및 주제를 수정할 수 있습니다.

highlightSettings 속성을 사용하여 하이라이트 주석의 설정을 가져오거나 설정할 수 있습니다.
 The highlightSettings 속성은 강조 표시 주석의 색상, 불투명도, 작성자, 주제, 수정 날짜 및 잠금 여부 속성을 설정하는 데 사용됩니다.

취소선 주석의 설정을 strikethroughSettings 속성을 사용하여 가져오거나 설정할 수도 있습니다. strikethroughSettings 속성은 취소선 주석의 색상, 불투명도, 작성자, 주제, 수정 날짜 및 잠금 여부 속성을 설정하는 데 사용됩니다.

다음 기능은 underlineSettings 속성을 사용하여 밑줄 주석의 설정을 가져오거나 설정할 수 있는 기능입니다. underlineSettings 속성은 밑줄 주석의 색상, 불투명도, 작성자, 주제, 수정 날짜 및 잠금 여부 속성을 설정하는 데 사용됩니다.

## 텍스트 강조 주석 추가

PDF 문서에 텍스트 강조 주석을 추가하려면 다음 작업을 수행해야 합니다:

1. PDF 파일 로드 - 새로운 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체.
1. 주석 생성:

    - [HighlightAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/HighlightAnnotation) 및 매개변수 설정 (제목, 색상).- [StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/StrikeOutAnnotation) 및 매개변수 설정 (제목, 색상).
- [SquigglyAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/SquigglyAnnotation) 및 매개변수 설정 (제목, 색상).
- [UnderlineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/UnderlineAnnotation) 및 매개변수 설정 (제목, 색상).
1. 그런 다음 모든 주석을 페이지에 추가해야 합니다.

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleTextMarkupAnnotation {
    // 문서 디렉토리의 경로.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddTextMarkupAnnotation() {
        try {
            // PDF 파일 불러오기
            Document document = new Document(_dataDir + "sample.pdf");
            Page page = document.getPages().get_Item(1);
            TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
            tfa.visit(page);

            // 주석 생성
            HighlightAnnotation highlightAnnotation = new HighlightAnnotation(page,
                    tfa.getTextFragments().get_Item(1).getRectangle());
            highlightAnnotation.setTitle("Aspose 사용자");
            highlightAnnotation.setColor(Color.getLightGreen());

            StrikeOutAnnotation strikeOutAnnotation = new StrikeOutAnnotation(page,
                    tfa.getTextFragments().get_Item(2).getRectangle());
            strikeOutAnnotation.setTitle("Aspose 사용자");
            strikeOutAnnotation.setColor(Color.getBlue());

            SquigglyAnnotation squigglyAnnotation = new SquigglyAnnotation(page,
                    tfa.getTextFragments().get_Item(3).getRectangle());
            squigglyAnnotation.setTitle("Aspose 사용자");
            squigglyAnnotation.setColor(Color.getRed());

            UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(page,
                    tfa.getTextFragments().get_Item(4).getRectangle());
            underlineAnnotation.setTitle("Aspose 사용자");
            underlineAnnotation.setColor(Color.getViolet());

            // 페이지에 주석 추가
            page.getAnnotations().add(highlightAnnotation);
            page.getAnnotations().add(squigglyAnnotation);
            page.getAnnotations().add(strikeOutAnnotation);
            page.getAnnotations().add(underlineAnnotation);
            document.save(_dataDir + "sample_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
}
```


If you want to highlight a multi-line fragment you should use advanced example:

```java
    /// <summary>
    /// 여러 줄의 일부분을 강조 표시하고 싶을 때 사용할 수 있는 고급 예제
    /// </summary>
    public static void AddHighlightAnnotationAdvanced() {
        Document document = new Document(_dataDir + "sample_mod.pdf");
        Page page = document.getPages().get_Item(1);
        TextFragmentAbsorber tfa = new TextFragmentAbsorber("Adobe\\W+Acrobat\\W+Reader", new TextSearchOptions(true));
        tfa.visit(page);
        for (TextFragment textFragment : tfa.getTextFragments()) {
            HighlightAnnotation highlightAnnotation = HighLightTextFragment(page, textFragment, Color.getYellow());
            page.getAnnotations().add(highlightAnnotation);
        }
        document.save(_dataDir + "sample_mod.pdf");
    }

    private static HighlightAnnotation HighLightTextFragment(Page page, TextFragment textFragment, Color color) {
        HighlightAnnotation ha;
        if (textFragment.getSegments().size() == 1) {
            ha = new HighlightAnnotation(page, textFragment.getSegments().get_Item(1).getRectangle());
            ha.setTitle("Aspose User");
            ha.setColor(color);
            ha.setModified(new Date());
            Rectangle rect = textFragment.getSegments().get_Item(1).getRectangle();
            ha.setQuadPoints(
                    new Point[] { new Point(rect.getLLX(), rect.getURY()), new Point(rect.getURX(), rect.getURY()),
                            new Point(rect.getLLX(), rect.getLLY()), new Point(rect.getURX(), rect.getLLY()) });
            return ha;
        }

        int offset = 0;
        Point[] quadPoints = new Point[textFragment.getSegments().size() * 4];
        for (TextSegment segment : textFragment.getSegments()) {
            Rectangle r = segment.getRectangle();
            quadPoints[offset + 0] = new Point(r.getLLX(), r.getURY());
            quadPoints[offset + 1] = new Point(r.getURX(), r.getURY());
            quadPoints[offset + 2] = new Point(r.getLLX(), r.getLLY());
            quadPoints[offset + 3] = new Point(r.getURX(), r.getLLY());
            offset += 4;
        }

        double llx = quadPoints[0].getX();
        double lly = quadPoints[0].getY();
        double urx = quadPoints[0].getX();
        double ury = quadPoints[0].getY();
        for (Point pt : quadPoints) {
            if (llx > pt.getX())
                llx = pt.getX();
            if (lly > pt.getY())
                lly = pt.getY();
            if (urx < pt.getX())
                urx = pt.getX();
            if (ury < pt.getY())
                ury = pt.getY();
        }
        ha = new HighlightAnnotation(page, new Rectangle(llx, lly, urx, ury));
        ha.setTitle("Aspose User");
        ha.setColor(color);
        ha.setModified(new Date());
        ha.setQuadPoints(quadPoints);
        return ha;
    }

    /// <summary>
    /// 강조 표시된 텍스트를 얻는 방법
    /// </summary>
    public static void GetHighlightedText() {
        // PDF 파일 로드
        Document document = new Document(_dataDir + "sample_mod.pdf");
        Page page = document.getPages().get_Item(1);

        AnnotationSelector annotationSelector1 = new AnnotationSelector(
                new HighlightAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector1);
        List<Annotation> highlightAnnotations = annotationSelector1.getSelected();
        for (Annotation ta : highlightAnnotations) {
            System.out.println("[" + ((HighlightAnnotation) ta).getMarkedText() + "]");
        }
    }
```


## 텍스트 마크업 주석 가져오기

PDF 문서에서 텍스트 마크업 주석을 가져오기 위해 다음 코드 스니펫을 사용해 보세요.

```java
     public static void GetTextMarkupAnnotation() {
        // PDF 파일 로드
        Document document = new Document(_dataDir + "sample_mod.pdf");
        Page page = document.getPages().get_Item(1);

        AnnotationSelector annotationSelector1 = new AnnotationSelector(
                new HighlightAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector1);
        AnnotationSelector annotationSelector2 = new AnnotationSelector(
                new SquigglyAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector2);

        List<Annotation> textMarkupAnnotations = annotationSelector1.getSelected();
        textMarkupAnnotations.addAll(annotationSelector2.getSelected());

        // 결과 출력
        for (Annotation ta : textMarkupAnnotations) {
            System.out.printf("[" + ta.getAnnotationType() + ta.getRect() + "]");
        }
    }
```


## 텍스트 마크업 주석 삭제

다음 코드 스니펫은 PDF 파일에서 텍스트 마크업 주석을 삭제하는 방법을 보여줍니다.

```java
   public static void DeleteTextMarkupAnnotation() {
        // PDF 파일 로드
        Document document = new Document(_dataDir + "sample_mod.pdf");
        Page page = document.getPages().get_Item(1);

        AnnotationSelector annotationSelector1 = new AnnotationSelector(
                new HighlightAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector1);
        AnnotationSelector annotationSelector2 = new AnnotationSelector(
                new SquigglyAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector2);

        List<Annotation> textMarkupAnnotations = annotationSelector1.getSelected();
        textMarkupAnnotations.addAll(annotationSelector2.getSelected());

        // 결과 출력
        for (Annotation ta : textMarkupAnnotations) {
            page.getAnnotations().delete(ta);
        }
        document.save(_dataDir + "sample_del.pdf");
    }
```