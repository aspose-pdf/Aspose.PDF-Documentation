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

### Installation from Aspose website

This package includes a large file which is stored as a bzip2 archive.

1. **Download** the archive **Aspose.PDF for Rust via C++** from the official Aspose website.
   The latest (most recent) version is listed at the top and is downloaded by default when you click the **Download** button.
   It is recommended to use this latest version. Only download a previous version if needed.
   Example: `Aspose.PDF-for-Rust-via-CPP-25.6.zip`

   The archive filename format is: `Aspose.PDF-for-Rust-via-CPP-YY.M.zip`, where:
   - `YY` = last two digits of the year (e.g., `25` for 2025)
   - `M` = month number from `1` to `12`

2. **Extract** the archive to your chosen directory `{path}` using a suitable tool:
   - On Linux/macOS:
     ```bash
     unzip Aspose.PDF-for-Rust-via-CPP-YY.M.zip -d {path}
     ```
   - On Windows, use built-in Explorer extraction or any unzip tool (7-Zip, WinRAR).

3. **Add** the library as a dependency in your Rust project. You can do this in two ways:

   - **Using the command line:**
     ```bash
     cargo add asposepdf --path {path}/asposepdf
     ```

   - **Manually editing `Cargo.toml`:**
     Open your project's `Cargo.toml` and add the following under `[dependencies]`:
     ```toml
     [dependencies]
     asposepdf = { path = "{path}/asposepdf" }
     ```

4. **Build** your project (`cargo build`). On the first build, the dynamic library for your platform will be unpacked automatically from the `.bz2` archive in the `lib` folder. This may cause a short delay.

> **Notes**
> - The `lib` folder contains all platform-specific `.bz2` archives with corresponding `.sha256` checksum files.
> - If the checksum file is missing or invalid, the build will fail.
> - Update the library by replacing the extracted files with a newer archive version.

### Installation from GitHub

This package includes precompiled native libraries (`.dll`, `.so`, `.dylib`) which are stored as compressed `.bz2` archives inside the GitHub repository.

1. **Add** the library as a dependency in your Rust project. You can do this in two ways:

- **Using the command line:**

```bash
cargo add asposepdf --git https://github.com/aspose-pdf/aspose-pdf-rust-cpp.git
```

- **Manually editing `Cargo.toml`:**

Open your project's `Cargo.toml` and add the following under `[dependencies]`:

```toml
[dependencies]
asposepdf = { git = "https://github.com/aspose-pdf/aspose-pdf-rust-cpp.git" }
```

**Note:** To use a specific release version, you can specify a tag:
  
```toml
asposepdf = { git = "https://github.com/aspose-pdf/aspose-pdf-rust-cpp.git", tag = "v1.25.7" }
```

2. **Build** your project (`cargo build`). On the first build, the appropriate dynamic library for your platform will be automatically unpacked from the `.bz2` archive in the `lib` folder. This may cause a short delay.

**Notes**

- You do not need to manually download or extract any files — everything is included in the GitHub repository.
- All `.bz2` archives have matching `.sha256` checksum files. The checksum is verified before unpacking.
- If the checksum verification fails or the archive is missing, the build will fail with a detailed error.
- The build script links the appropriate native library and ensures runtime availability using platform-specific options.

### Installation from crates.io

This package is available on [crates.io](https://crates.io/crates/asposepdf) and includes a build script that automatically extracts the required native library (`.dll`, `.so`, or `.dylib`) from a compressed `.bz2` archive during the build process.

1. **Add** the library as a dependency in your Rust project. You can do this in two ways:

- **Using the command line:**

```bash
cargo add asposepdf
```

- **Manually editing `Cargo.toml`:**

Open your project's `Cargo.toml` and add the following under `[dependencies]`:

```toml
[dependencies]
asposepdf = "1.25.7"
```

**Note:** The crates.io package requires you to provide the native dynamic libraries yourself (the .dll, .so, .dylib files).

2. **Set the path** to the directory containing the native libraries and download the required files:

- **Set the environment variable `ASPOSE_PDF_LIB_DIR`** to point to the folder where you will place the native `.bz2` archives, their `.sha256` checksum files, and the extracted native libraries (`.dll`, `.so`, `.dylib`, and for Windows also `.lib`):

- On Linux/macOS:

```bash
export ASPOSE_PDF_LIB_DIR=/path/to/lib
```

- On Windows (Command Prompt):

```cmd
set ASPOSE_PDF_LIB_DIR=C:\path\to\lib
```

- On Windows (PowerShell):

```powershell
$env:ASPOSE_PDF_LIB_DIR = "C:\path\to\lib"
```

- **Download the required `.bz2` archives** and checksum files from the GitHub repository's [`lib/` folder](https://github.com/aspose-pdf/aspose-pdf-rust-cpp/tree/main/lib) and **place them** into the folder set in `ASPOSE_PDF_LIB_DIR`:

- For **Linux x64**, download:
- `libAsposePDFforRust_linux_amd64.so.bz2`
- `libAsposePDFforRust_linux_amd64.so.bz2.sha256`

- For **macOS x86_64**, download:
- `libAsposePDFforRust_darwin_amd64.dylib.bz2`
- `libAsposePDFforRust_darwin_amd64.dylib.bz2.sha256`

- For **macOS arm64**, download:
- `libAsposePDFforRust_darwin_arm64.dylib.bz2`
- `libAsposePDFforRust_darwin_arm64.dylib.bz2.sha256`

- For **Windows x64**, download:
- `AsposePDFforRust_windows_amd64.dll.bz2`
- `AsposePDFforRust_windows_amd64.dll.bz2.sha256`
- `AsposePDFforRust_windows_amd64.lib` (native import library, not compressed)

**Note:**

You need to manually download these files from GitHub and place them into the directory pointed by `ASPOSE_PDF_LIB_DIR`.  
The build script will automatically unpack the native libraries from the `.bz2` archives on first build.

3. **Build** your project (`cargo build`). On the first build, the native library matching your platform will be automatically extracted and linked. This step may take a few seconds.

**Notes**

- You must provide the folder containing the `.bz2` and `.sha256` files separately, as these binary archives are not distributed via crates.io.
- If the required archive is missing or the checksum fails, the build will fail with a detailed error.
- The same binary files used for installation via GitHub or the Aspose website can be reused here.

## Quick Start

All code snippets are contained in the [snippet](https://onedrive.live.com/examples).