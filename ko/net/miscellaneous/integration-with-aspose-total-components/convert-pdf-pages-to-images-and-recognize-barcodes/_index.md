---
title: PDF 페이지를 이미지로 변환하고 바코드 인식
type: docs
weight: 10
url: /ko/net/convert-pdf-pages-to-images-and-recognize-barcodes/
---

{{% alert color="primary" %}}

PDF 문서는 일반적으로 텍스트, 이미지, 표, 첨부 파일, 그래프, 주석 및 기타 객체로 구성됩니다. 일부 고객은 문서에 바코드를 삽입한 다음 PDF 파일에서 바코드를 식별해야 합니다. 다음 기사에서는 PDF 파일의 페이지를 이미지로 변환하고 Aspose.Barcode for .NET을 사용하여 이미지에서 바코드를 식별하는 방법에 대해 설명합니다.

{{% /alert %}}
### **페이지를 이미지로 변환하고 바코드 인식**

{{% alert color="primary" %}}

Aspose.PDF for .NET은 PDF 문서를 관리하는 매우 강력한 제품입니다. 이 제품을 사용하면 PDF 문서의 페이지를 이미지로 쉽게 변환할 수 있습니다. Aspose.BarCode for .NET도 바코드를 생성하고 인식하는 데 매우 강력한 제품입니다.

Aspose.PDF.Facades 네임스페이스 아래의 PdfConverter 클래스는 PDF 페이지를 다양한 이미지 포맷으로 변환하는 것을 지원합니다.
#### **Aspose.PDF.Facades 사용하기**

{{% alert color="primary" %}}

PdfConverter 클래스에는 현재 PDF 페이지에서 이미지를 생성하는 GetNextImage라는 메소드가 포함되어 있습니다. 출력 이미지 형식을 지정하기 위해, 이 메소드는 System.Drawing.Imaging.ImageFormat 열거형에서 인자를 받습니다.

Aspose.Barcode에는 BarCodeRecognition이라는 네임스페이스가 포함되어 있으며, 이 안에는 BarCodeReader 클래스가 있습니다. BarCodeReader 클래스를 사용하면 이미지 파일에서 바코드를 읽고, 판별하고, 식별할 수 있습니다.

이 예제의 목적을 위해, Aspose.PDF.Facades.PdfConverter를 사용하여 PDF 파일의 페이지를 이미지로 변환하세요.
{{% /alert %}}

##### **프로그래밍 샘플**
**C#**

{{< highlight csharp >}}

 //PdfConverter 객체 생성

PdfConverter converter = new PdfConverter();

//입력 PDF 파일 바인딩

converter.BindPdf("Source.pdf");

// 처리할 시작 페이지 지정

converter.StartPage = 1;

// 처리할 마지막 페이지 지정

converter.EndPage = 1;

// 결과 이미지의 해상도를 지정하는 Resolution 객체 생성

converter.Resolution = new Aspose.PDF.Devices.Resolution(300);

//변환 과정 초기화

converter.DoConvert();

// 결과 이미지를 저장할 MemoryStream 객체 생성

MemoryStream imageStream = new MemoryStream();

// 페이지가 존재하는지 확인하고 이미지로 변환

while (converter.HasNextImage())

{

    // 주어진 이미지 형식으로 이미지 저장

    converter.GetNextImage(imageStream, System.Drawing.Imaging.ImageFormat.Png);

    // 스트림 위치를 스트림의 시작으로 설정

    imageStream.Position = 0;

{{< /highlight >}}

스트림 위치를 스트림 시작 부분으로 설정

imageStream.Position = 0;

BarCodeReader 객체 인스턴스화

Aspose.BarCodeRecognition.BarCodeReader barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);

바코드를 읽는 동안

while (barcodeReader.Read())

{

    바코드 이미지에서 바코드 텍스트 가져오기

    string code = barcodeReader.GetCodeText();

    콘솔 출력으로 바코드 텍스트 작성

    Console.WriteLine("BARCODE : " + code);

}

BarCodeReader 객체를 닫아 이미지 파일을 해제

barcodeReader.Close();

}

PdfConverter 인스턴스를 닫고 리소스 해제

converter.Close();

이미지 객체를 포함하는 스트림 닫기

imageStream.Close();

{{< /highlight >}}

{{% alert color="primary" %}}

위 코드 스니펫에서 출력 이미지는 MemoryStream 객체에 저장됩니다.
```
위 코드 스니펫에서 출력 이미지는 MemoryStream 객체에 저장됩니다.

{{% /alert %}}

{anchor:devices]
#### **PngDevice 클래스 사용하기**
Aspose.PDF.Devices에는 PngDevice가 있습니다. 이 클래스는 PDF 문서의 페이지를 PNG 이미지로 변환할 수 있습니다.

이 예제의 목적으로, 소스 PDF 파일을 Document로 로드하고 문서의 페이지를 PNG 이미지로 변환합니다. 이미지가 생성되면 Aspose.BarCodeRecognition 아래의 BarCodeReader 클래스를 사용하여 이미지에서 바코드를 식별하고 읽습니다.

{{% alert color="primary" %}}

여기 제공된 코드 샘플은 PDF 문서의 페이지를 순회하면서 각 페이지에 있는 바코드를 식별하려고 시도합니다.

{{% /alert %}}
##### **프로그래밍 샘플**
**C#**

{{< highlight csharp >}}

 //PDF 문서 열기

Aspose.PDF.Document pdfDocument = new Aspose.PDF.Document("source.pdf");

// PDF 파일의 개별 페이지를 순회

for (int pageCount = 1; pageCount <= pdfDocument.Pages.Count; pageCount++)

{

    using (MemoryStream imageStream = new MemoryStream())

using (MemoryStream imageStream = new MemoryStream())
{
    // Resolution 객체 생성
    Aspose.PDF.Devices.Resolution resolution = new Aspose.PDF.Devices.Resolution(300);

    // Resolution 객체를 인자로 받는 PngDevice 객체 인스턴스화
    Aspose.PDF.Devices.PngDevice pngDevice = new Aspose.PDF.Devices.PngDevice(resolution);

    // 특정 페이지를 변환하고 이미지를 스트림에 저장
    pngDevice.Process(pdfDocument.Pages[pageCount], imageStream);

    // 스트림 위치를 스트림의 시작부로 설정
    imageStream.Position = 0;

    // BarCodeReader 객체 인스턴스화
    Aspose.BarCodeRecognition.BarCodeReader barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);

    // String txtResult.Text = "";

    while (barcodeReader.Read())
    {
        // 바코드 이미지에서 바코드 텍스트 가져오기
        string code = barcodeReader.GetCodeText();
    }
}
```
```csharp
string code = barcodeReader.GetCodeText();

// 바코드 텍스트를 콘솔 출력에 작성합니다.

Console.WriteLine("BARCODE : " + code);

}

// BarCodeReader 객체를 닫아 이미지 파일을 해제합니다.

barcodeReader.Close();

}

}

{{< /highlight >}}



{{% alert color="primary" %}}

이 문서에서 다룬 주제에 대한 자세한 정보는 다음을 참조하세요:

- PDF 페이지를 다양한 이미지 형식으로 변환하기 (Facades)
- 모든 PDF 페이지를 PNG 이미지로 변환하기
- [바코드 읽기](https://docs.aspose.com/barcode/net/read-barcodes/)


{{% /alert %}}
```
