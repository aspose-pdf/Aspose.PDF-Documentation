---
title: PDF 인쇄 작업 - Facades
type: docs
weight: 10
url: /net/working-with-pdf-printing-facades/
description: 이 섹션에서는 PdfFileEditor 클래스를 사용하여 Aspose.PDF Facades로 PDF 파일을 인쇄하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## 프린터 및 페이지 설정을 사용하여 기본 프린터로 PDF 파일 인쇄

먼저 문서를 이미지로 변환한 다음 프린터로 인쇄합니다. 문서를 바인드하기 위해 BindPdf 메서드를 사용하여 PDF 파일을 기본 프린터로 인쇄할 수 있는 [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) 클래스의 인스턴스를 생성하고 특정 설정을 합니다. 예에서는 A4 형식, 세로 방향을 사용하고 있습니다. printerSettings에서, 가장 먼저 인쇄할 프린터의 이름을 지정합니다. 그렇지 않으면 기본 프린터로 인쇄됩니다. 다음으로 필요한 복사본 수를 적습니다.

```csharp
 public static void PrintingPDFFile()
        {
            // PdfViewer 객체 생성
            PdfViewer viewer = new PdfViewer();

            // 입력 PDF 파일 열기
            viewer.BindPdf(_dataDir + "sample.pdf");

            // 인쇄 속성 설정
            viewer.AutoResize = true;         // 조정된 크기로 파일 인쇄
            viewer.AutoRotate = true;         // 조정된 회전으로 파일 인쇄
            viewer.PrintPageDialog = false;   // 인쇄 시 페이지 번호 대화 상자 표시 안 함

            // 프린터 및 페이지 설정 및 PrintDocument 객체 생성
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();
            System.Drawing.Printing.PrintDocument prtdoc = new System.Drawing.Printing.PrintDocument();

            // 프린터 이름 설정
            ps.PrinterName = prtdoc.PrinterSettings.PrinterName;

            // 페이지 크기 설정 (필요한 경우)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // 페이지 여백 설정 (필요한 경우)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // 프린터 및 페이지 설정을 사용하여 문서 인쇄
            viewer.PrintDocumentWithSettings(pgs, ps);

            // 인쇄 후 PDF 파일 닫기
            viewer.Close();
        }
```

다음 코드를 사용하여 인쇄 대화 상자를 표시해 보세요:

```csharp
        public static void PrintingPDFDisplayPrintDialog()
        {
            // PdfViewer 객체 생성
            PdfViewer viewer = new PdfViewer();

            // 입력 PDF 파일 열기
            viewer.BindPdf(_dataDir + "sample.pdf");

            // 인쇄를 위한 속성 설정
            viewer.AutoResize = true;         // 조정된 크기로 파일 인쇄
            viewer.AutoRotate = true;         // 조정된 회전으로 파일 인쇄

            // 프린터 및 페이지 설정과 PrintDocument를 위한 객체 생성

            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings
            {

                // PageSize 설정 (필요한 경우)
                PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169),

                // PageMargins 설정 (필요한 경우)
                Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0)
            };

            System.Windows.Forms.PrintDialog printDialog = new System.Windows.Forms.PrintDialog();
            if (printDialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
            {
                // 문서 인쇄 코드가 여기에 위치합니다
                // 프린터 및 페이지 설정을 사용하여 문서 인쇄
                System.Drawing.Printing.PrinterSettings ps = printDialog.PrinterSettings;
                viewer.PrintDocumentWithSettings(pgs, ps);
            }

            // 인쇄 후 PDF 파일 닫기
            viewer.Close();
        }
```

## PDF를 소프트 프린터로 인쇄

파일로 출력하는 프린터가 있습니다. 가상 프린터의 이름을 설정하고, 이전 예제와 유사하게 설정을 합니다.

```csharp
public static void PrintingPDFToSoftPrinter()
        {
            // PdfViewer 객체 생성
            PdfViewer viewer = new PdfViewer();

            // 입력 PDF 파일 열기
            viewer.BindPdf(_dataDir + "sample.pdf");

            // 인쇄 속성 설정
            viewer.AutoResize = true;         // 조정된 크기로 파일 인쇄
            viewer.AutoRotate = true;         // 조정된 회전으로 파일 인쇄
            viewer.PrintPageDialog = false;   // 인쇄 시 페이지 번호 대화 상자 표시 안 함

            viewer.PrintAsImage = false;

            // 프린터 및 페이지 설정, PrintDocument를 위한 객체 생성
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // 프린터 이름 설정
            ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
            // 또는 PDF 프린터 설정
            //ps.PrinterName = "Adobe PDF";

            // 페이지 크기 설정 (필요한 경우)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // 페이지 여백 설정 (필요한 경우)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // 프린터 및 페이지 설정을 사용하여 문서 인쇄
            viewer.PrintDocumentWithSettings(pgs, ps);

            // 인쇄 후 PDF 파일 닫기
            viewer.Close();
        }
```

## 인쇄 대화상자 숨기기

Aspose.PDF for .NET은 인쇄 대화상자를 숨길 수 있습니다. 이를 위해 [PrintPageDialog](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/properties/printpagedialog) 메서드를 사용하세요.

다음 코드 스니펫은 인쇄 대화상자를 숨기는 방법을 보여줍니다.

```csharp
public static void PrintingPDFHidePrintDialog()
        {
            // PdfViewer 객체 생성
            PdfViewer viewer = new PdfViewer();

            // 입력 PDF 파일 열기
            viewer.BindPdf(_dataDir + "sample.pdf");

            // 인쇄를 위한 속성 설정
            viewer.AutoResize = true;         // 조정된 크기로 파일 인쇄
            viewer.AutoRotate = true;         // 조정된 회전으로 파일 인쇄

            viewer.PrintPageDialog = false;   // 인쇄 시 페이지 번호 대화상자 생성하지 않음

            // 프린터, 페이지 설정, PrintDocument 객체 생성
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // XPS/PDF 프린터 이름 설정
            ps.PrinterName = "OneNote for Windows 10";

            // PageSize 설정 (필요한 경우)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // PageMargins 설정 (필요한 경우)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // 프린터와 페이지 설정을 사용하여 문서 인쇄
            viewer.PrintDocumentWithSettings(pgs, ps);

            // 인쇄 후 PDF 파일 닫기
            viewer.Close();
        }
```

## 색상 PDF를 XPS 파일로 회색조로 인쇄하기

색상 PDF 문서는 [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer)를 사용하여 XPS 프린터로 회색조로 인쇄할 수 있습니다. 이를 위해서는 PdfViewer.PrintAsGrayscale 속성을 사용하고 *true*로 설정해야 합니다. 다음 코드 스니펫은 PdfViewer.PrintAsGrayscale 속성의 구현을 보여줍니다.

```csharp
public static void PrintingPDFasGrayscale()
        {
            // PdfViewer 객체 생성
            PdfViewer viewer = new PdfViewer();

            // 입력 PDF 파일 열기
            viewer.BindPdf(_dataDir + "sample.pdf");

            // 인쇄를 위한 속성 설정
            viewer.AutoResize = true;         // 조정된 크기로 파일 인쇄
            viewer.AutoRotate = true;         // 조정된 회전으로 파일 인쇄


            viewer.PrintPageDialog = false;   // 인쇄 시 페이지 번호 대화 상자 표시 안 함
            viewer.PrintAsGrayscale = false;

            // 프린터 및 페이지 설정 및 PrintDocument를 위한 객체 생성
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // XPS/PDF 프린터 이름 설정
            ps.PrinterName = "OneNote for Windows 10";

            // 페이지 크기 설정 (필요한 경우)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // 페이지 여백 설정 (필요한 경우)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // 프린터 및 페이지 설정을 사용하여 문서 인쇄
            viewer.PrintDocumentWithSettings(pgs, ps);

            // 인쇄 후 PDF 파일 닫기
            viewer.Close();
        }
```

## PDF to PostScript 변환

[PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) 클래스는 PDF 문서를 인쇄할 수 있는 기능을 제공하며, 이 클래스를 사용하여 PDF 파일을 PostScript 형식으로 변환할 수도 있습니다. PDF 파일을 PostScript로 변환하려면 PS 프린터를 설치하고 PdfViewer를 사용하여 파일로 인쇄하면 됩니다.

다음 코드 스니펫은 PDF를 인쇄하고 PostScript 형식으로 변환하는 방법을 보여줍니다.

```csharp
public static void PrintingPDFToPostScript()
        {
            // PdfViewer 객체 생성
            PdfViewer viewer = new PdfViewer();

            // 입력 PDF 파일 열기
            viewer.BindPdf(_dataDir + "sample.pdf");

            // 인쇄를 위한 속성 설정
            viewer.AutoResize = true;         // 조정된 크기로 파일 인쇄
            viewer.AutoRotate = true;         // 조정된 회전으로 파일 인쇄
            viewer.PrintPageDialog = false;   // 인쇄 시 페이지 번호 대화상자 생성 안 함

            viewer.PrintAsImage = false;

            // 프린터 및 페이지 설정과 PrintDocument 객체 생성
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // XPS/PDF 프린터 이름 설정
            ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
            // 출력 파일 이름과 PrintToFile 속성 설정
            ps.PrintFileName = _dataDir + "PdfToPostScript_out.ps";
            ps.PrintToFile = true;

            // PageSize 설정 (필요한 경우)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // PageMargins 설정 (필요한 경우)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // 프린터 및 페이지 설정을 사용하여 문서 인쇄
            viewer.PrintDocumentWithSettings(pgs, ps);

            // 인쇄 후 PDF 파일 닫기
            viewer.Close();
        }
```

## 인쇄 작업 상태 확인

PDF 파일은 물리적 프린터뿐만 아니라 Microsoft XPS 문서 작성기에도 [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) 클래스를 사용하여 인쇄 대화 상자를 표시하지 않고 인쇄할 수 있습니다. 큰 PDF 파일을 인쇄할 때, 프로세스가 오래 걸릴 수 있으므로 사용자는 인쇄 프로세스가 완료되었는지 문제를 겪었는지 확신하지 못할 수 있습니다. 인쇄 작업의 상태를 확인하려면 PrintStatus 속성을 사용합니다. 다음 코드 스니펫은 PDF 파일을 XPS 파일로 인쇄하고 인쇄 상태를 확인하는 방법을 보여줍니다.

```csharp
public static void CheckingPrintJobStatus()
        {
            // PdfViewer 객체 생성
            PdfViewer viewer = new PdfViewer();

            // 입력 PDF 파일 열기
            viewer.BindPdf(_dataDir + "sample1.pdf");

            // 인쇄를 위한 속성 설정
            viewer.AutoResize = true;         // 조정된 크기로 파일 인쇄
            viewer.AutoRotate = true;         // 조정된 회전으로 파일 인쇄
            viewer.PrintPageDialog = false;   // 인쇄 시 페이지 번호 대화 상자 생성 안 함

            viewer.PrintAsImage = false;

            // 프린터 및 페이지 설정, PrintDocument 객체 생성
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // XPS/PDF 프린터 이름 설정
            ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
            // 출력 파일 이름 및 PrintToFile 속성 설정
            ps.PrintFileName = _dataDir + "PdfToPostScript_out.ps";
            ps.PrintToFile = true;

            // PageSize 설정 (필요한 경우)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // PageMargins 설정 (필요한 경우)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // 프린터 및 페이지 설정으로 문서 인쇄
            viewer.PrintDocumentWithSettings(pgs, ps);

            // 인쇄 상태 확인
            if (viewer.PrintStatus != null && viewer.PrintStatus is Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            else
            {
                // 오류가 발견되지 않았습니다. 인쇄 작업이 성공적으로 완료되었습니다.
                Console.WriteLine("Printing completed without any issue..");
            }

            // 인쇄 후 PDF 파일 닫기
            viewer.Close();
        }

        struct PrintingJobSettings
        {
            public int ToPage { get; set; }
            public int FromPage { get; set; }
            public string OutputFile { get; set; }
            public System.Drawing.Printing.Duplex Mode { get; set; }
        }
```

## Simplex 및 Duplex 모드로 페이지 인쇄

특정 인쇄 작업에서 PDF 문서의 페이지는 Duplex 모드 또는 Simplex 모드로 인쇄할 수 있지만 단일 인쇄 작업 내에서 일부 페이지는 Simplex로, 일부 페이지는 Duplex로 인쇄할 수 없습니다. 그러나 이러한 요구 사항을 충족하기 위해 다른 페이지 범위 및 PrintingJobSettings 객체를 사용할 수 있습니다. 다음 코드 스니펫은 PDF 파일의 일부 페이지를 Simplex 모드로, 일부 페이지를 Duplex 모드로 인쇄하는 방법을 보여줍니다.

```csharp
 public static void PrintingPagesInSimplexAndDuplexMode()
        {
            int printingJobIndex = 0;
            string inPdf = _dataDir + "sample-8page.pdf";
            string output = _dataDir;
            IList<PrintingJobSettings> printingJobs = new List<PrintingJobSettings>();

            PrintingJobSettings printingJob1 = new PrintingJobSettings
            {
                FromPage = 1,
                ToPage = 3,
                OutputFile = output + "sample_1_3.xps",
                Mode = Duplex.Default
            };

            printingJobs.Add(printingJob1);

            PrintingJobSettings printingJob2 = new PrintingJobSettings
            {
                FromPage = 4,
                ToPage = 6,
                OutputFile = output + "sample_4_6.xps",
                Mode = Duplex.Simplex
            };

            printingJobs.Add(printingJob2);

            PrintingJobSettings printingJob3 = new PrintingJobSettings
            {
                FromPage = 7,
                ToPage = 7,
                OutputFile = output + "sample_7.xps",
                Mode = Duplex.Default
            };

            printingJobs.Add(printingJob3);

            PdfViewer viewer = new PdfViewer();

            viewer.BindPdf(inPdf);
            viewer.AutoResize = true;
            viewer.AutoRotate = true;
            viewer.PrintPageDialog = false;

            PrinterSettings ps = new PrinterSettings();
            PageSettings pgs = new PageSettings();

            ps.PrinterName = "Microsoft XPS Document Writer";
            ps.PrintFileName = System.IO.Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
            ps.PrintToFile = true;
            ps.FromPage = printingJobs[printingJobIndex].FromPage;
            ps.ToPage = printingJobs[printingJobIndex].ToPage;
            ps.Duplex = printingJobs[printingJobIndex].Mode;
            ps.PrintRange = PrintRange.SomePages;

            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);
            ps.DefaultPageSettings.PaperSize = pgs.PaperSize;
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            viewer.EndPrint += (sender, args) =>
            {
                if (++printingJobIndex < printingJobs.Count)
                {
                    ps.PrintFileName = System.IO.Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
                    ps.FromPage = printingJobs[printingJobIndex].FromPage;
                    ps.ToPage = printingJobs[printingJobIndex].ToPage;
                    ps.Duplex = printingJobs[printingJobIndex].Mode;
                    viewer.PrintDocumentWithSettings(pgs, ps);
                }
            };

            viewer.PrintDocumentWithSettings(pgs, ps);
        }
```