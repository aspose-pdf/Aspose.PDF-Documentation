---
title: 첨부 파일 추출 및 저장
linktitle: 첨부 파일 추출 및 저장
type: docs
weight: 20
url: /ko/java/extract-and-save-an-attachment/
description: Aspose.PDF for Java를 사용하면 PDF 문서에서 모든 첨부 파일을 가져올 수 있습니다. 또한, 문서에서 개별 첨부 파일을 가져올 수 있습니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서에서 첨부 파일 가져오기

Aspose.PDF를 사용하면 PDF 문서에서 모든 첨부 파일을 가져오는 것이 가능합니다. 이는 문서를 PDF와 별도로 저장하려고 할 때나 PDF에서 첨부 파일을 제거해야 할 때 유용합니다.

다음 코드 스니펫은 PDF 문서에서 모든 첨부 파일을 가져오는 방법을 보여줍니다.

```java
   public static void GetAttachmentsFromPDFDocument() {
// 문서 열기
Document pdfDocument = new Document(_dataDir+"input.pdf");
  // 특정 임베디드 파일 가져오기
  FileSpecification fileSpecification = pdfDocument.getEmbeddedFiles().get_Item(1);
  // 파일 속성 가져오기
  System.out.printf("이름: - " + fileSpecification.getName());
  System.out.printf("\n설명: - " + fileSpecification.getDescription());
  System.out.printf("\nMime 유형: - " + fileSpecification.getMIMEType());
  // PDF 파일에서 첨부 파일 가져오기
  try {
   InputStream input = fileSpecification.getContents();
   File file = new File(fileSpecification.getName());
   // PDF에서 파일 경로 생성
   file.getParentFile().mkdirs();
   // PDF에서 파일 생성 및 추출
   java.io.FileOutputStream output = new java.io.FileOutputStream(fileSpecification.getName(), true);
   byte[] buffer = new byte[4096];
   int n = 0;
   while (-1 != (n = input.read(buffer)))
    output.write(buffer, 0, n);
   // InputStream 객체 닫기
   input.close();
   output.close();
  } catch (IOException e) {
   e.printStackTrace();
  }
  // Document 객체 닫기
  pdfDocument.dispose();
        
    }

```


## 첨부 파일 정보 가져오기

[PDF 문서에서 첨부 파일 가져오기](/pdf/ko/java/get-attachments-from-a-pdf-document/)에서 언급한 바와 같이, 첨부 파일 정보는 [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) 객체에 보관되며, [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 EmbeddedFiles 컬렉션에 다른 첨부 파일들과 함께 수집됩니다.

[FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) 객체는 첨부 파일에 대한 정보를 얻기 위한 메서드를 제공합니다. 예를 들어:

- getName() – 파일 이름을 가져옵니다.
- [getDescription()](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification#getDescription--) – 파일 설명을 가져옵니다.
- getMIMEType() – 파일의 MIME 타입을 가져옵니다.
- getParams() – 파일 매개변수에 대한 정보 (예: CheckSum, CreationDate, ModDate 및 Size)를 가져옵니다.

이 매개변수를 얻으려면 먼저 getParams() 메서드가 null을 반환하지 않는지 확인하십시오.

for 루프를 사용하여 EmbeddedFiles 컬렉션의 모든 첨부 파일을 반복하거나, 인덱스 값을 지정하여 개별 첨부 파일을 가져오십시오.
 다음 코드 스니펫은 특정 첨부 파일에 대한 정보를 얻는 방법을 보여줍니다.

```java
    public static void GetAttachmentInformation() {
  // 문서 열기
  Document pdfDocument = new Document(_dataDir+"input.pdf");
  // 특정 임베디드 파일 가져오기
  FileSpecification fileSpecification = pdfDocument.getEmbeddedFiles().get_Item(1);
  // 파일 속성 가져오기
  System.out.println("Name:-" + fileSpecification.getName());
  System.out.println("Description:- " + fileSpecification.getDescription());
  System.out.println("Mime Type:-" + fileSpecification.getMIMEType());
  // 매개변수 객체가 매개변수를 포함하고 있는지 확인
  if (fileSpecification.getParams() != null) {
   System.out.println("CheckSum:- " + fileSpecification.getParams().getCheckSum());
   System.out.println("Creation Date:- " + fileSpecification.getParams().getCreationDate());
   System.out.println("Modification Date:- " + fileSpecification.getParams().getModDate());
   System.out.println("Size:- " + fileSpecification.getParams().getSize());
  } 
```