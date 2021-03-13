---
title: Install Aspose.PDF for .NET
linktitle: Installation
type: docs
weight: 40
url: /net/installation/
description: This section shows a product description and instructions for installing Aspose.PDF for .Net on your own, as well as using NuGet.
lastmod: "2020-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Aspose.PDF C# component

{{% alert color="primary" %}}

**Aspose.PDF is a .NET** component built to allow developers to create PDF documents, whether simple or complex, on the fly programmatically. Aspose.PDF for .NET allows developers to insert tables, graphs, images, hyperlinks, custom fonts - and more - into PDF documents. Moreover, it is also possible to compress PDF documents. Aspose.PDF for .NET provides excellent security features to develop secure PDF documents. And the most distinct feature of Aspose.PDF for .NET is that it supports the creation of PDF documents through both an API and from XML templates.

{{% /alert %}}

## Product Description

**Aspose.PDF for .NET** is a robust .NET component that lets developers create PDF documents from scratch without using Adobe Acrobat. It provides a simple Application Programming Interface (API) that is easy to learn and use.

**Aspose.PDF for .NET** is implemented using Managed C# and it can be used with any .NET language like C#, VB.NET and J# etc. It can be integrated with any kind of application either it's an ASP.NET Web Application or a Windows Application.

So that the developers can get up and running quickly, Aspose.PDF for .NET provides fully featured demos and working examples written in C#. Using these demos, developers can quickly learn about the features provided by Aspose.PDF for .NET.

The fast, light-weight component creates PDF documents efficiently and helps your application perform better. Aspose.PDF for .NET is our customers' first choice when creating PDF documents because of its price, superb performance and great support.

**Aspose.PDF for .NET** is multithread safe as long as only one thread works on a document at a time. It is a typical scenario to have one thread working on one document. Different threads can safely work on different documents at the same time.

## Declaration

All Aspose .NET components require Full Trust permission set. The reason is, Aspose .NET components need to access registry settings, system files other than virtual directory for certain operations like parsing fonts etc. Moreover, Aspose .NET Components are based on core .NET system classes that also require Full Trust permission set in many cases.

Internet Service Providers hosting multiple applications from different companies mostly enforce Medium Trust security level. In case of .NET 2.0, such security level applies the following constraints:

- **OleDbPermission is not available.** This means you cannot use the ADO.NET managed OLE DB data provider to access databases.
- **EventLogPermission is not available.** This means you cannot access the Windows event log.
- **ReflectionPermission is not available.** This means you cannot use reflection.
- **RegistryPermission is not available.** This means you cannot access the registry.
- **WebPermission is restricted.** This means your application can only communicate with an address or range of addresses that you define in the `<trust>` element.
- **FileIOPermission is restricted.** This means you can only access files in your application's virtual directory hierarchy.
Due to the reasons specified above, Aspose .NET components cannot be used on servers granting permission set other than Full Trust.

# Installation

## Evaluate Aspose.PDF for .NET

You can easily download Aspose.PDF for .Net for evaluation. The evaluation download is the same as the purchased download. The evaluation version simply becomes licensed when you add a few lines of code to apply the license.

The evaluation version of Aspose.PDF (without a license specified) provides full product functionality, but it has two limitations: it inserts an evaluation watermark, and only four elements of any collection can be viewed/edited.

{{% alert color="primary" %}}

If you want to test Aspose.PDF for .NET without the evaluation version limitations, you can also request a 30-day Temporary License. Please refer to [How to get a Temporary License?](https://purchase.aspose.com/temporary-license)

{{% /alert %}}

## Installing Aspose.PDF for .NET through NuGet

NuGet is a free, open source developer-focused package management system for the .NET platform intent on simplifying the process of incorporating third party libraries into a .NET application during development. It is a Visual Studio extension that makes it easy to add, remove, and update libraries and tools in Visual Studio projects that use the .NET Framework. A library or tool can easily be shared with other developers by creating a NuGet package and storing it inside a NuGet repository. When you install the package, NuGet copies files to your solution and automatically makes the necessary changes, such as adding references and changing your app.config or web.config files. If you decide to remove the library, NuGet removes files and reverses whatever changes it made to your project so that no clutter is left.

### Referencing Aspose.PDF for .NET

#### Install package using the Package Manager Console

- Open your .NET application in Visual Studio.
- On the Tools menu, select **NuGet Package Manager** and then **Package Manager Console**.
- Type the command `Install-Package Aspose.PDF` to install the latest full release, or type the command `Install-Package Aspose.PDF -prerelease` to install the latest release including hot fixes.
- Press `Enter`

#### Update package using the Package Manager Console

If you have already referenced the component through NuGet, follow these steps to update the reference to the latest version:

- Open you .NET application in Visual Studio.
- On the Tools menu, select **NuGet Package Manager** and then **Package Manager Console**.
- Type the command `Update-Package Aspose.PDF` to reference the latest full release, or type the command `Update-Package Aspose.PDF -prerelease` to install latest release including hot fixes.

#### Install Package using the Package Manager GUI

Follow these steps to reference the component using the package manager GUI:

- Open you .NET application in Visual Studio.
- From the Project menu select **Manage NuGet Packages**.
- Select **Broswe** tab.
- Type Aspose.PDF into the search box to find Aspose.PDF for .NET.
- Click Install/Update next to the latest version of Aspose.PDF for .NET.

![Installation](../images/install.gif)

### Working with .NET Core DLLs in Non-Windows Environment

As Aspose.PDF for .NET provides .NET Standard 2.0 (.NET Core 2.0) support, so it can be used in Core Applications running in Linux like operating systems. We are constantly working over improving the .NET Core support in our API. However, there are some following operations which we recommend our customers to perform, in order to get better results while using features of Aspose.PDF for .NET:

Please install:

- libgdiplus package
- package with Microsoft compatible fonts: **ttf-mscorefonts-installer**. (e.g. `sudo apt-get install ttf-mscorefonts-installer`)
These fonts should be placed in "/usr/share/fonts/truetype/msttcorefonts" directory as Aspose.PDF for .NET scans this folder on Linux like operating systems. In case operating system has other default folder/directory for fonts, you should use following line of code before performing any operation using Aspose.PDF.

```csharp
Aspose.Pdf.Text.FontRepository.Sources.Add(new FolderFontSource("<user's path to ms fonts>"));
```
