---
title: Docker에서 Aspose.PDF for .NET 6 실행 방법
linktitle: Docker에서 Aspose.PDF for .NET 6 사용하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/docker/dotnet6/
description: Docker Linux 또는 Windows 컨테이너를 사용하여 .NET 6 애플리케이션에 Aspose.PDF 기능 통합
lastmod: "2024-08-22"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to run Aspose.PDF for .NET 6 in Docker",
    "alternativeHeadline": "Run Aspose.PDF in .NET 6 with Docker Support",
    "abstract": "이 기능은 개발자가 Docker Linux 또는 Windows 컨테이너를 활용하여 .NET 6 애플리케이션 내에서 Aspose.PDF 기능을 원활하게 통합할 수 있도록 합니다. 이 기능은 ASP.NET Core 애플리케이션에서 PDF 문서를 직접 생성하는 과정을 단순화하여 클라우드 기반 환경에서 문서 관리의 효율성을 향상시킵니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1067",
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
    "url": "/net/docker/dotnet6/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/docker/dotnet6/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 단순하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

## 필수 조건

다음 예제는 다음과 함께 테스트되었습니다:

* Docker v.20.10.11 및 Docker Desktop 4.3.2.
* Visual Studio 2022 Community Edition v.17.0.5.
* 아래 제공된 예제에서 .NET 6 SDK가 사용됩니다.
* Aspose.PDF for .NET v.22.01.

## Docker Linux 컨테이너용 샘플 애플리케이션 생성

1. Visual Studio 2022를 실행하고 **ASP.NET Core Web App (Model-View-Controller)** 템플릿을 선택한 후 **다음**을 클릭합니다.
1. **새 프로젝트 구성** 창에서 원하는 프로젝트 이름과 위치를 설정한 후 **다음**을 클릭합니다.
1. **추가 정보** 창에서 **.NET 6.0 (장기 지원)**을 선택하고 Docker 지원을 활성화합니다. 필요에 따라 **Docker OS**를 Linux로 설정할 수도 있습니다.
1. **생성**을 클릭합니다.
1. **도구->Nuget 패키지 관리자->패키지 관리자 콘솔**을 선택하고 **Aspose.PDF for .NET**를 설치합니다 (명령어 `Install-Package Aspose.PDF` 사용).

### Linux 컨테이너에서 ASP.NET Core Web App을 사용하여 PDF 문서 생성

이 앱에서는 **복잡한 예제**의 코드를 사용할 것입니다. 더 자세한 설명은 [이 링크](/pdf/net/complex-pdf-example/)를 참조하세요.

1. `wwwroot` 폴더에 `images` 폴더를 만들고 이미지 `logo.png`를 넣습니다. 이 이미지는 [여기](/pdf/net/docker/logo.png)에서 다운로드할 수 있습니다.
1. `HomeController.cs`의 코드를 다음 스니펫으로 교체합니다 (다른 네임스페이스를 가질 수 있습니다):

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와도 작동합니다.

```cs
using Aspose.Pdf;
using Aspose.Pdf.Text;
using Docker.Linux.Demo01.Models;
using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;

namespace Docker.Linux.Demo01.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;
        private readonly IWebHostEnvironment _appEnvironment;

        public HomeController(ILogger<HomeController> logger, IWebHostEnvironment appEnvironment)
        {
            _logger = logger;
            _appEnvironment = appEnvironment;
        }

        public IActionResult Index()
        {
            return View();
        }
        
        public IActionResult Generate()
        {
            const string file_type = "application/pdf";
            const string file_name = "sample.pdf";
            var memoryStream = new MemoryStream();

            _logger.LogInformation("Start");
            // Initialize document object
            using (var document = new Aspose.Pdf.Document())
            {
                // Add page
                var page = document.Pages.Add();

                // Add image
                var imageFileName = Path.Combine(_appEnvironment.WebRootPath, "images", "logo.png");
                page.AddImage(imageFileName, new Rectangle(20, 730, 120, 830));

                // -------------------------------------------------------------
                // Add Header
                var header = new TextFragment("New ferry routes in Fall 2020");
                header.TextState.Font = FontRepository.FindFont("Arial");
                header.TextState.FontSize = 24;
                header.HorizontalAlignment = HorizontalAlignment.Center;
                header.Position = new Position(130, 720);
                page.Paragraphs.Add(header);

                // Add description
                var descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. Ferry service is operating at half capacity and on a reduced schedule. Expect lineups.";
                var description = new TextFragment(descriptionText);
                description.TextState.Font = FontRepository.FindFont("Times New Roman");
                description.TextState.FontSize = 14;
                description.HorizontalAlignment = HorizontalAlignment.Left;
                page.Paragraphs.Add(description);

                // Add table
                var table = new Table
                {
                    ColumnWidths = "200",
                    Border = new BorderInfo(BorderSide.Box, 1f, Color.Black),
                    DefaultCellBorder = new BorderInfo(BorderSide.Box, 0.5f, Color.Gray),
                    DefaultCellPadding = new MarginInfo(4.5, 4.5, 4.5, 4.5),
                    Margin =
                    {
                        Top = 10,
                        Bottom = 10
                    },
                    DefaultCellTextState =
                    {
                        Font =  FontRepository.FindFont("Helvetica")
                    }
                };

                var headerRow = table.Rows.Add();
                headerRow.Cells.Add("Departs City");
                headerRow.Cells.Add("Departs Island");
                foreach (Cell headerRowCell in headerRow.Cells)
                {
                    headerRowCell.BackgroundColor = Color.LightGray;
                    headerRowCell.DefaultCellTextState.ForegroundColor = Color.FromRgb(0.1, 0.1, 0.1);
                }

                var time = new TimeSpan(6, 0, 0);
                var incTime = new TimeSpan(0, 30, 0);
                for (int i = 0; i < 10; i++)
                {
                    var dataRow = table.Rows.Add();
                    dataRow.Cells.Add(time.ToString(@"hh\:mm"));
                    time = time.Add(incTime);
                    dataRow.Cells.Add(time.ToString(@"hh\:mm"));
                }

                page.Paragraphs.Add(table);

                document.Save(memoryStream);
            }
            _logger.LogInformation("Finish");
            return File(memoryStream, file_type, file_name);
        }

        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
```

1. `Dockerfile`의 내용을 다음 내용으로 교체합니다:

```dockerfile
FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
RUN apt-get update && apt-get install -y libgdiplus
RUN sed -i'.bak' 's/$/ contrib/' /etc/apt/sources.list
RUN apt-get update; apt-get install -y ttf-mscorefonts-installer fontconfig

WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY ["Docker.Linux.Demo01/Docker.Linux.Demo01.csproj", "Docker.Linux.Demo01/"]
RUN dotnet restore "Docker.Linux.Demo01/Docker.Linux.Demo01.csproj"
COPY . .
WORKDIR "/src/Docker.Linux.Demo01"
RUN dotnet build "Docker.Linux.Demo01.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Docker.Linux.Demo01.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Docker.Linux.Demo01.dll"]
```

## Docker Windows 컨테이너용 샘플 애플리케이션 생성

1. Visual Studio 2022를 실행하고 **ASP.NET Core Web App (Model-View-Controller)** 템플릿을 선택한 후 **다음**을 클릭합니다.
1. **새 프로젝트 구성** 창에서 원하는 프로젝트 이름과 위치를 설정한 후 **다음**을 클릭합니다.
1. **추가 정보** 창에서 **.NET 6.0 (장기 지원)**을 선택하고 Docker 지원을 활성화합니다. 필요에 따라 **Docker OS**를 `Windows`로 설정할 수도 있습니다.
1. **생성**을 클릭합니다.
1. **도구->Nuget 패키지 관리자->패키지 관리자 콘솔**을 선택하고 **Aspose.PDF for .NET**를 설치합니다 (명령어 `Install-Package Aspose.PDF` 사용).

### Windows 컨테이너에서 ASP.NET Core Web App을 사용하여 PDF 문서 생성

이전 예제와 동일한 코드를 사용할 것입니다.

1. `wwwroot` 폴더에 `images` 폴더를 만들고 이미지 `logo.png`를 넣습니다. 이 이미지는 [여기](/pdf/net/docker/logo.png)에서 다운로드할 수 있습니다.
1. `HomeController.cs`의 코드를 위의 스니펫으로 교체합니다.

```dockerfile
FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:6.0.101-nanoserver-ltsc2022 AS build
WORKDIR /src
COPY ["Docker.Windows.Demo01/Docker.Windows.Demo01.csproj", "Docker.Windows.Demo01/"]
RUN dotnet restore "Docker.Windows.Demo01/Docker.Windows.Demo01.csproj"
COPY . .
WORKDIR "/src/Docker.Windows.Demo01"
RUN dotnet build "Docker.Windows.Demo01.csproj" -c Release -o /app/build -r win-x64 --self-contained true

FROM build AS publish
RUN dotnet publish "Docker.Windows.Demo01.csproj" -c Release -o /app/publish -r win-x64 --self-contained true

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Docker.Windows.Demo01.dll"]
```