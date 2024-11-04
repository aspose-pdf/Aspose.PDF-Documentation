---
title: PDF 문서 연결
type: docs
weight: 10
url: /java/concatenate-pdf-documents/
description: 이 섹션은 PdfFileEditor 클래스를 사용하여 com.aspose.pdf.facades로 PDF 문서를 연결하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 파일 경로를 사용하여 PDF 파일 연결 (Facades)

[PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) 클래스의 concatenate 메소드를 사용하여 두 개의 PDF 파일을 연결할 수 있습니다. concatenate 메소드는 세 개의 매개변수를 전달할 수 있게 해줍니다: 첫 번째 입력 PDF, 두 번째 입력 PDF, 그리고 출력 PDF입니다. 최종 출력 PDF는 두 입력 PDF 파일을 포함합니다.

다음 코드 스니펫은 파일 경로를 사용하여 PDF 파일을 연결하는 방법을 보여줍니다.

```java
    public static void ConcatenatePDFfilesUsingFilePaths01() {
        // PdfFileEditor 객체 생성
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // 파일 연결
        pdfEditor.concatenate(_dataDir + "Sample-Document-01.pdf", _dataDir + "Sample-Document-02.pdf",
                _dataDir + "Concatenate_Result_01.pdf");
    }
```


일부 경우, 개요가 많은 경우 사용자는 **CopyOutlines**를 false로 설정하여 결합 성능을 향상시킬 수 있습니다.

```java
  public static void ConcatenatePDFfilesUsingFilePaths02() {
        // PdfFileEditor 객체 생성
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // 파일 결합
        String[] inputFiles = Directory.GetFiles(_dataDir, "Sample-Document-0?.pdf");
        pdfEditor.CopyOutlines = false;
        var res = pdfEditor.Concatenate(inputFiles, _dataDir + "Concatenate_Result_02.pdf");
        Console.WriteLine(res);
    }
```

## MemoryStreams를 사용하여 여러 PDF 파일 결합

[PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor)의 [Concatenate](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#concatenate-com.aspose.pdf.IDocument:A-com.aspose.pdf.IDocument-) 메서드는 소스 PDF 파일과 대상 PDF 파일을 매개변수로 사용합니다.
 이러한 매개변수는 디스크에 있는 PDF 파일의 경로일 수도 있고, MemoryStreams일 수도 있습니다. 이제 이 예제에서는 먼저 디스크에서 PDF 파일을 읽기 위한 두 개의 파일 스트림을 생성합니다. 그런 다음 이 파일들을 바이트 배열로 변환합니다. PDF 파일의 바이트 배열은 MemoryStreams로 변환됩니다. PDF 파일에서 MemoryStreams를 얻으면 이를 연결 메서드에 전달하여 단일 출력 파일로 병합할 수 있게 됩니다.

다음 코드 스니펫은 MemoryStreams를 사용하여 여러 PDF 파일을 연결하는 방법을 보여줍니다:

```java
    public static void ConcatenateMultiplePDFfilesUsingMemoryStreams()
        {
            // PDF 파일을 읽기 위한 두 파일 스트림 생성
            FileInputStream fs1 = new FileInputStream(_dataDir + "Sample-Document-01.pdf");
            FileInputStream fs2 = new FileInputStream(_dataDir + "Sample-Document-02.pdf");

            // PDF 파일의 내용을 저장할 바이트 배열 생성
            byte[] buffer1 = new byte[Convert.ToInt32(fs1.le)];
            byte[] buffer2 = new byte[Convert.ToInt32(fs2.Length)];

            // PDF 파일 내용을 바이트 배열로 읽기
            fs1.Read(buffer1, 0, Convert.ToInt32(fs1.Length));
            fs2.Read(buffer2, 0, Convert.ToInt32(fs2.Length));

            // 이제 바이트 배열을 MemoryStreams로 변환한 후 해당 스트림을 연결
            using (MemoryStream pdfStream = new MemoryStream())
            {
                using (MemoryStream fileStream1 = new MemoryStream(buffer1))
                {
                    using (MemoryStream fileStream2 = new MemoryStream(buffer2))
                    {
                        // 스트림을 연결하기 위한 PdfFileEditor 클래스의 인스턴스 생성
                        PdfFileEditor pdfEditor = new PdfFileEditor();
                        // 두 입력 MemoryStreams를 연결하고 출력 MemoryStream에 저장
                        pdfEditor.Concatenate(fileStream1, fileStream2, pdfStream);
                        // MemoryStream을 다시 바이트 배열로 변환
                        byte[] data = pdfStream.ToArray();
                        // 출력 PDF 파일을 저장하기 위한 FileStream 생성
                        FileStream output = new FileStream(_dataDir + "Concatenate_Result_03.pdf", FileMode.Create,
                        FileAccess.Write);
                        // 출력 파일 스트림에 바이트 배열 내용 쓰기
                        output.Write(data, 0, data.Length);
                        // 출력 파일 닫기
                        output.Close();
                    }
                }
            }
            // 입력 파일 닫기
            fs1.Close();
            fs2.Close();
        }
```

## 여러 PDF 파일을 파일 경로로 연결하기 (Facades)

여러 PDF 파일을 연결하려면 파일 경로의 배열을 전달할 수 있는 연결 메서드의 오버로드를 사용할 수 있습니다. 최종 출력은 배열의 모든 파일에서 생성된 병합 파일로 저장됩니다.

다음 코드 스니펫은 파일 경로를 사용하여 PDF 파일 배열을 연결하는 방법을 보여줍니다.

```java
 public static void ConcatenateArrayOfPDFfilesUsingFilePaths() {
        // PdfFileEditor 객체 생성
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // 파일 배열
        string[] filesArray = new string[2];
        filesArray[0] = _dataDir + "Sample-Document-01.pdf";
        filesArray[1] = _dataDir + "Sample-Document-02.pdf";
        // 파일 연결
        pdfEditor.Concatenate(filesArray, _dataDir + "Concatenate_Result_04.pdf");
    }
```

## 스트림을 사용하여 PDF 파일 배열 연결하기 (Facades)

PDF 파일 배열 연결은 디스크에 있는 파일에만 국한되지 않습니다.
 You can also concatenate an array of PDF files from streams. If you want to concatenate multiple PDF files, you can use the appropriate overload of the Concatenate method. First, you need to create an array of input streams and one stream for output PDF and then call the Concatenate method. The output will be saved in the output stream.

다음 코드 스니펫은 스트림을 사용하여 PDF 파일 배열을 연결하는 방법을 보여줍니다.

```java
   public static void ConcatenateArrayOfPDFfilesUsingStreams() {
        // PdfFileEditor 객체 생성
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // 스트림 배열
        FileStream[] inputStreams = new FileStream[2];
        inputStreams[0] = new FileStream(_dataDir + "Sample-Document-01.pdf", FileMode.Open);
        inputStreams[1] = new FileStream(_dataDir + "Sample-Document-02.pdf", FileMode.Open);
        // 출력 스트림
        FileStream outputStream = new FileStream(_dataDir + "Concatenate_Result_05.pdf", FileMode.Create);
        // 파일 연결
        pdfEditor.Concatenate(inputStreams, outputStream);
    }
```

## PDF 양식 연결 및 필드 이름 고유성 유지

[com.aspose.pdf.facades](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/package-frame) 네임스페이스의 P[PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) 클래스는 PDF 파일을 연결할 수 있는 기능을 제공합니다.
 이제 병합할 Pdf 파일에 유사한 필드 이름을 가진 양식 필드가 있는 경우, Aspose.PDF는 결과 Pdf 파일에서 필드를 고유하게 유지하는 기능을 제공하며, 필드 이름을 고유하게 만들기 위해 접미사를 지정할 수도 있습니다. PdfFileEditor의 [KeepFieldsUnique](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#getKeepFieldsUnique--) 메서드를 true로 설정하면 Pdf 양식이 병합될 때 필드 이름이 고유하게 됩니다. 또한, PdfFileEditor의 [UniqueSuffix](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#getUniqueSuffix--) 메서드를 사용하여 양식이 병합될 때 필드 이름에 추가되어 고유하게 만드는 사용자 정의 접미사의 형식을 지정할 수 있습니다. 이 문자열에는 %NUM% 서브스트링이 포함되어 있어야 하며, 결과 파일에서 숫자로 대체됩니다.

이 기능을 구현하기 위한 간단한 코드 스니펫은 다음과 같습니다.

```java
  public static void ConcatenatePDFformsAndKeepFieldsNamesUnique()
        {
            // 입력 및 출력 파일 경로 설정

            string inputFile1 = _dataDir + "Sample-Form-01.pdf";
            string inputFile2 = _dataDir + "Sample-Form-02.pdf";
            string outFile = _dataDir + "ConcatenatePDFForms_out.pdf";

            // PdfFileEditor 객체 인스턴스화
            PdfFileEditor fileEditor = new PdfFileEditor
            {
                // 모든 필드에 대해 고유한 필드 ID를 유지하기 위해
                KeepFieldsUnique = true,
                // 양식이 병합될 때 필드 이름에 추가되어 고유하게 만드는 접미사의 형식
                UniqueSuffix = "_%NUM%"
            };

            // 파일을 병합하여 결과 Pdf 파일로 만듦
            fileEditor.Concatenate(inputFile1, inputFile2, outFile);
        }
```

## 빈 페이지 삽입으로 병합

PDF 파일이 병합되면, 문서의 시작 부분에 빈 페이지를 삽입할 수 있습니다. 여기서 목차를 만들 수 있습니다. 이 요구 사항을 달성하기 위해, 병합된 파일을 Document 객체에 로드하고 Page.Insert(…) 메서드를 호출하여 빈 페이지를 삽입해야 합니다.

```java
   public static void ConcatenatePDF_InsertBlankPage() {
        // PdfFileEditor 객체 생성
        PdfFileEditor pdfEditor = new PdfFileEditor();
        var documents = new Aspose.Pdf.Document[3];
        documents[0] = new Aspose.Pdf.Document(_dataDir + "Sample-Document-01.pdf");
        documents[1] = new Aspose.Pdf.Document(_dataDir + "Sample-Document-02.pdf");
        var destinationDoc = new Aspose.Pdf.Document();
        destinationDoc.Pages.Add();
        // 파일 병합
        pdfEditor.Concatenate(documents, destinationDoc);
        destinationDoc.Save(_dataDir + "Concatenate_Result_06.pdf");
    }
```