---
title: Add Page Number to PDF 
linktitle: Add Page Number
type: docs
weight: 100
url: /java/add-page-number/
description: Aspose.PDF for Java를 사용하여 PageNumber Stamp 클래스를 사용하여 PDF 파일에 페이지 번호 스탬프를 추가할 수 있습니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

모든 문서에는 페이지 번호가 있어야 합니다. 페이지 번호는 독자가 문서의 다양한 부분을 쉽게 찾을 수 있도록 합니다.
**Aspose.PDF for Java**를 사용하면 PageNumberStamp로 페이지 번호를 추가할 수 있습니다.

{{% alert color="primary" %}}

온라인으로 시도해 보세요. 이 링크에서 Aspose.PDF 변환 품질을 확인하고 결과를 온라인으로 확인할 수 있습니다. [products.aspose.app/pdf/page-number](https://products.aspose.app/pdf/page-number)

{{% /alert %}}

[PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) 클래스를 사용하여 PDF 문서에 페이지 번호 스탬프를 추가할 수 있습니다.
 [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) 클래스는 형식, 여백, 정렬, 시작 번호 등과 같은 페이지 번호 기반 스탬프를 생성하는 메서드를 제공합니다. 페이지 번호 스탬프를 추가하기 위해서는 필요한 속성을 가진 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체와 [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) 객체를 생성해야 합니다. 그런 다음 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 클래스의 [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.Page#addStamp-com.aspose.pdf.Stamp-) 메서드를 호출하여 PDF 파일에 스탬프를 추가할 수 있습니다. 페이지 번호 스탬프의 글꼴 속성도 설정할 수 있습니다.

다음 코드 스니펫은 PDF 파일에 페이지 번호를 추가하는 방법을 보여줍니다.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.FontStyles;
import com.aspose.pdf.HorizontalAlignment;
import com.aspose.pdf.PageNumberStamp;

public class ExampleAddPageNumberToPDF {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExampleAddPageNumber() {

        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "PageNumberStamp.pdf");

        // 페이지 번호 스탬프 생성
        PageNumberStamp pageNumberStamp = new PageNumberStamp();

        // 스탬프가 배경인지 여부
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Page # of " + pdfDocument.getPages().size());
        pageNumberStamp.setBottomMargin(10);
        pageNumberStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        // 텍스트 속성 설정
        pageNumberStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize(14.0F);
        pageNumberStamp.getTextState().setFontStyle(FontStyles.Bold);        
        pageNumberStamp.getTextState().setForegroundColor(Color.getAqua());

        // 특정 페이지에 스탬프 추가
        pdfDocument.getPages().get_Item(1).addStamp(pageNumberStamp);

        _dataDir = _dataDir + "PageNumberStamp_out.pdf";
        // 출력 문서 저장
        pdfDocument.save(_dataDir);

    }
}
```