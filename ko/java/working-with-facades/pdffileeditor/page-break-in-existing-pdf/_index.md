---
title: 기존 PDF에서 페이지 나누기
type: docs
weight: 30
url: /ko/java/page-break-in-existing-pdf/
description: 이 섹션에서는 PdfFileEditor 클래스를 사용하여 기존 PDF에서 페이지를 나누는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

기본 레이아웃으로, PDF 파일 내부의 콘텐츠는 왼쪽 상단에서 오른쪽 하단으로 추가됩니다. 콘텐츠가 페이지 하단 여백을 초과하면 페이지 나누기가 발생합니다. 그러나 요구 사항에 따라 페이지 나누기를 삽입해야 할 수도 있습니다. 이 요구 사항을 충족하기 위해 [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) 클래스에 AddPageBreak(...)라는 메서드가 추가되었습니다.

1. [public void AddPageBreak(Document src, Document dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#addPageBreak-com.aspose.pdf.IDocument-com.aspose.pdf.IDocument-com.aspose.pdf.facades.PdfFileEditor.PageBreak:A-)

1. [public void AddPageBreak(string src, string dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#addPageBreak-java.lang.String-java.lang.String-com.aspose.pdf.facades.PdfFileEditor.PageBreak:A-)
1. [public void AddPageBreak(Stream src, Stream dest, PageBreak[] pageBreaks)](https://docs.oracle.com/javase/7/docs/api/java/io/InputStream.html?is-external=true)

- src는 원본 문서/문서 경로/원본 문서가 있는 스트림입니다.
- dest는 문서가 저장될 대상 문서/경로/스트림입니다.
- PageBreak는 페이지 나누기 객체의 배열입니다. 페이지 나누기가 있어야 할 페이지의 인덱스와 페이지에서의 세로 위치라는 두 가지 속성을 가지고 있습니다.

## 예제 1 (페이지 나누기 추가)

```java
   public static void PageBrakeExample01() {
        // Document 인스턴스화
        Document doc = new Document(_dataDir + "Sample-Document-01.pdf");
        // 빈 Document 인스턴스화
        Document dest = new Document();
        // PdfFileEditor 객체 생성
        PdfFileEditor fileEditor = new PdfFileEditor();
        fileEditor.AddPageBreak(doc, dest, new PdfFileEditor.PageBreak[] { new PdfFileEditor.PageBreak(1, 450) });
        // 결과 파일 저장
        dest.Save(_dataDir + "PageBreak_out.pdf");
    }
```


## 예제 2

```java
  public static void PageBrakeExample02() {
        // PdfFileEditor 객체 생성
        PdfFileEditor fileEditor = new PdfFileEditor();

        fileEditor.AddPageBreak(_dataDir + "Sample-Document-02.pdf", _dataDir + "PageBreakWithDestPath_out.pdf",
                new PdfFileEditor.PageBreak[] { new PdfFileEditor.PageBreak(1, 450) });
    }
```

## 예제 3

```java
 public static void PageBrakeExample03() {
        // 소스 파일 스트림 생성
        Stream src = new FileStream(_dataDir + "Sample-Document-03.pdf", FileMode.Open, FileAccess.Read);
        // 대상 파일 스트림 생성
        Stream dest = new FileStream(_dataDir + "PageBreakWithStream_out.pdf", FileMode.Create, FileAccess.ReadWrite);
        // PdfFileEditor 객체 생성
        PdfFileEditor fileEditor = new PdfFileEditor();
        fileEditor.AddPageBreak(src, dest, new PdfFileEditor.PageBreak[] { new PdfFileEditor.PageBreak(1, 450) });
        dest.Close();
        src.Close();
    }
```