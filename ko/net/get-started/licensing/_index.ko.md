---
title: Aspose PDF 라이선스
linktitle: 라이선스 및 제한사항
type: docs
weight: 90
url: /net/licensing/
description: Aspose. PDF for .NET은 고객에게 클래식 라이선스와 미터드 라이선스를 제공합니다. 또한 제품을 더 잘 탐색할 수 있도록 제한된 라이선스를 사용할 수 있습니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 평가 버전의 제한

우리는 고객이 구매하기 전에 우리의 구성요소를 철저히 테스트하기를 원합니다. 그래서 평가 버전을 통해 평상시처럼 사용할 수 있습니다.

- **평가 워터마크가 있는 PDF 생성.** Aspose.PDF for .NET의 평가 버전은 전체 제품 기능을 제공하지만 생성된 PDF 문서의 모든 페이지 상단에 "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd"라는 워터마크가 있습니다.

- **처리할 수 있는 컬렉션 항목 수의 제한.**
평가 버전에서는 모든 컬렉션에서 요소를 단 4개만 처리할 수 있습니다(예: 페이지 4개, 폼 필드 4개 등).
평가 버전에서는 어떤 컬렉션에서든 단 4개의 요소만 처리할 수 있습니다(예: 단 4페이지, 4개의 폼 필드 등).

Aspose.HTML for .NET의 평가 제한 없이 테스트하고 싶다면, 30일 임시 라이선스도 요청할 수 있습니다. [임시 라이선스는 어떻게 받나요?](https://purchase.aspose.com/temporary-license)를 참조해 주세요.

## 고전 라이선스

라이선스는 파일이나 스트림 객체에서 로드할 수 있습니다. 라이선스를 설정하는 가장 쉬운 방법은 Aspose.PDF.dll 파일과 같은 폴더에 라이선스 파일을 넣고 경로 없이 파일 이름만 지정하는 것입니다. 아래 예시와 같습니다.

Aspose.PDF for .NET과 함께 다른 Aspose for .NET 컴포넌트를 사용하는 경우, [Aspose.Pdf.License](https://reference.aspose.com/pdf/net/aspose.pdf/license)와 같이 라이선스의 네임스페이스를 지정해 주세요.

### 파일에서 라이선스 로드

라이선스를 적용하는 가장 쉬운 방법은 Aspose.PDF.dll 파일과 같은 폴더에 라이선스 파일을 넣고 경로 없이 파일 이름만 지정하는 것입니다.

[SetLicense](https://reference.aspose.com/pdf/net/aspose.pdf/license/methods/setlicense/index) 메소드를 호출할 때, 전달하는 라이선스 이름은 라이선스 파일의 이름이어야 합니다.
[SetLicense](https://reference.aspose.com/pdf/net/aspose.pdf/license/methods/setlicense/index) 메소드를 호출할 때, 전달하는 라이선스 이름은 라이선스 파일의 이름과 동일해야 합니다.

```csharp
public static void SetLicenseExample()
{
    // 라이선스 객체 초기화
    Aspose.Pdf.License license = new Aspose.Pdf.License();
    try
    {
        // 라이선스 설정
        license.SetLicense("Aspose.Pdf.lic");
    }
    catch (Exception)
    {
        // 문제가 발생함
        throw;
    }
    Console.WriteLine("라이선스가 성공적으로 설정됐습니다.");
}
```
### 스트림 객체에서 라이선스 불러오기

다음 예제는 스트림에서 라이선스를 불러오는 방법을 보여줍니다.

```csharp
public static void SetLicenseFromStream()
{
    // 라이선스 객체 초기화
    Aspose.Pdf.License license = new Aspose.Pdf.License();
    // 파일 스트림에서 라이선스 불러오기
    System.IO.FileStream myStream =
        new System.IO.FileStream(
            "Aspose.Pdf.lic",
            System.IO.FileMode.Open);
    // 라이선스 설정
    license.SetLicense(myStream);
    Console.WriteLine("라이선스가 성공적으로 설정됐습니다.");
}
```
## 미터링 라이선스

Aspose.PDF는 개발자가 미터링 키를 적용할 수 있습니다. 이것은 새로운 라이선싱 메커니즘입니다. 새로운 라이선싱 메커니즘은 기존의 라이선싱 방법과 함께 사용됩니다. API 기능의 사용량을 기준으로 청구되길 원하는 고객은 미터링 라이선스를 사용할 수 있습니다. 자세한 내용은 미터링 라이선스 FAQ 섹션을 참조하십시오.

미터링 키를 적용하기 위해 Metered라는 새 클래스가 도입되었습니다. 다음은 미터링 공개 및 개인 키를 설정하는 방법을 보여주는 샘플 코드입니다.

자세한 내용은 [미터링 라이선스 FAQ](https://purchase.aspose.com/faqs/licensing/metered) 섹션을 참조하십시오.

```csharp
public static void SetMeteredLicense()
{
    // 미터링 공개 및 개인 키 설정
    Aspose.Pdf.Metered metered = new Aspose.Pdf.Metered();
    // setMeteredKey 속성에 접근하여 공개 및 개인 키를 매개변수로 전달
    metered.SetMeteredKey(
        "<여기에 공개 키 입력>",
        "<여기에 비공개 키 입력>");

    // 디스크에서 문서를 로드합니다.
    Document doc = new Document("input.pdf");
    //문서의 페이지 수를 가져옵니다
    Console.WriteLine(doc.Pages.Count);
}
```
**Aspose.PDF for .NET**을 사용하는 COM 애플리케이션은 라이선스 클래스를 사용해야 합니다.

고려해야 할 한 가지 점:
내장 리소스는 애플리케이션에 내장 리소스로 추가된 방식대로 어셈블리에 포함됩니다. 즉, 텍스트 파일을 내장 리소스로 추가하고 결과 EXE를 메모장에서 열면 텍스트 파일의 정확한 내용을 볼 수 있습니다. 따라서 라이선스 파일을 내장 리소스로 사용할 때 누구나 간단한 텍스트 편집기에서 exe 파일을 열어 라이선스의 내용을 보거나 추출할 수 있습니다.

따라서 애플리케이션과 함께 라이선스를 내장할 때 추가 보안 계층을 추가하기 위해 라이선스를 압축/암호화한 후 어셈블리에 내장할 수 있습니다. Aspose.PDF.lic 라이선스 파일이 있다고 가정하고, 비밀번호 test를 사용하여 Aspose.PDF.zip을 만든 다음 이 zip 파일을 솔루션에 내장합니다. 라이선스를 초기화하기 위해 다음 코드 스니펫을 사용할 수 있습니다:

```csharp
using System;
using System.IO;
using System.IO.Compression;
using System.Reflection;

namespace Aspose.Pdf.Examples
{
    class ExampleLicensing
    {
        public static void LicenseDemo()
        {
            License license = new License();
            license.SetLicense(GetSecureLicenseFromStream());
            Document doc = new Document("document.pdf");
            //문서의 페이지 수를 가져옵니다
            Console.WriteLine(doc.Pages.Count);
        }

        private static Stream GetSecureLicenseFromStream()
        {
            var assembly = Assembly.GetExecutingAssembly();
            var memoryStream = new MemoryStream();
            using (var zipToOpen = assembly.GetManifestResourceStream("Aspose.Pdf.Examples.License.Aspose.PDF.zip"))
            {
                using (ZipArchive archive = new ZipArchive(zipToOpen ?? throw new InvalidOperationException(), ZipArchiveMode.Read))
                {
                    var unpackedLicense  = archive.GetEntry("Aspose.PDF.lic");
                    unpackedLicense?.Open().CopyTo(memoryStream);
                }
            }

            memoryStream.Position = 0;
            return memoryStream;
        }
    }
}
```
### 2005/01/22 이전에 구매한 라이선스 적용하기

Aspose.PDF for .NET은 이제 오래된 스타일의 라이선스를 지원하지 않습니다. 2005년 1월 22일 이전에 라이선스를 구입하셨고 Aspose.PDF의 최신 버전으로 업데이트하신 경우, 새 라이선스 파일을 받기 위해 영업팀에 문의하십시오.
