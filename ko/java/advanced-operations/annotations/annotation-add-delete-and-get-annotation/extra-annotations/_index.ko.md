---
title: 추가 유형의 PDF 주석 사용
linktitle: 추가 주석
type: docs
weight: 60
url: /java/extra-annotations/
description: 이 섹션에서는 PDF 문서에 추가 유형의 주석을 추가하고, 가져오고, 삭제하는 방법을 설명합니다.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 기존 PDF 파일에 Caret Annotation 추가하는 방법

Caret Annotation은 텍스트 편집을 나타내는 기호입니다. Caret Annotation은 또한 마크업 주석이므로, Caret 클래스는 Markup 클래스에서 파생되며 Caret Annotation의 속성을 가져오거나 설정하는 함수와 Caret Annotation의 모양 흐름을 재설정하는 기능을 제공합니다.

Caret 주석을 만드는 단계:

1. PDF 파일 로드 - 새로운 [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. 새 [Caret Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/CaretAnnotation)을 만들고 Caret 매개변수(새 Rectangle, 제목, 주제, 플래그, 색상, 너비, 시작 스타일 및 종료 스타일)를 설정합니다. 이 주석은 텍스트 삽입을 나타내는 데 사용됩니다.
1. 새 [StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/StrikeOutAnnotation)을 만들고 매개변수(새 Rectangle, 제목, 색상, 새 QuadPoints 및 새 포인트, 주제, InReplyTo, ReplyType)를 설정합니다.
1. 이후 페이지에 주석을 추가할 수 있습니다.

다음 코드 스니펫은 PDF 파일에 Caret Annotation을 추가하는 방법을 보여줍니다:

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleCaretAnnotation {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddCaretAnnotation() {
        // PDF 파일을 로드합니다
        Document document = new Document(_dataDir + "sample.pdf");
        // 이 주석은 텍스트 삽입을 나타내는 데 사용됩니다
        CaretAnnotation caretAnnotation1 = new CaretAnnotation(
                document.getPages().get_Item(1), new Rectangle(299.988, 713.664, 308.708, 720.769));
        caretAnnotation1.setTitle("Aspose User");
        caretAnnotation1.setSubject("Inserted text 1");
        caretAnnotation1.setFlags(AnnotationFlags.Print);
        caretAnnotation1.setColor(Color.getBlue());

        // 이 주석은 텍스트 교체를 나타내는 데 사용됩니다
        CaretAnnotation caretAnnotation2 = new CaretAnnotation(
                document.getPages().get_Item(1), new Rectangle(361.246, 727.908, 370.081, 735.107));

        caretAnnotation2.setTitle("Aspose User");
        caretAnnotation2.setFlags(AnnotationFlags.Print);
        caretAnnotation2.setSubject("Inserted text 2");
        caretAnnotation2.setColor(Color.getBlue());

        StrikeOutAnnotation strikeOutAnnotation = new StrikeOutAnnotation(
                document.getPages().get_Item(1), new Rectangle(318.407, 727.826, 368.916, 740.098));

        strikeOutAnnotation.setColor(Color.getBlue());
        strikeOutAnnotation.setQuadPoints(new Point[] { new Point(321.66, 739.416),
                new Point(365.664, 739.416), new Point(321.66, 728.508),
                new Point(365.664, 728.508) });

        strikeOutAnnotation.setSubject("Cross-out");
        strikeOutAnnotation.setInReplyTo(caretAnnotation2);
        strikeOutAnnotation.setReplyType(ReplyType.Group);

        document.getPages().get_Item(1).getAnnotations().add(caretAnnotation1);
        document.getPages().get_Item(1).getAnnotations().add(caretAnnotation2);
        document.getPages().get_Item(1).getAnnotations().add(strikeOutAnnotation);

        document.save(_dataDir + "sample_caret.pdf");

    }
```


## 캐럿 주석 가져오기

PDF 문서에서 캐럿 주석을 가져오기 위해 다음 코드 스니펫을 사용해 보세요.

```java
    public static void GetCaretAnnotation() {
        // PDF 파일 로드
        Document document = new Document(_dataDir + "sample_caret.pdf");

        // AnnotationSelector를 사용하여 주석 필터링
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CaretAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> caretAnnotations = annotationSelector.getSelected();

        // 결과 출력
        for (Annotation ca : caretAnnotations) {
            System.out.println(ca.getRect());
        }
    }
```

## 캐럿 주석 삭제

다음 코드 스니펫은 PDF 파일에서 캐럿 주석을 삭제하는 방법을 보여줍니다.

```java
public static void DeleteCaretAnnotation() {
        // PDF 파일 로드
        Document document = new Document(_dataDir + "sample_caret.pdf");

        // AnnotationSelector를 사용하여 주석 필터링
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CaretAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> caretAnnotations = annotationSelector.getSelected();

        // 주석 삭제
        for (Annotation ca : caretAnnotations) {
            document.getPages().get_Item(1).getAnnotations().delete(ca);
        }
        document.save(_dataDir + "sample_caret_del.pdf");
    }
```


A [Link Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation)은 문서의 다른 곳으로 이동하거나 수행할 작업으로 연결되는 하이퍼텍스트 링크입니다.

## 링크 주석 추가

링크는 페이지 어디에나 배치할 수 있는 직사각형 영역입니다. 각 링크에는 해당하는 PDF 작업이 연결되어 있습니다. 이 작업은 사용자가 이 링크 영역을 클릭할 때 수행됩니다.

다음 코드 스니펫은 전화번호 예제를 사용하여 PDF 파일에 링크 주석을 추가하는 방법을 보여줍니다:

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleLinkAnnotation {

    // 문서 디렉터리 경로입니다.

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddLinkAnnotation() {
        try {
            // PDF 파일 로드
            Document document = new Document(_dataDir + "SimpleResume.pdf");
            Page page = document.getPages().get_Item(1);

            // 전화번호를 찾기 위한 TextFragmentAbsorber 객체 생성
            TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("678-555-0103");

            // 1페이지에 대해서만 흡수기 승인
            page.accept(textFragmentAbsorber);

            TextFragment phoneNumberFragment = textFragmentAbsorber.getTextFragments().get_Item(1);

            // 링크 주석 생성 및 전화번호 호출 작업 설정
            LinkAnnotation linkAnnotation = new LinkAnnotation(page, phoneNumberFragment.getRectangle());
            linkAnnotation.setAction(new GoToURIAction("callto:678-555-0103"));

            // 페이지에 주석 추가
            page.getAnnotations().add(linkAnnotation);
            document.save(_dataDir + "SimpleResume_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```


## 링크 주석 가져오기

다음 코드 스니펫을 사용하여 PDF 문서에서 LinkAnnotation을 가져보세요.

```java
    public static void GetLinkAnnotations() {

        // PDF 파일 로드
        Document document = new Document(_dataDir + "SimpleResume_mod.pdf");

        // AnnotationSelector를 사용하여 주석 필터링
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> linkAnnotations = annotationSelector.getSelected();

        // 결과 출력
        for (Annotation la : linkAnnotations) {

            LinkAnnotation l = (LinkAnnotation) la;

            // 각 링크 주석의 URL 출력
            System.out.println("URI: " + ((GoToURIAction) l.getAction()).getURI());

            TextAbsorber absorber = new TextAbsorber();
            absorber.getTextSearchOptions().setLimitToPageBounds(true);
            absorber.getTextSearchOptions().setRectangle(l.getRect());
            page.accept(absorber);

            String extractedText = absorber.getText();

            // 하이퍼링크와 연결된 텍스트 출력
            System.out.println(extractedText);
        }
    }
```


## 링크 주석 삭제

다음 코드 스니펫은 PDF 파일에서 링크 주석을 삭제하는 방법을 보여줍니다. 이를 위해 1페이지에 있는 모든 링크 주석을 찾아 제거해야 합니다. 그 후에 주석이 제거된 문서를 저장할 것입니다.

```java
    public static void DeleteLinkAnnotations() {
        // PDF 파일 로드
        Document document = new Document(_dataDir + "SimpleResume_mod.pdf");

        // AnnotationSelector를 사용하여 주석 필터링
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> linkAnnotations = annotationSelector.getSelected();

        for (Annotation la : linkAnnotations)
            page.getAnnotations().delete(la);

        // 주석이 제거된 문서 저장
        document.save(_dataDir + "SimpleResume_del.pdf");
    }
```

## Aspose.PDF for Java를 사용하여 특정 페이지 영역을 Redaction Annotation으로 수정

Aspose.PDF for Java는 기존 PDF 파일에 주석을 추가하고 조작하는 기능을 지원합니다. 최근 일부 고객들이 PDF 문서의 특정 페이지 영역에서 텍스트, 이미지 등을 제거(편집)해야 한다는 요구를 게시했습니다. 이 요구를 충족하기 위해 RedactionAnnotation이라는 클래스가 제공되며, 이 클래스를 사용하여 특정 페이지 영역을 편집하거나 기존 RedactionAnnotations를 조작하고 이를 편집(즉, 주석을 평탄화하고 그 아래의 텍스트를 제거)할 수 있습니다.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfAnnotationEditor;

public class ExampleRedactAnnotation {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RedactionAnnotation() {

        // 문서 열기
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        // 특정 페이지 영역에 대한 RedactionAnnotation 인스턴스 생성
        RedactionAnnotation annot = new RedactionAnnotation(page, new Rectangle(200, 500, 300, 600));
        annot.setFillColor(Color.getGreen());
        annot.setBorderColor(Color.getYellow());
        annot.setColor(Color.getBlue());

        // 편집 주석에 인쇄될 텍스트
        annot.setOverlayText("REDACTED");
        annot.setTextAlignment(HorizontalAlignment.Center);

        // 편집 주석에 오버레이 텍스트 반복
        annot.setRepeat(true);

        // 주석을 첫 페이지의 주석 컬렉션에 추가
        page.getAnnotations().add(annot);

        // 주석을 평탄화하고 페이지 내용을 편집(즉, 편집된 주석 아래의 텍스트 및 이미지 제거)
        annot.redact();
        document.save(_dataDir + "RedactPage_out.pdf");
    }
```


## Facades 접근 방식

Aspose.PDF.Facades 네임스페이스에는 PDF 파일 내의 기존 주석을 조작하는 기능을 제공하는 [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor)라는 클래스도 있습니다. 이 클래스는 특정 페이지 영역을 제거할 수 있는 [RedactArea(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Redaction#getredactArea-com.aspose.pdf.Page-com.aspose.pdf.Rectangle-java.awt.Color-)라는 메서드를 포함하고 있습니다.

```java
    public static void RedactionAnnotationFacades(){
        PdfAnnotationEditor editor = new PdfAnnotationEditor();

        editor.bindPdf(_dataDir + "sample.pdf");

        // 특정 페이지 영역 삭제
        editor.redactArea(1, new Rectangle(100, 100, 20, 70), java.awt.Color.white);
        editor.bindPdf(_dataDir + "sample.pdf");
        editor.save( _dataDir + "FacadesApproach_out.pdf");
    }
```