---
title: PDF 파일에서 이미지 삭제
linktitle: 이미지 삭제
type: docs
weight: 20
url: /java/delete-images-from-pdf-file/
description: 이 섹션에서는 Aspose.PDF for Java를 사용하여 PDF 파일에서 이미지를 삭제하는 방법을 설명합니다.
lastmod: "2021-06-05"
---

PDF 파일에서 이미지를 삭제하려면 Images 컬렉션의 delete(..) 메서드를 사용하세요.

1. Document 객체를 생성하고 입력 PDF 파일을 엽니다.
1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 컬렉션에서 이미지를 포함한 페이지를 가져옵니다.
1. 이미지는 페이지의 [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) 컬렉션에 있는 Images 컬렉션에 저장됩니다.
1. Images 컬렉션의 Delete 메서드를 사용하여 이미지를 삭제합니다.
1. Document 객체의 Save 메서드를 사용하여 출력 파일을 저장합니다.

다음 코드 스니펫은 PDF 파일에서 이미지를 삭제하는 방법을 보여줍니다.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.FontStyles;
import com.aspose.pdf.HorizontalAlignment;
import com.aspose.pdf.PageNumberStamp;

public class ExampleDeleteImages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExampleAddPageNumber() {

        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "PageNumberStamp.pdf");

        // 페이지 번호 스탬프 생성
        PageNumberStamp pageNumberStamp = new PageNumberStamp();

        // 스탬프가 배경인지 여부
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Page # of " + pdfDocument.getPages().size());
        pageNumberStamp.setBottomMargin (10);
        pageNumberStamp.setHorizontalAlignment ( HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        // 텍스트 속성 설정
        pageNumberStamp.getTextState().setFont (FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize (14.0F);
        pageNumberStamp.getTextState().setFontStyle (FontStyles.Bold);        
        pageNumberStamp.getTextState().setForegroundColor (Color.getAqua());

        // 특정 페이지에 스탬프 추가
        pdfDocument.getPages().get_Item(1).addStamp(pageNumberStamp);

        _dataDir = _dataDir + "PageNumberStamp_out.pdf";
        // 출력 문서 저장
        pdfDocument.save(_dataDir);

    }
}
```