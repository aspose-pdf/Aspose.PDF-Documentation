---
title: PDF 인쇄 작업
type: docs
weight: 10
url: ko/java/print-pdf-file/
description: 이 섹션에서는 PdfViewer 클래스를 사용하여 Aspose.PDF Facades로 PDF 파일을 인쇄하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 프린터 및 페이지 설정을 사용하여 기본 프린터에 PDF 파일 인쇄

[PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) 클래스는 PDF 파일을 기본 프린터에 인쇄할 수 있게 합니다. 따라서 [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) 객체를 생성하고 openPdfFile(..) 메서드를 사용하여 PDF를 엽니다.

printDocument(..) 메서드를 호출하여 PDF를 기본 프린터에 인쇄합니다.

다음 코드 스니펫은 프린터 및 페이지 설정을 사용하여 PDF를 기본 프린터에 인쇄하는 방법을 보여줍니다.

```java
 public static void PrintingPDFFile() {
        // PdfViewer 객체 생성
        PdfViewer viewer = new PdfViewer();

        // 입력 PDF 파일 열기
        viewer.bindPdf(_dataDir + "sample.pdf");

        // 인쇄 속성 설정
        viewer.setAutoResize(true); // 조정된 크기로 파일 인쇄
        viewer.setAutoRotate(true); // 조정된 회전으로 파일 인쇄
        viewer.setPrintPageDialog(false); // 인쇄 시 페이지 번호 대화 상자 생성 안 함

        // 프린터 및 페이지 설정과 PrintDocument 객체 생성
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // 프린터 이름 설정
        printerSettings.setPrinterName("Microsoft Print to PDF");
        

        // 페이지 크기 설정 (필요한 경우)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // 페이지 여백 설정 (필요한 경우)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // 프린터 및 페이지 설정을 사용하여 문서 인쇄
        viewer.printDocumentWithSettings(pageSettings, printerSettings);
        
        // 인쇄 후 PDF 파일 닫기
        viewer.close();
    }
```


문서 인쇄 대화 상자를 표시하려면 다음 코드 스니펫을 사용해 보세요:

```java
public static void PrintingPDFDisplayPrintDialog() {
        // PdfViewer 객체 생성
        PdfViewer viewer = new PdfViewer();

        // 입력 PDF 파일 열기
        viewer.bindPdf(_dataDir + "sample.pdf");

        // 인쇄를 위한 속성 설정
        viewer.setAutoResize(true); // 크기가 조정된 파일 인쇄
        viewer.setAutoRotate(true); // 회전이 조정된 파일 인쇄
        viewer.setPrintPageDialog(true);

        // 프린터 및 페이지 설정과 PrintDocument를 위한 객체 생성
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // PageSize 설정 (필요한 경우)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // PageMargins 설정 (필요한 경우)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        java.awt.print.PrinterJob pj = java.awt.print.PrinterJob.getPrinterJob();

        if (pj.printDialog()) {
            printerSettings.setPrinterName(pj.getPrintService().getName());
            printerSettings.setCopies((short) pj.getCopies());
            // 프린터 및 페이지 설정을 사용하여 문서 인쇄
            viewer.printDocumentWithSettings(pageSettings, printerSettings);
        }
        // 인쇄 후 PDF 파일 닫기
        viewer.close();
    }
```


## 소프트 프린터로 PDF 인쇄하기

파일로 출력하는 프린터가 있습니다. 가상 프린터의 이름을 설정하고, 이전 예제와 유사하게 설정을 합니다.

```java
public static void PrintingPDFToSoftPrinter() {
        // PdfViewer 객체 생성
        PdfViewer viewer = new PdfViewer();

        // 입력 PDF 파일 열기
        viewer.bindPdf(_dataDir + "sample.pdf");

        // 인쇄를 위한 속성 설정
        viewer.setAutoResize(true); // 조정된 크기로 파일 인쇄
        viewer.setAutoRotate(true); // 조정된 회전으로 파일 인쇄
        viewer.setPrintPageDialog(false); // 인쇄 시 페이지 번호 대화상자를 표시하지 않음

        // 프린터 및 페이지 설정, PrintDocument 객체 생성
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Microsoft 소프트 프린터 설정
        printerSettings.setPrinterName("Microsoft Print to PDF");
        // 또는 Adobe
        // printerSettings.setPrinterName("Adobe PDF");

        // 페이지 크기 설정 (필요한 경우)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // 페이지 여백 설정 (필요한 경우)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // 프린터 및 페이지 설정을 사용하여 문서 인쇄
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // 인쇄 후 PDF 파일 닫기
        viewer.close();
    }
```


## 인쇄 대화 상자 숨기기

Aspose.PDF for Java를 사용하면 인쇄 대화 상자를 숨길 수 있습니다. 이를 위해 [getPrintPageDialog](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer#getPrintPageDialog--) 메서드를 사용하십시오.

다음 코드 조각은 인쇄 대화 상자를 숨기는 방법을 보여줍니다.

```java
public static void PrintingPDFHidePrintDialog() {
        // PdfViewer 객체 생성
        PdfViewer viewer = new PdfViewer();

        // 입력 PDF 파일 열기
        viewer.bindPdf(_dataDir + "sample.pdf");

        // 인쇄 속성 설정
        viewer.setAutoResize(true); // 조정된 크기로 파일 인쇄
        viewer.setAutoRotate(true); // 조정된 회전으로 파일 인쇄

        viewer.setPrintPageDialog(false); // 인쇄 시 페이지 번호 대화 상자를 생성하지 않음

        // 프린터 및 페이지 설정 및 PrintDocument용 객체 생성
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // 프린터 Microsoft Soft Printer 설정
        printerSettings.setPrinterName("Microsoft Print to PDF");

        // 페이지 크기 설정 (필요한 경우)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // 페이지 여백 설정 (필요한 경우)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // 프린터 및 페이지 설정을 사용하여 문서 인쇄
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // 인쇄 후 PDF 파일 닫기
        viewer.close();
    }
```


## XPS 파일로 컬러 PDF를 그레이스케일로 인쇄하기

컬러 PDF 문서는 [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer)를 사용하여 XPS 프린터로 그레이스케일로 인쇄할 수 있습니다. 이를 위해서는 PdfViewer.PrintAsGrayscale 속성을 사용하고 이를 *true*로 설정해야 합니다.

다음 코드 스니펫은 PdfViewer.PrintAsGrayscale 속성의 구현을 보여줍니다.

```java
 public static void PrintingPDFasGrayscale() {
        // PdfViewer 객체 생성
        PdfViewer viewer = new PdfViewer();

        // 입력 PDF 파일 열기
        viewer.bindPdf(_dataDir + "sample.pdf");

        // 인쇄를 위한 속성 설정
        viewer.setAutoResize(true); // 조정된 크기로 파일 인쇄
        viewer.setAutoRotate(true); // 조정된 회전으로 파일 인쇄

        viewer.setPrintAsGrayscale(true);

        // 프린터 및 페이지 설정과 PrintDocument 객체 생성
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Microsoft 소프트 프린터 설정
        printerSettings.setPrinterName("Microsoft Print to PDF");

        // 페이지 크기 설정 (필요한 경우)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // 페이지 여백 설정 (필요한 경우)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // 프린터 및 페이지 설정을 사용하여 문서 인쇄
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // 인쇄 후 PDF 파일 닫기
        viewer.close();
    }
```


## PDF to PostScript 변환

[PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) 클래스는 PDF 문서를 인쇄하는 기능을 제공하며, 이 클래스를 사용하여 PDF 파일을 PostScript 형식으로 변환할 수도 있습니다. PDF 파일을 PostScript로 변환하려면, 먼저 PS 프린터를 설치하고 PdfViewer를 사용하여 파일로 인쇄하면 됩니다.

다음 코드 스니펫은 PDF를 인쇄하고 PostScript 형식으로 변환하는 방법을 보여줍니다.

```java
public static void PrintingPDFToPostScript() {
        // PdfViewer 객체 생성
        PdfViewer viewer = new PdfViewer();

        // 입력 PDF 파일 열기
        viewer.bindPdf(_dataDir + "sample.pdf");

        // 인쇄 속성 설정
        viewer.setAutoResize(true); // 파일을 조정된 크기로 인쇄
        viewer.setAutoRotate(true); // 파일을 조정된 회전으로 인쇄

        viewer.setPrintAsGrayscale(true);

        // 프린터 및 페이지 설정과 PrintDocument 객체 생성
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // PostScript 프린터 설정
        printerSettings.setPrinterName("HP Universal Printing PS (v7.0.0)");
        printerSettings.setPrintToFile(true);
        printerSettings.setPrintFileName(_dataDir+"result.ps");

        // 페이지 크기 설정 (필요한 경우)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // 페이지 여백 설정 (필요한 경우)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // 프린터 및 페이지 설정을 사용하여 문서 인쇄
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // 인쇄 후 PDF 파일 닫기
        viewer.close();
    }
```


## 인쇄 작업 상태 확인

PDF 파일은 [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) 클래스를 사용하여 인쇄 대화 상자를 표시하지 않고 물리적 프린터나 Microsoft XPS 문서 작성기로 인쇄할 수 있습니다. 큰 PDF 파일을 인쇄할 때 프로세스가 오래 걸릴 수 있으므로 사용자는 인쇄 프로세스가 완료되었는지 문제를 겪었는지 확신할 수 없습니다. 인쇄 작업의 상태를 확인하려면 PrintStatus 속성을 사용하십시오. 다음 코드 조각은 XPS 파일로 PDF 파일을 인쇄하고 인쇄 상태를 얻는 방법을 보여줍니다.

```java
public static void CheckingPrintJobStatus() {
        // PdfViewer 객체 생성
        PdfViewer viewer = new PdfViewer();

        // 입력 PDF 파일 열기
        viewer.bindPdf(_dataDir + "sample.pdf");

        // 인쇄 속성 설정
        viewer.setAutoResize(true); // 크기가 조정된 파일 인쇄
        viewer.setAutoRotate(true); // 회전이 조정된 파일 인쇄

        viewer.setPrintAsGrayscale(true);

        // 프린터 및 페이지 설정과 PrintDocument에 대한 객체 생성
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Microsoft 소프트 프린터 설정
        printerSettings.setPrinterName("HP Universal Printing PS (v7.0.0)");

        // PageSize 설정 (필요한 경우)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // PageMargins 설정 (필요한 경우)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // 프린터 및 페이지 설정을 사용하여 문서 인쇄
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // 인쇄 상태 확인
        if (viewer.getPrintStatus() != null) {
            Exception ex = (Exception) viewer.getPrintStatus();
            System.out.println(ex.getMessage());
        } else {
            // 오류가 발견되지 않았습니다. 인쇄 작업이 성공적으로 완료되었습니다.
            System.out.println("Everything went OK!");
        }
        // 인쇄 후 PDF 파일 닫기
        viewer.close();
    }
```