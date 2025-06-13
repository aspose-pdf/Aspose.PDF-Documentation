---
title: How to Install Aspose.PDF for Rust via C++
linktitle: Installation
type: docs
weight: 20
url: /rust-cpp/installation/
description: This section shows a product description and instructions for installing Aspose.PDF for Rust on your own.
lastmod: "2025-06-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Installation guide of Aspose.PDF for Rust
Abstract: The Aspose.PDF for Rust via C++ Installation guide provides step-by-step instructions to install and configure the library for use in Rust projects with C++ integration. It covers various installation methods, including manual setup and using package managers like NuGet. The guide also outlines system requirements, dependencies, and the necessary configuration steps to ensure seamless integration into development environments. This documentation helps developers get started with creating, reading, and manipulating PDF documents in Rust via C++ effectively.     
SoftwareApplication: rust-cpp
---

## Installation

This package includes a large file which is stored as a bzip2 archive.

1. Add the asposepdf package to Your Project:


releases //// 


2. Generate the large file: позже

For **macOS and linux**

  1. Open Terminal

  1. List the folders of the github.com/aspose-pdf within the Go module cache:

        ```sh
        ls $(go env GOMODCACHE)/github.com/aspose-pdf/
        ```

  1. Change curent folder to the specific version folder of the package obtained in the previous step:

      ```sh
      cd $(go env GOMODCACHE)/github.com/aspose-pdf/aspose-pdf-go-cpp@vx.x.x
      ```

      Replace `@vx.x.x` with the actual package version.

  1. Run go generate with superuser privileges:

      ```sh
      sudo go generate
      ```

For **Windows**

  1. Open Command Prompt
  
  1. List the folders of the github.com/aspose-pdf within the Go module cache:

      ```cmd
      for /f "delims=" %G in ('go env GOMODCACHE') do for /d %a in ("%G\github.com\aspose-pdf\*") do echo %~fa
      ```

  1. Change curent folder to the specific version folder of the package obtained in the previous step:

      ```cmd
      cd <specific version folder of the package>
      ```

  1. Run go generate:

      ```cmd
      go generate
      ```

  1. Add specific version folder of the package to the %PATH% environment variable:

      ```cmd
      setx PATH "%PATH%;<specific version folder of the package>\lib\"
      ```

      Replace `<specific version folder of the package>` with the actual path obtained from step 2.

## Testing

The test run from the root package folder:

```sh
go test -v
```

## Quick Start

All code snippets are contained in the [snippet](https://github.com/aspose-pdf/aspose-pdf-rust-cpp).