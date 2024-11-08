---
title: PDF에서 테이블 데이터 추출
linktitle: 테이블 데이터 추출
type: docs
weight: 40
url: /ko/androidjava/extract-data-from-table-in-pdf/
description: Java를 통한 Aspose.PDF for Android을 사용하여 PDF에서 표 데이터를 추출하는 방법을 배웁니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 프로그래밍을 통해 PDF에서 테이블 추출하기

PDF에서 테이블을 추출하는 것은 쉽지 않은 작업입니다. 테이블은 다양한 방식으로 생성될 수 있기 때문입니다.

Java를 통한 Aspose.PDF for Android은 테이블을 쉽게 가져올 수 있는 도구를 제공합니다. 테이블 데이터를 추출하려면 다음 단계를 수행해야 합니다:

1. 문서 열기 - [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체를 인스턴스화합니다;
1. [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber) 객체를 생성합니다.

1. 분석할 페이지를 결정하고 원하는 페이지에 [visit](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#visit-com.aspose.pdf.Page-)을 적용합니다. 표 형식의 데이터가 스캔되어 [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedTable) 리스트에 저장됩니다. 이 리스트는 [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--) 메소드를 통해 얻을 수 있습니다.
1. 데이터를 얻기 위해 `TableList`를 반복하고 [흡수된 행](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow) 리스트와 흡수된 셀 리스트를 처리합니다. 첫 번째 리스트는 [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--) 메소드를 호출하여 접근할 수 있으며, 두 번째 리스트는 [getCellList](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow#getCellList--) 메소드를 호출하여 접근할 수 있습니다.

1. 각 [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedCell)은 [TextFragmentCollections](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentCollection)를 포함합니다. 자신의 목적에 맞게 처리할 수 있습니다.

다음 예제는 모든 페이지에서 표 추출을 보여줍니다:

```java
public void extractTable () {
        // 문서 열기
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        com.aspose.pdf.TableAbsorber absorber=new com.aspose.pdf.TableAbsorber();

        File file=new File(fileStorage, "extracted-text.txt");
        FileOutputStream fileOutputStream;

        try {
            fileOutputStream=new FileOutputStream(file);

        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(fileOutputStream));
        // 페이지 스캔
        for (Page page : (Iterable<? extends Page>) document.getPages()) {
            absorber.visit(page);
            for (com.aspose.pdf.AbsorbedTable table : absorber.getTableList()) {
                try {
                    bw.write("Table");
                    bw.newLine();
                    // 행 목록을 반복
                    for (com.aspose.pdf.AbsorbedRow row : table.getRowList()) {
                        // 셀 목록을 반복
                        for (com.aspose.pdf.AbsorbedCell cell : row.getCellList()) {
                            for (com.aspose.pdf.TextFragment fragment : cell.getTextFragments()) {
                                StringBuilder sb=new StringBuilder();
                                for (TextSegment seg :
                                        (Iterable<? extends TextSegment>) fragment.getSegments())
                                    sb.append(seg.getText());
                                bw.write(sb.toString() + "|");
                            }
                        }
                        bw.newLine();
                    }
                } catch (IOException e) {
                    resultMessage.setText(e.getMessage());
                    return;
                }
            }
        }
        try {
            bw.close();
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


## PDF 페이지의 특정 영역에서 표 추출하기

각 흡수된 표는 페이지에서 표의 위치를 설명하는 [Rectangle](https://reference.aspose.com/pdf/java/aspose.pdf.text/absorbedtable/properties/rectangle) 속성을 가집니다.

따라서 특정 지역에 위치한 표를 추출하려면 특정 좌표를 사용해야 합니다.

다음 예제는 사각형 주석으로 표시된 표를 추출하는 방법을 보여줍니다:

```java
public void extractMarkedTable () {
        // 문서 열기
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        com.aspose.pdf.Page page=document.getPages().get_Item(1);

        com.aspose.pdf.AnnotationSelector annotationSelector=
                new com.aspose.pdf.AnnotationSelector(
                        new com.aspose.pdf.SquareAnnotation(page, com.aspose.pdf.Rectangle.getTrivial()));

        List list=annotationSelector.getSelected();
        if (list.size() == 0) {
            resultMessage.setText("표가 표시되지 않았습니다.");
            return;
        }

        com.aspose.pdf.SquareAnnotation squareAnnotation = (com.aspose.pdf.SquareAnnotation) list.get(0);

        com.aspose.pdf.TableAbsorber absorber=new com.aspose.pdf.TableAbsorber();
        absorber.visit(page);

        for (com.aspose.pdf.AbsorbedTable table : absorber.getTableList()) {
            {
                boolean isInRegion=(squareAnnotation.getRect().getLLX() < table.getRectangle().getLLX())
                        && (squareAnnotation.getRect().getLLY() < table.getRectangle().getLLY())
                        && (squareAnnotation.getRect().getURX() > table.getRectangle().getURX())
                        && (squareAnnotation.getRect().getURY() > table.getRectangle().getURY());

                if (isInRegion) {
                    File file=new File(fileStorage, "extracted-text.txt");
                    FileOutputStream fileOutputStream;

                    try {
                        fileOutputStream=new FileOutputStream(file);

                    } catch (FileNotFoundException e) {
                        resultMessage.setText(e.getMessage());
                        return;
                    }

                    BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(fileOutputStream));
                    try {
                        // 표 구문 분석
                        for (com.aspose.pdf.AbsorbedRow row : table.getRowList()) {
                            {
                                for (com.aspose.pdf.AbsorbedCell cell : row.getCellList()) {
                                    for (com.aspose.pdf.TextFragment fragment :
                                            cell.getTextFragments()) {
                                        bw.write(fragment.getText());
                                    }
                                    bw.write("|");
                                }
                                bw.newLine();
                            }
                        }
                        bw.close();
                        // -------------
                    } catch (IOException e) {
                        resultMessage.setText(e.getMessage());
                        return;
                    }
                    resultMessage.setText(R.string.success_message);
                }
            }
        }
    }
```


## PDF에서 테이블 데이터를 추출하여 CSV 파일로 저장하기

다음 예제는 테이블을 추출하여 CSV 파일로 저장하는 방법을 보여줍니다.
PDF를 Excel 스프레드시트로 변환하는 방법은 [PDF를 Excel로 변환](/pdf/ko/java/convert-pdf-to-excel/) 기사를 참조하십시오.

```java
 public void extractTableSaveCSV () {
        // 문서 열기
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        File file=new File(fileStorage, "PDFToXLS_out.csv");
        // ExcelSave Option 객체 인스턴스화
        com.aspose.pdf.ExcelSaveOptions excelSave=new com.aspose.pdf.ExcelSaveOptions();
        excelSave.setFormat(com.aspose.pdf.ExcelSaveOptions.ExcelFormat.CSV);
        try {
            document.save(file.toString(), excelSave);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```