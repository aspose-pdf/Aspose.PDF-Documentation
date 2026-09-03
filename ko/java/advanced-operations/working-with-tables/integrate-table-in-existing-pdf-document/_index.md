---
title: Java의 데이터 소스와 PDF 테이블 통합
linktitle: 테이블 통합
type: docs
weight: 30
url: /java/integrate-table/
description: PDF 테이블을 Java의 CSV 파일과 같은 구조화된 데이터 소스와 통합하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 구조화된 데이터에서 PDF 테이블 작성
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 테이블을 외부 데이터와 통합하는 방법을 설명합니다. CSV 데이터 읽기, 특정 열 선택, 구문 분석된 행에서 스타일이 지정된 테이블 개체 작성 및 결과를 PDF 문서로 렌더링하는 방법을 다룹니다.
---
Java 예제는 외부 데이터 프레임 라이브러리에 의존하지 않고 CSV 데이터에서 PDF 테이블을 작성합니다.


## 
CSV 행에서 테이블 작성



선택한 CSV 열을 스타일이 지정된 PDF 테이블로 변환해야 하는 경우 이 예를 사용하십시오.


1. 
[표](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/)를 생성하고 테두리를 구성합니다.

1. 
CSV 헤더 행에서 필요한 열 인덱스를 감지합니다.
1. 헤더 행과 요청된 데이터 행 수를 추가한 다음 테이블을 반환합니다.


```java
public static Table createTableFromCsv(List<String[]> rows, int maxRows) {
    Table table = new Table();
    table.setBorder(new BorderInfo(BorderSide.All, 1, Color.getLightGray()));
    table.setDefaultCellBorder(new BorderInfo(BorderSide.Bottom, 1, Color.getLightGray()));

    String[] header = rows.get(0);
    int[] selectedColumns = findColumns(header, "city", "country", "population", "iso3");

    Row headerRow = table.getRows().add();
    headerRow.setRowBroken(false);
    for (int columnIndex : selectedColumns) {
        Cell cell = headerRow.getCells().add(header[columnIndex]);
        cell.setBackgroundColor(Color.getLightGray());
    }

    int limit = Math.min(maxRows, rows.size() - 1);
    for (int rowIndex = 1; rowIndex <= limit; rowIndex++) {
        Row row = table.getRows().add();
        String[] rowData = rows.get(rowIndex);
        for (int columnIndex : selectedColumns) {
            row.getCells().add(columnIndex < rowData.length ? rowData[columnIndex] : "");
        }
    }

    return table;
}
```

## 
CSV 데이터에서 PDF 만들기



CSV 입력을 PDF 테이블 문서로 렌더링해야 하는 경우 이 예를 사용하십시오.


1. 
입력 파일에서 CSV 행을 읽습니다.

1. 
콘솔에서 구문 분석된 행의 하위 집합을 미리 봅니다.
1. PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 생성하고 생성된 테이블을 추가한 후 출력 파일을 저장합니다.


```java
public static void createPdfFromCsv(Path inputFile, Path outputFile, int maxRows) throws Exception {
    List<String[]> rows = readCsv(inputFile);
    for (int i = 0; i < Math.min(20, rows.size()); i++) {
        System.out.println(String.join(" | ", rows.get(i)));
    }

    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(createTableFromCsv(rows, maxRows));
        document.save(outputFile.toString());
    }
}
```

## 
이름으로 CSV 열 인덱스 찾기



CSV 헤더 행에 특정 명명된 열을 배치해야 하는 경우 이 도우미를 사용하세요.


1. 
요청된 열 이름을 반복합니다.

1. 
일치하는 색인이 있는지 헤더 행을 검색합니다.
1. 수집된 열 위치를 반환합니다.


```java
private static int[] findColumns(String[] header, String... names) {
    int[] indexes = new int[names.length];
    for (int i = 0; i < names.length; i++) {
        indexes[i] = 0;
        for (int j = 0; j < header.length; j++) {
            if (names[i].equals(header[j])) {
                indexes[i] = j;
                break;
            }
        }
    }
    return indexes;
}
```

## 
파일에서 CSV 행 읽기



테이블 생성 전에 CSV 소스를 메모리에 로드해야 하는 경우 이 도우미를 사용하세요.


1. 
입력 파일의 모든 줄을 읽습니다.

1. 
CSV 파서 도우미를 사용하여 각 줄을 분할합니다.
1. 수집된 행 값을 반환합니다.


```java
private static List<String[]> readCsv(Path inputFile) throws Exception {
    List<String[]> rows = new ArrayList<>();
    for (String line : Files.readAllLines(inputFile)) {
        rows.add(splitCsvLine(line));
    }
    return rows;
}
```

## 
하나의 CSV 줄을 값으로 분할



CSV 행에 인용된 값과 이스케이프된 인용 문자가 포함될 수 있는 경우 이 도우미를 사용하세요.


1. 
줄의 문자를 반복합니다.

1. 
파서가 현재 인용된 텍스트 안에 있는지 추적합니다.
1. 최종 값 목록을 작성하고 배열로 반환합니다.

```java
private static String[] splitCsvLine(String line) {
    List<String> values = new ArrayList<>();
    StringBuilder current = new StringBuilder();
    boolean inQuotes = false;
    for (int i = 0; i < line.length(); i++) {
        char ch = line.charAt(i);
        if (ch == '"') {
            if (inQuotes && i + 1 < line.length() && line.charAt(i + 1) == '"') {
                current.append('"');
                i++;
            } else {
                inQuotes = !inQuotes;
            }
        } else if (ch == ',' && !inQuotes) {
            values.add(current.toString());
            current.setLength(0);
        } else {
            current.append(ch);
        }
    }
    values.add(current.toString());
    return values.toArray(String[]::new);
}
```
