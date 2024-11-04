---
title: PDF에서 표 데이터 추출 
linktitle: 표 데이터 추출
type: docs
weight: 40
url: /java/extract-data-from-table-in-pdf/
description: Aspose.PDF for Java를 사용하여 PDF에서 표 형식을 추출하는 방법을 배웁니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 프로그래밍 방식으로 PDF에서 표 추출하기

PDF에서 표를 추출하는 것은 간단하지 않은 작업입니다. 왜냐하면 표는 다양한 방식으로 생성될 수 있기 때문입니다.

Aspose.PDF for Java는 표를 쉽게 검색할 수 있는 도구를 제공합니다. 표 데이터를 추출하려면 다음 단계를 수행해야 합니다:

1. 문서 열기 - [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체를 인스턴스화합니다;
1. [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber) 객체를 생성합니다.

1. 분석할 페이지를 결정하고 원하는 페이지에 [visit](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#visit-com.aspose.pdf.Page-)을 적용합니다. 표 형식 데이터가 스캔되며, 결과는 [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedTable)의 리스트로 저장됩니다. 이 리스트는 [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--) 메소드를 통해 얻을 수 있습니다.
1. 데이터를 얻기 위해 `TableList`를 반복하고 [흡수된 행](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow) 리스트와 흡수된 셀 리스트를 처리합니다. 첫 번째 리스트는 [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--) 메소드를 호출하여 접근할 수 있으며, 두 번째 리스트는 [getCellList](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow#getCellList--) 메소드를 호출하여 접근할 수 있습니다.

1. 각 [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedCell)에는 [TextFragmentCollections](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentCollection)이 포함되어 있습니다. 이를 자신의 목적으로 처리할 수 있습니다.

다음 예제는 모든 페이지에서 테이블 추출을 보여줍니다:

```java
public static void Extract_Table() {
    // 원본 PDF 문서 로드
    String filePath = "/home/aspose/pdf-examples/Samples/sample_table.pdf";
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);
    com.aspose.pdf.TableAbsorber absorber = new com.aspose.pdf.TableAbsorber();

    // 페이지 스캔
    for (com.aspose.pdf.Page page : pdfDocument.getPages()) {
        absorber.visit(page);
        for (com.aspose.pdf.AbsorbedTable table : absorber.getTableList()) {
            System.out.println("Table");
            // 행 목록을 반복
            for (com.aspose.pdf.AbsorbedRow row : table.getRowList()) {
                // 셀 목록을 반복
                for (com.aspose.pdf.AbsorbedCell cell : row.getCellList()) {
                    for (com.aspose.pdf.TextFragment fragment : cell.getTextFragments()) {
                        StringBuilder sb = new StringBuilder();
                        for (com.aspose.pdf.TextSegment seg : fragment.getSegments())
                            sb.append(seg.getText());
                        System.out.print(sb.toString() + "|");
                    }
                }
                System.out.println();
            }
        }
    }
}
```


## PDF 페이지의 특정 영역에서 테이블 추출하기

각 흡수된 테이블은 페이지에서 테이블의 위치를 설명하는 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedTable#getRectangle--) 속성을 가지고 있습니다.

따라서 특정 지역에 위치한 테이블을 추출하려면 특정 좌표로 작업해야 합니다.

다음 예제는 사각형 주석으로 표시된 테이블을 추출하는 방법을 보여줍니다:

```java
public static void Extract_Marked_Table() {
    // 원본 PDF 문서 로드
    String filePath = "<... 여기에 pdf 파일 경로 입력 ...>";
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);
    com.aspose.pdf.Page page = pdfDocument.getPages().get_Item(1);

    com.aspose.pdf.AnnotationSelector annotationSelector = new com.aspose.pdf.AnnotationSelector(
            new com.aspose.pdf.SquareAnnotation(page, com.aspose.pdf.Rectangle.getTrivial()));

    java.util.List<com.aspose.pdf.Annotation> list = annotationSelector.getSelected();
    if (list.size() == 0) {
        System.out.println("표시된 테이블을 찾을 수 없습니다..");
        return;
    }

    com.aspose.pdf.SquareAnnotation squareAnnotation = (com.aspose.pdf.SquareAnnotation) list.get(0);

    com.aspose.pdf.TableAbsorber absorber = new com.aspose.pdf.TableAbsorber();
    absorber.visit(page);

    for (com.aspose.pdf.AbsorbedTable table : absorber.getTableList()) {
        {
            boolean isInRegion = (squareAnnotation.getRect().getLLX() < table.getRectangle().getLLX())
                    && (squareAnnotation.getRect().getLLY() < table.getRectangle().getLLY())
                    && (squareAnnotation.getRect().getURX() > table.getRectangle().getURX())
                    && (squareAnnotation.getRect().getURY() > table.getRectangle().getURY());

            if (isInRegion) {
                for (com.aspose.pdf.AbsorbedRow row : table.getRowList()) {
                    {
                        for (com.aspose.pdf.AbsorbedCell cell : row.getCellList()) {
                            for (com.aspose.pdf.TextFragment fragment : cell.getTextFragments()) {
                                StringBuilder sb = new StringBuilder();
                                for (com.aspose.pdf.TextSegment seg : fragment.getSegments())
                                    sb.append(seg.getText());
                                System.out.print(sb.toString() + "|");
                            }
                        }
                        System.out.println();
                    }
                }
            }
        }
    }
}
```


## PDF에서 테이블 데이터 추출하여 CSV 파일로 저장하기

다음 예제는 테이블을 추출하여 CSV 파일로 저장하는 방법을 보여줍니다. PDF를 Excel 스프레드시트로 변환하는 방법은 [PDF를 Excel로 변환](/pdf/java/convert-pdf-to-excel/) 문서를 참조하세요.

```java
public static void Extract_Table_Save_CSV()
{
    String filePath = "/home/admin1/pdf-examples/Samples/sample_table.pdf";
    // PDF 문서 로드
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);

    // ExcelSave Option 객체 인스턴스화
    com.aspose.pdf.ExcelSaveOptions excelSave = new com.aspose.pdf.ExcelSaveOptions();
    excelSave.setFormat(com.aspose.pdf.ExcelSaveOptions.ExcelFormat.CSV);

    // XLS 형식으로 출력 저장
    pdfDocument.save("PDFToXLS_out.xlsx", excelSave);
}
```