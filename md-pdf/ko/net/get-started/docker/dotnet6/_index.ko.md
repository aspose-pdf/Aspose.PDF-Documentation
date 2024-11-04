---
title: Docker에서 Aspose.PDF for .NET 6 실행 방법
linktitle: Docker에서 Aspose.PDF for .NET 6 사용하기
type: docs
weight: 10
url: /net/docker/dotnet6/
description: Docker Linux 또는 Windows 컨테이너를 사용하여 애플리케이션에 Aspose.PDF 기능을 통합
lastmod: "2024-01-21"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 사전 요구 사항

다음 예제는 다음과 함께 테스트되었습니다:

* Docker v.20.10.11 및 Docker Desktop 4.3.2
* Visual Studio 2022 커뮤니티 에디션 v.17.0.5
* 아래 제공된 예제에서 .NET 6 SDK가 사용됩니다.
* Aspose.PDF for .NET v.22.01

## Docker Linux 컨테이너를 위한 샘플 애플리케이션 생성

1. Visual Studio 2022를 실행하고 **ASP.NET Core 웹 앱(Model-View-Controller)** 템플릿을 선택한 다음 **다음**을 클릭합니다.
1. **새 프로젝트 구성** 창에서 원하는 프로젝트 이름과 위치를 설정하고 **다음**을 클릭합니다.
1. **추가 정보** 창에서 **.NET 6.0 (장기 지원)** 을 선택하고 Docker 지원을 활성화합니다. 필요한 경우 **Docker OS**를 Linux로 설정할 수도 있습니다.
1.
1.
1. **도구->Nuget 패키지 관리자->패키지 관리자 콘솔**을 선택하고 **Aspose.PDF for .NET**을 설치하세요 (명령어 사용 `Install-Package Aspose.PDF`)

### 리눅스 컨테이너에서 ASP.NET Core 웹 앱을 사용하여 PDF 문서 생성하기

이 앱에서는 **복잡한 예제**의 코드를 사용할 것입니다. 자세한 설명은 [이 링크](/pdf/net/complex-pdf-example/)를 참고하세요.

1. `wwwroot` 폴더에 `images` 폴더를 생성하고 `logo.png` 이미지를 넣으세요. 이 이미지는 [여기](/pdf/net/docker/logo.png)에서 다운로드할 수 있습니다.
1. `HomeController.cs`의 코드를 다음 스니펫으로 교체하세요(다른 네임스페이스를 사용할 수도 있음을 유의하세요):

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리에서도 작동합니다.

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
            var memoryStream = new System.IO.MemoryStream();

            _logger.LogInformation("시작");
            // 문서 객체 초기화
            var document = new Document();
            // 페이지 추가
            var page = document.Pages.Add();

            // 이미지 추가
            var imageFileName = System.IO.Path.Combine(_appEnvironment.WebRootPath, "images", "logo.png");
            page.AddImage(imageFileName, new Rectangle(20, 730, 120, 830));

            // -------------------------------------------------------------
            // 헤더 추가
            var header = new TextFragment("2020년 가을 새로운 페리 노선");
            header.TextState.Font = FontRepository.FindFont("Arial");
            header.TextState.FontSize = 24;
            header.HorizontalAlignment = HorizontalAlignment.Center;
            header.Position = new Position(130, 720);
            page.Paragraphs.Add(header);

            // 설명 추가
            var descriptionText = "방문객은 온라인으로 티켓을 구매해야 하며, 티켓은 하루에 5,000장으로 제한됩니다. 페리 서비스는 절반 용량으로 운영되며 일정이 축소되었습니다. 줄을 서서 기다릴 것으로 예상하세요.";
            var description = new TextFragment(descriptionText);
            description.TextState.Font = FontRepository.FindFont("Times New Roman");
            description.TextState.FontSize = 14;
            description.HorizontalAlignment = HorizontalAlignment.Left;
            page.Paragraphs.Add(description);

            // 테이블 추가
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
            headerRow.Cells.Add("출발 도시");
            headerRow.Cells.Add("출발 섬");
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
            _logger.LogInformation("완료");
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
1. `Dockerfile`의 내용을 다음으로 교체하세요:

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

## Docker Windows 컨테이너용 샘플 애플리케이션 만들기

1.
1.
1. **새 프로젝트 구성** 창에서 원하는 프로젝트 이름과 위치를 설정하고 **다음**을 누릅니다.
1. **추가 정보** 창에서 **.NET 6.0 (장기 지원)** 을 선택하고 Docker 지원을 활성화합니다. 필요하다면 **Docker OS**를 `Windows`로 설정할 수 있습니다.
1. **생성**을 누릅니다.
1. **도구->Nuget 패키지 관리자->패키지 관리자 콘솔**을 선택하고 `Install-Package Aspose.PDF` 명령을 사용하여 **Aspose.PDF for .NET**을 설치합니다.

### Windows 컨테이너에서 ASP.NET Core 웹 앱을 사용하여 PDF 문서 생성하기

이전 예제와 동일한 코드를 사용할 것입니다.

1. `wwwroot` 폴더에 `images` 폴더를 만들고 `logo.png` 이미지를 넣습니다. 이 이미지는 [여기](/pdf/net/docker/logo.png)에서 다운로드할 수 있습니다.
1. `HomeController.cs`의 코드를 위의 스니펫으로 교체하세요.

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

