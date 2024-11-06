---
title: PDF에서 이미지 추출 및 바코드 인식
type: docs
weight: 20
url: ko/net/extract-images-from-pdf-and-recognize-barcodes/
---

{{% alert color="primary" %}}

PDF 문서는 일반적으로 텍스트, 이미지, 표, 첨부 파일, 그래프, 주석 및 기타 관련 객체로 구성됩니다. PDF 파일 내에 바코드가 포함되어 있고 일부 고객은 PDF 파일 내에 존재하는 바코드를 식별할 필요가 있습니다. 다음 기사에서는 PDF 페이지에서 이미지를 추출하고 그 안에 있는 바코드를 식별하는 방법에 대한 단계를 설명합니다.

{{% /alert %}}

Aspose.PDF for .NET의 문서 객체 모델에 따르면, PDF 파일은 하나 이상의 페이지를 포함하며 각 페이지는 리소스 객체에서 이미지, 폼 및 폰트의 컬렉션을 포함합니다.
Aspose.PDF for .NET의 문서 객체 모델에 따르면, PDF 파일은 하나 이상의 페이지를 포함하며 각 페이지에는 리소스 객체에 이미지, 양식, 글꼴의 컬렉션이 포함됩니다.

**C#**

```csharp
//문서 열기
Aspose.PDF.Document pdfDocument = new Aspose.PDF.Document("source.pdf");

// PDF 파일의 개별 페이지를 순회
for (int pageCount = 1; pageCount <= pdfDocument.Pages.Count; pageCount++)
{
    // PDF 페이지에서 추출된 각 이미지를 순회
    foreach (XImage xImage in pdfDocument.Pages[pageCount].Resources.Images)
    {
        using (MemoryStream imageStream = new MemoryStream())
        {
            //출력 이미지 저장
            xImage.Save(imageStream, System.Drawing.Imaging.ImageFormat.Jpeg);

            // 스트림 위치를 스트림의 시작으로 설정
            imageStream.Position = 0;

            // BarCodeReader 객체 인스턴스화
            Aspose.BarCodeRecognition.BarCodeReader barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);

            while (barcodeReader.Read())
            {
                // 바코드 이미지에서 바코드 텍스트 가져오기
                string code = barcodeReader.GetCodeText();

                // 콘솔 출력으로 바코드 텍스트 작성
                Console.WriteLine("BARCODE : " + code);
            }

            // 이미지 파일을 해제하기 위해 BarCodeReader 객체 닫기
            barcodeReader.Close();
        }
    }
}
```

이 문서에서 다룬 주제에 대한 자세한 정보는 다음 링크를 방문하십시오.

- [PDF 파일에서 이미지 추출하기](/net/extract-images-from-the-pdf-file/)
- [바코드 읽기](https://docs.aspose.com/barcode/net/read-barcodes/)
