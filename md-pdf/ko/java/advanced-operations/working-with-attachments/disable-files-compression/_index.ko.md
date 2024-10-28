---
title: 파일을 포함된 리소스로 추가할 때 압축 비활성화
linktitle: 파일 압축 비활성화
type: docs
weight: 40
url: /java/disable-files-compression-when-adding-as-embedded-resources/
description: 이 문서는 파일을 포함된 리소스로 추가할 때 압축을 비활성화하는 방법을 설명합니다.
lastmod: "2021-06-05"
---

[FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) 클래스는 개발자가 PDF 문서에 첨부 파일을 추가할 수 있도록 합니다. 기본적으로 첨부 파일은 압축됩니다. 우리는 파일을 포함된 리소스로 추가할 때 압축을 비활성화할 수 있도록 API를 업데이트했습니다. 이는 개발자가 파일이 처리되는 방식을 더욱 제어할 수 있게 해줍니다.

개발자가 파일 압축을 제어할 수 있도록 [setEncoding(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification#setEncoding-int-) 메서드가 [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) 클래스에 추가되었습니다.
 이 속성은 파일 압축에 사용할 인코딩을 결정합니다. 이 메서드는 [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding) 열거형에서 값을 허용합니다. 가능한 값은 [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).None 및 [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).Zip입니다.

Encoding이 [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).None으로 설정되면 첨부 파일은 압축되지 않습니다. 기본 인코딩은 [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).Zip입니다.

다음 코드 스니펫은 PDF 문서에 첨부 파일을 추가하는 방법을 보여줍니다.

```java
    public static void DisableFilesCompressionWhenAddingAsEmbeddedResources() throws IOException{
  // 소스/입력 파일의 참조 가져오기
  java.nio.file.Path path = java.nio.file.Paths.get(_dataDir+"input.pdf");
  // 소스 파일의 모든 내용을 ByteArray로 읽어오기
  byte[] data = java.nio.file.Files.readAllBytes(path);
  // ByteArray 내용을 기반으로 Stream 객체 인스턴스 생성
  InputStream is = new ByteArrayInputStream(data);
  // 스트림 인스턴스로부터 Document 객체 인스턴스화
  Document pdfDocument = new Document(is);
  // 첨부 파일로 추가할 새 파일 설정
  FileSpecification fileSpecification = new FileSpecification("test.txt", "샘플 텍스트 파일");
  // Encoding 속성을 FileEncoding.None으로 설정
  fileSpecification.setEncoding(FileEncoding.None);
  // 문서의 첨부 파일 컬렉션에 첨부 파일 추가
  pdfDocument.getEmbeddedFiles().add(fileSpecification);
  // 새 출력 저장
  pdfDocument.save("output.pdf");
    }
```