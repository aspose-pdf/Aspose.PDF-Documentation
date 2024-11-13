---
title: Converting Documents in Microsoft Azure
linktitle: Converting Documents in Microsoft Azure
type: docs
weight: 110
url: /net/microsoft-azure/
lastmod: "2024-10-25"
sitemap:
    changefreq: "weekly"
    priority: 0.5
---

This article provides detailed step-by-step instructions for converting PDF documents in Microsoft Azure using Aspose.PDF for .NET.

## Prerequisites

* Azure Account: You need an Azure subscription, create a free account before beginning.
* Visual Studio 2022 Community Edition with installed Azure development or Visual Studio Code.

## Restrictions

When you are working with Aspose.PDF for .NET in an Azure environment, it’s often necessary to configure your Azure service for Full Trust to leverage the full capabilities of Aspose.PDF. This is particularly important for advanced operations, such as PDF-to-image conversions, font embedding, and file format conversions, which need unrestricted access to system resources.

Aspose.PDF performs certain operations that may require access to:

* System resources such as fonts and images.
* Temporary storage for processing files.
* Memory management that might need elevated permissions to operate efficiently.

Azure environments, particularly App Service and Azure Functions, run in a partial trust environment by default. Partial trust restricts certain resources that libraries like Aspose.PDF rely on, which can lead to issues or errors in document processing.

## Set license

It is recommended to use the license file as an embedded resource in your application. If you don’t want to embed the license file in your project, you can store it in Azure Blob Storage and load it from there.
