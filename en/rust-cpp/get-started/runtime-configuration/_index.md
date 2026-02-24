---
title: Runtime Configuration Aspose.PDF for Rust via C++
linktitle: Runtime Configuration
type: docs
weight: 20
url: /rust-cpp/runtime-configuration/
description: Rust applications that depend on native dynamic libraries—such as Aspose.PDF—require correct runtime path configuration to function properly on Linux and macOS systems
lastmod: "2026-02-24"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Configuring RPATH for Native Aspose.PDF for Rust
Abstract: When working with native dynamic libraries in Rust, proper runtime linking is essential to ensure your application can locate required dependencies. On Linux and macOS, the system dynamic loader does not automatically search the executable’s directory unless RPATH is explicitly configured. This article explains how to configure RPATH so your Rust application can correctly locate the Aspose.PDF native library at runtime. It covers project-level configuration using Cargo, environment-based configuration with RUSTFLAGS, and system-wide installation options, along with notes on Windows behavior.
SoftwareApplication: rust-cpp
---

> This is a standard requirement when using native dynamic libraries in Rust.

On Linux and macOS, the system dynamic loader does not automatically search the executable directory unless RPATH is configured. To ensure your application can find the Aspose.PDF native library at runtime, you need to configure the **RPATH** (Run-time Search Path).

Our build script extracts the library and attempts to create a symbolic link to it in your output directory (e.g., `target/debug/`). To enable the executable to find it, choose one of the following options:

## Option 1: Project-level Configuration (Recommended)

Create a folder named `.cargo` in your project's root directory (if it doesn't exist) and create a file named `config.toml` inside it:

```toml
[target.'cfg(target_os = "linux")']
rustflags = ["-C", "link-arg=-Wl,-rpath,$ORIGIN"]

[target.'cfg(target_os = "macos")']
rustflags = ["-C", "link-arg=-Wl,-rpath,@loader_path"]
```

## Option 2: RUSTFLAGS Environment Variable

Build your project with the following flag:

```bash
# Linux
RUSTFLAGS="-C link-arg=-Wl,-rpath,\$ORIGIN" cargo build

# macOS
RUSTFLAGS="-C link-arg=-Wl,-rpath,@loader_path" cargo build
```

## Option 3: System-wide Installation (Not recommended for development)

If you prefer to install the library globally:

* **Linux:** Copy the `.so` file to `/usr/local/lib` and run `sudo ldconfig`.
* **macOS:** Copy the `.dylib` file to `/usr/local/lib`.

> **Windows**
> No action is typically required because the library is located in the same folder as the `.exe`. Alternatively, you can add the directory containing the `.dll` to your system `PATH` environment variable.