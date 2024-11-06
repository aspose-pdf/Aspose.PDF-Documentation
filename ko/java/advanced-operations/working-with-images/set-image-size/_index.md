---
title: 이미지 크기 설정
linktitle: 이미지 크기 설정
type: docs
weight: 80
url: ko/java/set-image-size/
description: 이 섹션은 Java 라이브러리를 사용하여 PDF 파일의 이미지 크기를 설정하는 방법을 설명합니다.
lastmod: "2021-06-05"
---

PDF 파일에 추가되는 이미지의 크기를 설정할 수 있습니다. 크기를 설정하기 위해 com.aspose.pdf.Image 클래스의 [setFixWidth](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image#setFixWidth-double-) 및 [setFixHeight](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image#setFixHeight-double-) 메서드를 사용할 수 있습니다.

다음 코드 스니펫은 이미지의 크기를 설정하는 방법을 보여줍니다:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleSetImageSize {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Replace() {
        // Document 객체 인스턴스화
        Document doc = new Document();
        // PDF 파일의 페이지 컬렉션에 페이지 추가
        Page page = doc.getPages().add();
        // 이미지 인스턴스 생성
        Image img = new Image();
        // 포인트 단위로 이미지 너비와 높이 설정
        img.setFixWidth (100);
        img.setFixHeight (100);
        // 이미지 형식을 SVG로 설정
        img.setFileType (ImageFileType.Svg);
        // 소스 파일 경로
        img.setFile (_dataDir + "aspose-logo.jpg");
        page.getParagraphs().add(img);
        // 페이지 속성 설정
        page.getPageInfo().setWidth(800);
        page.getPageInfo().setHeight(800);        
        // 결과 PDF 파일 저장
        doc.save(_dataDir + "SetImageSize_out.pdf");
    }
}
```