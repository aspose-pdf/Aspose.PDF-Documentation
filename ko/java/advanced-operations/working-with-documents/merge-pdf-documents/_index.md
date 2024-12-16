---
title: PDF 병합 프로그래밍
linktitle: PDF 파일 병합
type: docs
weight: 50
url: /ko/java/merge-pdf-documents/
description: 이 페이지는 Java를 사용하여 PDF 문서를 하나의 PDF 파일로 병합하는 방법을 설명합니다.
lastmod: "2021-06-05"
---

이제 PDF 파일 병합은 가장 수요가 많은 작업 중 하나입니다.
이 문서는 Aspose.PDF for Java를 사용하여 여러 PDF 파일을 하나의 PDF 문서로 병합하는 방법을 보여줍니다. 예제는 Java로 작성되었지만, API는 다른 프로그래밍 언어에서도 사용할 수 있습니다. PDF 파일은 첫 번째 파일이 다른 문서의 끝에 추가되는 방식으로 병합됩니다.

## Java를 사용하여 PDF 파일 병합

{{% alert color="primary" %}}

Aspose.PDF를 사용하여 PDF 파일을 병합하고 이 링크에서 결과를 온라인으로 확인할 수 있습니다: [products.aspose.app/pdf/merger](https://products.aspose.app/pdf/merger)

{{% /alert %}}

두 개의 PDF 파일을 연결하려면:

1. 각각 하나의 입력 PDF 파일을 포함하는 두 개의 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document) 객체를 생성합니다.

1. 그런 다음 다른 PDF 파일을 추가할 Document 객체에 대해 [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) 컬렉션의 Add 메서드를 호출합니다.
1. 두 번째 Document 객체의 PageCollection 컬렉션을 첫 번째 PageCollection 컬렉션의 Add 메서드에 전달합니다.
1. 마지막으로 Save 메서드를 사용하여 출력 PDF 파일을 저장합니다.

다음 코드 스니펫은 Java로 PDF 파일을 연결하는 방법을 보여줍니다.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleMerge {
    // 문서 디렉토리 경로
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Merge() {
        
        // 첫 번째 문서 열기
        Document pdfDocument1 = new Document(_dataDir + "Concat1.pdf");
        // 두 번째 문서 열기
        Document pdfDocument2 = new Document(_dataDir + "Concat2.pdf");

        // 두 번째 문서의 페이지를 첫 번째 문서에 추가
        pdfDocument1.getPages().add(pdfDocument2.getPages());

        // 연결된 출력 파일 저장
        pdfDocument1.save(_dataDir+"ConcatenatePdfFiles_out.pdf");

    }

}
```