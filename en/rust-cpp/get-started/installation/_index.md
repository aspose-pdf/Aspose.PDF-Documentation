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

1. Download the archive Aspose.PDF for Rust via C++ from the official Aspose website. The latest (most recent) version is listed at the top and is downloaded by default when you click the Download button. It is recommended to use this latest version. Only download a previous version if needed. Example: Aspose.PDF-for-Rust-via-CPP-25.6.zip

The archive filename format is: Aspose.PDF-for-Rust-via-CPP-YY.M.zip, where: - YY = last two digits of the year (e.g., 25 for 2025) - M = month number from 1 to 12

1. Extract the archive to your chosen directory {path} using a suitable tool:

- On Linux/macOS: bash unzip Aspose.PDF-for-Rust-via-CPP-YY.M.zip -d {path}
- On Windows, use built-in Explorer extraction or any unzip tool (7-Zip, WinRAR).

2. Add the library as a dependency in your Rust project. You can do this in two ways:

- Using the command line: 

```bash 

    cargo add asposepdf --path {path}/asposepdf
```

- Manually editing Cargo.toml: Open your project's Cargo.toml and add the following under [dependencies]: toml [dependencies] asposepdf = { path = "{path}/asposepdf" }

3. Build your project (cargo build). On the first build, the dynamic library for your platform will be unpacked automatically from the .bz2 archive in the lib folder. This may cause a short delay.

## Notes

- The lib folder contains all platform-specific .bz2 archives with corresponding .sha256 checksum files.
- If the checksum file is missing or invalid, the build will fail.
- Update the library by replacing the extracted files with a newer archive version.

## Quick Start

All code snippets are contained in the [snippet](https://onedrive.live.com/examples).