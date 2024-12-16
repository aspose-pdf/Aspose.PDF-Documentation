---
title: 프로그래밍 방식으로 PDF 페이지 자르기
linktitle: 페이지 자르기
type: docs
weight: 80
url: /ko/java/crop-pages/
description: Aspose.PDF for Java를 사용하여 너비, 높이, 블리드, 크롭 및 트림박스와 같은 페이지 속성을 가져올 수 있습니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 페이지 속성 가져오기

PDF 파일의 각 페이지에는 너비, 높이, 블리드, 크롭 및 트림박스와 같은 여러 속성이 있습니다. Aspose.PDF for Java를 사용하면 이러한 속성에 액세스할 수 있습니다.

- **미디어 박스**: 미디어 박스는 가장 큰 페이지 박스입니다. 이는 문서가 PostScript 또는 PDF로 인쇄될 때 선택된 페이지 크기(예: A4, A5, 미국 레터 등)에 해당합니다. 다시 말해, 미디어 박스는 PDF 문서가 표시되거나 인쇄되는 매체의 물리적 크기를 결정합니다.
- **블리드 박스**: 문서에 블리드가 있는 경우 PDF에도 블리드 박스가 포함됩니다.
 Bleed는 페이지의 가장자리를 넘어 확장되는 색상(또는 예술 작품)의 양입니다. 이는 문서가 인쇄되고 크기에 맞게 잘릴 때("트림") 잉크가 페이지의 가장자리까지 도달하도록 보장하기 위해 사용됩니다. 페이지가 잘못 잘리더라도 - 트림 표시에서 약간 벗어나게 잘리더라도 - 페이지에 흰색 가장자리가 나타나지 않습니다.
- **Trim box**: 트림 박스는 인쇄 및 트림 후 문서의 최종 크기를 나타냅니다.
- **Art box**: 아트 박스는 문서의 실제 페이지 내용 주위에 그려진 박스입니다. 이 페이지 박스는 다른 응용 프로그램에서 PDF 문서를 가져올 때 사용됩니다.
- **Crop box**: 크롭 박스는 Adobe Acrobat에서 PDF 문서가 표시되는 "페이지" 크기입니다. 일반 보기에서는 Adobe Acrobat에서 크롭 박스의 내용만 표시됩니다. 이러한 속성에 대한 자세한 설명은 Adobe.Pdf 사양, 특히 10.10.1 페이지 경계를 참조하십시오.
- **Page.Rect**: MediaBox와 DropBox의 교차점(일반적으로 보이는 직사각형)입니다. 아래 그림은 이러한 속성을 설명합니다.  
자세한 내용은 [이 페이지](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)를 방문하십시오.

아래 스니펫은 페이지를 자르는 방법을 보여줍니다:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleCropPages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    // 문서 열기
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    public static void CropPagesPDF() {
        Document pdfDocument = new Document("crop_page.pdf");
        Page page = pdfDocument.getPages().get_Item(1);

        System.out.println(page.getCropBox());
        System.out.println(page.getTrimBox());
        System.out.println(page.getArtBox());
        System.out.println(page.getBleedBox());
        System.out.println(page.getMediaBox());

        // 새로운 박스 사각형 생성
        Rectangle newBox = new Rectangle(200, 220, 2170, 1520);

        page.setCropBox(newBox);
        page.setTrimBox(newBox);
        page.setArtBox(newBox);
        page.setBleedBox(newBox);

        // 출력 문서 저장
        pdfDocument.save(_dataDir + "crop_page_modified.pdf");
    }
}
```

In this example we used a sample file [here](crop_page.pdf). Initially our page looks like shown on the Figure 1.  
이 예제에서는 [여기](crop_page.pdf)에서 샘플 파일을 사용했습니다. 초기에는 페이지가 그림 1과 같이 보입니다.  
![Figure 1. Cropped Page](crop_page.png)  

After the change, the page will look like Figure 2.  
변경 후 페이지는 그림 2와 같이 보일 것입니다.  
![Figure 2. Cropped Page](crop_page2.png)