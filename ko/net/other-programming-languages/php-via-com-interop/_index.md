---
title: PHP를 통한 COM Interop
type: docs
weight: 50
url: ko/net/php-via-com-interop/
---

## 전제 조건

{{% alert color="primary" %}}
COM과 함께 작동하도록 PHP를 구성하십시오. 자세한 내용은 <http://www.php.net/manual/en/ref.com.php>를 참조하세요. 자세한 내용은 [Use Aspose.pdf for .NET via COM Interop](/pdf/net/use-aspose-pdf-for-net-via-com-interop/)라는 기사를 확인하세요.

{{% /alert %}}

## Hello World! 예제

{{% alert color="primary" %}}
이것은 PHP를 통해 COM Interop을 사용하여 새 PDF 파일을 생성하고 [Aspose.PDF for .NET](/pdf/net/)를 사용하여 PDF 파일에 텍스트를 추가하는 간단한 애플리케이션을 보여줍니다.

{{% /alert %}}

```php
<?php
echo "<h2>PHP를 사용하여 COM 상호 운용성을 통해 Aspose.PDF for .NET 호출</h2>";
echo "<h3>PDF에서 Excel로 변환</h3>";

//라이센스 설정
$lic = new COM("Aspose.PDF.License");
$lic->SetLicense("C:/temp/Aspose.Total.lic");

//Pdf 문서 로드
$input="C:/temp/HelloWorld.pdf";
$helper = new COM("Aspose.PDF.ComHelper");

$pdf = $helper->OpenFile($input);

// 원하는 파일 형식으로 PDF 문서를 저장합니다. 이 경우 형식에 대해 SaveFormat 열거 값 9를 전달합니다.

$output = "C:/temp/test_php.xls";
$pdf->Save_4($output,9);
?>
```

