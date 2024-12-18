---

title: PDF의 테이블 셀에 이미지 삽입
type: docs
weight: 20
url: /ko/java/insert-an-image-into-a-table-cell-in-pdf/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

테이블은 데이터를 표시하는 중요한 요소입니다. 테이블은 데이터 표현에 있어 보기 좋은 형식을 제공합니다. 테이블은 종종 숫자 정보를 표시하는 데 사용됩니다. Aspose.PDF API는 PDF 파일에 테이블을 생성할 수 있는 기능을 제공하는 Table 클래스를 제공합니다.

단순한 테이블을 만드는 대신, 테이블 테두리 스타일, 여백 정보, 정렬, 배경색, 열 너비, 제목 정보, 각 페이지에 반복될 행의 값 등 다양한 서식 옵션을 설정할 수 있습니다.

{{% /alert %}}

## Aspose.PDF 접근 방식

우리의 DOM (문서 객체 모델)에 따르면, 문서는 페이지로 구성됩니다.
 페이지는 하나 이상의 문단을 포함하며, 문단은 이미지, 텍스트, 폼 필드, 헤딩, 플로팅 박스, 그래프, 첨부 파일 또는 테이블일 수 있습니다. 테이블은 다시 행의 모음이며 각 행은 셀의 모음입니다. 셀은 문단의 모음입니다.

따라서 우리의 DOM에 따르면 테이블 셀은 이미지 포함 위에 명시된 문단 요소 중 어느 것이든 포함할 수 있습니다.

## 셀 너비 이해하기

특히 테이블 셀에 이미지를 표시할 때는 셀 너비에 대한 명확한 이해가 필요합니다. 그래야 이미지 너비가 셀의 너비에 고정되어 올바르게 표시됩니다. 이미지는 Image 클래스의 setFixedWidth() 메서드를 사용하여 너비를 설정할 수 있습니다.

## 코드 예제

```java

 String dataDir = "C:\\temp\\";

//빈 생성자를 호출하여 Document 객체를 인스턴스화합니다.

Document pdfDocument = new Document();

//Document 객체에 페이지를 생성합니다.

com.aspose.pdf.Page page = pdfDocument.getPages().add();



//테이블 객체를 인스턴스화합니다.

Table table = new Table();

//원하는 페이지의 문단 컬렉션에 테이블을 추가합니다.

page.getParagraphs().add(table);

//테이블의 열 너비를 설정합니다.

table.setColumnWidths("100 100 120");



//다른 사용자 정의 BorderInfo 객체를 사용하여 테이블 테두리를 설정합니다.

table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 1F));



//페이지에 이미지 객체를 생성합니다.

com.aspose.pdf.Image img1 = new com.aspose.pdf.Image();

//이미지 파일의 경로를 설정합니다.

img1.setFile(dataDir + "logo.jpg");



img1.setFixWidth(100);

img1.setFixHeight(100);

//테이블에 행을 생성한 다음 행에 셀을 생성합니다.

Row row1 = table.getRows().add();

row1.getCells().add("셀 안의 샘플 텍스트");

// 이미지를 담고 있는 셀을 추가합니다.

Cell cell2 = row1.getCells().add();

//테이블 셀에 이미지를 추가합니다.

cell2.getParagraphs().add(img1);



row1.getCells().add("이미지가 있는 이전 셀");

row1.getCells().get_Item(2).setVerticalAlignment(VerticalAlignment.Center);



//문서를 저장합니다.

pdfDocument.save(dataDir + "Image_in_Cell.pdf");    

```