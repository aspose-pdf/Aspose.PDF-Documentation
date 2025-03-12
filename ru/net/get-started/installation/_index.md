---
title: Как установить Aspose.PDF for .NET
linktitle: Установка
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ru/net/installation/
description: Этот раздел содержит описание продукта и инструкции по установке Aspose.PDF for .NET самостоятельно, а также с использованием NuGet.
lastmod: "2024-09-04"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to Install Aspose.PDF for .NET",
    "alternativeHeadline": "Seamless PDF Creation with Aspose.PDF for .NET",
    "abstract": "Aspose.PDF for .NET — это мощный компонент, который позволяет разработчикам программно генерировать и манипулировать PDF-документами без зависимости от Adobe Acrobat. С поддержкой вставки сложных элементов, таких как таблицы, изображения и пользовательские шрифты, а также с надежными функциями безопасности и бесшовной интеграцией через NuGet, этот универсальный инструмент повышает производительность и эффективность в приложениях .NET.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Aspose.PDF, PDF documents, .NET component, NuGet installation, C# API, Temporary License, multithread safe, eval version limitations, .NET Core support, font installation",
    "wordcount": "1214",
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
    "url": "/net/installation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/installation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для опытных пользователей и разработчиков."
}
</script>

## Компонент Aspose.PDF C#

{{% alert color="primary" %}}

**Aspose.PDF — это компонент .NET**, созданный для того, чтобы позволить разработчикам создавать PDF-документы, будь то простые или сложные, программно. Aspose.PDF for .NET позволяет разработчикам вставлять таблицы, графики, изображения, гиперссылки, пользовательские шрифты и многое другое в PDF-документы. Более того, также возможно сжимать PDF-документы. Aspose.PDF for .NET предоставляет отличные функции безопасности для разработки защищенных PDF-документов. И самой отличительной особенностью Aspose.PDF for .NET является то, что он поддерживает создание PDF-документов как через API, так и из XML-шаблонов.

{{% /alert %}}

## Описание продукта

**Aspose.PDF for .NET** — это надежный компонент .NET, который позволяет разработчикам создавать PDF-документы с нуля без использования Adobe Acrobat. Он предоставляет простой интерфейс программирования приложений (API), который легко изучить и использовать.

**Aspose.PDF for .NET** реализован с использованием Managed C# и может использоваться с любым языком .NET, таким как C#, VB.NET и J# и т.д. Он может быть интегрирован с любым типом приложения, будь то веб-приложение ASP.NET или настольное приложение Windows.

Чтобы разработчики могли быстро начать работу, Aspose.PDF for .NET предоставляет полнофункциональные демонстрации и рабочие примеры, написанные на C#. С помощью этих демонстраций разработчики могут быстро узнать о функциях, предоставляемых Aspose.PDF for .NET.

Быстрый, легковесный компонент эффективно создает PDF-документы и помогает вашему приложению работать лучше. Aspose.PDF for .NET является первым выбором наших клиентов при создании PDF-документов благодаря своей цене, отличной производительности и отличной поддержке.

**Aspose.PDF for .NET** безопасен для многопоточности, если только один поток работает с документом в одно время. Это типичный сценарий, когда один поток работает с одним документом. Разные потоки могут безопасно работать с разными документами одновременно.

## Декларация

Все компоненты Aspose .NET требуют разрешения Full Trust. Причина в том, что компоненты Aspose .NET нуждаются в доступе к настройкам реестра, системным файлам, отличным от виртуального каталога, для выполнения определенных операций, таких как парсинг шрифтов и т.д. Более того, компоненты Aspose .NET основаны на основных системных классах .NET, которые также требуют разрешения Full Trust во многих случаях.

Поставщики интернет-услуг, размещающие несколько приложений от разных компаний, в основном применяют уровень безопасности Medium Trust. В случае .NET 2.0 такой уровень безопасности накладывает следующие ограничения:

- **OleDbPermission недоступен.** Это означает, что вы не можете использовать управляемый OLE DB провайдер данных ADO.NET для доступа к базам данных.
- **EventLogPermission недоступен.** Это означает, что вы не можете получить доступ к журналу событий Windows.
- **ReflectionPermission недоступен.** Это означает, что вы не можете использовать рефлексию.
- **RegistryPermission недоступен.** Это означает, что вы не можете получить доступ к реестру.
- **WebPermission ограничен.** Это означает, что ваше приложение может общаться только с адресом или диапазоном адресов, которые вы определяете в элементе `<trust>`.
- **FileIOPermission ограничен.** Это означает, что вы можете получить доступ только к файлам в иерархии виртуального каталога вашего приложения.
Из-за указанных выше причин компоненты Aspose .NET не могут использоваться на серверах, предоставляющих разрешение, отличное от Full Trust.

## Установка

### Оценка Aspose.PDF for .NET

Вы можете легко скачать Aspose.PDF for .NET для оценки. Загрузка для оценки такая же, как и загрузка после покупки. Оценочная версия просто становится лицензированной, когда вы добавляете несколько строк кода для применения лицензии.

Оценочная версия Aspose.PDF (без указанной лицензии) предоставляет полную функциональность продукта. Тем не менее, у нее есть два ограничения: она вставляет водяной знак оценки, и только первые четыре страницы любого документа могут быть просмотрены/отредактированы.

{{% alert color="primary" %}}

Если вы хотите протестировать Aspose.PDF for .NET без ограничений оценочной версии, вы также можете запросить временную лицензию на 30 дней. Пожалуйста, обратитесь к [Как получить временную лицензию?](https://purchase.aspose.com/temporary-license)

{{% /alert %}}

### Установка Aspose.PDF for .NET через NuGet

NuGet — это бесплатная, ориентированная на разработчиков система управления пакетами с открытым исходным кодом для платформы .NET, предназначенная для упрощения процесса интеграции сторонних библиотек в приложение .NET во время разработки. Это расширение Visual Studio, которое упрощает добавление, удаление и обновление библиотек и инструментов в проектах Visual Studio, использующих .NET Framework. Библиотека или инструмент могут быть легко поделены с другими разработчиками, создав пакет NuGet и сохранив его внутри репозитория NuGet. Когда вы устанавливаете пакет, NuGet копирует файлы в ваше решение и автоматически вносит необходимые изменения, такие как добавление ссылок и изменение ваших файлов app.config или web.config. Если вы решите удалить библиотеку, NuGet удаляет файлы и отменяет любые изменения, которые он внес в ваш проект, чтобы не осталось беспорядка.

### Ссылка на Aspose.PDF for .NET

#### Установить пакет с помощью консоли диспетчера пакетов

- Откройте ваше .NET приложение в Visual Studio.
- В меню "Инструменты" выберите **Диспетчер пакетов NuGet**, а затем **Консоль диспетчера пакетов**.
- Введите команду `Install-Package Aspose.PDF`, чтобы установить последнюю полную версию, или введите команду `Install-Package Aspose.PDF -prerelease`, чтобы установить последнюю версию, включая исправления.
- Нажмите `Enter`.

#### Обновить пакет с помощью консоли диспетчера пакетов

Если вы уже ссылались на компонент через NuGet, выполните следующие шаги, чтобы обновить ссылку на последнюю версию:

- Откройте ваше .NET приложение в Visual Studio.
- В меню "Инструменты" выберите **Диспетчер пакетов NuGet**, а затем **Консоль диспетчера пакетов**.
- Введите команду `Update-Package Aspose.PDF`, чтобы сослаться на последнюю полную версию, или введите команду `Update-Package Aspose.PDF -prerelease`, чтобы установить последнюю версию, включая исправления.

#### Установить пакет с помощью графического интерфейса диспетчера пакетов

Выполните следующие шаги, чтобы сослаться на компонент с помощью графического интерфейса диспетчера пакетов:

- Откройте ваше .NET приложение в Visual Studio.

- В меню "Проект" выберите **Управление пакетами NuGet**.

![Installation_step](../images/install_step.png)

- Выберите вкладку **Обзор**.

![Installation_step1](../images/install_step1.png)

- Введите Aspose.PDF в поле поиска, чтобы найти Aspose.PDF for .NET.

- Нажмите Установить/Обновить рядом с последней версией Aspose.PDF for .NET.

![Installation_step2](../images/Install_step2.png)

- И нажмите Принять в всплывающем окне.

![Installation_step3](../images/Install_step3.png)

![Installation](../images/install.gif)

### Работа с .NET Core DLL в среде, отличной от Windows

Поскольку Aspose.PDF for .NET поддерживает .NET Standard 2.0 (.NET Core 2.0), его можно использовать в Core-приложениях, работающих в операционных системах, подобных Linux. Мы постоянно работаем над улучшением поддержки .NET Core в нашем API. Тем не менее, есть некоторые операции, которые мы рекомендуем нашим клиентам выполнять, чтобы получить лучшие результаты при использовании функций Aspose.PDF for .NET:

Пожалуйста, установите:

- пакет libgdiplus
- пакет с совместимыми шрифтами Microsoft: **ttf-mscorefonts-installer**. (например, `sudo apt-get install ttf-mscorefonts-installer`)
Эти шрифты должны быть размещены в каталоге "/usr/share/fonts/truetype/msttcorefonts", так как Aspose.PDF for .NET сканирует эту папку в операционных системах, подобных Linux. В случае, если операционная система имеет другую папку/каталог по умолчанию для шрифтов, вы должны использовать следующую строку кода перед выполнением любых операций с использованием Aspose.PDF.

```csharp
Aspose.Pdf.Text.FontRepository.Sources.Add(new FolderFontSource("<user's path to ms fonts>"));
```

#### Настройка Aspose.PDF for .NET в Visual Studio Code
- Установите .NET SDK

1. Посетите официальный [сайт Microsoft .NET](https://dotnet.microsoft.com/download).
2. Скачайте последнюю версию .NET SDK.
3. Запустите установщик.
4. Откройте терминал и проверьте установку, выполнив:
```bash
dotnet --version
```

- Установите Visual Studio Code

1. Перейдите на https://code.visualstudio.com/.
2. Скачайте соответствующую версию для вашей операционной системы.

- Установите необходимые расширения VS Code

1. Откройте Visual Studio Code.
2. Нажмите на значок представления расширений (квадратный значок на левой боковой панели).
3. Найдите и установите следующие расширения:
   - "C#" от Microsoft
   - "C# Dev Kit" от Microsoft
   - ".NET Core Test Explorer" (необязательно, но рекомендуется)

- Создайте новый проект .NET

1. Откройте Visual Studio Code
2. Перейдите в Терминал > Новый терминал
3. Перейдите в желаемый каталог проекта
```bash
# Create a new console application
dotnet new console -n AsposePDFNetDemo
# Navigate into the project directory
cd AsposePDFNetDemo
```

- Добавьте пакет NuGet

```bash
# Install Aspose.PDF package
dotnet add package Aspose.PDF
```

- Проверьте установку пакета

1. Откройте файл `.csproj`
2. Убедитесь, что ссылка на пакет Aspose.PDF добавлена:
```xml
<ItemGroup>
  <PackageReference Include="Aspose.PDF" Version="x.x.x" />
</ItemGroup>
```

- Создайте конфигурацию отладки

1. Нажмите Ctrl+Shift+P (Cmd+Shift+P на Mac).
2. Введите ">.NET: Генерировать ресурсы для сборки и отладки".
3. Выберите ваш проект.
4. Создайте или измените `.vscode/launch.json`:
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": ".NET Core Launch (console)",
            "type": "coreclr",
            "request": "launch",
            "preLaunchTask": "build",
            "program": "${workspaceFolder}/bin/Debug/net7.0/AsposePDFNetDemo.dll",
            "args": [],
            "cwd": "${workspaceFolder}",
            "console": "internalConsole",
            "stopAtEntry": false
        }
    ]
}
```

- Напишите пример кода в Program.cs

Замените содержимое `Program.cs` на:
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
using System;
using Aspose.Pdf;
using Aspose.Pdf.Text;

class Program 
{
    static void Main(string[] args)
    {
        // Activate your license, you can comment out these codelines to use library in Evaluation mode
        var license = new Aspose.Pdf.License();
        license.SetLicense("Aspose.PDF.NET.lic");

        // Create PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            var page = document.Pages.Add();
            
            // Create a text fragment
            var textFragment = new Aspose.Pdf.Text.TextFragment("Hello, Aspose.PDF for .NET!");
            textFragment.Position = new Aspose.Pdf.Text.Position(100, 600);
            
            // Add text to the page
            page.Paragraphs.Add(textFragment);
            
            // Save PDF document
            document.Save("sample.pdf");
        }
    }
}
```

- Соберите и запустите

```bash
dotnet restore
dotnet build
dotnet run
```