---
title: Install the C++ library
linktitle: Installation
type: docs
weight: 40
url: /cpp/installation/
description: Install or update the Aspose.PDF.Cpp NuGet package and prepare a C++ project for PDF processing.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Install and Reference the Native C++ PDF SDK
Abstract: Add Aspose.PDF for C++ to a Visual Studio project through NuGet or use a downloaded SDK distribution. Restore the package, configure the project, and verify the setup with a small PDF example.
---

Use the native [Aspose.PDF.Cpp package](https://www.nuget.org/packages/Aspose.PDF.Cpp/) when adding Aspose.PDF to a C++ project.

## Install with NuGet

1. Open your C++ project in Visual Studio.
1. Select Tools > NuGet Package Manager > Package Manager Console.
1. Run the following command:

```powershell
Install-Package Aspose.PDF.Cpp
```

1. Restore packages and build the project.
1. Run a small document-creation example to verify the configuration.

To select a specific release, add the -Version option with an available package version.

## Update an existing installation

Run the following command in Package Manager Console:

```powershell
Update-Package Aspose.PDF.Cpp
```

Rebuild and verify the application's PDF workflows after updating.

## Install from a distribution

Download a suitable SDK from [Aspose releases](https://releases.aspose.com/pdf/cpp/). Configure include paths, library paths, and runtime deployment using the instructions supplied with that distribution.

Review [System Requirements](/pdf/cpp/system-requirements/) and [Licensing](/pdf/cpp/licensing/) before deployment.
