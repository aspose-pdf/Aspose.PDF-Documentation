---
title: PDF 스티커 주석
linktitle: 스티커 주석
type: docs
weight: 50
url: /ko/java/sticky-annotations/
description: 이 주제는 스티커 주석에 관한 것으로, 예시로 본문에서 워터마크 주석을 보여줍니다. 페이지에 그래픽을 나타내는 데 사용됩니다. 이 작업을 해결하기 위한 코드 스니펫을 확인하세요.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 워터마크 주석 추가

워터마크 주석은 인쇄된 페이지의 크기와 관계없이 페이지에 고정된 크기와 위치로 인쇄되어야 하는 그래픽을 나타내는 데 사용됩니다.

[WatermarkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/WatermarkAnnotation)을 사용하여 PDF 페이지의 특정 위치에 워터마크 텍스트를 추가할 수 있습니다. 워터마크의 불투명도는 불투명도 속성을 사용하여 제어할 수도 있습니다.

다음 코드 스니펫을 확인하여 WatermarkAnnotation을 추가하세요.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleWatermarkAnnotation {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddWaterMarkAnnotation()
    {
        // PDF 파일 로드
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        // 주석 생성
        WatermarkAnnotation wa = new WatermarkAnnotation(page, new Rectangle(100, 500, 400, 600));

        // 주석을 페이지의 주석 컬렉션에 추가
        page.getAnnotations().add(wa);

        // 폰트 설정을 위한 TextState 생성
        TextState ts = new TextState();

        ts.setForegroundColor(Color.getBlue());
        ts.setFont(FontRepository.findFont("Times New Roman"));
        ts.setFontSize(32);

        // 주석 텍스트의 불투명도 수준 설정
        wa.setOpacity(0.5);

        // 주석에 텍스트 추가
        wa.setTextAndState(new String[] { "Aspose.PDF", "Watermark", "Demo" }, ts);

        // 문서 저장
        document.save(_dataDir + "sample_watermark.pdf");
    }
}
```


## 워터마크 주석 가져오기

```java
    public static void GetWatermarkAnnotation() {
        // PDF 파일 로드
        Document document = new Document(_dataDir + "sample_watermark.pdf");

        // AnnotationSelector를 사용하여 주석 필터링
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new WatermarkAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> WatermarkAnnotations = annotationSelector.getSelected();

        // 결과 출력
        for (Annotation fa : WatermarkAnnotations) {
            System.out.println(fa.getRect());
        }
    }
```

## 워터마크 주석 삭제

```java
    public static void DeleteWatermarkAnnotation() {
         // PDF 파일 로드
         Document document = new Document(_dataDir + "sample_watermark.pdf");

         // AnnotationSelector를 사용하여 주석 필터링
         Page page = document.getPages().get_Item(1);
         AnnotationSelector annotationSelector = new AnnotationSelector(
                 new WatermarkAnnotation(page, Rectangle.getTrivial()));
         page.accept(annotationSelector);
         List<Annotation> WatermarkAnnotations = annotationSelector.getSelected();

         // 주석 삭제
         for (Annotation fa : WatermarkAnnotations) {
            page.getAnnotations().delete(fa);
        }
        document.save(_dataDir + "sample_watermark_del.pdf");
    }
```