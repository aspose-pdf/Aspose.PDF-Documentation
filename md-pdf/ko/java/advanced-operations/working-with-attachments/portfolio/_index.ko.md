---
title: PDF 문서에서 포트폴리오 작업하기
linktitle: 포트폴리오
type: docs
weight: 40
url: /java/portfolio/
description: Java로 PDF 포트폴리오를 만드는 방법. Microsoft Excel 파일, Word 문서 및 이미지 파일을 사용하여 PDF 포트폴리오를 만들어야 합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

먼저, **PDF 포트폴리오 파일 형식이 무엇인지** 알아봅시다.

예를 들어, Word, Excel, PowerPoint 프레젠테이션 등을 첨부 파일로 포함하는 PDF 포트폴리오 파일을 생각해 보세요. 여기서 각 첨부 파일은 원래 문서 형식을 유지하지만 하나의 PDF 포트폴리오 파일에 포함되거나 조립됩니다. 물론, PDF 포트폴리오의 각 개별 파일을 드라이브나 폴더에 있는 것처럼 열고 읽거나 편집할 수 있습니다. 또한, 일반 PDF 문서와 마찬가지로 워터마크를 적용하거나, 암호 및 보안 권한을 설정하여 PDF 포트폴리오의 첨부 파일에 대한 보기, 인쇄 또는 변경 권한을 설정할 수 있습니다.

우리는 원래의 유형 또는 형식의 네이티브 파일을 PDF 포트폴리오 파일에 첨부 파일로 배치하거나 조립할 수 있습니다.

## PDF 포트폴리오 생성 방법

Aspose.PDF는 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스를 사용하여 PDF 포트폴리오 문서를 생성할 수 있습니다. [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) 클래스로 파일을 가져온 후 Document.Collection 객체에 파일을 추가합니다. 파일이 추가되면 Document 클래스의 Save 메서드를 사용하여 포트폴리오 문서를 저장합니다.

다음 예제는 Microsoft Excel 파일, Word 문서 및 이미지 파일을 사용하여 PDF 포트폴리오를 생성합니다.

아래의 코드는 다음과 같은 포트폴리오를 생성합니다.

### Aspose.PDF로 생성된 PDF 포트폴리오

![Aspose.PDF for Java로 생성된 PDF 포트폴리오](working-with-pdf-portfolio_1.jpg)

```java
    public static void CreatePortfolio() throws IOException {
        // 문서 객체 인스턴스화
        Document pdfDocument = new Document();

        // 문서 컬렉션 객체 인스턴스화
        pdfDocument.setCollection(new Collection());

        // 포트폴리오에 추가할 파일 가져오기
        FileSpecification excel = new FileSpecification(_dataDir + "HelloWorld.xlsx");
        FileSpecification word = new FileSpecification(_dataDir + "HelloWorld.docx");
        FileSpecification image = new FileSpecification(_dataDir + "aspose-logo.jpg");

        // 파일 설명 제공
        excel.setDescription ("Excel 파일");
        word.setDescription ("Word 파일");
        image.setDescription ("이미지 파일");

        // 파일을 문서 컬렉션에 추가
        pdfDocument.getCollection().add(excel);
        pdfDocument.getCollection().add(word);
        pdfDocument.getCollection().add(image);

        // 포트폴리오 문서 저장
        pdfDocument.save(_dataDir + "CreatePDFPortfolio_out.pdf");
    }
```


## PDF 포트폴리오에서 파일 추출

PDF 포트폴리오는 다양한 출처(예: PDF, Word, Excel, JPEG 파일)의 콘텐츠를 하나의 통합된 컨테이너로 모을 수 있게 해줍니다. 원본 파일은 개별 정체성을 유지하지만 PDF 포트폴리오 파일로 조합됩니다. 사용자는 각 구성 파일을 다른 구성 파일과 독립적으로 열고, 읽고, 편집하고, 서식을 지정할 수 있습니다.

Aspose.PDF는 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스를 사용하여 PDF 포트폴리오 문서를 생성할 수 있도록 합니다. 또한 PDF 포트폴리오에서 파일을 추출할 수 있는 기능도 제공합니다.

다음 코드 스니펫은 PDF 포트폴리오에서 파일을 추출하는 단계를 보여줍니다.

![Extract files from PDF Portfolio](working-with-pdf-portfolio_2.jpg)

```java
    public static void ExtractPortfolio() throws IOException {
        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "PDFPortfolio.pdf");
        // 임베디드 파일 컬렉션 가져오기
        EmbeddedFileCollection embeddedFiles = pdfDocument.getEmbeddedFiles();

        // 포트폴리오의 개별 파일을 반복
        for (FileSpecification fileSpecification : embeddedFiles) {
            InputStream initialStream = fileSpecification.getContents();
            byte[] buffer = new byte[fileSpecification.getContents().available()];
            initialStream.read(buffer);

            File targetFile = new File(_dataDir + fileSpecification.getName());
            OutputStream outStream = new FileOutputStream(targetFile);
            outStream.write(buffer);
            outStream.close();
        }
    }
```


## PDF 포트폴리오에서 파일 제거

PDF 포트폴리오에서 파일을 삭제/제거하려면 다음 코드 라인을 사용해 보세요.

```java
public static void RemoveFilesFromPDFPortfolio() {
    // 소스 PDF 포트폴리오 로드
    Document pdfDocument = new Document(_dataDir + "PDFPortfolio.pdf");
    pdfDocument.getCollection().delete();
    pdfDocument.save(_dataDir + "No_PortFolio_out.pdf");
}
```