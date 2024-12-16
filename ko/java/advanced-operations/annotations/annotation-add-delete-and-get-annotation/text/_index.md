---
title: PDF 텍스트 주석
Texttitle: 텍스트 주석
type: docs
weight: 10
url: /ko/java/text-annotation/
description: Aspose.PDF for Java를 사용하여 PDF 문서에서 텍스트 주석을 추가, 가져오기 및 삭제할 수 있습니다.
lastmod: "2021-11-24"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

텍스트 주석을 추가, 삭제 및 가져오는 것은 다양한 종류의 주석에 대해 유사합니다. 텍스트 주석을 예로 들어보겠습니다.

## 기존 PDF 파일에 텍스트 주석을 추가하는 방법

이 튜토리얼에서는 기존 PDF 문서에 텍스트를 추가하는 방법을 배웁니다. 텍스트 도구를 사용하면 문서의 어느 위치에나 텍스트를 추가할 수 있습니다. 텍스트 주석은 PDF 문서의 특정 위치에 첨부된 주석입니다. 닫힌 상태에서는 주석이 아이콘으로 표시되며, 열리면 읽는 사람이 선택한 글꼴과 크기로 메모 텍스트를 포함하는 팝업 창이 표시되어야 합니다.

주석은 특정 페이지의 [Annotations](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection) 컬렉션에 포함되어 있습니다.
 이 컬렉션은 해당 개별 페이지에 대한 주석만 포함합니다. 각 페이지는 고유한 주석 컬렉션을 가지고 있습니다.

특정 페이지에 주석을 추가하려면 Add 메서드를 사용하여 해당 페이지의 주석 컬렉션에 추가하십시오.

1. 먼저, PDF에 추가할 주석을 만듭니다.
1. 그런 다음 입력 PDF를 엽니다.
1. [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 객체의 주석 컬렉션에 주석을 추가합니다.

다음 코드 스니펫은 PDF 페이지에 주석을 추가하는 방법을 보여줍니다.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleTextAnnotation {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void AddTextAnnotation()
    {
        // PDF 파일 로드
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);
        Rectangle rect = new Rectangle(200, 750, 400, 790);
        TextAnnotation textAnnotation = new TextAnnotation(page, rect);

        textAnnotation.setTitle("Aspose User");
        textAnnotation.setSubject("Sample Subject");
        textAnnotation.setState (AnnotationState.Accepted);
        textAnnotation.setContents("주석에 대한 샘플 내용");
        textAnnotation.setOpen(true);
        textAnnotation.setIcon(TextIcon.Circle);

        Border border = new Border(textAnnotation);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        textAnnotation.setBorder(border);
        textAnnotation.setRect(rect);

        page.getAnnotations().add(textAnnotation);
        document.save(_dataDir + "sample_textannot.pdf");
    }
}
```

## 새 자유 텍스트 주석 추가 (또는 생성)

자유 텍스트 주석은 페이지에 직접 텍스트를 표시합니다. PdfContentEditor.CreateFreeText 메서드는 이러한 유형의 주석을 생성할 수 있도록 합니다. 다음 코드 조각에서는 문자열의 첫 번째 발생 위에 자유 텍스트 주석을 추가합니다.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleFreeTextAnnotation {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void AddFreeTextAnnotation()
    {
        // PDF 파일 로드
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        DefaultAppearance defaultAppearance = new DefaultAppearance();
        defaultAppearance.setFontName("Helvetica");
        defaultAppearance.setFontSize(12);
        defaultAppearance.setTextColor(java.awt.Color.BLUE);

        FreeTextAnnotation freeTextAnnotation = new FreeTextAnnotation(page, new Rectangle(300.0, 770.0, 400.0, 790.0), defaultAppearance);

        freeTextAnnotation.setRichText("자유 텍스트 데모");
        page.getAnnotations().add(freeTextAnnotation);
        document.save(_dataDir + "sample_freetext.pdf");
    }
}
```


## 무료 텍스트 주석 가져오기

Aspose.PDF for Java를 사용하면 PDF 문서에서 무료 텍스트 주석을 가져올 수 있습니다.

다음 코드 스니펫을 확인하여 이 작업을 해결하세요:

```java
public static void GetFreeTextAnnotation() {
        // PDF 파일 로드
        Document document = new Document(_dataDir + "sample_freetext.pdf");

        // AnnotationSelector를 사용하여 주석 필터링
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new FreeTextAnnotation(page, Rectangle.getTrivial(), new DefaultAppearance()));
        page.accept(annotationSelector);
        List<Annotation> freeTextAnnotations = annotationSelector.getSelected();

        // 결과 출력
        for (Annotation fa : freeTextAnnotations) {
            System.out.println(fa.getRect());
        }
    }
```

## 무료 텍스트 주석 삭제

Aspose.PDF for Java를 사용하면 PDF 문서에서 무료 텍스트 주석을 삭제할 수 있습니다.

다음 코드 스니펫을 확인하여 이 작업을 해결하세요:

```java
  public static void DeleteFreeTextAnnotation() {
         // PDF 파일을 로드합니다
         Document document = new Document(_dataDir + "sample_freetext.pdf");

         // AnnotationSelector를 사용하여 주석을 필터링합니다
         Page page = document.getPages().get_Item(1);
         AnnotationSelector annotationSelector = new AnnotationSelector(
                 new FreeTextAnnotation(page, Rectangle.getTrivial(), new DefaultAppearance()));
         page.accept(annotationSelector);
         List<Annotation> freeTextAnnotations = annotationSelector.getSelected();

         // 주석을 삭제합니다
         for (Annotation fa : freeTextAnnotations) {
            page.getAnnotations().delete(fa);
        }
        document.save(_dataDir + "sample_freetext_del.pdf");
    }
```

## PDF 파일 페이지에서 모든 주석 삭제하기

[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 객체의 [AnnotationCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection) 컬렉션에는 해당 페이지의 모든 주석이 포함되어 있습니다.
 페이지에서 모든 주석을 삭제하려면 AnnotationCollection 컬렉션의 *Delete* 메서드를 호출하십시오.

다음 코드 스니펫은 특정 페이지에서 모든 주석을 삭제하는 방법을 보여줍니다.

```java
    public static void DeleteTextAnnotation() {
         // PDF 파일 로드
         Document document = new Document(_dataDir + "sample_textannot.pdf");

         // AnnotationSelector를 사용하여 주석 필터링
         Page page = document.getPages().get_Item(1);
         AnnotationSelector annotationSelector = new AnnotationSelector(
                 new TextAnnotation(page, Rectangle.getTrivial()));
         page.accept(annotationSelector);
         List<Annotation> TextAnnotations = annotationSelector.getSelected();

         // 주석 삭제
         for (Annotation fa : TextAnnotations) {
            page.getAnnotations().delete(fa);
        }
        document.save(_dataDir + "sample_textannot_del.pdf");
    }
```

## PDF 문서 페이지에서 모든 주석 가져오기

Aspose.PDF는 전체 문서 또는 특정 페이지에서 주석을 가져올 수 있도록 합니다. 페이지에서 PDF 문서의 모든 주석을 가져오려면 원하는 페이지 리소스의 [AnnotationCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection) 컬렉션을 통해 반복합니다. 다음 코드 스니펫은 페이지의 모든 주석을 가져오는 방법을 보여줍니다.

```java
  public static void GetTextAnnotation() {
        // PDF 파일 로드
        Document document = new Document(_dataDir + "sample_textannot.pdf");

        // AnnotationSelector를 사용하여 주석 필터링
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new TextAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> TextAnnotations = annotationSelector.getSelected();

        // 결과 출력
        for (Annotation fa : TextAnnotations) {
            System.out.println(fa.getRect());
        }
    }
```