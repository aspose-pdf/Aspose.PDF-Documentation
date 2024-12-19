---
title: How to Install Aspose.PDF for Go via C++
linktitle: Installation
type: docs
weight: 20
url: /go-cpp/installation/
description: This section shows a product description and instructions for installing Aspose.PDF for Go on your own.
lastmod: "2024-12-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Installation

This package includes a large file which is stored as a bzip2 archive.

1. Add the asposepdf package to Your Project:

    ```sh
    go get github.com/aspose-pdf/aspose-pdf-go-cpp@latest
    ```

2. Generate the large file:

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

All code snippets are contained in the [snippet](https://github.com/aspose-pdf/aspose-pdf-go-cpp).