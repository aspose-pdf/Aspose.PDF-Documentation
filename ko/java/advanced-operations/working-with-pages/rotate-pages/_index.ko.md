---
title: PDF 페이지 회전 프로그래밍
linktitle: PDF 페이지 회전
type: docs
weight: 60
url: /java/rotate-pages/
description: 페이지 방향 변경 및 페이지 내용을 새로운 페이지 방향에 맞추기 위한 Java 사용법.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 페이지 방향 변경

이 문서에서는 기존 PDF 파일의 페이지 방향을 업데이트하거나 변경하는 방법을 설명합니다.

Aspose.PDF for Java는 페이지 방향을 가로에서 세로로 또는 그 반대로 변경하는 기능을 제공합니다. 페이지 방향을 변경하려면 다음 코드 스니펫을 사용하여 페이지의 [MediaBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#setMediaBox-com.aspose.pdf.Rectangle-)를 설정합니다.

Rotate() 메서드를 사용하여 회전 각도를 설정하여 페이지 방향을 변경할 수도 있습니다.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleRotatePDFPages  {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RotatePages() {
        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "sample2.pdf");

        for (Page page : pdfDocument.getPages())
        {            
            // Rectangle r = page.getMediaBox();
            // double newHeight = r.getWidth();
            // double newWidth = r.getHeight();
            // double newLLX = r.getLLX();
            // // 페이지 크기 변경을 보상하기 위해 페이지를 위로 이동해야 합니다
            // // (페이지의 하단 가장자리는 0,0이고 정보는 일반적으로 페이지의
            // //  상단에서 배치됩니다. 따라서 이전 높이와 새로운 높이의 차이만큼
            // //  하단 가장자리를 위로 이동합니다.
            // double newLLY = r.getLLY() + (r.getHeight() - newHeight);
            // page.setMediaBox (new Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));
            // // 원본 파일에 설정된 경우 CropBox를 설정해야 할 때가 있습니다.
            // page.setCropBox(new Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));

            // 페이지 회전 각도 설정
            page.setRotate(Rotation.on90);
        }

        _dataDir = _dataDir + "ChangeOrientation_out.pdf";
        // 출력 파일 저장
        pdfDocument.save(_dataDir);
    }    
}
```