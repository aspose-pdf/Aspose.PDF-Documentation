---
title: Aspose PDF 라이센스
linktitle: 라이센스 및 제한 사항
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /ko/net/licensing/
description: Aspose.PDF for .NET는 고객에게 클래식 라이센스와 미터 라이센스를 받을 것을 권장합니다. 또한 제품을 더 잘 탐색할 수 있도록 제한된 라이센스를 사용할 수 있습니다.
lastmod: "2025-02-07"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Aspose PDF for .NET License",
    "alternativeHeadline": "Licensing Options for Aspose.PDF for .NET Users",
    "abstract": "Aspose PDF for .NET은 고정 가격과 사용 기반 청구 옵션 중에서 선택할 수 있는 클래식 및 미터 라이센스를 포함한 강력한 라이센스 프레임워크를 소개합니다. 클래식 라이센스는 파일 또는 스트림에서 쉽게 로드할 수 있으며, 혁신적인 미터 라이센스는 API 사용량에 따라 유연한 계량을 제공하여 다양한 사용자 요구를 충족합니다. 이 이중 라이센스 전략은 개발자를 위한 PDF 솔루션의 접근성과 확장성을 향상시킵니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "869",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/licensing/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/licensing/"
    },
    "dateModified": "2025-02-07",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

## 평가 버전의 제한 사항

고객이 구매하기 전에 구성 요소를 철저히 테스트할 수 있도록 평가 버전에서는 일반적으로 사용하는 것처럼 사용할 수 있습니다.

- **평가 워터마크가 있는 PDF 생성.** Aspose.PDF for .NET의 평가 버전은 전체 제품 기능을 제공하지만 생성된 PDF 문서의 모든 페이지 상단에 "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2025 Aspose Pty Ltd."라는 텍스트가 워터마크로 표시됩니다.

- **처리할 수 있는 페이지 수 제한.**
평가 버전에서는 문서의 처음 네 페이지만 처리할 수 있습니다.

> 평가 버전의 제한 없이 Aspose.PDF for .NET을 테스트하려면 30일 임시 라이센스를 요청할 수도 있습니다. [임시 라이센스를 받는 방법?](https://purchase.aspose.com/temporary-license)를 참조하십시오.

## 클래식 라이센스

라이센스는 파일 또는 스트림 객체에서 로드할 수 있습니다. 라이센스를 설정하는 가장 쉬운 방법은 라이센스 파일을 Aspose.PDF.dll 파일과 동일한 폴더에 두고 경로 없이 파일 이름만 지정하는 것입니다. 아래 예제와 같이.

Aspose.PDF for .NET와 함께 다른 Aspose for .NET 구성 요소를 사용하는 경우 [Aspose.Pdf.License](https://reference.aspose.com/pdf/net/aspose.pdf/license)와 같이 라이센스의 네임스페이스를 지정하십시오.

### 파일에서 라이센스 로드하기

라이센스를 적용하는 가장 쉬운 방법은 라이센스 파일을 Aspose.PDF.dll 파일과 동일한 폴더에 두고 경로 없이 파일 이름만 지정하는 것입니다.

[SetLicense](https://reference.aspose.com/pdf/net/aspose.pdf/license/methods/setlicense/index) 메서드를 호출할 때 전달하는 라이센스 이름은 라이센스 파일의 이름이어야 합니다. 예를 들어, 라이센스 파일 이름을 "Aspose.PDF.lic.xml"로 변경하면 해당 파일 이름을 Pdf.SetLicense(…) 메서드에 전달하십시오.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetLicenseExample()
{
    // Initialize license object
    var license = new Aspose.Pdf.License();
    try
    {
        // Set license
        license.SetLicense("Aspose.Pdf.lic");
    }
    catch (Exception)
    {
        // Something went wrong
        throw;
    }
    Console.WriteLine("License set successfully.");
}
```
### 스트림 객체에서 라이센스 로드하기

다음 예제는 스트림에서 라이센스를 로드하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetLicenseFromStream()
{
    // Initialize license object
    var license = new Aspose.Pdf.License();
    // Load license from the file stream
    var myStream = new FileStream(
            "Aspose.Pdf.lic",
            FileMode.Open);
    // Set license
    license.SetLicense(myStream);
    Console.WriteLine("License set successfully.");
}
```
## 미터 라이센스

Aspose.PDF는 개발자가 미터 키를 적용할 수 있도록 합니다. 미터 라이센스 메커니즘은 기존 라이센스 방법과 함께 사용됩니다. API 기능 사용량에 따라 청구되기를 원하는 고객은 미터 라이센스를 사용할 수 있습니다. 자세한 내용은 미터 라이센스 FAQ 섹션을 참조하십시오.
이 가이드는 원활한 구현을 위한 모범 사례와 라이센스 상태 변경으로 인한 중단을 방지하는 방법을 제공합니다.

"Metered" 클래스는 미터 키를 적용하는 데 사용됩니다. 다음은 미터 공개 및 비공개 키를 설정하는 방법을 보여주는 샘플 코드입니다.

자세한 내용은 [미터 라이센스 FAQ](https://purchase.aspose.com/faqs/licensing/metered) 섹션을 참조하십시오.

__미터 라이센스 방법__

미터 라이센스를 적용하려면 `SetMeteredKey` 메서드를 사용하여 공개 및 비공개 키를 제공하여 미터 라이센스를 활성화합니다. 이는 적절한 라이센스를 보장하기 위해 애플리케이션 초기화 중에 한 번 수행해야 합니다.

예시:

```csharp
 var metered = new Aspose.Pdf.Metered();
 metered.SetMeteredKey("your-public-key", "your-private-key");
 ```
라이센스 상태 확인은 `IsMeteredLicensed()`를 사용하여 미터 라이센스가 활성화되어 있는지 확인합니다.

예시:

```csharp
bool isLicensed = Aspose.Pdf.License.IsMeteredLicensed();
if (!isLicensed) 
{
    metered.SetMeteredKey("your-public-key", "your-private-key");
}
 ```
`Metered.GetConsumptionCredit()` 메서드는 소비 크레딧에 대한 정보를 가져오는 데 사용됩니다.
`Metered.GetConsumptionQuantity()` 메서드는 소비 파일 크기에 대한 정보를 가져오는 데 사용됩니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetMeteredLicense()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    // Set metered public and private keys
    var metered = new Aspose.Pdf.Metered();
    // Access the setMeteredKey property and pass public and private keys as parameters
    metered.SetMeteredKey("your public key", "your private key");
    // Get current Consumption Credit and Quantity
    var currentMonthCreditsSpent = Aspose.Pdf.Metered.GetConsumptionCredit();
    var currentMonthConsumedMegabytes = Aspose.Pdf.Metered.GetConsumptionQuantity();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Add five pages
        AddPages(document, 5);

        // Save the document
        document.Save(dataDir + "output.pdf");

        // Wait to be sure the transaction completed
        System.Threading.Thread.Sleep(10000);
        // Get current Consumption Credit and Quantity
        var nowCredit = Aspose.Pdf.Metered.GetConsumptionCredit();
        var nowQuantity = Aspose.Pdf.Metered.GetConsumptionQuantity();
        Console.WriteLine("Credit: was={0} now={1} difference={2}", currentMonthCreditsSpent, nowCredit, nowCredit - currentMonthCreditsSpent);
        Console.WriteLine("Quantity: was={0} now={1} difference={2}", currentMonthConsumedMegabytes, nowQuantity, nowQuantity - currentMonthConsumedMegabytes); 
    }
}

private static void AddPages(Document document, int n)
{
    for (int i = 0; i < n; i++)
    {
        document.Pages.Add();
    }
} 
```

__미터 라이센스에 대한 모범 사례__

✅ 권장 접근 방식: 싱글톤 패턴
안정적인 라이센스 설정을 보장하기 위해:

- 애플리케이션 시작 시 라이센스를 한 번 적용합니다.
- 싱글톤 패턴(또는 유사한 접근 방식)을 사용하여 미터 라이센스 인스턴스를 생성하고 재사용합니다.
- `IsMeteredLicensed()`를 사용하여 주기적으로 라이센스 상태를 확인합니다. 라이센스가 무효화되면 다시 적용합니다.
- 올바르게 구현되면 라이센스 서버가 일시적으로 사용할 수 없더라도 라이센스는 24시간 동안 유효합니다.

예시: 싱글톤 구현

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
public class AsposeLicenseManager
{
    private static AsposeLicenseManager _instance;
    private static readonly object _lock = new object();
    private Aspose.Pdf.Metered _metered;

    private AsposeLicenseManager()
    {
        _metered = new Aspose.Pdf.Metered();
        _metered.SetMeteredKey("your-public-key", "your-private-key");
    }

    public static AsposeLicenseManager Instance
    {
        get
        {
            lock (_lock)
            {
                if (_instance == null)
                {
                    _instance = new AsposeLicenseManager();
                }
                return _instance;
            }
        }
    }

    public void ValidateLicense()
    {
        if (!Aspose.Pdf.License.IsMeteredLicensed())
        {
        _metered.SetMeteredKey("your-public-key", "your-private-key");
        }
    }
}
```

❌ 피해야 할 일반적인 실수:

- 빈번한 라이센스 적용
- 모든 작업에 대해 새로운 미터 라이센스 인스턴스를 생성하지 마십시오.
- 초기화 중에 라이센스 서버에 연결할 수 없는 경우 라이센스가 평가 모드로 돌아갈 수 있습니다.
- 각 작업에 대해 라이센스를 반복적으로 적용하지 마십시오.
- 빈번한 라이센스 적용은 라이센스 서버가 일시적으로 사용할 수 없을 경우 시험 모드로 돌아갈 수 있습니다.

__요약:__

✅ 애플리케이션 시작 시 미터 라이센스를 한 번 설정합니다.
✅ 단일 인스턴스를 관리하기 위해 싱글톤 패턴을 사용합니다.
✅ 필요할 경우 주기적으로 라이센스를 확인하고 다시 적용합니다.
❌ 시험 모드로 돌아가는 것을 방지하기 위해 빈번한 라이센스 적용을 피하십시오.
이러한 모범 사례를 따르면 미터 라이센스를 사용하여 Aspose.PDF를 원활하고 중단 없이 사용할 수 있습니다.

라이센스가 초기화된 경우 이 객체가 "존재하는" 한, 라이센스 서버와의 연결이 어떤 이유로든 끊어지더라도 라이센스는 추가로 7일 동안 활성으로 간주됩니다. 무언가를 수행해야 할 때마다 라이센스를 초기화하고 초기화 순간에 서버에 연결이 없으면 라이센스는 평가 모드로 전환됩니다.
사용자가 라이센스를 초기화한 경우 이 객체가 "존재하는" 한, 라이센스 서버와의 연결이 어떤 이유로든 끊어지더라도 라이센스는 추가로 24시간 동안 활성으로 간주됩니다. 무언가를 수행해야 할 때마다 라이센스를 초기화하고 초기화 순간에 서버에 연결이 없으면 라이센스는 평가 모드로 전환됩니다.

**Aspose.PDF for .NET**과 함께 작업하는 COM 애플리케이션도 License 클래스를 사용해야 합니다.

고려해야 할 한 가지 사항:
임베디드 리소스는 추가된 방식으로 어셈블리에 포함됩니다. 즉, 애플리케이션에 텍스트 파일을 임베디드 리소스로 추가하고 결과 EXE를 메모장으로 열면 텍스트 파일의 정확한 내용을 볼 수 있습니다. 따라서 라이센스 파일을 임베디드 리소스로 사용할 때는 누구나 EXE 파일을 간단한 텍스트 편집기로 열어 임베디드 라이센스의 내용을 볼 수 있습니다.

따라서 애플리케이션과 함께 라이센스를 임베드할 때 추가 보안 계층을 제공하기 위해 라이센스를 압축/암호화한 후 이를 어셈블리에 임베드할 수 있습니다. 예를 들어 Aspose.PDF.lic 라이센스 파일이 있다고 가정하면, 비밀번호 test로 Aspose.PDF.zip을 만들고 이 zip 파일을 솔루션에 임베드합니다. 다음 코드 조각을 사용하여 라이센스를 초기화할 수 있습니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetLicenseFromStream()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    var license = new Aspose.Pdf.License();
    license.SetLicense(GetSecureLicenseFromStream());
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the page count of document
        Console.WriteLine(document.Pages.Count);
    }
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
```