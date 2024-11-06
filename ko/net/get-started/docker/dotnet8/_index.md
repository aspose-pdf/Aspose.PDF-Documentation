---
title: Docker에서 Aspose.PDF 실행하는 방법
linktitle: Docker 사용하기
type: docs
weight: 20
url: ko/net/docker/dotnet8/
description: Docker Linux 컨테이너를 사용하여 애플리케이션에 Aspose.PDF 기능을 통합하세요
lastmod: "2024-01-21"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 필수 조건

다음 예제는 다음과 함께 테스트되었습니다:

* Docker v.25.0.2 및 Docker Desktop 4.27.1
* Visual Studio 2022 Community Edition v.17.0.5
* 아래 제공된 예제에서는 .NET 8 SDK가 사용됩니다.
* Aspose.PDF.Drawing v.24.01

## Docker Linux 컨테이너를 위한 샘플 애플리케이션 생성

1. Visual Studio 2022를 실행하고 **ASP.NET Core Web App (Model-View-Controller)** 템플릿을 선택한 후 **다음**을 클릭하세요
1. **새 프로젝트 구성** 창에서 원하는 프로젝트 이름과 위치를 설정하고 **다음**을 클릭하세요
1. **추가 정보** 창에서 **.NET 6.0 (장기 지원)**을 선택하고 Docker 지원을 활성화하세요. 필요한 경우 **Docker OS**를 Linux로 설정할 수도 있습니다.
1. **생성**을 클릭하세요
1.
### ASP.NET Core 웹 앱을 사용하여 Linux 컨테이너에서 PDF 문서 생성

**Complex Example**의 코드를 이 앱에서 사용할 것입니다. 자세한 설명은 [이 링크](/pdf/net/complex-pdf-example/)를 따라주세요.

1. `wwwroot` 폴더에 `images` 폴더를 만들고 `logo.png` 이미지를 넣습니다. 이 이미지는 [여기](/pdf/net/docker/logo.png)에서 다운로드할 수 있습니다.
1. `wwwroot` 폴더에 `fonts` 폴더를 만들고 [Roboto](https://fonts.google.com/specimen/Roboto) 폰트를 넣습니다.
1. `wwwroot` 폴더에 `samples` 폴더를 만들고 샘플 데이터를 넣습니다.
1. `HomeController.cs`의 코드를 다음 스니펫으로 교체하세요 (다른 네임스페이스를 사용할 수 있음을 유의하세요):

```cs
using Aspose.Pdf;
using Aspose.Pdf.Devices;
using Aspose.Pdf.Text;
using Docker.LinuxDemo.Models;
using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;

namespace Docker.LinuxDemo.Controllers
{
    // <summary>
    // 홈 페이지 및 Linux 데모 애플리케이션에서 PDF 생성을 위한 컨트롤러를 나타냅니다.
    // </summary>
    public class HomeController(ILogger<HomeController> logger, IWebHostEnvironment appEnvironment) : Controller
    {
        private readonly ILogger<HomeController> _logger = logger;
        private readonly IWebHostEnvironment _appEnvironment = appEnvironment;

        // <summary>
        // 인덱스 뷰를 표시합니다.
        // </summary>
        public IActionResult Index()
        {
            return View();
        }

        // <summary>
        // PDF 문서를 생성하고 파일로 반환합니다.
        // </summary>
        public IActionResult Generate()
        {
            const string fileType = "application/pdf";
            const string fileName = "sample.pdf";
            FontRepository.Sources.Add(new FolderFontSource(Path.Combine(_appEnvironment.WebRootPath, "fonts")));
            var memoryStream = new MemoryStream();

            _logger.LogInformation("PDF 생성: 시작");
            // 문서 객체 초기화
            var document = new Document();
            // 페이지 추가
            var page = document.Pages.Add();

            // 이미지 추가
            var imageFileName = Path.Combine(_appEnvironment.WebRootPath, "images", "logo.png");
            page.AddImage(imageFileName, new Rectangle(20, 730, 120, 830));

            // 헤더 추가
            var header = new TextFragment("2020년 가을 새로운 페리 노선");
            header.TextState.Font = FontRepository.FindFont("Roboto");
            header.TextState.FontSize = 24;
            header.HorizontalAlignment = HorizontalAlignment.Center;
            header.Position = new Position(130, 720);
            page.Paragraphs.Add(header);

            // 설명 추가
            var descriptionText = "방문객은 온라인으로 티켓을 구매해야 하며, 티켓은 하루 5,000장으로 제한됩니다. 페리 서비스는 절반의 용량으로 운영되며, 감축된 일정으로 운영됩니다. 줄을 서서 기다릴 것을 예상하세요.";
            var description = new TextFragment(descriptionText);
            description.TextState.Font = FontRepository.FindFont("Helvetica");
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
            _logger.LogInformation("PDF 생성: 완료");
            return File(memoryStream, fileType, fileName);
        }

        // <summary>
        // 제공된 id를 기반으로 다른 형식으로 파일을 변환합니다.
        // </summary>
        public FileStreamResult Convert(string id)
        {
            return id switch
            {
                "xps-to-pdf" => ConvertXpsToPdf(),
                "pdf-to-jpeg" => ConvertPdfToJpeg(),
                _ => throw new NotImplementedException(),
            };
        }

        // <summary>
        // PDF 파일을 JPEG 형식으로 변환하고 파일로 반환합니다.
        // </summary>
        private FileStreamResult ConvertPdfToJpeg()
        {
            const string fileType = "image/jpeg";
            const string fileName = "sample.jpeg";

            var memoryStream = new MemoryStream();
            var pdfFileName = Path.Combine(_appEnvironment.WebRootPath, "samples", "samples-new.pdf");

            var document = new Document(pdfFileName);
            var resolution = new Resolution(300);
            var renderer = new JpegDevice(resolution, 90);
            renderer.Process(document.Pages[1], memoryStream);
            memoryStream.Seek(0, SeekOrigin.Begin);
            return File(memoryStream, fileType, fileName);
        }

        // <summary>
        // XPS 파일을 PDF 형식으로 변환하고 파일로 반환합니다.
        // </summary>
        private FileStreamResult ConvertXpsToPdf()
        {
            const string fileType = "application/pdf";
            const string fileName = "sample.pdf";

            var memoryStream = new MemoryStream();
            var xpsFileName = Path.Combine(_appEnvironment.WebRootPath, "samples", "samples-new.oxps");

            var document = new Document(xpsFileName, new XpsLoadOptions());
            document.Save(memoryStream);

            return File(memoryStream, fileType, fileName);
        }

        // <summary>
        // 개인 정보 보호 뷰를 표시합니다.
        // </summary>
        public IActionResult Privacy()
        {
            return View();
        }

        // <summary>
        // 오류 뷰를 표시합니다.
        // </summary>
        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
```
1. `Dockerfile`의 내용을 다음 내용으로 교체하세요:

```dockerfile
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS base

RUN apt-get update && apt-get install -y libgdiplus
RUN apt install software-properties-common -y
RUN echo "deb http://deb.debian.org/debian bookworm contrib non-free" > /etc/apt/sources.list.d/contrib.list
RUN apt update && apt upgrade
RUN apt install ttf-mscorefonts-installer -y


USER app
WORKDIR /app
EXPOSE 8080
EXPOSE 8081

FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
ARG BUILD_CONFIGURATION=Release
WORKDIR /src
COPY ["Docker.Demo/Docker.LinuxDemo.csproj", "Docker.Demo/"]
RUN dotnet restore "./Docker.Demo/./Docker.LinuxDemo.csproj"
COPY . .
WORKDIR "/src/Docker.Demo"
RUN dotnet build "./Docker.LinuxDemo.csproj" -c $BUILD_CONFIGURATION -o /app/build

FROM build AS publish
ARG BUILD_CONFIGURATION=Release
RUN dotnet publish "./Docker.LinuxDemo.csproj" -c $BUILD_CONFIGURATION -o /app/publish /p:UseAppHost=false

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Docker.LinuxDemo.dll"]
```

