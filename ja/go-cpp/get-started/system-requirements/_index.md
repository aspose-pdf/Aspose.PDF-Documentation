---
title: システム要件
linktitle: システム要件
type: docs
weight: 30
url: /ja/go-cpp/system-requirements/
description: このセクションでは、開発者が Aspose.PDF for Go を正常に使用するために必要な、サポートされているオペレーティングシステムを一覧表示します。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Go のシステム要件ページ
Abstract: Aspose.PDF for Go のシステム要件ページには、さまざまなプラットフォームでライブラリを設定するために必要な詳細が記載されています。サポートされているオペレーティングシステム、システム依存関係、ハードウェア構成など、ライブラリのインストール成功と最適なパフォーマンスを確保するために必要な環境設定が概説されています。また、Go のサポートされているバージョンなどのソフトウェア前提条件や、異なるシステム上でライブラリを効果的に実行するために必要な追加設定情報も含まれています。この情報は、開発者が開発環境を正しく設定するのに役立ちます。
SoftwareApplication: go-cpp
---

## C++ を使用した Aspose.PDF for Go のサポートプラットフォーム

パッケージ asposepdf は、開発者が PDF ファイルを直接操作できる強力なツールキットであり、PDF に関するさまざまなタスクを実行するのに役立ちます。
PDF を他の形式に変換するための固有機能が含まれています。

Linux x64、macOS x86_64、macOS arm64、および Windows x64 プラットフォームのサポートを実装しました。[cgo](https://go.dev/wiki/cgo) を使用しています。

パッケージのルートディレクトリにある ‘lib’ フォルダーからのプラットフォーム固有の動的ライブラリのバージョンが、結果として得られるアプリケーションを配布するために必要です：

- **libAsposePDFforGo_linux_amd64.so** は Linux x64 プラットフォーム用です。
- **libAsposePDFforGo_darwin_arm64.dylib** は macOS arm64 プラットフォーム用です。
- **libAsposePDFforGo_darwin_amd64.dylib** は macOS x86_64 プラットフォーム用です。
- **AsposePDFforGo_windows_amd64.dll** は Windows x64 プラットフォーム用です。

Windows x64 プラットフォームには必要です [MinGW-W64](https://www.mingw-w64.org/) インストールされています。
