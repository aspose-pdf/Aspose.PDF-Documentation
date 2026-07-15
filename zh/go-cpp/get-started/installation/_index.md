---
title: 如何通过 C++ 安装 Aspose.PDF for Go
linktitle: 安装
type: docs
weight: 20
url: /zh/go-cpp/installation/
description: 本节展示了产品描述和自行安装 Aspose.PDF for Go 的说明。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Go 安装指南
Abstract: Aspose.PDF for Go via C++ 安装指南提供逐步说明，用于在 Go 项目中进行 C++ 集成时安装和配置该库。它涵盖了多种安装方式，包括手动设置以及使用 Go Modules（go get）等依赖管理方式。指南还概述了系统要求、依赖项以及确保在开发环境中实现无缝集成的必要配置步骤。此文档帮助开发者在 Go 中通过 C++ 有效地创建、读取和操作 PDF 文档。
SoftwareApplication: go-cpp
---

## 安装

此软件包包括一个存储为 bzip2 存档的大文件。

1. 将 asposepdf 包添加到您的项目：

```sh
go get github.com/aspose-pdf/aspose-pdf-go-cpp@latest
```

2. 生成大文件：

- **macOS 和 Linux**

1. 打开终端

2. 列出 Go 模块缓存中 github.com/aspose-pdf 的文件夹：

```sh
ls $(go env GOMODCACHE)/github.com/aspose-pdf/
```

3. 将当前文件夹更改为上一步获取的包的特定版本文件夹：

```sh
cd $(go env GOMODCACHE)/github.com/aspose-pdf/aspose-pdf-go-cpp@vx.x.x
```

将 `@vx.x.x` 替换为实际的包版本。

4. 以超级用户权限运行 go generate：

```sh
sudo go generate
```

- **Windows**

1. 打开命令提示符

2. 列出 Go 模块缓存中 github.com/aspose-pdf 的文件夹：

```cmd
for /f "delims=" %G in ('go env GOMODCACHE') do for /d %a in ("%G\github.com\aspose-pdf\*") do echo %~fa
```

3. 将当前文件夹更改为上一步获取的包的特定版本文件夹：

```cmd
cd <specific version folder of the package>
```

4. 运行 go generate：

```cmd
go generate
```

5. 将包的特定版本文件夹添加到 %PATH% 环境变量中：

```cmd
setx PATH "%PATH%;<specific version folder of the package>\lib\"
```

替换 `<specific version folder of the package>` 使用从第2步获取的实际路径。

## 测试

从根包文件夹运行的测试：

```sh
go test -v
```

## 快速入门

所有代码片段都包含在 [代码片段](https://github.com/aspose-pdf/aspose-pdf-go-cpp).