---
title: 복잡한 PDF 생성
linktitle: 복잡한 PDF 생성
type: docs
weight: 60
url: /java/complex-pdf-example/
description: Aspose.PDF for Java는 하나의 문서에 이미지, 텍스트 조각, 표가 포함된 보다 복잡한 문서를 작성할 수 있도록 합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

[Hello, World](/pdf/java/hello-world-example/) 예제에서는 Java와 Aspose.PDF를 사용하여 PDF 문서를 생성하는 간단한 단계를 보여주었습니다. 이 기사에서는 Java와 Aspose.PDF for Java를 사용하여 보다 복잡한 문서를 만드는 방법을 살펴보겠습니다. 예를 들어, 여객 페리 서비스를 운영하는 가상의 회사의 문서를 가져옵니다.  
우리 문서는 이미지, 두 개의 텍스트 조각(헤더 및 단락), 및 하나의 표를 포함할 것입니다. 이러한 문서를 작성하기 위해 DOM 기반 접근 방식을 사용할 것입니다. [DOM API의 기초](/pdf/java/basics-of-dom-api/) 섹션에서 더 읽어볼 수 있습니다.

문서를 처음부터 작성하려면 특정 단계를 따라야 합니다:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) 객체를 인스턴스화합니다. 이 단계에서는 메타데이터가 포함된 빈 PDF 문서를 생성하지만 페이지는 포함되지 않습니다.
1. 문서 객체에 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page)를 추가합니다. 이제 문서에 한 페이지가 포함됩니다.
1. [Image](https://reference.aspose.com/pdf/java/com.aspose.pdf/image)를 추가합니다. 이것은 PDF 연산자와의 저수준 작업을 기반으로 하는 복잡한 작업입니다.
    - 스트림에서 이미지 로드
    - 페이지 리소스의 Images 컬렉션에 이미지 추가
    - GSave 연산자 사용: 이 연산자는 현재 그래픽 상태를 저장합니다.
    - [Matrix](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/) 객체를 생성합니다.
    - ConcatenateMatrix 연산자 사용: 이미지가 배치되어야 하는 방식을 정의합니다.
    - Do 연산자 사용: 이 연산자는 이미지를 그립니다.
    - GRestore 연산자 사용: 이 연산자는 그래픽 상태를 복원합니다.

1. 헤더를 위한 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment)를 만듭니다. 헤더에는 Arial 폰트를 사용하고 폰트 크기는 24pt, 가운데 정렬을 사용할 것입니다.
1. 헤더를 페이지의 [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--)에 추가합니다.
1. 설명을 위한 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment)를 만듭니다. 설명에는 Arial 폰트를 사용하고 폰트 크기는 24pt, 가운데 정렬을 사용할 것입니다.
1. (설명)을 페이지의 Paragraphs에 추가합니다.
1. 테이블을 만들고 테이블 속성을 추가합니다.
1. (테이블)을 페이지의 [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--)에 추가합니다.
1. 문서를 "Complex.pdf"로 저장합니다.

```java
package com.aspose.pdf.examples;

/**
 * 복잡한 예제
 */

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.Duration;
import java.time.LocalTime;

import com.aspose.pdf.*;
import com.aspose.pdf.operators.ConcatenateMatrix;
import com.aspose.pdf.operators.Do;
import com.aspose.pdf.operators.GRestore;
import com.aspose.pdf.operators.GSave;

public final class ComplexExample {

    private ComplexExample() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/");

    public static void main(String[] args) throws FileNotFoundException {
        // 문서 객체 초기화
        Document document = new Document();
        // 페이지 추가
        Page page = document.getPages().add();

        // -------------------------------------------------------------
        // 이미지 추가
        Path imageFileName = Paths.get(_dataDir.toString(),"logo.png");
        java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File(imageFileName.toString()));
        // 이미지 페이지 리소스의 이미지 컬렉션에 추가
        page.getResources().getImages().add(imageStream);

        // GSave 연산자 사용: 이 연산자는 현재 그래픽 상태를 저장합니다
        page.getContents().add(new GSave());
        Rectangle _logoPlaceHolder = new Rectangle(20, 730, 120, 830);

        // Matrix 객체 생성
        Matrix matrix = new Matrix(new double[] {
            _logoPlaceHolder.getURX() - _logoPlaceHolder.getLLX(), 0, 0,
            _logoPlaceHolder.getURY() - _logoPlaceHolder.getLLY(),
            _logoPlaceHolder.getLLX(), _logoPlaceHolder.getLLY() });

        // ConcatenateMatrix (행렬 결합) 연산자 사용: 이미지가 배치되는 방법 정의
        page.getContents().add(new ConcatenateMatrix(matrix));
        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
        // Do 연산자 사용: 이 연산자는 이미지를 그립니다
        page.getContents().add(new Do(ximage.getName()));
        // GRestore 연산자 사용: 이 연산자는 그래픽 상태를 복원합니다
        page.getContents().add(new GRestore());

        // -------------------------------------------------------------
        // 헤더 추가
        TextFragment header = new TextFragment("2020년 가을 새로운 페리 노선");
        header.getTextState().setFont(FontRepository.findFont("Arial"));
        header.getTextState().setFontSize(24);
        header.setHorizontalAlignment (HorizontalAlignment.Center);
        header.setPosition(new Position(130, 720));
        page.getParagraphs().add(header);

        // 설명 추가
        String descriptionText = "방문자는 온라인으로 티켓을 구매해야 하며, 티켓은 하루에 5,000장으로 제한됩니다. 페리 서비스는 절반의 수용력으로 운영되며, 일정이 축소되었습니다. 대기열을 예상하세요.";
        TextFragment description = new TextFragment(descriptionText);
        description.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        description.getTextState().setFontSize(14);
        description.setHorizontalAlignment(HorizontalAlignment.Left);
        page.getParagraphs().add(description);


        // 테이블 추가
        Table table = new Table();
        table.setColumnWidths("200");
        table.setBorder(new BorderInfo(BorderSide.Box, 1f, Color.getDarkSlateGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.Box, 0.5f, Color.getBlack()));
        table.getMargin().setBottom(10);
        table.getDefaultCellTextState().setFont(FontRepository.findFont("Helvetica"));

        Row headerRow = table.getRows().add();
        headerRow.getCells().add("출발 도시");
        headerRow.getCells().add("출발 섬");

        for (Cell headerRowCell : headerRow.getCells())
        {
            headerRowCell.setBackgroundColor(Color.getGray());
            headerRowCell.getDefaultCellTextState().setForegroundColor(Color.getWhiteSmoke());
        }

        LocalTime time = LocalTime.of(6,0);
        Duration incTime = Duration.ofMinutes(30);

        for (int i = 0; i < 10; i++)
        {
            Row dataRow = table.getRows().add();
            dataRow.getCells().add(time.toString());
            time=time.plus(incTime);
            dataRow.getCells().add(time.toString());
        }

        page.getParagraphs().add(table);

        document.save(Paths.get(_dataDir.toString(), "Complex.pdf").toString());
    }

}
```